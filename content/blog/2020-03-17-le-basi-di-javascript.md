---
title: 3. Le basi di Javascript
author: Alberto
type: post
date: 2020-03-17T21:40:43+00:00
url: /le-basi-di-javascript/
tags:
  - Guide
  - Inizia Qui

---
**Javascript** è il linguaggio che permette di **creare animazioni **nei contenuti web. Tutte le gallery, gli slider, i pop up, le transizioni di pagina e ogni effetto animato che vedi navigando online è realizzato con **Javascript**.

Questo linguaggio **si è sviluppato moltissimo**, passando dall’essere una cosa in più, un modo per creare effetti divertenti e simpatici, ad essere oggi uno dei più utilizzati al mondo, non solo per animazioni. ma per creare **vere e proprie strutture software** in grado di far funzionare applicativi potentissimi.

In questo articolo **tratteremo le basi**, partiremo **da zero** e vedremo come funziona questo linguaggio di programmazione, e creeremo insieme qualcosa di **semplice** ma utile per capire come utilizzare questo linguaggio.

Faremo prima un po’ di teoria e poi passeremo a creare qualcosa di utilizzabile sulla nostra pagina web.

Se ti perdi durante l’articolo sul fondo di questo articolo potrai trovare il codice di tutto ciò che andremo a creare.

<hr class="wp-block-separator has-css-opacity"/>

_Questo corso è rivolto ai **principianti**, pertanto se conosci già Javascript questo articolo non fa per te, se invece sei agli inizi **BENVENUTO **e buono studio! Vedrai che** imparerai presto** a cerare fantastici contenuti web!_

<hr class="wp-block-separator has-css-opacity"/>

## Inserire Javascript nell’HTML

Iniziamo ad **inserire** del codice Javascript nel nostro file html (se non sai di cosa sto parlando dai un’occhiata ai nostri articoli su [HTML][1] e [CSS][2])

Come per il codice CSS, anche il Javascript può essere inserit in **modi diversi:**

  * Javascript interno
  * Javascript esterno

### Codice Javascript interno

In questo caso il codice Javascript è inserito **direttamente nel file html **prima del fine body (), fra i tag `<script>` e `</script>.`

**Esempio:**

Apriamo il nostro “**index.html**“, andiamo sul fondo e inseriamo questo codice appena prima del tag _****_:

<pre class="wp-block-code"><code>&lt;script&gt;
   alert("CIAO");
&lt;/script&gt;</code></pre>

Ora **salviamo** e **apriamo** la pagina “index.html”. Ecco che apparirà un **popup** con scritto “CIAO!”.

{{< image src="/img/uploads/2022/03/image-10.png" >}}

## Codice Javascript esterno

Per inserire il javascript esterno occorre **creare un file .js** e **importarlo** nell’html. Come per il CSS questo è** il metodo migliore**, quasi sempre.

**Esempio:**

Andiamo nella nostra cartella “**HTML**” sul desktop, la apriamo con code (guadra la guida [Le basi di HTML][1]) e creiamo un file (**CTRL+N**) e lo salviamo (**CTRL+S**) con il nome “_**scripts.js**_“.

All’interno di questo file scriviamo:

<pre class="wp-block-code"><code>alert("CIAO");</code></pre>

Ora **salviamo** “**_scripts.js_**” e apriamo “**_index.html_**“.

Qua, sempre prima del __, inseriamo questo:

<pre class="wp-block-code"><code>&lt;script src="scripts.js"&gt;&lt;/script&gt;</code></pre>

Ora **salviamo** e **aggiorniamo** il browser.

**Il risultato è uguale a prima**: il popup, solo che il modo con cui l’abbiamo fatto apparire è diverso.

## Un po’ di teoria

### Alert

Abbiamo appena utilizzato la funziona “**alert**“, che permette di far apparire un **popup** nella pagina web con del testo al suo interno. Raramente questo è utilizzato per i popup, perché l**‘estetica è un po’ bruttina** ed esistono metodi molto migliori per far comparire dei popup nelle pagine web, ma può essere molto utile **in fase di debugging**.

