---
title: 1. Creare un tema WordPress da zero – Parte 1
author: Alberto
type: post
date: 2020-04-30T22:18:09+00:00
url: /creare-un-tema-wordpress-da-zero-parte-1/
nectar_blog_post_view_count:
  - 46
tags:
  - Guide
  - WordPress DEV

---
**WordPress&nbsp;**è una piattaforma&nbsp;**fantastica**! Permette di creare**&nbsp;siti web di ogni tipo**&nbsp;in maniera semplice e&nbsp;**veloce**, grazie all’infinita quantità di&nbsp;**temi&nbsp;**e&nbsp;**plugin&nbsp;**disponibili, moltissimi dei quali in maniera gratuita.

Però&nbsp;**quando si vuole fare il salto di livello**&nbsp;ed avere un sito web veramente&nbsp;**performante**, allora conviene utilizzare un**&nbsp;tema sviluppato da zero**, in grado di implementare tutte le funzioni necessarie nella maniera più performante!

**Niente errori**&nbsp;in console, niente stringhe in inglese, niente codici sparsi in giro per il sito, niente css e js inutili… Solo ciò che serve realmente, sviluppato nel modo corretto.

**Oggi vediamo come creare un tema WordPress da zero!**

Mettiti comodo e**&nbsp;prenditi il tuo tempo**, ci vorrà un po’, ma alla fine avrai realizzato&nbsp;**il tuo primo tema WordPress&nbsp;**funzionante e nel rispetto di tutte le best practice.

_**Partiremo da un’installazione di WordPress, se non sai come installare il CMS ti consiglio di seguire le guide per&nbsp;[Inizia Qui][1].**_

_Questo tutorial è suddiviso in 3 parti, alla fine potrai scaricare l’intero tema che creeremo insieme per confrontarlo e correggere eventuali errori. Ti consiglio di seguire le varie parti e scaricare il tema solo alla fine, ma se ti servisse prima lo puoi trovare sul fondo della&nbsp;[parte 3][2]._

## CREIAMO IL NOSTRO TEMA

Se apri la cartella del tuo sito&nbsp;**WordPress&nbsp;**noterai che all’interno sono presenti&nbsp;**3 cartelle**:

  * wp-admin
  * wp-content
  * wp-includes

A noi per il momento interessa solamente la “**wp-content**“, quindi iniziamo ad&nbsp;**aprirla**.

All’interno di wp-content apriamo ora la cartella “**themes**“, che come puoi intuire contiene**&nbsp;i temi del progetto.**

**Procediamo quindi a creare il nostro primo tema!**

Creiamo una&nbsp;**nuova cartella**&nbsp;e la chiamiamo “**il-mio-tema**“, dopodiché apriamo la cartella con&nbsp;**<a href="http://code.visualstudio.com/" target="_blank" rel="noreferrer noopener">VS Code</a>**. (Se non sai come fare questo passaggio visualizza le&nbsp;[guide per principianti][3])

Un&nbsp;**tema WordPress**&nbsp;per essere riconosciuto necessita solamente di**&nbsp;2 file:**

  * style.css
  * index.php

**creiamo quindi questi 2 file all’interno della cartella “il-mio-tema”**&nbsp;e inseriamo questo codice in “**style.css**“, in modo da indicare a WordPress i dati del tema:

<pre class="wp-block-code"><code>/*
Theme Name: Il mio tema
Author: Specialista WP
Description: Il mio primo tema WordPress
Version: 0.0.1
*/</code></pre>

Puoi&nbsp;**sostituire&nbsp;**l’autore con il tuo nome, così come il nome del tema e la descrizione.

Se ora salvi il file CSS e vai nel backend di WordPress in “**Aspetto – Temi**” vedrai comparire il nostro tema!<figure class="wp-block-image size-full">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-12-2.png" alt="" class="wp-image-316" /> </figure>

Puoi&nbsp;**attivare il tema&nbsp;**e&nbsp;_voilà_! Il tema è fatto!

Non è poi tanto complicato vero? Già, però ora il tema è&nbsp;**vuoto**, occorre riempirlo!

Inizia con l’inserire questo codice nella “**index.php**“, è un&nbsp;**layout di base**&nbsp;creato con&nbsp;[bootstrap&nbsp;][4]sul quale andremo a costruire il nostro sito:

**index.html**

