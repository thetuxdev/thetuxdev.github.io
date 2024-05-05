---
title: 3. Creare un tema WordPress da zero – Parte 3
author: Alberto
type: post
date: 2020-04-30T22:16:10+00:00
url: /creare-un-tema-wordpress-da-zero-parte-3/
nectar_blog_post_view_count:
  - 26
tags:
  - Guide
  - WordPress DEV

---
Negli [ultimi tutorial][1] abbiamo iniziato a **creare un tema WordPress da zero**, e siamo arrivati già a un buon punto!

Ci mancano però ancora un paio di cosette per rendere accettabile il nostro lavoro. **Vediamo di andare avanti!**

<p class="has-text-align-center has-vivid-red-color has-text-color">
  <em>Ti ricordo che sul fondo di questo articolo potrai trovare un link al tema completo. Potrai scaricarlo per cercare eventuali errori ed utilizzarlo come vorrai! Consideralo un regalo!</em>
</p>

Ma riprendiamo il **tutorial**!

## Inserire immagini

Con WordPress è semplicissimo inserire immagini all&#8217;interno degli articoli, delle pagine o dei widget, ma se volessimo inserire per esempio un logo? Oppure un&#8217;immagine in un punto specifico del sito?

Per fare questo dobbiamo utilizzare la funzione _get\_template\_directory_uri_, che ci permette di **collegarci alla cartella del nostro tema**. Vediamo come fare.

### Inseriamo un logo nella navbar

Per prima cosa rechiamoci nella cartella del nostro tema e creiamo un&#8217;altra cartella chiamata &#8220;**img**&#8220;. Qua dentro ora possiamo inserire le immagini che vogliamo inserire nel tema. Inseriamo un logo. Io lo chiamerò &#8220;**logo.png**&#8220;.

Ora andiamo nel nostro _header.php_ e inseriamo il logo prima del titolo del nostro sito, in questo modo:

<pre class="wp-block-code"><code>&lt;img src="&lt;?php echo get_template_directory_uri(); ?&gt;/img/logo.png" alt="" height="50"&gt;</code></pre>

La funzione _get\_template\_directory_uri_ inserirà il percorso della cartella del nostro sito, a cui noi aggiungiamo il percorso per raggiungere l&#8217;immagine.

Prova a salvare e aggiornare il sito, dovresti vedere **il logo comparire** prima del nome del sito!

Se appare brutto puoi **modificarlo tramite CSS**, ma per il momento ci interessa il fatto che compaia!

La funzione _get\_template\_directory_uri_ può essere utilizzata ogni volta che dobbiamo raggiungere qualcosa contenuto nella **cartella del nostro tema.**

Potremmo anche utilizzarla per inserire i file CSS e JS nel sito, ma WordPress prevede un sistema diverso, che vedremo fra poco.

## Hook

Nello sviluppo WordPress gli **hook** hanno una grande importanza.

Ci permettono di _aggrapparci_ a questi per inserire le nostre customizzazioni. Questo permette a noi sviluppatori di inserire delle **modifiche al nostro tema** senza toccare il core di WordPress.

Ci sono alcuni hook che sono **fondamentali** in ogni tema ben fatto.

### wp_title

Un primo hook da inserire è il _wp_title_, che va messo nel meta tag <title>, nell'<head> della pagina.

Apriamo quindi il nostro _heder.php_ e modifichiamo il <title> in questo modo:

<pre class="wp-block-code"><code>&lt;title&gt;&lt;?php wp_title(); ?&gt;&lt;/title&gt;</code></pre>

In questo modo il tag del titolo verrà **gestito da WordPress** nel migliore dei modi.

### wp_head

Sempre nel nostro header dobbiamo aggiungere l&#8217;hook _wp_head_. Questo ci permette di inserire i nostri CSS e JS nell'<head> della pagina, come vedremo fra poco.

Aggiungiamo quindi questo codice giusto prima del _</head>_:

<pre class="wp-block-code"><code>&lt;?php wp_head(); ?&gt;</code></pre>

### body_class

Rimaniamo sempre nel nostro header.php e aggiungiamo un hook anche al <body>, in questo modo:

<pre class="wp-block-code"><code>&lt;body &lt;?php body_class(); ?&gt;&gt;</code></pre>

Così WordPress **gestirà al meglio il body** del nostro tema.

### wp_footer

L&#8217;ultimo hook che andremo ad aggiungere è il _wp_footer_, che permette di inserire i contenuti prima del _</body>_, come i file javascript.

