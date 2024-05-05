---
title: Gulp.js in un tema WordPress
author: Alberto
type: post
date: 2019-09-30T20:13:00+00:00
url: /gulp-js-in-un-tema-wordpress/
nectar_blog_post_view_count:
  - 39
tags:
  - Guide
  - Web Dev

---
Da qualche tempo sto lavorando su&nbsp;**progetti abbastanza grandi**&nbsp;e non è sempre facile riuscire a gestire il tutto senza perdersi nei&nbsp;**migliaia di file e cartelle**&nbsp;contenuti nel progetto.

**L’organizzazione del codice**&nbsp;è una parte fondamentale per lo sviluppo di software, che sia web, desktop o mobile.

Fortunatamente oggi possiamo utilizzare degli strumenti in grado di&nbsp;**aiutarci nel processo di sviluppo&nbsp;**e gestione del progetto.

Uno di questi è**&nbsp;Gulp.js!**

## Cos’è Gulp.js {.wp-block-heading}

Gulp è un&nbsp;**task runner**, cioè un programma che permette di&nbsp;**automatizzare una serie di operazioni**&nbsp;ripetitive e costanti, come minificare codice CSS e JS, effettuare refresh ad ogni salvataggio, sincronizzare pagine web, ottimizzare le immagini e molto altro.

_**Per semplificare**_&nbsp;una volta impostato correttamente Gulp all’interno del mio progetto, ogni volta che salvo un file in automatico Gulp fa un check sull’operazione appena effettuata (il salvataggio) ed agisce di conseguenza, in questo caso fa un refresh del browser.

Se invece modifico un file CSS, al salvataggio Gulp minimizzerà il file e farà il refresh del browser!

Prova a pensare in un progetto che richiede mesi di sviluppo, poter evitare di&nbsp;_refresshare&nbsp;_il browser ogni volta, compilare i file SASS, ottimizzare le immagini etc. permette agli sviluppatori di&nbsp;**risparmiare moltissimo tempo**, o perlomeno concentrarsi su altro piuttosto che su azioni banali e ripetitive!

## Gulp e WordPress {.wp-block-heading}

Il bello di Gulp è che può essere utilizzato in&nbsp;**qualsiasi tipo di progetto**, anche durante lo sviluppo di un&nbsp;**tema&nbsp;**o&nbsp;**plugin&nbsp;**per&nbsp;**WordPress**, andando a&nbsp;**velocizzare&nbsp;**molto i tempi di programmazione!

Se vuoi installare ed&nbsp;**iniziare&nbsp;**ad utilizzare Gulp ti consiglio questo articolo:&nbsp;<https://css-tricks.com/gulp-for-beginners/>&nbsp;. Io ho iniziato da qui!

## Il mio Gulp per WordPress! {.wp-block-heading}

Se vuoi una&nbsp;**base di partenza**&nbsp;per configurare&nbsp;**Gulp&nbsp;**nel tuo progetto puoi guardare sul&nbsp;<a href="https://github.com/alby-dev/" target="_blank" rel="noreferrer noopener">mio profilo github</a>, ho inserito&nbsp;<a href="https://github.com/alby-dev/gulp-for-wordpress" target="_blank" rel="noreferrer noopener">il mio file</a>&nbsp;di&nbsp;**configurazione base per Gulp in WordPress.**

Nel mio ultimo progetto tramite&nbsp;**Gulp&nbsp;**ho effettuato queste&nbsp;**automazioni**:

  * Effettuare un&nbsp;**refresh&nbsp;**ad ogni modifica di qualsiasi file
  * Ottimizzare le&nbsp;**immagini**
  * Unire tutti i file&nbsp;**SCSS&nbsp;**in uno solo, compilarlo e minificarlo
  * Unire tutti i file&nbsp;**JS&nbsp;**in uno solo e minificarlo

Per poter utilizzare&nbsp;**Gulp&nbsp;**occorre sdoppiare la cartella con le risorse del sito. Una sarà la cartella di sviluppo, solidamente chiamata “**src**“, l’altra sarà quella che verrà pubblicata, chiamata “**assets**“

Su github puoi trovare il mio file di configurazione per gestire i task&nbsp;**Gulp all’interno di un tema WordPress.**

Per&nbsp;**iniziare&nbsp;**ad utilizzarlo devi solamente copiare il mio gulpfile.js all’interno del tuo tema e dare questo comando dalla CLI:

<pre class="wp-block-code"><code>npm install --save-dev gulp gulp-imagemin gulp-uglify gulp-sass browser-sync del gulp-concat gulp-clean</code></pre>

Ora non ti resta che**&nbsp;modificare la riga 3**&nbsp;del file inserendo il path del tuo progetto WordPress.

Spero di essere riuscito ad invogliarti a&nbsp;**utilizzare questo strumento.&nbsp;**Sebbene sia un po’ complicato da configurare, sono sicuro che una volta che l’avrai capito a fondo&nbsp;**non potrai più farne a meno!**

Fammi sapere cosa ne pensi nei&nbsp;**commenti&nbsp;**e&nbsp;**buon codice!**