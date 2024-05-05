---
title: 'Certificato SSL: come reindirizzare http a https'
author: Alberto
type: post
date: 2019-11-30T20:06:00+00:00
url: /certificato-ssl-come-reindirizzare-http-a-https/
nectar_blog_post_view_count:
  - 35
tags:
  - Guide
  - Web Dev

---
Vediamo come installare un certificato SSL sul nostro sito e passare da http a https.

Vuoi rimuovere la scritta “**non sicuro**” che compare** vicino all’URL** del tuo sito? Allora questo articolo fa al caso tuo!

**Non **andremo ad approfondire che cos’è **l’HTTPS**, ma vedremo semplicemente come far funzionare il tuo sito in modo che sia sicuro.

La procedura è molto semplice, ti basterà seguire questi due passaggi:

## 1. Attivare l’SSL sul tuo spazio web

Entra nel **pannello di controllo** del tuo servizio di Hosting e cerca “**Attiva HTTPS**“, “**Attiva SSL**” o qualcosa di simile (varia a seconda del servizio).

Una volta trovata la sezione giusta **attiva il servizio**. **Può volerci qualche ora** prima che sia attivo.

Dopo qualche ora prova a collegarti al tuo sito digitando https://www.nomesito.it. Se tutto funziona correttamente vai al passaggio 2.

Se visualizzi degli **errori **probabilmente è perché hai dei link http per fogli di stile, immagini e file js. Prova a** sostituire l’http con https** in tutti i riferimenti a immagini, css e js, dovrebbe sistemarsi tutto.

Se utilizzi **[WordPress][1] **puoi utilizzare dei **plugin **che si occupano del problema, ad esempio<a href="https://it.wordpress.org/plugins/really-simple-ssl/" rel="noreferrer noopener" target="_blank"> Really Simple SSL</a> oppure <a href="https://it.wordpress.org/plugins/wp-force-ssl/" rel="noreferrer noopener" target="_blank">WP Force SSL</a>. Utilizzando questi plugin puoi saltare il punto 2, i plugin si occupano di tutto da soli

## 2. REDIRIGERE IL TRAFFICO VERSO HTTPS

Se hai effettuato correttamente il punto uno ora puoi aprire il file **.htaccess** presente nella root del tuo sito (se non c’è crealo) e inserire questo codice:

<pre class="wp-block-code"><code>RewriteEngine on

RewriteCond %{HTTP:X-Forwarded-Proto} !https

RewriteRule ^.*$ https://%{SERVER_NAME}%{REQUEST_URI} [L,R=301]</code></pre>

In questo modo tutte le chiamate al server verranno redirette verso **l’https**.

Se questo codice crea un errore circa i reindirizzamenti puoi sostituire 

<pre class="wp-block-code"><code>RewriteCond %{HTTP:X-Forwarded-Proto} !https</code></pre>

con

<pre class="wp-block-code"><code>RewriteCond %{HTTPS}  !=on.</code></pre>

Con questi semplici passaggi puoi installare un certificato SSL e redirigere il traffico da http a https, ottenendo un sito web più sicuro.

 [1]: /come-installare-e-personalizzare-un-tema-wordpress-2/