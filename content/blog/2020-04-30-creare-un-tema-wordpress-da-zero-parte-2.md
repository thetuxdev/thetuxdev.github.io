---
title: 2. Creare un tema WordPress da zero – Parte 2
author: Alberto
type: post
date: 2020-04-30T22:17:34+00:00
url: /creare-un-tema-wordpress-da-zero-parte-2/
nectar_blog_post_view_count:
  - 26
tags:
  - Guide
  - WordPress DEV

---
Nella**[ parte 1][1]** di questa guida per **creare un tema WordPress da zero** abbiamo iniziato a creare in nostro primo tema WordPress, creando **header**, **footer **e **sidebar **e imparando come funziona il **loop **di WordPress.

Ora andiamo a&nbsp;**rendere dinamico**&nbsp;il contenuto delle varie sezioni!

## MENU

WordPress permette di impostare dei&nbsp;**menu**, nella sezione “**Aspetto – Menu**“.

Questi menu&nbsp;**creati nel backend**&nbsp;possono essere&nbsp;**inseriti nel frontend**, rendendo così eventuali modifiche molto semplici ed immediate.

**Vediamo come fare.**

Per prima cosa dobbiamo&nbsp;**abilitare il nostro tema all’utilizzo dei menu**. Se infatti provi ad andare nel backend a certare la sezione “Aspetto – Menu” ora non la troverai ancora.

Per abilitarla dobbiamo creare quello che sarà il file più importante di tutto il tema:&nbsp;_**functions.php**_.

Creiamo quindi un file chiamato&nbsp;_functions.php_&nbsp;e inseriamo al suo interno questo codice:

<pre class="wp-block-code"><code>&lt;?php
//Setup del tema
function il_mio_tema_setup() {

//Imposto il menù per la navbar
    register_nav_menus(array(
		'navigation' =&gt; __( 'Menu Navbar','il-mio-tema'),
	));

}

add_action('after_setup_theme', 'il_mio_tema_setup');</code></pre>

Abbiamo creato una funzione di&nbsp;**setup del tema**, che utilizzeremo ancora in seguito per inserire altre personalizzazioni.

Qua abbiamo**&nbsp;registrato un nuovo menu**&nbsp;attraverso la funzione&nbsp;_register\_nav\_menus&nbsp;_e l’abbiamo chiamato ‘**Menu Navbar**‘.

Se ora andiamo nel&nbsp;**backend&nbsp;**vedremo che la sezione “Aspetto – Menu” è attiva e utilizzabile.

Procediamo quindi a&nbsp;**creare un nuovo menù:**<figure class="wp-block-image size-full">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-31-1024x324-1.png" alt="" class="wp-image-319" /> </figure>

Per il momento inseriamo solamente la home page e la pagina di esempio di default di WordPress, giusto per avere del contenuto al suo interno e clicchiamo su “**Crea menu**“.

Poi possiamo impostare il menù nella&nbsp;**posizione&nbsp;**“Menù navbar”:<figure class="wp-block-image size-full">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-32-1024x142-1.png" alt="" class="wp-image-321" /> </figure>

Ora non ci resta che&nbsp;**inserire questo menù nella nostra barra di navigazione**, nell’header del tema.

Apriamo quindi_&nbsp;header.php_&nbsp;e sostituiamo l'<ul> della nav con questo:

<pre class="wp-block-code"><code>            &lt;div class="collapse navbar-collapse" id="navbarSupportedContent"&gt;
                &lt;?php
                $args = array(
                    'theme_location' =&gt; 'navigation',
                    'depth'      =&gt; 2,
                    'container' =&gt; false,
                    'menu_class' =&gt; 'navbar-nav ml-auto',
                    'add_li_class'  =&gt; 'nav-item',
                    'link_class'   =&gt; 'nav-link',
                    'walker'     =&gt; new Bootstrap_Walker_Nav_Menu()

                );

                ?&gt;
                &lt;?php wp_nav_menu($args); ?&gt;
            &lt;/div&gt;
</code></pre>

IMPORTANTE: per selezionare il giusto menù abbiamo inserito il theme_location uguale al nome di registrazione del menu inserito in functions.php.