Andiamo quindi nel _footer.php_ e inseriamo questo giusto prima del </body>

<pre class="wp-block-code"><code>&lt;?php wp_footer(); ?&gt;</code></pre>

## Inserire CSS e JS in un tema WordPress

Il **metodo corretto** per inserire dei file CSS e JS all&#8217;interno di un tema WordPress è un po&#8217; particolare.

Sebbene funzioni anche in metodo classico di inserimento nell'<head> e prima del </body> (metodo che abbiamo utilizzato nella parte 1 di questa serie di tutorial), un tema WordPress ben fatto deve inserire i file CSS e JS attraverso il file **_functions.php._**

### CSS

Iniziamo ad aprire il nostro file _functions.php_ e inseriamo questo codice per embeddare il nostro file style.css nel tema:

<pre class="wp-block-code"><code>function risorse_il_mio_tema() {
	//CSS
         enqueue_style('style', get_stylesheet_uri());
}
add_action('wp_enqueue_scripts', 'risorse_il_mio_tema');</code></pre>

In questo modo embedderemo il file _style.css_, obbligatorio in ogni tema WordPress.

Ora inseriamo il CSS di **[Bootstrap][2]** in maniera corretta. Lo aggiungiamo a questa funzione, in questo modo:

<pre class="wp-block-code"><code>wp_enqueue_style( 'bootstrap','http://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css','','','all');</code></pre>

Ricorda di inserire **Bootstrap** come **primo file**, prima di &#8220;style&#8221;, per un corretto funzionamento.

Ora andiamo nell&#8217;header.php e rimuoviavo il CSS di bootstrap, che ora verrà inserito nella maniera corretta tramite functions.php

### JS

Inseriamo ora i file **javascript di Bootstrap** nel modo corretto.

Anche i file Javascript vanno inseriti come i CSS, nella stessa funzione, in questo modo:

<pre class="wp-block-code"><code>//JS
wp_enqueue_script( 'jquery-js', 'http://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js', '','' ,true);
wp_enqueue_script( 'bootstrap-js', 'http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js', '','' ,true);
</code></pre>

Ora possiamo eliminare i file JS di bootstrap dal nostro **footer.php**

Per semplicità ti riscrivo **tutta la funzione** di embeddamento di CSS e JS:

<pre class="wp-block-code"><code>/* CSS e JS */
function risorse_il_mio_tema() {
	//CSS
	wp_enqueue_style( 'bootstrap','http://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css','','','all');
	wp_enqueue_style('style', get_stylesheet_uri());

	//JS
	wp_enqueue_script( 'jquery-js', 'http://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js', '','' ,true);
	wp_enqueue_script( 'bootstrap-js', 'http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js', '','' ,true);

}
add_action('wp_enqueue_scripts', 'risorse_il_mio_tema');</code></pre>

**In questo modo hai inserito i codici CSS e JS secondo le Best Practice di WordPress!**

## Paginazione

Se il nostro tema inizierà ad avere molti articoli, allora la pagina archivio diventerà presto molto pesante.

Fortunatamente WordPress fornisce una funzione per facilitare moltissimo la **paginazione**.

Puoi decidere quanti articoli far visualizzare nelle pagine archivio tramite la sezione &#8220;**Impostazioni &#8211; Lettura**&#8220;.

<div class="wp-block-image">
  <figure class="aligncenter size-full"><img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-38-1.png" alt="" class="wp-image-328" /></figure>
</div>

Per inserire la paginazione nel frontend andiamo nel nostro _**archive.php**_ e inseriamo questa funzione **dopo il** **loop**:

<pre class="wp-block-code"><code>&lt;?php echo paginate_links(); ?&gt;</code></pre>

In questo modo **i link di paginazione saranno gestiti interamente da WordPress!**

Fantastico vero? Nulla di più semplice! Non ti resta che rendere questi link un po&#8217; più carini, tramite **CSS**.

### Commenti

Il sito inizia ad avere senso, ma non abbiamo ancora inserito una sezione commenti! Vediamo come fare!

Iniziamo creando un file **_comments.php_** nella cartella del nostro tema.

**comments.php**