Se sto creando una funzione e non riesco a trovare l’errore, posso inserire un “alert” a metà funzione e vedere così se l’errore si verifica prima o dopo.

### Console.log

Un altro modo per visualizzare errori in Javascript è la funzione “**console.log**“. Questa permette di **inserire del testo nella console di Javascript**. Anche questa è molto utile in fase di debug e sviluppo.

**Ecco un esempio:**

<pre class="wp-block-code"><code>console.log("CIAO!");</code></pre>

Se inserisci questa in “_**scripts.js**_“, salvi e aggiorni, non vedrai accadere niente. Questo perché il **“CIAO!” **che abbiamo scritto **è inserito nella console di Javascript**, non nel body della pagina. Per vedere la console Javascript premi il tasto “**f12**“, oppure fai click con il tasto destro e clicca su “**ispeziona**” (Su google chrome, ma è molto simile su tutti i browser)

### Commenti

I **commenti** sono **importantissimi** in ogni linguaggio di programmazione.

Per inserire i commenti in Javascript esistono** due modi:**

Se il commento è su **una sola riga **puoi inserire un** doppio slash** prima della riga. In questo modo** tutta la riga sarà commentata.**

**Esempio**

<pre class="wp-block-code"><code>// Questo è un commento su una riga Javascript</code></pre>

Se invece **il commento è più lungo**, puoi usare la stessa sintassi del CSS:**_ /\* Commento \*/_**

**Esempio:**

<pre class="wp-block-code"><code>/*
Questo è un commento
Javascript su più righe
*/</code></pre>

### Variabili

A differenza di HTML e CSS, **Javscript è un vero e proprio linguaggio di programmazione**, e non dei più semplici.

Come ogni linguaggio di prograammazione è possibile **utilizzare delle variabili per memorizzare i dati e fare calcoli.**

Inserire una variabile è molto semplice, basta inserire “**var**” prima della variabile, in questo modo:

<pre class="wp-block-code"><code>var anni = 30;</code></pre>

È fondamentale **inserire il punto e virgola** alla fine della variabile, per indicare che la regola finisce in quel punto. Senza il punto e virgola verranno generati degli errori.

Ora possiamo **richiamare la variabile dentro il console.log **oppure in un **alert**, in questo modo:

<pre class="wp-block-code"><code>console.log(anni);</code></pre>

oppure:

<pre class="wp-block-code"><code>alert(anni);</code></pre>

**Salviamo** e **aggiorniamo** e vedremo il numero “**30**” apparire nel popup oppure nella cosole.

**Ma possiamo fare di più!**

Impostiamo **una serie di variabili:**

<pre class="wp-block-code"><code>var nome = "Marco";
var altezza = "1.83";
var anni = 30;</code></pre>

Adesso possiamo c**reare una frase ed inserire al suo interno le nostre variabili,** oltre che utilizzarle per fare dei calcoli.

I **valori testuali devono essere inseriti fra virgolette**, mentre i **valori numerici senza**. In questo modo possiamo fare anche delle **operazioni aritmetiche.**

**Ecco un esempio:**

<pre class="wp-block-code"><code>console.log('Ciao, mi chiamo ' + nome + ' e sono alto ' + altezza + ' metri. In questo momento ho ' + anni + ' anni. Fra 5 anni avrò ' + (anni + 5) + ' anni.'); &lt;/script&gt;
</code></pre>

Per inserire una **variabile in un testo** occorre **concatenarla**, metterla insieme.

Per fare questo abbiamo utilizzato il segno** ‘+’.**

### Funzioni

Le funzioni sono delle **parti di codice che svolgono una determinata azione**.

Isolando una parte di codice in una funzione, questa potrà essere **richiamata** più volte all’interno del progetto.

Le funzioni possono avere dei **parametri**, che ne personalizzano l’azione.

**Esempio:**

Andiamo sul file _**scripts.js **_e scriviamo:

<pre class="wp-block-code"><code>function ciao() {
   alert ("CIAO");
}</code></pre>

Ora andiamo sul file _**index.htm**_l e aggiungiamo un bottone, in questo modo:

