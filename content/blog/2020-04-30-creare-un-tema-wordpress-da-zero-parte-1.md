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
**WordPress **è una piattaforma **fantastica**! Permette di creare** siti web di ogni tipo** in maniera semplice e **veloce**, grazie all’infinita quantità di **temi **e **plugin **disponibili, moltissimi dei quali in maniera gratuita.

Però **quando si vuole fare il salto di livello** ed avere un sito web veramente **performante**, allora conviene utilizzare un** tema sviluppato da zero**, in grado di implementare tutte le funzioni necessarie nella maniera più performante!

**Niente errori** in console, niente stringhe in inglese, niente codici sparsi in giro per il sito, niente css e js inutili… Solo ciò che serve realmente, sviluppato nel modo corretto.

**Oggi vediamo come creare un tema WordPress da zero!**

Mettiti comodo e** prenditi il tuo tempo**, ci vorrà un po’, ma alla fine avrai realizzato **il tuo primo tema WordPress **funzionante e nel rispetto di tutte le best practice.

_**Partiremo da un’installazione di WordPress, se non sai come installare il CMS ti consiglio di seguire le guide per [Inizia Qui][1].**_

_Questo tutorial è suddiviso in 3 parti, alla fine potrai scaricare l’intero tema che creeremo insieme per confrontarlo e correggere eventuali errori. Ti consiglio di seguire le varie parti e scaricare il tema solo alla fine, ma se ti servisse prima lo puoi trovare sul fondo della [parte 3][2]._

## CREIAMO IL NOSTRO TEMA

Se apri la cartella del tuo sito **WordPress **noterai che all’interno sono presenti **3 cartelle**:

  * wp-admin
  * wp-content
  * wp-includes

A noi per il momento interessa solamente la “**wp-content**“, quindi iniziamo ad **aprirla**.

All’interno di wp-content apriamo ora la cartella “**themes**“, che come puoi intuire contiene** i temi del progetto.**

**Procediamo quindi a creare il nostro primo tema!**

Creiamo una **nuova cartella** e la chiamiamo “**il-mio-tema**“, dopodiché apriamo la cartella con **<a href="http://code.visualstudio.com/" rel="noreferrer noopener" target="_blank">VS Code</a>**. (Se non sai come fare questo passaggio visualizza le [guide per principianti][3])

Un **tema WordPress** per essere riconosciuto necessita solamente di** 2 file:**

  * style.css
  * index.php

**creiamo quindi questi 2 file all’interno della cartella “il-mio-tema”** e inseriamo questo codice in “**style.css**“, in modo da indicare a WordPress i dati del tema:

<pre class="wp-block-code"><code>/*
Theme Name: Il mio tema
Author: Specialista WP
Description: Il mio primo tema WordPress
Version: 0.0.1
*/</code></pre>

Puoi **sostituire **l’autore con il tuo nome, così come il nome del tema e la descrizione.

Se ora salvi il file CSS e vai nel backend di WordPress in “**Aspetto – Temi**” vedrai comparire il nostro tema!<figure class="wp-block-image size-full">
<img alt="" class="wp-image-316" decoding="async" src="/img/uploads/2022/03/image-12-2.png"/> </figure>

Puoi **attivare il tema **e _voilà_! Il tema è fatto!

Non è poi tanto complicato vero? Già, però ora il tema è **vuoto**, occorre riempirlo!

Inizia con l’inserire questo codice nella “**index.php**“, è un **layout di base** creato con [bootstrap ][4]sul quale andremo a costruire il nostro sito:

**index.html**

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

        &lt;div class="row"&gt;
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
                        consectetur magna. Maecenas laoreet sodales tristique. [...]
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
                        consectetur magna. Maecenas laoreet sodales tristique. [...]
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
                        consectetur magna. Maecenas laoreet sodales tristique. [...]
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
            &lt;!-- /CONTENUTO --&gt;

            &lt;!-- SIDEBAR --&gt;
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
            &lt;!-- /SIDEBAR --&gt;

        &lt;/div&gt;&lt;!-- /.row --&gt;

    &lt;/div&gt;&lt;!-- /.container --&gt;

    &lt;footer&gt;
        &lt;div class="container text-center mb-5"&gt;
            &lt;p&gt;Sito realizzato da &lt;a href=""&gt;Specialista WP!&lt;/a&gt;&lt;/p&gt;
        &lt;/div&gt;
    &lt;/footer&gt;


    &lt;!-- Bootstrap core JavaScript
    ================================================== --&gt;
    &lt;!-- Placed at the end of the document so the pages load faster --&gt;
    &lt;script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"&gt;&lt;/script&gt;
    &lt;script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"&gt;&lt;/script&gt;
&lt;/body&gt;

&lt;/html&gt;</code></pre>

Se ora **salvi **e **_refreshi _**la home del sito vedrai del contenuto!

La pagina è commentata, quindi dovresti riuscire a capire bene il codice al suo interno.

_Ricorda sempre di commentare il codice indicando cosa stai facendo, potrà aiutare i tuoi collaboratori ma anche il te stesso del futuro quando ritornerà al codice dopo molto tempo!_

**Ora procediamo con la creazione del tema!**

## DIVIDERE IN SEZIONI

Ora esiste solamente index.php, ma noi vogliamo creare un** tema vero e proprio**, che avrà delle parti di layout che si **ripeteranno **spesso e altre parti da aggiornare **dinamicamente**.