<pre class="wp-block-code"><code>&lt;!DOCTYPE html>
&lt;html lang="it">

&lt;head>
    &lt;meta charset="utf-8">
    &lt;meta http-equiv="X-UA-Compatible" content="IE=edge">
    &lt;meta name="viewport" content="width=device-width, initial-scale=1">
    &lt;!-- I 3 meta tags qua sopra DEVONO essere inseriti come primi -->
    &lt;meta name="description" content="">
    &lt;meta name="author" content="">

    &lt;title>Il mio primo tema&lt;/title>

    &lt;!-- Bootstrap core CSS -->
    &lt;link href="http://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">

&lt;/head>

&lt;body>

    &lt;nav class="navbar navbar-expand-lg navbar-light bg-light">
        &lt;div class="container">
            &lt;a class="navbar-brand" href="#">Il mio primo tema&lt;/a>
            &lt;button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                &lt;span class="navbar-toggler-icon">&lt;/span>
            &lt;/button>

            &lt;div class="collapse navbar-collapse" id="navbarSupportedContent">
                &lt;ul class="navbar-nav ml-auto">
                    &lt;li class="nav-item active">
                        &lt;a class="nav-link" href="#">Home &lt;span class="sr-only">(current)&lt;/span>&lt;/a>
                    &lt;/li>
                    &lt;li class="nav-item">
                        &lt;a class="nav-link" href="#">Chi sono&lt;/a>
                    &lt;/li>
                    &lt;li class="nav-item">
                        &lt;a class="nav-link" href="#">Blog&lt;/a>
                    &lt;/li>
                    &lt;li class="nav-item">
                        &lt;a class="nav-link" href="#">Contatti&lt;/a>
                    &lt;/li>
                &lt;/ul>
            &lt;/div>
        &lt;/div>
    &lt;/nav>


    &lt;div class="container mt-5">

        &lt;div class="row">
            &lt;!-- CONTENUTO -->
            &lt;div class="col-sm-8">

                &lt;!-- ARTICOLO -->
                &lt;div class="articolo-list">
                    &lt;!-- TITOLO -->
                    &lt;h2 class="">Il mio articolo&lt;/h2>
                    &lt;!-- META -->
                    &lt;p>15 luglio 2020 - Scritto da &lt;a href="#">Alberto&lt;/a>&lt;/p>
                    &lt;!-- CONTENT -->
                    &lt;p>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque et justo ultrices, blandit nulla in, convallis metus. Nullam et mollis orci.
                        Nulla magna augue, accumsan in metus ut, pulvinar facilisis libero. Aliquam erat volutpat. Nulla lectus tortor, lacinia id imperdiet ut, sagittis
                        consectetur magna. Maecenas laoreet sodales tristique. &#91;...]
                    &lt;/p>
                &lt;/div>
                &lt;!-- /ARTICOLO -->

                &lt;!-- ARTICOLO -->
                &lt;div class="articolo-list mt-5">
                    &lt;!-- TITOLO -->
                    &lt;h2 class="">Il mio articolo 2&lt;/h2>
                    &lt;!-- META -->
                    &lt;p>16 luglio 2020 - Scritto da &lt;a href="#">Alberto&lt;/a>&lt;/p>
                    &lt;!-- CONTENT -->
                    &lt;p>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque et justo ultrices, blandit nulla in, convallis metus. Nullam et mollis orci.
                        Nulla magna augue, accumsan in metus ut, pulvinar facilisis libero. Aliquam erat volutpat. Nulla lectus tortor, lacinia id imperdiet ut, sagittis
                        consectetur magna. Maecenas laoreet sodales tristique. &#91;...]
                    &lt;/p>
                &lt;/div>
                &lt;!-- /ARTICOLO -->

                &lt;!-- ARTICOLO -->
                &lt;div class="articolo-list mt-5">
                    &lt;!-- TITOLO -->
                    &lt;h2 class="">Il mio articolo 3&lt;/h2>
                    &lt;!-- META -->
                    &lt;p>17 luglio 2020 - Scritto da &lt;a href="#">Alberto&lt;/a>&lt;/p>
                    &lt;!-- CONTENT -->
                    &lt;p>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque et justo ultrices, blandit nulla in, convallis metus. Nullam et mollis orci.
                        Nulla magna augue, accumsan in metus ut, pulvinar facilisis libero. Aliquam erat volutpat. Nulla lectus tortor, lacinia id imperdiet ut, sagittis
                        consectetur magna. Maecenas laoreet sodales tristique. &#91;...]
                    &lt;/p>
                &lt;/div>
                &lt;!-- /ARTICOLO -->

                &lt;!-- NAVIGATION LINKS -->
                &lt;nav aria-label="Page navigation example">
                    &lt;ul class="pagination justify-content-center mb-5">
                        &lt;li class="page-item disabled">
                            &lt;a class="page-link" href="#" tabindex="-1" aria-disabled="true">Precedente&lt;/a>
                        &lt;/li>
                        &lt;li class="page-item">&lt;a class="page-link" href="#">1&lt;/a>&lt;/li>
                        &lt;li class="page-item">&lt;a class="page-link" href="#">2&lt;/a>&lt;/li>
                        &lt;li class="page-item">&lt;a class="page-link" href="#">3&lt;/a>&lt;/li>
                        &lt;li class="page-item">
                            &lt;a class="page-link" href="#">Successivo&lt;/a>
                        &lt;/li>
                    &lt;/ul>
                &lt;/nav>
                &lt;!-- /NAVIGATION LINKS -->
            &lt;/div>
            &lt;!-- /CONTENUTO -->

            &lt;!-- SIDEBAR -->
            &lt;div class="col-sm-3 col-sm-offset-1 blog-sidebar">
                &lt;div>
                    &lt;h4>Chi sono&lt;/h4>
                    &lt;p>Etiam porta &lt;em>sem malesuada magna&lt;/em> mollis euismod. Cras mattis consectetur purus sit amet fermentum. Aenean lacinia bibendum nulla sed consectetur.&lt;/p>
                &lt;/div>
                &lt;div>
                    &lt;h4>Ultimi articoli&lt;/h4>
                    &lt;ol class="list-unstyled">
                        &lt;li>&lt;a href="#">Il mio articolo 1&lt;/a>&lt;/li>
                        &lt;li>&lt;a href="#">Il mio articolo 2&lt;/a>&lt;/li>
                        &lt;li>&lt;a href="#">Il mio articolo 3&lt;/a>&lt;/li>

                    &lt;/ol>
                &lt;/div>
                &lt;div>
                    &lt;h4>Social&lt;/h4>
                    &lt;ol class="list-unstyled">
                        &lt;li>&lt;a href="#">GitHub&lt;/a>&lt;/li>
                        &lt;li>&lt;a href="#">Twitter&lt;/a>&lt;/li>
                        &lt;li>&lt;a href="#">Facebook&lt;/a>&lt;/li>
                    &lt;/ol>
                &lt;/div>
            &lt;/div>
            &lt;!-- /SIDEBAR -->

        &lt;/div>&lt;!-- /.row -->

    &lt;/div>&lt;!-- /.container -->

    &lt;footer>
        &lt;div class="container text-center mb-5">
            &lt;p>Sito realizzato da &lt;a href="https://albertoreineri.it">Specialista WP!&lt;/a>&lt;/p>
        &lt;/div>
    &lt;/footer>


    &lt;!-- Bootstrap core JavaScript
    ================================================== -->
    &lt;!-- Placed at the end of the document so the pages load faster -->
    &lt;script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js">&lt;/script>
    &lt;script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js">&lt;/script>