Per far funzionare correttamente il&nbsp;**dropdown&nbsp;**di bootstrap dobbiamo ancora aggiungere una funzione che permetta di gestire i vari sottomenù. Questa funzione è chiamata “**walker**“, puoi semplicemente incollare questo codice nel&nbsp;_functions.php_:

<pre class="wp-block-code"><code>// Custom Walker Class for Bootstrap Menu
add_action( 'after_setup_theme', 'bootstrap_setup' );

if ( ! function_exists( 'bootstrap_setup' ) ):

  function bootstrap_setup(){

    class Bootstrap_Walker_Nav_Menu extends Walker_Nav_Menu {


      function start_lvl( &$output, $depth = 0, $args = array() ) {

        $indent = str_repeat( "\t", $depth );
        $output    .= "\n$indent&lt;ul class=\"dropdown-menu\"&gt;\n";

      }

      function start_el( &$output, $item, $depth = 0, $args = array(), $id = 0 ) {

        $indent = ( $depth ) ? str_repeat( "\t", $depth ) : '';

        $li_attributes = '';
        $class_names = $value = '';

        $classes = empty( $item-&gt;classes ) ? array() : (array) $item-&gt;classes;
        $classes&#91;] = ($args-&gt;walker-&gt;has_children) ? 'dropdown' : '';
        $classes&#91;] = ($item-&gt;current || $item-&gt;current_item_ancestor) ? 'active' : '';
        $classes&#91;] = 'menu-item-' . $item-&gt;ID;
        $classes&#91;] = 'nav-item';


        $class_names = join( ' ', apply_filters( 'nav_menu_css_class', array_filter( $classes ), $item, $args ) );
        $class_names = ' class="' . esc_attr( $class_names ) . '"';

        $id = apply_filters( 'nav_menu_item_id', 'menu-item-'. $item-&gt;ID, $item, $args );
        $id = strlen( $id ) ? ' id="' . esc_attr( $id ) . '"' : '';

        $output .= $indent . '&lt;li' . $id . $value . $class_names . $li_attributes . '&gt;';

        $attributes  = ! empty( $item-&gt;attr_title ) ? ' title="'  . esc_attr( $item-&gt;attr_title ) .'"' : '';
        $attributes .= ! empty( $item-&gt;target )     ? ' target="' . esc_attr( $item-&gt;target     ) .'"' : '';
        $attributes .= ! empty( $item-&gt;xfn )        ? ' rel="'    . esc_attr( $item-&gt;xfn        ) .'"' : '';
        $attributes .= ! empty( $item-&gt;url )        ? ' href="'   . esc_attr( $item-&gt;url        ) .'"' : '';
        $attributes .= ($args-&gt;walker-&gt;has_children)      ? ' class="nav-link dropdown-toggle" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"' : 'class="nav-link"';

        $item_output = $args-&gt;before;
        $item_output .= ($depth &gt; 0) ? '&lt;a class="dropdown-item"' . $attributes . '&gt; ' : '&lt;a'. $attributes .'&gt;';
        $item_output .= $args-&gt;link_before . apply_filters( 'the_title', $item-&gt;title, $item-&gt;ID ) . $args-&gt;link_after;
        $item_output .= '&lt;/a&gt;';
        $item_output .= $args-&gt;after;

        $output .= apply_filters( 'walker_nav_menu_start_el', $item_output, $item, $depth, $args );
      }

    }

  }

endif;

</code></pre>

Ora se salvi e aggiorni dovresti avere**&nbsp;il menu funzionante e dinamico!**

## WIDGET

I&nbsp;**widget&nbsp;**sono una parte&nbsp;**importantissima&nbsp;**di WordPress. Consentono di creare una**&nbsp;sezione inseribile in più parti**&nbsp;in maniera semplice e veloce.

### INIZIALIZZIAMO I WIDGET

Per inizializzare un widget dobbiamo andare sempre nel&nbsp;_functions.php_&nbsp;ed inserire questo codice:

<pre class="wp-block-code"><code>// Widgets
function InizializzazioneWidget() {

	register_sidebar( array(
		'name' =&gt; 'Sidebar',
		'id' =&gt; 'sidebar1',
		'before_widget' =&gt; '&lt;div class="sidebar"&gt;',
		'after_widget' =&gt; '&lt;/div&gt;',
		'before_title' =&gt; '&lt;h3&gt;',
		'after_title' =&gt; '&lt;/h3&gt;',
	));
}

