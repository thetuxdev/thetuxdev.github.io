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

Con **l’HTML** strutturiamo i nostri siti, con il **CSS** li modelliamo e li formattiamo e con il **Javascript** aggiungiamo funzionalità interattive e animazioni.

**<a href="https://jquery.com/" rel="noreferrer noopener" target="_blank">JQuery</a>** è una libreria Javascript che consente di **ottenere grandi risultati scrivendo meno codice**. In pratica si potrebbe utilizzare il vanilla Javascript (Javascript puro) per fare le stesse cose che si fanno con JQuery, però con questa libreria è più **semplice** e **veloce**!

Inoltre JQuery **è compatibile con la maggior parte dei browser,** il che significa che non dobbiamo preoccuparci di testare gli effettu su tutti i browser presenti, ma possiamo stare tranquilli che tutto funzionerà ovunque!

Vuoi **vedere** come** JQuery è più semplice** rispetto a Javascript?

**Ecco un esempio!**

In questo esempio andremo ad inserire la stringa “**Ciao mondo!**” in un div con id #ciao, guarda la differenza fra i due codici:

**Javascript:**

<pre class="wp-block-code"><code>document.getElementById('ciao').innerHTML = 'Ciao mondo!'</code></pre>

**JQuery:**

<pre class="wp-block-code"><code>$('#ciao').html('Ciao mondo!')</code></pre>

**Visto?** Già da una cosa semplicissima come questa si può vedere che il codice è molto più semplice con JQuery!

**Ti sei convinto **che può valere la pena imparare ad utilizzare questa libreria? Molto bene!

**Iniziamo!**

## Installazione di JQuery

**JQuery** è semplicemente un **file Javascript **da inserire nel nostro HTML.

Questo inserimento può essere fatto in **due modi:** tramite **CDN** oppure **scaricando** i file in locale.

Puoi **scaricare** i file di JQuery dal sito ufficiale a questo link:

<https: download="" jquery.com=""></https:>

Oppure puoi utilizzare una **CDN**, come faremo in questa guida. Utilizzeremo infatti una CDN di google:

<https: developers.google.com="" libraries="" speed=""></https:>

### Template HTML

Iniziamo con il creare un file **HTML** di base in cui installare JQuery. Ecco il nostro **scheletro** HTML:

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

Molto bene, abbiamo un progetto web configurato per poter utilizzare **JQuery**, vediamo ora come usare questa libreria!

## Le basi

**JQuery** è utilizzato per **connettersi con gli elementi HTML** nel browser tramite **DOM**.

Il **DOM** (Document Object Model) è il metodo con cui **Javascript** (e quindi anche JQuery) **interagisce con l’HTML** nel browser.

Per visualizzare esattamente qual è il DOM, facciamo clic con il tasto destro sulla pagina nel browser e selezioniamo **Ispeziona**. Il codice HTML che vediamo nel riquadro di ispezione è il DOM. Ogni elemento HTML è considerato un oggetto che JavaScript può utilizzare. JavaScript può aggiungere, rimuovere e modificare ognuno di questi elementi.

Il livello più esterno del DOM è l’oggetto **document**. Per iniziare a manipolare la pagina con jQuery, dobbiamo prima assicurarci che il document sia pronto, “_ready_“.

Apriamo quindi il nostro file _scripts.js _e inseriamo questo codice:

<pre class="wp-block-code"><code>$(document).ready(function() {
  // Tutte le funzioni di JQuery vanno inserite qui!
})</code></pre>

Qualsiasi jQuery personalizzato che scriveremo sarà contenuto all’interno di questa **funzione**. 

Nell’introduzione di questo articolo, abbiamo visto un semplice script “**Ciao mondo!**“. Per avviare questo script e stampare il testo sul browser con jQuery, per prima cosa creiamo un elemento vuoto a cui applichiamo un id “ciao”.

Torniamo quindi nel nostro_ index.html _e inseriamo questo nel _<body>:_

<pre class="wp-block-code"><code>&lt;p id="ciao"&gt;&lt;/p&gt;</code></pre>

