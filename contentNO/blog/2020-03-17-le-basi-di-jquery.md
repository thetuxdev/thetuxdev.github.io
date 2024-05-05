---
title: 5. Le basi di jQuery
author: Alberto
type: post
date: 2020-03-17T19:43:58+00:00
url: /le-basi-di-jquery/
nectar_blog_post_view_count:
  - 27
tags:
  - Guide
  - Inizia Qui

---
Se hai letto le nostre [guide precedenti][1], ormai saprai bene che **HTML**, **CSS** e **Javascript** sono i tre **linguaggi fondamentali **del web.

Con&nbsp;**l’HTML**&nbsp;strutturiamo i nostri siti, con il&nbsp;**CSS**&nbsp;li modelliamo e li formattiamo e con il&nbsp;**Javascript**&nbsp;aggiungiamo funzionalità interattive e animazioni.

**<a href="https://jquery.com/" target="_blank" rel="noreferrer noopener">JQuery</a>**&nbsp;è una libreria Javascript che consente di&nbsp;**ottenere grandi risultati scrivendo meno codice**. In pratica si potrebbe utilizzare il vanilla Javascript (Javascript puro) per fare le stesse cose che si fanno con JQuery, però con questa libreria è più&nbsp;**semplice**&nbsp;e&nbsp;**veloce**!

Inoltre JQuery&nbsp;**è compatibile con la maggior parte dei browser,**&nbsp;il che significa che non dobbiamo preoccuparci di testare gli effettu su tutti i browser presenti, ma possiamo stare tranquilli che tutto funzionerà ovunque!

Vuoi&nbsp;**vedere**&nbsp;come**&nbsp;JQuery è più semplice**&nbsp;rispetto a Javascript?

**Ecco un esempio!**

In questo esempio andremo ad inserire la stringa “**Ciao mondo!**” in un div con id #ciao, guarda la differenza fra i due codici:

**Javascript:**

<pre class="wp-block-code"><code>document.getElementById('ciao').innerHTML = 'Ciao mondo!'</code></pre>

**JQuery:**

<pre class="wp-block-code"><code>$('#ciao').html('Ciao mondo!')</code></pre>

**Visto?**&nbsp;Già da una cosa semplicissima come questa si può vedere che il codice è molto più semplice con JQuery!

**Ti sei convinto&nbsp;**che può valere la pena imparare ad utilizzare questa libreria? Molto bene!

**Iniziamo!**

## Installazione di JQuery {.wp-block-heading}

**JQuery**&nbsp;è semplicemente un&nbsp;**file Javascript&nbsp;**da inserire nel nostro HTML.

Questo inserimento può essere fatto in&nbsp;**due modi:**&nbsp;tramite&nbsp;**CDN**&nbsp;oppure&nbsp;**scaricando**&nbsp;i file in locale.

Puoi&nbsp;**scaricare**&nbsp;i file di JQuery dal sito ufficiale a questo link:

<https://jquery.com/download/>

Oppure puoi utilizzare una&nbsp;**CDN**, come faremo in questa guida. Utilizzeremo infatti una CDN di google:

<https://developers.google.com/speed/libraries/>

### Template HTML {.wp-block-heading}

Iniziamo con il creare un file&nbsp;**HTML**&nbsp;di base in cui installare JQuery. Ecco il nostro&nbsp;**scheletro**&nbsp;HTML:

<pre class="wp-block-code"><code>&lt;!DOCTYPE html&gt;
&lt;html lang="it"&gt;
  &lt;head&gt;
    &lt;title&gt;Corso intensivo jQuery&lt;/title&gt;
    &lt;!-- CSS --&gt;
    &lt;link rel="stylesheet" href="css/styles.css" /&gt;
  &lt;/head&gt;

  &lt;body&gt;


    &lt;script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"&gt;&lt;/script&gt;
    &lt;script src="js/scripts.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;</code></pre>

Ecco il nostro scheletro. Insieme al file html creiamo anche una cartella “**css**” con al suo interno un file “_style.css_” e una cartella “**js**” con al suo interno un file “_scripts.js_“.

<p class="has-text-align-center has-vivid-red-color has-text-color">
  Ricordati di inserire il file “scripts.js” sotto a JQuery, altrimenti non funzionerà!
</p>

Molto bene, abbiamo un progetto web configurato per poter utilizzare&nbsp;**JQuery**, vediamo ora come usare questa libreria!

## Le basi {.wp-block-heading}

