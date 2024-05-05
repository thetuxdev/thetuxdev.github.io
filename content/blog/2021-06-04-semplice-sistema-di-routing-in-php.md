---
title: Semplice sistema di routing in PHP
author: Alberto
type: post
date: 2021-06-04T17:53:11+00:00
url: /semplice-sistema-di-routing-in-php/
nectar_blog_post_view_count:
  - 131
tags:
  - Guide
  - PHP

---
Usare un sistema di routing in php può portare grandi vantaggi a un progetto.

Gli&nbsp;**URL&nbsp;**delle pagine web di un sito sono**&nbsp;molto importanti**, sia per i motori di ricerca, sia per gli utenti, che sempre di più li usano per navigare velocemente all’interno di un sito.

_Se per esempio l’url di una pagina che elenca una serie di articoli è http://www.nomesito.it/2019/05/15 l’utente, se conosce minimamente come funziona un browser ed il web, saprà già che se cancella il “15” dall’URL vedrà l’elenco degli articoli del mese, se cancella “05” vedrà l’elenco degli articoli dell’anno e così via._

Questo fa parte delle convenzioni che sono venute a crearsi nel corso di questi anni, e che è bene rispettare nella creazione di un sito web.

Una cosa che non mi è mai piaciuta dei primi siti web che realizzavo era vedere il “.php” alla fine dell’URL. Al giorno d’oggi sa veramente di poco professionale.

**Ma è possibile creare degli URL custom e SEO friendly senza utilizzare un CMS o un framework?**

La risposta è**&nbsp;assolutamente SI!!!**

Se sei interessato ad una semplice soluzione per “nascondere” il “.php” alla fine dell’URL leggi questo&nbsp;[articolo][1].

Se vuoi imparare ad utilizzare un semplice sistema di routing in PHP ecco come puoi fare.

## CREARE UN SISTEMA DI GESTIONE DEL ROUTING DEL SITO<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio">

<div class="wp-block-embed__wrapper">
</div></figure>

Andremo a&nbsp;**dirigere tutto il traffico alla index.php e poi eseguiremo un “routing” alla pagina che vogliamo**.

### Dirigere tutto il traffico alla index.php

Aprite il file .htaccess (se non esiste createlo) e inserite il seguente codice:

<pre class="wp-block-code"><code>RewriteEngine On

RewriteBase /

RewriteCond %{REQUEST_FILENAME} !-d

RewriteCond %{REQUEST_FILENAME} !-f

RewriteRule ^(.+)$ index.php &#91;QSA,L]</code></pre>

In questo modo qualsiasi richiesta verrà fatta al server questo aprirà il file “index.php”

### Creare un sistema di routing

Nel file index.php inserisci il seguente codice:

<pre class="wp-block-code"><code>&lt;?php

$request = $_SERVER&#91;'REQUEST_URI'];

switch ($request) {
    case '/' :
        require __DIR__ . '/views/index.php';
        break;
    case '' :
        require __DIR__ . '/views/index.php';
        break;
    case '/chi-siamoi' :
        require __DIR__ . '/views/chi-siamo.php';
        break;
    default:
        require __DIR__ . '/views/404.php';
        break;
}</code></pre>

In questo modo si salverà nella variabile&nbsp;**$request**&nbsp;la richiesta inviata al server (la parte dell’url dopo “www.nomesito.it”).

Dopodiché effettuando una switch si può richiamare la pagina corrispondente alla richiesta nell’URL.&nbsp;

Nei casi in cui la richiesta sia vuota oppure uno “**/**” allora si rimanda alla&nbsp;**homepage**, altrimenti si può rimandare alla pagina corretta.

Nell’esempio ho creato una cartella “**views**” nella root del sito nella quale saranno presenti i file delle singole pagine. In questo modo il codice sarà anche più snello e capibile.

Infine è già presente anche la gestione dell’errore&nbsp;**404**, senza dover inserire altro codice nell’htaccess.

### Creare le views

A questo punto non ci resta che creare i file per le nostre&nbsp;**views**, cioè le pagine visualizzate dall’utente.

Potete creare semplicemente i seguenti file con il seguente codice in ognuno di essi:

**/views/index.php**

<pre class="wp-block-code"><code>&lt;h1&gt;Home Page&lt;/h1&gt;</code></pre>

**/views/chi-siamo.php**

<pre class="wp-block-code"><code>&lt;h1&gt;Chi siamo&lt;/h1&gt;</code></pre>

**/views/404.php**

<pre class="wp-block-code"><code>&lt;h1&gt;Errore 404&lt;/h1&gt;</code></pre>

E voilà! Avrete un sistema di routing in PHP semplice da gestire ma funzionale.

Questo sistema&nbsp;è alla base di&nbsp;<a href="https://orange.albertoreineri.it/" target="_blank" rel="noreferrer noopener">Orange CMS</a>, il mio CMS realizzato in php. Ampliandolo a dovere è possibile raggiungere risultati molto soddisfacenti.

Spero possa esservi di aiuto.

_Buon codice!_

Se l’articolo ti è stato&nbsp;**utile&nbsp;**lasciami un commento oppure condividilo sui social, lo&nbsp;**apprezzerei&nbsp;**molto!

 [1]: https://albertoreineri.it/guide/nascondere-lestensione-alla-fine-dellurl/