<pre class="wp-block-code"><code>&lt;button onclick="ciao()"&gt;Salutami&lt;/button&gt;</code></pre>

**Salviamo** e **aggiorniamo** e vedremo che **cliccando sul nuovo bottone apparirà il popup con scritto “CIAO”.**

### Parametri

Adesso aggiungiamo un **parametro**. Andiamo nella funzione a la modifichiamo così:

<pre class="wp-block-code"><code>function ciao(nome) {
    alert ("CIAO "+nome);
 }</code></pre>

e sul file _**index.html**_ modifichiamo così il bottone:

<pre class="wp-block-code"><code>&lt;button onclick="ciao('Marco')"&gt;Salutami&lt;/button&gt;</code></pre>

**Salviamo** e **aggiorniamo** e possiamo vedere che ora il saluto è rivolto al nome inserito nel parametro della funzione!

“Marco” è il nostro parametro

### If Else

Gli “If” sono **alla base di tutta la programmazione**. Ogni azione è fatta come conseguenza di un’altra. Vediamo cosa significa.

Utilizziamo sempre il bottone del saluto. Possiamo prevedere che se il nome è “Marco” allora il popup dirà “Ciao Marco”, se invece il nome è “Mark”, possiamo far apparire “Hello Mark”.

**Vediamo come fare:**

Sostituiamo la funzione con questa:

<pre class="wp-block-code"><code>function ciao(nome) {
    if(nome=="Marco"){
        alert ("CIAO "+nome);
    }else if(nome=="Mark"){
        alert ("Hello "+nome);
    }else{
        alert ("Buongiorno "+nome);
    }
 }</code></pre>

Ora possiamo andare a **modificare il parametro nel bottone**, da “Marco” a “Mark”, oppure inserire un nome totalmente diverso.

Se il nome è Marco allora il popup sarà “Ciao Marco”, se Mark allora “Hello Mark”, se altro sarà “Buongiorno + nome”.

Da notare come **ci siano due segni uguale**, questo perché nel Javascript un uguale assegna il valore, per confrontarli invece occorre usarne 2 o 3 a seconda dei casi. Per il momento ci basta sapere che quando dobbiamo connfrontare più valori bisogna inserire 2 segni uguale.

### Eventi

**Il Javascript può essere richiamato all’interno dell’HTML all’accadere di determinati eventi, **per esempio al click, al passaggio con il mouse etc.

Oggi esistono anche molti altri modi, ma per iniziare questi sono i più semplici ed immediati.

**Esempio:**

<pre class="wp-block-code"><code>&lt;button onclick="alert('CIAO!')"&gt;Salutami&lt;/button&gt;</code></pre>

In questo caso al click del bottone apparirà il **popup di saluto.**

## Creiamo il nostro primo effetto

Al di là della teoria, **a noi interessa soprattutto vedere come possiamo utilizzare Javascript per creare gli effetti per le nostre pagine web.**

Quindi ora andremo a **creare un semplice effetto che cambierà lo sfondo del body al click di un bottone.**

**Vediamo come fare:**

Iniziamo con il creare un bottone nella nostra_** index.html:**_

<pre class="wp-block-code"><code>&lt;button onclick="cambiaSfondo()"&gt; Cambia sfondo! &lt;/button&gt;</code></pre>

Ora andiamo nel nostro **_scripts.js_** e creiamo la funzione **cambiaSfondo()**:

<pre class="wp-block-code"><code>function cambiaSfondo(){
   document.body.style.backgroundColor='#000';
}</code></pre>

Se **salviamo** e **aggiorniamo** vedremo che ora** al click del bottone lo sfondo diventerà nero.**

Abbiamo detto al browser che al click del bottone deve selezionare il colore di sfondo del body (body.style.backgroundcolor) e impostarlo a nero.

Notiamo però che **è un’unica azione**, una volta che lo sfondo è nero non possiamo più tornare al bianco…

**Andiamo ad aggiungere ancora qualche linea di codice:**