Procediamo quindi a** dividere il layout** del nostro sito in quattro sezioni:

  * header.php
  * footer.php
  * sidebar.php
  * content.php

**Creiamo **questi** quattro file** nella cartella del nostro tema ed andiamo a **spezzettare la index.php** in questo modo:

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
            &lt;/div&gt;&lt;!-- /.row --&gt;

&lt;/div&gt;&lt;!-- /.container --&gt;

    &lt;footer&gt;
        &lt;div class="container text-center mb-5"&gt;
            &lt;p&gt;Sito realizzato da &lt;a href=""&gt;Specialista WP!&lt;/a&gt;&lt;/p&gt;
        &lt;/div&gt;
    &lt;/footer&gt;


    &lt;!-- Bootstrap core JavaScript
    ================================================== --&gt;
    &lt;!-- Placed at the end of the document so the pages load faster --&gt;
    &lt;script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"&gt;&lt;/script&gt;
    &lt;script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"&gt;&lt;/script&gt;
&lt;/body&gt;

&lt;/html&gt;</code></pre>

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
                        consectetur magna. Maecenas laoreet sodales tristique. [...]
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
                        consectetur magna. Maecenas laoreet sodales tristique. [...]
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
                        consectetur magna. Maecenas laoreet sodales tristique. [...]
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

Ora la nostra index.php è **molto più semplice** no?

Le funzioni _get_header()_,_ get_sidebar() _e _get_footer()_ vanno automaticamente ad inserire i fine _header.php_, _sidebar.php _e_ footer.php_.

Per inserire un file diverso abbiamo utilizzato la funzione _get\_template\_part()_ indicando il nome del file php da cui prendere il codice.

Nella programmazione è molto importante **suddividere i contenuti **in parti più piccole, in modo da rendere i file più semplici e facilmente leggibili.

## IMPOSTAZIONI PRINCIPALI

Vediamo ora come **recuperare **alcune delle **informazioni principali** del nostro sito.

Nel **backend **puoi impostare un nome e una descrizione al tuo sito, nella sezione “**Impostazioni – Generali**“.<figure class="wp-block-image size-full">
<img alt="" class="wp-image-317" decoding="async" src="/img/uploads/2022/03/image-14-1.png"/> </figure>

**Inserisci **il **titolo **del sito e un **motto**. Ora vediamo come recuperare questi dati nel **frontend**!

Andiamo in **header.php** e modifichiamo il **titolo **nella navbar del sito.

Eliminiamo quindi la scritta “**Il mio primo tema**” e la sostituiamo con

<pre class="wp-block-code"><code>&lt;?php echo get_bloginfo( 'name' ); ?&gt;</code></pre>

In questo modo **il nome del sito sarà dinamico.**

Possiamo anche inserire il **motto **del sito con questa funzione:

<pre class="wp-block-code"><code>&lt;?php echo get_bloginfo( 'description' ); ?&gt;</code></pre>

Infine possiamo impostare **i link alla home del sito** sul titolo, in questo modo:

<pre class="wp-block-code"><code>&lt;a class="navbar-brand" href="&lt;?php echo esc_url( home_url( '/' ) ); ?&gt;"&gt;&lt;?php echo get_bloginfo( 'name' ); ?&gt;&lt;/a&gt;</code></pre>

Molto bene! **Abbiamo iniziato a rendere dinamico il nostro sito!** Ora buttiamoci in qualcosa di più complicato ma **fondamentale**!

## IL LOOP

**Il loop sta alla base di ogni tema WordPress**. Consente di inserire una serie di dati recuperandoli dal database.

Possiamo utilizzarlo per inserire l’elenco degli articoli, delle pagine, di una determinata categoria, di sezioni speciali etc.

Tutti i contenuti in WordPress vengono generati da loop! Possiamo dire che **è la funzione più importante di tutte!**

Nel **backend **al momento abbiamo solamente **l’articolo **di default: “Ciao mondo!”, vediamo come **farlo comparire nella home page del sito.**

Il **loop **di WordPress è molto semplice:

<pre class="wp-block-code"><code>&lt;?php
if (have_posts()) :
    while (have_posts()) : the_post();
?&gt;

        &lt;!-- Contenuto del loop --&gt;

&lt;?php
    endwhile;
endif;
?&gt;</code></pre>

Direi che **si spiega** abbastanza **da solo**.

Se ci sono dei post allora inizia il loop, nel quale inserisce i post finché ce ne sono.

Proviamo ad **inserire il loop nella nostra home page**, in index.php

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

Ora **rendiamo dinamico il contenuto** all’interno del file content.php

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

Prova a **creare un nuovo articolo** nel backend e a pubblicarlo, lo vedrai comparire anche nella home page!

**Grande! Stai iniziando a fare sul serio con WordPress!**

Se vuoi continuare a sviluppare il tuo primo tema WordPress da zero prosegui con la [parte 2][5]!

<p class="has-text-align-right">
<a href="/creare-un-tema-wordpress-da-zero-parte-2/">Parte 2 &gt;&gt;</a>
</p>

 [1]: /inizia-qui/
 [2]: /creare-un-tema-wordpress-da-zero-parte-3/
 [3]: /le-basi-dellhtml/
 [4]: /le-basi-di-bootstrap/
 [5]: /creare-un-tema-wordpress-da-zero-parte-2/