add_action('widgets_init', 'InizializzazioneWidget');
</code></pre>

Ora abbiamo&nbsp;**aggiunto la possibilità di inserire widget nella sidebar**. I widget saranno inseriti in un div con classe “**sidebar**” e il titolo di ogni widget sarà un <h3>.

Se andiamo nel backend in “**Aspetto – Widget**” possiamo vedere che abbiamo un’area riservata alla sidebar:<figure class="wp-block-image size-full">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-33.png" alt="" class="wp-image-322" /> </figure>

Proviamo ad inserire dei widget al suo interno. Al momento non verranno inseriti nel frontend.

Dobbiamo**&nbsp;andare a dire alla sidebar di prendere il suo contenuto attraverso i widget**!

Apriamo quindi il nostro file&nbsp;_sidebar.php_, cancelliamo tutto e sostituiamo il codice con questo:

<pre class="wp-block-code"><code>&lt;!-- SIDEBAR --&gt;
&lt;div class="col-sm-3 col-sm-offset-1 blog-sidebar"&gt;
    &lt;?php if (is_active_sidebar('sidebar1')) : ?&gt;

        &lt;?php dynamic_sidebar('sidebar1'); ?&gt;

    &lt;?php endif; ?&gt;
&lt;/div&gt;
&lt;!-- /SIDEBAR --&gt;</code></pre>

Ora nel backend proviamo ad inserire il Widget&nbsp;**“Articoli recenti”**&nbsp;nella sidebar, inserendo “Articoli recenti” come titolo e salvando.<figure class="wp-block-image size-full">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-34-1.png" alt="" class="wp-image-323" /> </figure>

Se tutto è andato liscio dovresti vedere gli ultimi articoli apparire nella sidebar!<figure class="wp-block-image">

<img decoding="async" src="https://albertoreineri.it.local/wp-content/uploads/2020/04/image-35.png" alt="" class="wp-image-582" /> </figure>

**Fantastico! Hai appena creato un widget!**

Puoi creare&nbsp;**widget anche in altre parti del sito**, per esempio nel footer.

**Esercizio:**

Prova a creare dei widget da solo adesso.

Crea 4 widget da inserire nel footer del sito. Ricordati, devi registrare 4 zone per il footer in functions.php e andare nel file footer.php a inserire le aree giuste!

Ecco il risultato nel front-end:<figure class="wp-block-image size-full">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-36-1024x138-1.png" alt="" class="wp-image-326" /> </figure>

Prenditi un po’ di tempo e prova a farlo, qua sotto ti lascerò**&nbsp;il codice:**

**functions.php**

<pre class="wp-block-code"><code>// Widgets
function InizializzazioneWidget() {

	register_sidebar( array(
		'name' =&gt; 'Sidebar',
		'id' =&gt; 'sidebar1',
		'before_widget' =&gt; '&lt;div class="sidebar"&gt;',
		'after_widget' =&gt; '&lt;/div&gt;',
		'before_title' =&gt; '&lt;h3&gt;',
		'after_title' =&gt; '&lt;/h3&gt;',
	));

    register_sidebar( array(
		'name' =&gt; 'Footer Area 1',
		'id' =&gt; 'footer1',
		'before_widget' =&gt; '&lt;div class="widget-item"&gt;',
		'after_widget' =&gt; '&lt;/div&gt;',
		'before_title' =&gt; '&lt;h2&gt;',
		'after_title' =&gt; '&lt;/h2&gt;',
    ));

    register_sidebar( array(
		'name' =&gt; 'Footer Area 2',
		'id' =&gt; 'footer2',
		'before_widget' =&gt; '&lt;div class="widget-item"&gt;',
		'after_widget' =&gt; '&lt;/div&gt;',
		'before_title' =&gt; '&lt;h2&gt;',
		'after_title' =&gt; '&lt;/h2&gt;',
    ));

    register_sidebar( array(
		'name' =&gt; 'Footer Area 3',
		'id' =&gt; 'footer3',
		'before_widget' =&gt; '&lt;div class="widget-item"&gt;',
		'after_widget' =&gt; '&lt;/div&gt;',
		'before_title' =&gt; '&lt;h2&gt;',
		'after_title' =&gt; '&lt;/h2&gt;',
    ));

    register_sidebar( array(
		'name' =&gt; 'Footer Area 4',
		'id' =&gt; 'footer4',
		'before_widget' =&gt; '&lt;div class="widget-item"&gt;',
		'after_widget' =&gt; '&lt;/div&gt;',
		'before_title' =&gt; '&lt;h2&gt;',
		'after_title' =&gt; '&lt;/h2&gt;',
	));


}