<pre class="wp-block-code"><code>function cambiaSfondo(){
    var sfondo = document.body.style.backgroundColor;
    if(sfondo=="rgb(0, 0, 0)"){
        document.body.style.backgroundColor='#fff';
    }else{
        document.body.style.backgroundColor='#000';

    }
}</code></pre>

In questo modo facciamo un **controllo del colore di sfond**o. Se è nero lo impostiamo bianco, altrimento sarà nero.

Così facendo possiamo **cambiare colore di sfondo ogni volta che clicchiamo sul bottone.**

**Congratulazioni! Hai appena creato il tuo primo effetto Javascript!!!**

## Animazione di un componente

Se al posto dello sfondo intero volessimo modificare solamente un **componente**, possiamo farlo utilizzando gli **id** ([Le basi di CSS][2]).

Iniziamo con il creare un **div con id=”box”**

<pre class="wp-block-code"><code>&lt;div id="box" onmouseover="cambiaBoxOver()" onmouseout="cambiaBoxOut()"&gt;
   Questo contenitore cambiarà colore al passaggio del mouse
&lt;/div&gt;</code></pre>

Ora **creiamo le due funzioni in scripts.js:**

<pre class="wp-block-code"><code> function cambiaBoxOver(){
    document.getElementById('box').style.backgroundColor="coral";
    document.getElementById('box').style.color="blue";
}

 function cambiaBoxOut(){
    document.getElementById('box').style.backgroundColor="white";
    document.getElementById('box').style.color="black";

}</code></pre>

**Salviamo** e **aggiorniamo** e vediamo che **il contenitore cambia colore e sfondo al passaggio del mouse.**

Molto bene, **queste sono le basi per iniziare a smanettare un po’ con il Javascript.**

**Cercando online potrai trovare moltissime guide e tutorial sull’argomento.**

**È però bene conoscere anche un po’ di Javascript** e soprattutto JQuery, per poter **evitare di installare un’infinità di plugin e crearci da soli tutti gli effetti e le funzioni che vogliamo!**

### CODICE COMPLETO:

**index.html**

<pre class="wp-block-code"><code>&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;

&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;La mia prima pagina web&lt;/title&gt;&lt;!-- Il titolo della pagina che appare nella scheda del browser --&gt;
    &lt;link rel="stylesheet" href="style.css"&gt;
&lt;/head&gt;