&lt;/body>

&lt;/html></code></pre>

Se ora&nbsp;**salvi&nbsp;**e&nbsp;**_refreshi&nbsp;_**la home del sito vedrai del contenuto!

La pagina è commentata, quindi dovresti riuscire a capire bene il codice al suo interno.

_Ricorda sempre di commentare il codice indicando cosa stai facendo, potrà aiutare i tuoi collaboratori ma anche il te stesso del futuro quando ritornerà al codice dopo molto tempo!_

**Ora procediamo con la creazione del tema!**

## DIVIDERE IN SEZIONI

Ora esiste solamente index.php, ma noi vogliamo creare un**&nbsp;tema vero e proprio**, che avrà delle parti di layout che si&nbsp;**ripeteranno&nbsp;**spesso e altre parti da aggiornare&nbsp;**dinamicamente**.

Procediamo quindi a**&nbsp;dividere il layout**&nbsp;del nostro sito in quattro sezioni:

  * header.php
  * footer.php
  * sidebar.php
  * content.php

**Creiamo&nbsp;**questi**&nbsp;quattro file**&nbsp;nella cartella del nostro tema ed andiamo a&nbsp;**spezzettare la index.php**&nbsp;in questo modo:

**heder.php**

<pre class="wp-block-code"><code>&lt;!DOCTYPE html&gt;
&lt;html lang="it"&gt;