add_action('widgets_init', 'InizializzazioneWidget');</code></pre>

**footer.php**

<pre class="wp-block-code"><code>&lt;div class="row"&gt;

            &lt;?php if (is_active_sidebar('footer1')) : ?&gt;

                &lt;div class="col-lg-3"&gt;
                    &lt;?php dynamic_sidebar('footer1'); ?&gt;
                &lt;/div&gt;

            &lt;?php endif; ?&gt;

            &lt;?php if (is_active_sidebar('footer2')) : ?&gt;

                &lt;div class="col-lg-3"&gt;
                    &lt;?php dynamic_sidebar('footer2'); ?&gt;
                &lt;/div&gt;

            &lt;?php endif; ?&gt;

            &lt;?php if (is_active_sidebar('footer3')) : ?&gt;

                &lt;div class="col-lg-3"&gt;
                    &lt;?php dynamic_sidebar('footer3'); ?&gt;
                &lt;/div&gt;

            &lt;?php endif; ?&gt;

            &lt;?php if (is_active_sidebar('footer4')) : ?&gt;

                &lt;div class="col-lg-3"&gt;
                    &lt;?php dynamic_sidebar('footer4'); ?&gt;
                &lt;/div&gt;

            &lt;?php endif; ?&gt;
        &lt;/div&gt;</code></pre>

Molto bene, ora&nbsp;**il sito inizia a prendere forma!**&nbsp;Andiamo ora a cerare i layout per le pagine, gli articoli e gli archivi.

## LAYOUT PAGINE

Per creare un layout dedicato alle pagine di WordPress dobbiamo andare nella cartella del nostro tema e creare un file_**&nbsp;page.php**_.

**page.php**

<pre class="wp-block-code"><code>&lt;?php get_header(); ?&gt;


&lt;?php
if (have_posts()) :
    while (have_posts()) : the_post();

?&gt;
        &lt;!-- TITOLO --&gt;
        &lt;h1&gt;&lt;?php the_title(); ?&gt;&lt;/h1&gt;

        &lt;!-- IMMAGINE EVIDENZA --&gt;
        &lt;?php the_post_thumbnail(); ?&gt;

        &lt;!-- CONTENUTO --&gt;
        &lt;?php the_content(); ?&gt;

&lt;?php

    endwhile;
endif;
?&gt;

&lt;?php get_footer(); ?&gt;</code></pre>

Questo codice ci permetterà di**&nbsp;visualizzare il titolo, l’immagine in evidenza ed il contenuto**&nbsp;della pagina salvata nel backend.

Per differenziarla dagli articoli non abbiamo inserito la sidebar nelle pagine.

Vediamo ora come creare un articolo.

### LAYOUT ARTICOLI

Per creare un layout dedicato agli articoli ci basterà creare il file&nbsp;_**single.php&nbsp;**_all’interno del tema e inserire il loop:

**single.php**

<pre class="wp-block-code"><code>&lt;?php get_header(); ?&gt;

&lt;div class="container"&gt;
    &lt;div class="row"&gt;g&lt;!-- CONTENTUO --&gt;
        &lt;div class="col-lg-8"&gt;

            &lt;?php
            if (have_posts()) :
                while (have_posts()) : the_post();

            ?&gt;
                    &lt;!-- TITOLO --&gt;
                    &lt;h1&gt;&lt;?php the_title(); ?&gt;&lt;/h1&gt;

                    &lt;!-- IMMAGINE EVIDENZA --&gt;
                    &lt;?php the_post_thumbnail(); ?&gt;

                    &lt;!-- CONTENUTO --&gt;
                    &lt;?php the_content(); ?&gt;

            &lt;?php

                endwhile;
            endif;
            ?&gt;

        &lt;/div&gt;
        &lt;!-- SIDEBAR --&gt;
        &lt;div class="col-lg-4"&gt;

            &lt;?php get_sidebar(); ?&gt;

        &lt;/div&gt;
    &lt;/div&gt;