**JQuery**&nbsp;è utilizzato per&nbsp;**connettersi con gli elementi HTML**&nbsp;nel browser tramite&nbsp;**DOM**.

Il&nbsp;**DOM**&nbsp;(Document Object Model) è il metodo con cui&nbsp;**Javascript**&nbsp;(e quindi anche JQuery)&nbsp;**interagisce con l’HTML**&nbsp;nel browser.

Per visualizzare esattamente qual è il DOM, facciamo clic con il tasto destro sulla pagina nel browser e selezioniamo&nbsp;**Ispeziona**.&nbsp;Il codice HTML che vediamo nel riquadro di ispezione è il DOM.&nbsp;Ogni elemento HTML è considerato un oggetto che JavaScript può utilizzare.&nbsp;JavaScript può aggiungere, rimuovere e modificare ognuno di questi elementi.

Il livello più esterno del DOM è l’oggetto&nbsp;**document**.&nbsp;Per iniziare a manipolare la pagina con jQuery, dobbiamo prima assicurarci che il document sia pronto, “_ready_“.

Apriamo quindi il nostro file&nbsp;_scripts.js&nbsp;_e inseriamo questo codice:

<pre class="wp-block-code"><code>$(document).ready(function() {
  // Tutte le funzioni di JQuery vanno inserite qui!
})</code></pre>

Qualsiasi jQuery personalizzato che scriveremo sarà contenuto all’interno di questa&nbsp;**funzione**.&nbsp;

Nell’introduzione di questo articolo, abbiamo visto un semplice script “**Ciao mondo!**“.&nbsp;Per avviare questo script e stampare il testo sul browser con jQuery, per prima cosa creiamo un elemento vuoto a cui applichiamo un id “ciao”.

Torniamo quindi nel nostro_&nbsp;index.html&nbsp;_e inseriamo questo nel&nbsp;_<body>:_

<pre class="wp-block-code"><code>&lt;p id="ciao"&gt;&lt;/p&gt;</code></pre>

**jQuery**&nbsp;viene chiamato con e rappresentato dal&nbsp;**simbolo del dollaro&nbsp;**(&nbsp;`$`).&nbsp;Accediamo al DOM con jQuery utilizzando principalmente la&nbsp;**sintassi CSS&nbsp;**e applichiamo un’azione con un metodo.&nbsp;Un esempio di base di jQuery segue questo formato:

<pre class="wp-block-code"><code>$('selector').method()</code></pre>