&lt;head&gt;
    &lt;meta charset="utf-8"&gt;
    &lt;meta http-equiv="X-UA-Compatible" content="IE=edge"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1"&gt;
    &lt;!-- I 3 meta tags qua sopra DEVONO essere inseriti come primi --&gt;
    &lt;meta name="description" content=""&gt;
    &lt;meta name="author" content=""&gt;

    &lt;title&gt;Il mio primo tema&lt;/title&gt;

    &lt;!-- Bootstrap core CSS --&gt;
    &lt;link href="http://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet"&gt;

&lt;/head&gt;

&lt;body&gt;

    &lt;nav class="navbar navbar-expand-lg navbar-light bg-light"&gt;
        &lt;div class="container"&gt;
            &lt;a class="navbar-brand" href="#"&gt;Il mio primo tema&lt;/a&gt;
            &lt;button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"&gt;
                &lt;span class="navbar-toggler-icon"&gt;&lt;/span&gt;
            &lt;/button&gt;

            &lt;div class="collapse navbar-collapse" id="navbarSupportedContent"&gt;
                &lt;ul class="navbar-nav ml-auto"&gt;
                    &lt;li class="nav-item active"&gt;
                        &lt;a class="nav-link" href="#"&gt;Home &lt;span class="sr-only"&gt;(current)&lt;/span&gt;&lt;/a&gt;
                    &lt;/li&gt;
                    &lt;li class="nav-item"&gt;
                        &lt;a class="nav-link" href="#"&gt;Chi sono&lt;/a&gt;
                    &lt;/li&gt;
                    &lt;li class="nav-item"&gt;
                        &lt;a class="nav-link" href="#"&gt;Blog&lt;/a&gt;
                    &lt;/li&gt;
                    &lt;li class="nav-item"&gt;
                        &lt;a class="nav-link" href="#"&gt;Contatti&lt;/a&gt;
                    &lt;/li&gt;
                &lt;/ul&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/nav&gt;


    &lt;div class="container mt-5"&gt;

        &lt;div class="row"&gt;</code></pre>

**footer.php**

<pre class="wp-block-code"><code>
            &lt;/div>&lt;!-- /.row -->

&lt;/div>&lt;!-- /.container -->

    &lt;footer>
        &lt;div class="container text-center mb-5">
            &lt;p>Sito realizzato da &lt;a href="https://albertoreineri.it">Specialista WP!&lt;/a>&lt;/p>
        &lt;/div>
    &lt;/footer>


    &lt;!-- Bootstrap core JavaScript
    ================================================== -->
    &lt;!-- Placed at the end of the document so the pages load faster -->
    &lt;script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js">&lt;/script>
    &lt;script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js">&lt;/script>
&lt;/body>

&lt;/html></code></pre>

**sidebar.php**

<pre class="wp-block-code"><code>            &lt;!-- SIDEBAR --&gt;
            &lt;div class="col-sm-3 col-sm-offset-1 blog-sidebar"&gt;
                &lt;div&gt;
                    &lt;h4&gt;Chi sono&lt;/h4&gt;
                    &lt;p&gt;Etiam porta &lt;em&gt;sem malesuada magna&lt;/em&gt; mollis euismod. Cras mattis consectetur purus sit amet fermentum. Aenean lacinia bibendum nulla sed consectetur.&lt;/p&gt;
                &lt;/div&gt;
                &lt;div&gt;
                    &lt;h4&gt;Ultimi articoli&lt;/h4&gt;
                    &lt;ol class="list-unstyled"&gt;
                        &lt;li&gt;&lt;a href="#"&gt;Il mio articolo 1&lt;/a&gt;&lt;/li&gt;
                        &lt;li&gt;&lt;a href="#"&gt;Il mio articolo 2&lt;/a&gt;&lt;/li&gt;
                        &lt;li&gt;&lt;a href="#"&gt;Il mio articolo 3&lt;/a&gt;&lt;/li&gt;

                    &lt;/ol&gt;
                &lt;/div&gt;
                &lt;div&gt;
                    &lt;h4&gt;Social&lt;/h4&gt;
                    &lt;ol class="list-unstyled"&gt;
                        &lt;li&gt;&lt;a href="#"&gt;GitHub&lt;/a&gt;&lt;/li&gt;
                        &lt;li&gt;&lt;a href="#"&gt;Twitter&lt;/a&gt;&lt;/li&gt;
                        &lt;li&gt;&lt;a href="#"&gt;Facebook&lt;/a&gt;&lt;/li&gt;
                    &lt;/ol&gt;
                &lt;/div&gt;
            &lt;/div&gt;
            &lt;!-- /SIDEBAR --&gt;</code></pre>