**jQuery** viene chiamato con e rappresentato dal **simbolo del dollaro **( `$`). Accediamo al DOM con jQuery utilizzando principalmente la **sintassi CSS **e applichiamo un’azione con un metodo. Un esempio di base di jQuery segue questo formato:

<pre class="wp-block-code"><code>$('selector').method()</code></pre>

Poiché un ID è rappresentato da un simbolo hash (#) nei CSS, accederemo all’ID ciao con il selettore_ #ciao_ _#ciao_. _html()_ è un metodo che modifica l’HTML all’interno di un elemento.

<pre class="wp-block-code"><code>$('#ciao').html('Ciao mondo!')</code></pre>

Il codice viene eseguito non **appena il documento è pronto. **

**Salviamo** tutto e apriamo index.html nel browser, **vedremo apparire l**a scritta “Ciao mondo”. Questa scritta è stata inserita da JQuery!

## I selettori

La maggior parte dei **selettori jQuery s**ono gli stessi di quelli che utilizziamo nei [CSS][2], con alcune aggiunte specifiche di jQuery. L’elenco completo dei selettori jQuery <a href="https://api.jquery.com/category/selectors/" rel="noreferrer noopener" target="_blank">è disponibile qui</a> .

Di seguito una breve panoramica di alcuni dei selettori più comunemente usati.

  * _$(“*”)_– **Carattere jolly:** seleziona ogni elemento.
  * _$(this)_– **Corrente:** seleziona l’elemento corrente su cui operare all’interno di una funzione.
  * _$(“p”)_– **Elemento:** seleziona ogni istanza del _<p>_tag.
  * _$(“.esempio”)_– **Classe:** seleziona ogni elemento a cui è applicata la classe “esempio”.
  * _$(“#esempio”)_– **Id:** seleziona una singola istanza dell’ID univoco “esempio”.
  * _$(“[type=’text’]”)_– **Attributo:** seleziona qualsiasi elemento con _text_applicato _type_all’attributo.
  * _$(“p:first-of-type”)_– **Pseudo Element:** seleziona il primo _<p>_.

Generalmente, le **classi** e gli **ID **sono ciò che verrà utilizzato maggiormente: le classi quando si vogliono selezionare più elementi e gli id â€‹â€‹quando si vuole selezionarne solo uno.

## Eventi jQuery

Nell’esempio “Ciao mondo!”, il codice è stato eseguito non appena la pagina è stata caricata e il documento era pronto, e quindi non richiedeva l’interazione dell’utente. Chiaramente in questo caso, avremmo potuto facilmente scrivere il testo direttamente nell’HTML senza preoccuparci di jQuery.

Tuttavia, dovremo utilizzare jQuery se vogliamo **far apparire il testo sulla pagina con il clic di un pulsante**. Possiamo aggiungere un pulsante al nostro HTML per attivare l’evento.

<pre class="wp-block-code"><code>&lt;button id="trigger"&gt;Cliccami!&lt;/button&gt;
&lt;p id="ciao"&gt;&lt;/p&gt;</code></pre>

Ora possiamo usare il metodo _click() _per inserire il nostro testo “Ciao mondo!”:

<pre class="wp-block-code"><code>$('#trigger').click(function() {
  $('#ciao').html('Ciao mondo!')
})</code></pre>

Salva e aggiorna e se tutto è andato liscio, facendo clic sul pulsante vedrai apparire il testo.

Un elenco completo dei metodi degli eventi jQuery <a href="https://api.jquery.com/category/events/" rel="noreferrer noopener" target="_blank">è disponibile qui</a> . Un **evento** avviene ogni volta che l’utente interagisce con il browser. Abbiamo appena appreso [click ()][3] , che viene eseguito con un solo clic del mouse.

Di seguito ti lascio una breve panoramica di alcuni dei metodi di eventi più comunemente utilizzati.

  * [hover ()][4] – **Hover** viene eseguito quando il mouse viene spostato su un elemento. [mouseenter ()][5] e [mouseleave () si][6] applicano solo al mouse che entra o esce da un elemento, rispettivamente.
  * [submit ()][7] – **Submit** viene eseguito quando viene inviato un modulo.
  * [scroll ()][8] – Lo **scorrimento** viene eseguito quando si [scorre][8] lo schermo.
  * [keydown ()][9] – **Keydown** viene eseguito quando si preme un tasto sulla tastiera.

## Effetti jQuery

<a href="https://api.jquery.com/category/effects/" rel="noreferrer noopener" target="_blank">Gli effetti jQuery</a> lavorano di pari passo con gli eventi consentendo di aggiungere facilmente animazioni e manipolare in altro modo gli elementi della pagina.

Faremo un esempio in cui **apriamo e chiudiamo un overlay / popup modale.** Mentre potremmo usare **due id**: uno per aprire la modal e un altro per chiuderla. Utilizzeremo una classe per aprire e chiudere facilmente la modal con la stessa funzione.

**index.html**

<pre class="wp-block-code"><code>&lt;button class="trigger"&gt;Apri&lt;/button&gt;

&lt;section class="overlay"&gt;
  &lt;button class="trigger"&gt;Chiudi&lt;/button&gt;
&lt;/section&gt;</code></pre>

Useremo una minima quantità di CSS per nascondere il _overlay_ con _display: none_ e centrarlo sullo schermo.

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

Infine, useremo il metodo _toggle()_, che commuterà la proprietà  _display_ CSS tra _none_ e _block_, nascondendo e mostrando l’overlay quando si fa clic.

<pre class="wp-block-code"><code>$('.trigger').click(function() {
  $('.overlay').toggle()
})</code></pre>

Ora potrai **attivare / disattivare la visibilità del modale facendo clic sui pulsanti. **

Puoi anche provare a modificare _toggle()_ per _fadeToggle()_ o _slideToggle()_ per vedere un paio di altri effetti incorporati jQuery.

Di seguito una breve panoramica di alcuni dei metodi di effetto più comunemente usati.

  * [toggle ()][10] – **Attiva** / **disattiva** la visibilità di uno o più elementi. [show ()][11] e [hide ()][12] sono gli effetti unidirezionali correlati.
  * [fadeToggle ()][13] – **Fade Toggle** attiva / **disattiva** la visibilità e anima l’opacità di uno o più elementi. [fadeIn ()][14] e [fadeOut ()][15] sono i relativi effetti unidirezionali.
  * [slideToggle ()][16] – **Slide Toggle** attiva o **disattiva** la visibilità di uno o più elementi con un effetto scorrevole. [slideDown ()][17] e [slideup ()][18] sono i relativi effetti unidirezionali.
  * [animate ()][19] – **Animate** esegue effetti di animazione personalizzati sulla proprietà CSS di un elemento.

## Conclusione

Ora che hai imparato le basi di JQuery puoi **sbizzarrirti** e provare a realizzare gli effetti che vuoi!

Prova quindi a **creare qualche effetto **all’hover del mouse, al click, allo scroll, andando a modificare le **classi CSS **come il colore, lo sfondo o anche l’immagine!

**Con JQuery si può fare veramente di tutto**, basta mettersi sotto e studiare un pochino!

Ora che hai capito le basi dei linguaggi **front-end **è ora di dedicare un po’ di tempo anche al **linguaggio principale di WordPress: **

<div class="wp-block-columns are-vertically-aligned-center is-layout-flex wp-container-core-columns-is-layout-1 wp-block-columns-is-layout-flex">
<div class="wp-block-column is-vertically-aligned-center is-layout-flow wp-block-column-is-layout-flow">
<p>
<em><a href="/le-basi-di-bootstrap/">&lt;&lt; Le basi di Bootstrap</a></em>
</p>
</div>
<div class="wp-block-column is-vertically-aligned-center is-layout-flow wp-block-column-is-layout-flow">
<p class="has-text-align-right">
<em><a href="/le-basi-di-php/">Le basi di PHP &gt;&gt;</a></em>
</p>
</div>
</div>

 [1]:
 [2]: /le-basi-del-css/
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
 [19]: https://api.jquery.com/animate/</p></p></body>