&lt;body&gt;
    &lt;div class="container"&gt;

        &lt;!-- Javascript --&gt;
        &lt;button onclick="ciao('Ugo')"&gt;Salutami&lt;/button&gt;
        &lt;!-- Titolo --&gt;
        &lt;button onclick="cambiaSfondo()"&gt;
            Cambia sfondo!
        &lt;/button&gt;
        &lt;div id="box" onmouseover="cambiaBoxOver()" onmouseout="cambiaBoxOut()"&gt;
            Questo contenitore cambiarà colore al passaggio del mouse
        &lt;/div&gt;
        &lt;!-- /Javascript--&gt;

        &lt;h1&gt;La mia prima pagina web&lt;/h1&gt;

        &lt;!-- Paragrafo --&gt;
        &lt;p&gt;Benvenuto nella mia prima pagina web!&lt;/p&gt;

        &lt;br&gt;&lt;!-- questo è un a capo--&gt;

        &lt;!-- Sottotitolo --&gt;
        &lt;h2&gt;Sottotitolo&lt;/h2&gt;

        &lt;p&gt;Questo è il secondo paragrafo della mia prima pagina web&lt;/p&gt;

        &lt;br&gt;

        &lt;h2&gt;Elenco&lt;/h2&gt;
        &lt;!-- Elenco --&gt;
        &lt;ul&gt;
            &lt;li&gt;Primo Item&lt;/li&gt;&lt;!-- Item di un elenco --&gt;
            &lt;li&gt;Secondo Item&lt;/li&gt;
        &lt;/ul&gt;

        &lt;!-- Immagine
    &lt;img src="img/immagine.jpg" width="200"&gt; --&gt;

        &lt;!-- DIV: block element --&gt;
        &lt;div style="background-color: green;"&gt;
            Questo è un contenitore con sfondo verde
        &lt;/div&gt;

        &lt;!-- SPAN: inline element --&gt;
        &lt;p&gt;
            Questo è un paragrafo con del testo inserito a caso. In questo testo voglio
            &lt;span style="color:red"&gt;colorare&lt;/span&gt; una parola di rosso
        &lt;/p&gt;

        &lt;!-- FORM --&gt;
        &lt;form&gt;
            &lt;!-- Casella di testo --&gt;
            &lt;input type="text" placeholder="Nome"&gt;
            &lt;br&gt;&lt;br&gt;
            &lt;input type="text" placeholder="Cognome"&gt;
            &lt;br&gt;&lt;br&gt;
            &lt;!-- Menù a tendina --&gt;
            &lt;select name="select" id=""&gt;
                &lt;option value="0"&gt;Opzione 1&lt;/option&gt;
                &lt;option value="1"&gt;Opzione 2&lt;/option&gt;
                &lt;option value="2"&gt;Opzione 3&lt;/option&gt;
            &lt;/select&gt;
            &lt;br&gt;&lt;br&gt;
            &lt;!-- Area di testo --&gt;
            &lt;textarea name="" id="" cols="30" rows="10" placeholder="Inserisci il testo qui."&gt;&lt;/textarea&gt;
            &lt;br&gt;&lt;br&gt;
            &lt;!-- Checkbox--&gt;
            &lt;input type="checkbox" name="privacy" value="0"&gt;Accetto la Privacy Policy
            &lt;br&gt;&lt;br&gt;
            &lt;!-- Bottone --&gt;
            &lt;button&gt;Invia&lt;/button&gt;
        &lt;/form&gt;

        &lt;h2&gt;Margin e Padding&lt;/h2&gt;
        &lt;h3&gt;Margin:&lt;/h3&gt;
        &lt;div class="box-margin"&gt;
            Questo è un box con del margine
        &lt;/div&gt;

        &lt;div class="box-margin-top"&gt;
            Questo box ha solo il margine superiore
        &lt;/div&gt;

        &lt;h3&gt;Padding&lt;/h3&gt;
        &lt;div class="box-padding"&gt;
            Questo è un box con del padding
        &lt;/div&gt;

        &lt;!--
&lt;div class="immagine-sfondo"&gt;
    Questo div ha un'immagine di sfondo!
&lt;/div&gt;
--&gt;

    &lt;/div&gt;

    &lt;script src="scripts.js"&gt;&lt;/script&gt;
&lt;/body&gt;

&lt;/html&gt;</code></pre>

**scripts.js**

<pre class="wp-block-code"><code>function cambiaSfondo(){
    var sfondo = document.body.style.backgroundColor;
    if(sfondo=="rgb(0, 0, 0)"){
        document.body.style.backgroundColor='#fff';
    }else{
        document.body.style.backgroundColor='#000';

    }
}

function ciao(nome) {
    if(nome=="Marco"){
        alert ("CIAO "+nome);
    }else if(nome=="Mark"){
        alert ("Hello "+nome);
    }else{
        alert ("Buongiorno "+nome);
    }

 }

 function cambiaBoxOver(){
    document.getElementById('box').style.backgroundColor="coral";
    document.getElementById('box').style.color="blue";
}

 function cambiaBoxOut(){
    document.getElementById('box').style.backgroundColor="white";
    document.getElementById('box').style.color="black";

}</code></pre>
<div class="wp-block-columns are-vertically-aligned-center is-layout-flex wp-container-core-columns-is-layout-3 wp-block-columns-is-layout-flex">
<div class="wp-block-column is-vertically-aligned-center is-layout-flow wp-block-column-is-layout-flow">
<p>
<em><a href="/le-basi-dellhtml/">&lt;&lt; Le basi di CSS</a></em>
</p>
</div>
<div class="wp-block-column is-vertically-aligned-center is-layout-flow wp-block-column-is-layout-flow">
<p class="has-text-align-right">
<em><a href="/le-basi-di-bootstrap/">Le basi di Bootstrap &gt;&gt;</a></em>
</p>
</div>
</div>

 [1]: /le-basi-dellhtml/
 [2]: /le-basi-del-css/