**content.php**

<pre class="wp-block-code"><code>

            &lt;!-- CONTENUTO --&gt;
            &lt;div class="col-sm-8"&gt;

                &lt;!-- ARTICOLO --&gt;
                &lt;div class="articolo-list"&gt;
                    &lt;!-- TITOLO --&gt;
                    &lt;h2 class=""&gt;Il mio articolo&lt;/h2&gt;
                    &lt;!-- META --&gt;
                    &lt;p&gt;15 luglio 2020 - Scritto da &lt;a href="#"&gt;Alberto&lt;/a&gt;&lt;/p&gt;
                    &lt;!-- CONTENT --&gt;
                    &lt;p&gt;
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque et justo ultrices, blandit nulla in, convallis metus. Nullam et mollis orci.
                        Nulla magna augue, accumsan in metus ut, pulvinar facilisis libero. Aliquam erat volutpat. Nulla lectus tortor, lacinia id imperdiet ut, sagittis
                        consectetur magna. Maecenas laoreet sodales tristique. &#91;...]
                    &lt;/p&gt;
                &lt;/div&gt;
                &lt;!-- /ARTICOLO --&gt;

                &lt;!-- ARTICOLO --&gt;
                &lt;div class="articolo-list mt-5"&gt;
                    &lt;!-- TITOLO --&gt;
                    &lt;h2 class=""&gt;Il mio articolo 2&lt;/h2&gt;
                    &lt;!-- META --&gt;
                    &lt;p&gt;16 luglio 2020 - Scritto da &lt;a href="#"&gt;Alberto&lt;/a&gt;&lt;/p&gt;
                    &lt;!-- CONTENT --&gt;
                    &lt;p&gt;
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque et justo ultrices, blandit nulla in, convallis metus. Nullam et mollis orci.
                        Nulla magna augue, accumsan in metus ut, pulvinar facilisis libero. Aliquam erat volutpat. Nulla lectus tortor, lacinia id imperdiet ut, sagittis
                        consectetur magna. Maecenas laoreet sodales tristique. &#91;...]
                    &lt;/p&gt;
                &lt;/div&gt;
                &lt;!-- /ARTICOLO --&gt;

                &lt;!-- ARTICOLO --&gt;
                &lt;div class="articolo-list mt-5"&gt;
                    &lt;!-- TITOLO --&gt;
                    &lt;h2 class=""&gt;Il mio articolo 3&lt;/h2&gt;
                    &lt;!-- META --&gt;
                    &lt;p&gt;17 luglio 2020 - Scritto da &lt;a href="#"&gt;Alberto&lt;/a&gt;&lt;/p&gt;
                    &lt;!-- CONTENT --&gt;
                    &lt;p&gt;
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque et justo ultrices, blandit nulla in, convallis metus. Nullam et mollis orci.
                        Nulla magna augue, accumsan in metus ut, pulvinar facilisis libero. Aliquam erat volutpat. Nulla lectus tortor, lacinia id imperdiet ut, sagittis
                        consectetur magna. Maecenas laoreet sodales tristique. &#91;...]
                    &lt;/p&gt;
                &lt;/div&gt;
                &lt;!-- /ARTICOLO --&gt;

                &lt;!-- NAVIGATION LINKS --&gt;
                &lt;nav aria-label="Page navigation example"&gt;
                    &lt;ul class="pagination justify-content-center mb-5"&gt;
                        &lt;li class="page-item disabled"&gt;
                            &lt;a class="page-link" href="#" tabindex="-1" aria-disabled="true"&gt;Precedente&lt;/a&gt;
                        &lt;/li&gt;
                        &lt;li class="page-item"&gt;&lt;a class="page-link" href="#"&gt;1&lt;/a&gt;&lt;/li&gt;
                        &lt;li class="page-item"&gt;&lt;a class="page-link" href="#"&gt;2&lt;/a&gt;&lt;/li&gt;
                        &lt;li class="page-item"&gt;&lt;a class="page-link" href="#"&gt;3&lt;/a&gt;&lt;/li&gt;
                        &lt;li class="page-item"&gt;
                            &lt;a class="page-link" href="#"&gt;Successivo&lt;/a&gt;
                        &lt;/li&gt;
                    &lt;/ul&gt;
                &lt;/nav&gt;
                &lt;!-- /NAVIGATION LINKS --&gt;
            &lt;/div&gt;
            &lt;!-- /CONTENUTO --&gt;</code></pre>