Poiché un ID è rappresentato da un simbolo hash (#) nei CSS, accederemo all’ID ciao con il selettore_&nbsp;#ciao_&nbsp;_#ciao_.&nbsp;_html()_&nbsp;è un metodo che modifica l’HTML all’interno di un elemento.

<pre class="wp-block-code"><code>$('#ciao').html('Ciao mondo!')</code></pre>

Il codice viene eseguito non&nbsp;**appena il documento è pronto.&nbsp;**

**Salviamo**&nbsp;tutto e apriamo index.html nel browser,&nbsp;**vedremo apparire l**a scritta “Ciao mondo”. Questa scritta è stata inserita da JQuery!

## I selettori {.wp-block-heading}

La maggior parte dei **selettori jQuery s**ono gli stessi di quelli che utilizziamo nei [CSS][2], con alcune aggiunte specifiche di jQuery. L’elenco completo dei selettori jQuery <a href="https://api.jquery.com/category/selectors/" target="_blank" rel="noreferrer noopener">è disponibile qui</a> .

Di seguito una breve panoramica di alcuni dei selettori più comunemente usati.

  * _$(“*”)_–&nbsp;**Carattere jolly:**&nbsp;seleziona ogni elemento.
  * _$(this)_–&nbsp;**Corrente:**&nbsp;seleziona l’elemento corrente su cui operare all’interno di una funzione.
  * _$(“p”)_–&nbsp;**Elemento:**&nbsp;seleziona ogni istanza del&nbsp;_<p>_tag.
  * _$(“.esempio”)_–&nbsp;**Classe:**&nbsp;seleziona ogni elemento a cui è&nbsp;applicata&nbsp;la&nbsp;classe “esempio”.
  * _$(“#esempio”)_–&nbsp;**Id:**&nbsp;seleziona una singola istanza&nbsp;dell’ID&nbsp;univoco&nbsp;“esempio”.
  * _$(“[type=’text’]”)_–&nbsp;**Attributo:**&nbsp;seleziona qualsiasi elemento con&nbsp;_text_applicato&nbsp;_type_all’attributo.
  * _$(“p:first-of-type”)_–&nbsp;**Pseudo Element:**&nbsp;seleziona il primo&nbsp;_<p>_.

Generalmente, le&nbsp;**classi**&nbsp;e gli&nbsp;**ID&nbsp;**sono ciò che verrà utilizzato maggiormente: le classi quando si vogliono selezionare più elementi e gli id â€‹â€‹quando si vuole selezionarne solo uno.

## Eventi jQuery {.wp-block-heading}

Nell’esempio “Ciao mondo!”, il codice è stato eseguito non appena la pagina è stata caricata e il documento era pronto, e quindi non richiedeva l’interazione dell’utente.&nbsp;Chiaramente in questo caso, avremmo potuto facilmente scrivere il testo direttamente nell’HTML senza preoccuparci di jQuery.

Tuttavia, dovremo utilizzare jQuery se vogliamo&nbsp;**far apparire il testo sulla pagina con il clic di un pulsante**.&nbsp;Possiamo aggiungere un pulsante al nostro HTML per attivare l’evento.

<pre class="wp-block-code"><code>&lt;button id="trigger"&gt;Cliccami!&lt;/button&gt;
&lt;p id="ciao"&gt;&lt;/p&gt;</code></pre>

Ora possiamo usare il&nbsp;metodo&nbsp;_click()&nbsp;_per inserire il nostro testo “Ciao mondo!”:

<pre class="wp-block-code"><code>$('#trigger').click(function() {
  $('#ciao').html('Ciao mondo!')
})</code></pre>

Salva e aggiorna e se tutto è andato liscio, facendo clic sul pulsante vedrai apparire il testo.

Un elenco completo dei metodi degli eventi jQuery&nbsp;<a href="https://api.jquery.com/category/events/" target="_blank" rel="noreferrer noopener">è disponibile qui</a>&nbsp;.&nbsp;Un&nbsp;**evento**&nbsp;avviene ogni volta che l’utente interagisce con il browser.&nbsp;Abbiamo appena appreso&nbsp;[click ()][3]&nbsp;, che viene eseguito con un solo clic del mouse.

Di seguito ti lascio una breve panoramica di alcuni dei metodi di eventi più comunemente utilizzati.

  * [hover ()][4]&nbsp;–&nbsp;**Hover**&nbsp;viene eseguito quando il mouse viene spostato su un elemento.&nbsp;[mouseenter ()][5]&nbsp;e&nbsp;[mouseleave () si][6]&nbsp;applicano solo al mouse che entra o esce da un elemento, rispettivamente.
  * [submit ()][7]&nbsp;–&nbsp;**Submit**&nbsp;viene eseguito quando viene inviato un modulo.
  * [scroll ()][8]&nbsp;– Lo&nbsp;**scorrimento**&nbsp;viene eseguito quando si&nbsp;[scorre][8]&nbsp;lo schermo.
  * [keydown ()][9]&nbsp;–&nbsp;**Keydown**&nbsp;viene eseguito quando si preme un tasto sulla tastiera.

## Effetti jQuery {.wp-block-heading}

<a href="https://api.jquery.com/category/effects/" target="_blank" rel="noreferrer noopener">Gli effetti jQuery</a>&nbsp;lavorano di pari passo con gli eventi consentendo di aggiungere facilmente animazioni e manipolare in altro modo gli elementi della pagina.

Faremo un esempio in cui&nbsp;**apriamo e chiudiamo un overlay / popup modale.**&nbsp;Mentre potremmo usare&nbsp;**due id**: uno per aprire la modal e un altro per chiuderla. Utilizzeremo una classe per aprire e chiudere facilmente la modal con la stessa funzione.

**index.html**

<pre class="wp-block-code"><code>&lt;button class="trigger"&gt;Apri&lt;/button&gt;

&lt;section class="overlay"&gt;
  &lt;button class="trigger"&gt;Chiudi&lt;/button&gt;
&lt;/section&gt;</code></pre>

Useremo una minima quantità di CSS per nascondere il&nbsp;_overlay_&nbsp;con&nbsp;_display: none_&nbsp;e centrarlo sullo schermo.

**style.css**

<pre class="wp-block-code"><code>.overlay {
  display: none;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  height: 200px;
  width: 200px;
  background: gray;
}</code></pre>

Infine, useremo il metodo&nbsp;_toggle()_, che commuterà la&nbsp;proprietà&nbsp;&nbsp;_display_&nbsp;CSS&nbsp;tra&nbsp;_none_&nbsp;e&nbsp;_block_, nascondendo e mostrando l’overlay quando si fa clic.

<pre class="wp-block-code"><code>$('.trigger').click(function() {
  $('.overlay').toggle()
})</code></pre>

Ora potrai&nbsp;**attivare / disattivare la visibilità del modale facendo clic sui pulsanti.&nbsp;**

Puoi anche provare a modificare&nbsp;_toggle()_&nbsp;per&nbsp;_fadeToggle()_&nbsp;o&nbsp;_slideToggle()_&nbsp;per vedere un paio di altri effetti incorporati jQuery.

Di seguito una breve panoramica di alcuni dei metodi di effetto più comunemente usati.

  * [toggle ()][10]&nbsp;–&nbsp;**Attiva**&nbsp;/&nbsp;**disattiva**&nbsp;la visibilità di uno o più elementi.&nbsp;[show ()][11]&nbsp;e&nbsp;[hide ()][12]&nbsp;sono gli effetti unidirezionali correlati.
  * [fadeToggle ()][13]&nbsp;–&nbsp;**Fade Toggle**&nbsp;attiva /&nbsp;**disattiva**&nbsp;la visibilità e anima l’opacità di uno o più elementi.&nbsp;[fadeIn ()][14]&nbsp;e&nbsp;[fadeOut ()][15]&nbsp;sono i relativi effetti unidirezionali.
  * [slideToggle ()][16]&nbsp;–&nbsp;**Slide Toggle**&nbsp;attiva o&nbsp;**disattiva**&nbsp;la visibilità di uno o più elementi con un effetto scorrevole.&nbsp;[slideDown ()][17]&nbsp;e&nbsp;[slideup ()][18]&nbsp;sono i relativi effetti unidirezionali.
  * [animate ()][19]&nbsp;–&nbsp;**Animate**&nbsp;esegue effetti di animazione personalizzati sulla proprietà CSS di un elemento.

## Conclusione {.wp-block-heading}

Ora che hai imparato le basi di JQuery puoi&nbsp;**sbizzarrirti**&nbsp;e provare a realizzare gli effetti che vuoi!

Prova quindi a&nbsp;**creare qualche effetto&nbsp;**all’hover del mouse, al click, allo scroll, andando a modificare le&nbsp;**classi CSS&nbsp;**come il colore, lo sfondo o anche l’immagine!

**Con JQuery si può fare veramente di tutto**, basta mettersi sotto e studiare un pochino!

Ora che hai capito le basi dei linguaggi&nbsp;**front-end&nbsp;**è ora di dedicare un po’ di tempo anche al&nbsp;**linguaggio principale di WordPress:&nbsp;**

<div class="wp-block-columns are-vertically-aligned-center is-layout-flex wp-container-core-columns-is-layout-1 wp-block-columns-is-layout-flex">
  <div class="wp-block-column is-vertically-aligned-center is-layout-flow wp-block-column-is-layout-flow">
    <p>
      <em><a href="https://albertoreineri.it/guide/le-basi-di-bootstrap/"><< Le basi di Bootstrap</a></em>
    </p>
  </div>

  <div class="wp-block-column is-vertically-aligned-center is-layout-flow wp-block-column-is-layout-flow">
    <p class="has-text-align-right">
      <em><a href="https://albertoreineri.it/guide/le-basi-di-php/">Le basi di PHP >></a></em>
    </p>
  </div>
</div>

 [1]: /guide
 [2]: https://albertoreineri.it/guide/le-basi-del-css/
 [3]: https://api.jquery.com/click/
 [4]: https://api.jquery.com/hover/
 [5]: https://api.jquery.com/mouseenter/
 [6]: https://api.jquery.com/mouseleave/
 [7]: https://api.jquery.com/submit/
 [8]: https://api.jquery.com/scroll/
 [9]: https://api.jquery.com/keydown/
 [10]: https://api.jquery.com/toggle/
 [11]: https://api.jquery.com/show/
 [12]: https://api.jquery.com/hide/
 [13]: https://api.jquery.com/fadetoggle/
 [14]: https://api.jquery.com/fadein/
 [15]: https://api.jquery.com/fadeout/
 [16]: https://api.jquery.com/slidetoggle/
 [17]: https://api.jquery.com/slidedown/
 [18]: https://api.jquery.com/slideup
 [19]: https://api.jquery.com/animate/