<pre class="wp-block-code"><code>
&lt;div id="comments" class="comments-area"&gt;

    &lt;?php if ( have_comments() ) : ?&gt;
        &lt;h2 class="comments-title"&gt;
            &lt;?php
                printf( _nx( 'Un commento per "%2$s"', '%1$s Commenti su "%2$s"', get_comments_number(), 'comments title', 'beauty-mountain' ),
                    number_format_i18n( get_comments_number() ), '&lt;span&gt;' . get_the_title() . '&lt;/span&gt;' );
            ?&gt;
        &lt;/h2&gt;

        &lt;ol class="comment-list"&gt;
            &lt;?php
                wp_list_comments( array(
                    'style'       =&gt; 'ol',
                    'short_ping'  =&gt; true,
                    'avatar_size' =&gt; 74,
                ) );
            ?&gt;
        &lt;/ol&gt;&lt;!-- .comment-list --&gt;

        &lt;?php
            // Ci sono più commenti?
            if ( get_comment_pages_count() &gt; 1 && get_option( 'page_comments' ) ) :
        ?&gt;
        &lt;nav class="navigation comment-navigation" role="navigation"&gt;
            &lt;h1 class="screen-reader-text section-heading"&gt;&lt;?php _e( 'Comment navigation', 'beauty-mountain' ); ?&gt;&lt;/h1&gt;
            &lt;div class="nav-previous"&gt;&lt;?php previous_comments_link( __( '&larr; Older Comments', 'beauty-mountain' ) ); ?&gt;&lt;/div&gt;
            &lt;div class="nav-next"&gt;&lt;?php next_comments_link( __( 'Newer Comments &rarr;', 'beauty-mountain' ) ); ?&gt;&lt;/div&gt;
        &lt;/nav&gt;&lt;!-- .comment-navigation --&gt;
        &lt;?php endif; ?&gt;

        &lt;?php if ( ! comments_open() && get_comments_number() ) : ?&gt;
        &lt;p class="no-comments"&gt;&lt;?php _e( 'Comments are closed.' , 'beauty-mountain' ); ?&gt;&lt;/p&gt;
        &lt;?php endif; ?&gt;

    &lt;?php endif; // have_comments() ?&gt;

    &lt;?php comment_form(); ?&gt;

&lt;/div&gt;&lt;!-- #comments --&gt;</code></pre>

Questo codice ti pemetterà di inserire i commenti, ora andiamo nel file **_single.php,_** quello che contiene i nostri articoli, e inseriamo il template per i commenti dopo il contenuto:

<pre class="wp-block-code"><code>&lt;!-- COMMENTI --&gt;
&lt;?php comments_template(); ?&gt;</code></pre>

In questo modo potrai **vedere i commenti sui tuoi articoli!**

<div style="height:50px" aria-hidden="true" class="wp-block-spacer">
</div>

**Perfetto!** Direi che per iniziare abbiamo già creato qualcosa di carino!

Prima di lasciarti andare via ti condivido ancora **un po&#8217; di CSS** per rendere il nostro lavoro un po&#8217; più carino.

Ricorda che puoi **scaricare l&#8217;intero tema**, per controllare errori e verificare di aver capito tutto al meglio! Clicca **sul bottone sul fondo** dell&#8217;articolo per scaricare il tema!

Non è un tema perfetto ma può essere un buon **starter theme** per i tuoi progetti futuri!

**style.css**

<pre class="wp-block-code"><code>/*
Theme Name: Il mio tema
Author: Specialista WP
Description: Il mio primo tema WordPress
Version: 0.0.1
*/

/*
 * Globals
 */

a:hover{
  text-decoration: none;
}

img{
  max-width: 100%;
  height:auto
}

footer{
  background-color: #888;
  margin-top: 50px;
  padding-top: 50px;
  color:#000;
  margin-bottom: 0;
  padding-bottom: 50px;
}

</code></pre>

<div class="wp-block-columns are-vertically-aligned-center is-layout-flex wp-container-core-columns-is-layout-5 wp-block-columns-is-layout-flex">
  <div class="wp-block-column is-vertically-aligned-center is-layout-flow wp-block-column-is-layout-flow">
    <p>
      <em><a href="https://albertoreineri.it/guide/le-basi-dellhtml/"><< Parte 2</a></em>
    </p>
  </div>

  <div class="wp-block-column is-vertically-aligned-center is-layout-flow wp-block-column-is-layout-flow">
    <p class="has-text-align-right">
      <em><a href="https://albertoreineri.it/guide/creare-un-plugin-wordpress/">Creare Plugin >></a></em>
    </p>
  </div>
</div>

<div style="height:50px" aria-hidden="true" class="wp-block-spacer">
</div>

<div style="height:50px" aria-hidden="true" class="wp-block-spacer">
</div>

 [1]: /argomento/wordpress-dev/
 [2]: https://albertoreineri.it/guide/le-basi-di-bootstrap/