Ora non ci resta che richiamare i vari pezzi di contenuto nella index.php, in modo da montare il sito, in questo modo:

**index.php**

<pre class="wp-block-code"><code>&lt;?php get_header(); ?&gt;

&lt;?php get_template_part( 'content', get_post_format() ); ?&gt;

&lt;?php get_sidebar(); ?&gt;

&lt;?php get_footer(); ?&gt;</code></pre>

Ora la nostra index.php è&nbsp;**molto più semplice**&nbsp;no?

Le funzioni&nbsp;_get_header()_,_&nbsp;get_sidebar()&nbsp;_e&nbsp;_get_footer()_&nbsp;vanno automaticamente ad inserire i fine&nbsp;_header.php_,&nbsp;_sidebar.php&nbsp;_e_&nbsp;footer.php_.

Per inserire un file diverso abbiamo utilizzato la funzione&nbsp;_get\_template\_part()_&nbsp;indicando il nome del file php da cui prendere il codice.

Nella programmazione è molto importante&nbsp;**suddividere i contenuti&nbsp;**in parti più piccole, in modo da rendere i file più semplici e facilmente leggibili.

## IMPOSTAZIONI PRINCIPALI

Vediamo ora come&nbsp;**recuperare&nbsp;**alcune delle&nbsp;**informazioni principali**&nbsp;del nostro sito.

Nel&nbsp;**backend&nbsp;**puoi impostare un nome e una descrizione al tuo sito, nella sezione “**Impostazioni – Generali**“.<figure class="wp-block-image size-full">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-14-1.png" alt="" class="wp-image-317" /> </figure>

**Inserisci&nbsp;**il&nbsp;**titolo&nbsp;**del sito e un&nbsp;**motto**. Ora vediamo come recuperare questi dati nel&nbsp;**frontend**!

Andiamo in&nbsp;**header.php**&nbsp;e modifichiamo il&nbsp;**titolo&nbsp;**nella navbar del sito.

Eliminiamo quindi la scritta “**Il&nbsp;mio&nbsp;primo&nbsp;tema**” e la sostituiamo con

<pre class="wp-block-code"><code>&lt;?php echo get_bloginfo( 'name' ); ?&gt;</code></pre>

In questo modo&nbsp;**il nome del sito sarà dinamico.**

Possiamo anche inserire il&nbsp;**motto&nbsp;**del sito con questa funzione:

<pre class="wp-block-code"><code>&lt;?php echo get_bloginfo( 'description' ); ?&gt;</code></pre>

Infine possiamo impostare&nbsp;**i link alla home del sito**&nbsp;sul titolo, in questo modo:

<pre class="wp-block-code"><code>&lt;a class="navbar-brand" href="&lt;?php echo esc_url( home_url( '/' ) ); ?&gt;"&gt;&lt;?php echo get_bloginfo( 'name' ); ?&gt;&lt;/a&gt;</code></pre>

Molto bene!&nbsp;**Abbiamo iniziato a rendere dinamico il nostro sito!**&nbsp;Ora buttiamoci in qualcosa di più complicato ma&nbsp;**fondamentale**!

## IL LOOP

**Il loop sta alla base di ogni tema WordPress**. Consente di inserire una serie di dati recuperandoli dal database.

Possiamo utilizzarlo per inserire l’elenco degli articoli, delle pagine, di una determinata categoria, di sezioni speciali etc.

Tutti i contenuti in WordPress vengono generati da loop! Possiamo dire che&nbsp;**è la funzione più importante di tutte!**

Nel&nbsp;**backend&nbsp;**al momento abbiamo solamente&nbsp;**l’articolo&nbsp;**di default: “Ciao mondo!”, vediamo come&nbsp;**farlo comparire nella home page del sito.**