&lt;/div&gt;

&lt;?php get_footer(); ?&gt;</code></pre>

In questo caso abbiamo il contenuto dell’articolo sulla sinistra e la sidebar sulla destra.

Ed ecco il nostro bel layout per gli articoli!

## LAYOUT ARCHIVI

Un&nbsp;**archivio&nbsp;**è una pagina che contiene un&nbsp;**elenco di post.**

Iniziamo con il creare una categoria “**blog**” nel backend di WordPress, dopodiché inseriamo questa categoria nel nostro menu di navigazione.

Creiamo anche un paio di articoli con categoria “blog”, in modo da avere dei contenuti da visualizzare nel frontend.

Ora andiamo nella cartella del nostro tema e creiamo un file&nbsp;_**archive.php&nbsp;**_contenente questo codice:

**archive.php**

<pre class="wp-block-code"><code>&lt;?php get_header(); ?&gt;

&lt;div class="container"&gt;
    &lt;div class="row"&gt;
        &lt;!-- CONTENTUO --&gt;
        &lt;div class="col-lg-8"&gt;
            &lt;h1&gt;
                &lt;?php
                single_cat_title();
                ?&gt;
            &lt;/h1&gt;

            &lt;?php
            if (have_posts()) :
                while (have_posts()) : the_post();

            ?&gt;
                    &lt;a href="&lt;?php the_permalink(); ?&gt;"&gt;
                        &lt;div class="articolo"&gt;
                            &lt;!-- TITOLO --&gt;
                            &lt;h1&gt;&lt;?php the_title(); ?&gt;&lt;/h1&gt;

                            &lt;!-- IMMAGINE EVIDENZA --&gt;
                            &lt;?php the_post_thumbnail(); ?&gt;

                            &lt;!-- CONTENUTO --&gt;
                            &lt;?php the_excerpt(); ?&gt;
                        &lt;/div&gt;
                    &lt;/a&gt;
            &lt;?php

                endwhile;
            endif;
            ?&gt;

        &lt;/div&gt;
        &lt;!-- SIDEBAR --&gt;
        &lt;div class="col-lg-4"&gt;

            &lt;?php get_sidebar(); ?&gt;

        &lt;/div&gt;
    &lt;/div&gt;

&lt;/div&gt;



&lt;?php get_footer(); ?&gt;</code></pre>

Il&nbsp;**loop&nbsp;**come puoi vedere&nbsp;**è sempre lo stesso**, però in questo caso al posto che visualizzare il contenuto (the_content), abbiamo visualizzato&nbsp;**l’excerpt**!

Un&nbsp;**excerpt&nbsp;**è una parte del contenuto, un’anteprima del testo vero e proprio.

In più abbiamo inserito il link ad ogni singolo articolo, utilizzando&nbsp;_**the_permalink**_.

Non è così complicato vero?

**Il tema è sempre più completo!&nbsp;**Ci mancano solamente ancora un paio di passaggi. Leggi la parte numero 3 per imparare a creare un tema WordPress completo!

<div class="wp-block-columns are-vertically-aligned-center is-layout-flex wp-container-core-columns-is-layout-6 wp-block-columns-is-layout-flex">
  <div class="wp-block-column is-vertically-aligned-center is-layout-flow wp-block-column-is-layout-flow">
    <p>
      <em><a href="https://albertoreineri.it/guide/le-basi-dellhtml/"><< Parte 1</a></em>
    </p>
  </div>

  <div class="wp-block-column is-vertically-aligned-center is-layout-flow wp-block-column-is-layout-flow">
    <p class="has-text-align-right">
      <em><a href="https://albertoreineri.it/guide/creare-un-tema-wordpress-da-zero-parte-3/">Parte 3 >></a></em>
    </p>
  </div>
</div>

 [1]: https://albertoreineri.it/guide/creare-un-tema-wordpress-da-zero-parte-1/