Il&nbsp;**loop&nbsp;**di WordPress è molto semplice:

<pre class="wp-block-code"><code>&lt;?php
if (have_posts()) :
    while (have_posts()) : the_post();
?&gt;

        &lt;!-- Contenuto del loop --&gt;

&lt;?php
    endwhile;
endif;
?&gt;</code></pre>

Direi che&nbsp;**si spiega**&nbsp;abbastanza&nbsp;**da solo**.

Se ci sono dei post allora inizia il loop, nel quale inserisce i post finché ce ne sono.

Proviamo ad&nbsp;**inserire il loop nella nostra home page**, in index.php

**index.php**

<pre class="wp-block-code"><code>&lt;?php get_header(); ?&gt;

&lt;?php
if (have_posts()) :
    while (have_posts()) : the_post();

        get_template_part('content', get_post_format());

    endwhile;
endif;
?&gt;

&lt;?php get_sidebar(); ?&gt;

&lt;?php get_footer(); ?&gt;</code></pre>

Ora&nbsp;**rendiamo dinamico il contenuto**&nbsp;all’interno del file content.php

**content.php**

<pre class="wp-block-code"><code>

            &lt;!-- CONTENUTO --&gt;
            &lt;div class="col-sm-8"&gt;

                &lt;!-- ARTICOLO --&gt;
                &lt;div class="articolo-list"&gt;
                    &lt;!-- TITOLO --&gt;
                    &lt;h2 class=""&gt;&lt;?php the_title(); ?&gt;&lt;/h2&gt;
                    &lt;!-- META --&gt;
                    &lt;p&gt;&lt;?php the_date('d/m/Y'); ?&gt;  - Scritto da &lt;a href="#"&gt;&lt;?php the_author(); ?&gt;&lt;/a&gt;&lt;/p&gt;
                    &lt;!-- CONTENT --&gt;
                    &lt;?php the_content(); ?&gt;

                &lt;/div&gt;
                &lt;!-- /ARTICOLO --&gt;

                &lt;!-- NAVIGATION LINKS --&gt;
                &lt;nav aria-label="Page navigation example"&gt;
                    &lt;ul class="pagination justify-content-center mb-5"&gt;
                        &lt;li class="page-item disabled"&gt;
                            &lt;a class="page-link" href="#" tabindex="-1" aria-disabled="true"&gt;Precedente&lt;/a&gt;
                        &lt;/li&gt;
                        &lt;li class="page-item"&gt;&lt;a class="page-link" href="#"&gt;1&lt;/a&gt;&lt;/li&gt;
                        &lt;li class="page-item"&gt;&lt;a class="page-link" href="#"&gt;2&lt;/a&gt;&lt;/li&gt;
                        &lt;li class="page-item"&gt;&lt;a class="page-link" href="#"&gt;3&lt;/a&gt;&lt;/li&gt;
                        &lt;li class="page-item"&gt;
                            &lt;a class="page-link" href="#"&gt;Successivo&lt;/a&gt;
                        &lt;/li&gt;
                    &lt;/ul&gt;
                &lt;/nav&gt;
                &lt;!-- /NAVIGATION LINKS --&gt;
            &lt;/div&gt;
            &lt;!-- /CONTENUTO --&gt;</code></pre>

Benissimo! Ora in home page compare solamente il nostro primo articolo.

Prova a&nbsp;**creare un nuovo articolo**&nbsp;nel backend e a pubblicarlo, lo vedrai comparire anche nella home page!

**Grande! Stai iniziando a fare sul serio con WordPress!**

Se vuoi continuare a sviluppare il tuo primo tema WordPress da zero prosegui con la&nbsp;[parte 2][5]!

<p class="has-text-align-right">
  <a href="https://albertoreineri.it/guide/creare-un-tema-wordpress-da-zero-parte-2/">Parte 2 >></a>
</p>

 [1]: https://albertoreineri.it.local/inizia-qui/inizia-qui-principiante/
 [2]: https://albertoreineri.it/guide/creare-un-tema-wordpress-da-zero-parte-3/
 [3]: https://albertoreineri.it/guide/le-basi-dellhtml/
 [4]: https://albertoreineri.it/guide/le-basi-di-bootstrap/
 [5]: https://albertoreineri.it/guide/creare-un-tema-wordpress-da-zero-parte-2/