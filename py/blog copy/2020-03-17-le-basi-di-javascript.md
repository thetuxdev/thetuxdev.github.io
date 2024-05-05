---
title: 3. Le basi di Javascript
author: Alberto
type: post
date: 2020-03-17T21:40:43+00:00
url: /le-basi-di-javascript/
nectar_blog_post_view_count:
  - 34
tags:
  - Guide
  - Inizia Qui

---
**Javascript&nbsp;**è il linguaggio che permette di**&nbsp;creare animazioni&nbsp;**nei contenuti web. Tutte le gallery, gli slider, i pop up, le transizioni di pagina e ogni effetto animato che vedi navigando online è realizzato con&nbsp;**Javascript**.

Questo linguaggio**&nbsp;si è sviluppato moltissimo**, passando dall’essere una cosa in più, un modo per creare effetti divertenti e simpatici, ad essere oggi uno dei più utilizzati al mondo, non solo per animazioni. ma per creare&nbsp;**vere e proprie strutture software**&nbsp;in grado di far funzionare applicativi potentissimi.

In questo articolo&nbsp;**tratteremo le basi**, partiremo&nbsp;**da zero&nbsp;**e vedremo come funziona questo linguaggio di programmazione, e creeremo insieme qualcosa di&nbsp;**semplice**&nbsp;ma utile per capire come utilizzare questo linguaggio.

Faremo prima un po’ di teoria e poi passeremo a creare qualcosa di utilizzabile sulla nostra pagina web.

Se ti perdi durante l’articolo sul&nbsp;fondo di questo&nbsp;articolo potrai trovare il&nbsp;codice&nbsp;di tutto ciò che andremo a creare.

<hr class="wp-block-separator has-css-opacity" />

_Questo corso è rivolto ai&nbsp;**principianti**, pertanto se conosci già Javascript questo articolo non fa per te, se invece sei agli inizi&nbsp;**BENVENUTO&nbsp;**e buono studio! Vedrai che**&nbsp;imparerai presto**&nbsp;a cerare fantastici contenuti web!_

<hr class="wp-block-separator has-css-opacity" />

## Inserire Javascript nell’HTML

Iniziamo ad&nbsp;**inserire**&nbsp;del codice Javascript nel nostro file html (se non sai di cosa sto parlando dai un’occhiata ai nostri articoli su&nbsp;[HTML][1]&nbsp;e&nbsp;[CSS][2])

Come per il codice CSS, anche il Javascript può essere inserit in&nbsp;**modi diversi:**

  * Javascript interno
  * Javascript esterno

### Codice Javascript interno

In questo caso il codice Javascript è inserito&nbsp;**direttamente nel file html&nbsp;**prima del fine body (</body>), fra i tag&nbsp;_**<script>**_&nbsp;e&nbsp;**</script>.**

**Esempio:**

Apriamo il nostro “**index.html**“, andiamo sul fondo e inseriamo questo codice appena prima del tag&nbsp;_**</body>**_:

<pre class="wp-block-code"><code>&lt;script&gt;
   alert("CIAO");
&lt;/script&gt;</code></pre>

Ora&nbsp;**salviamo**&nbsp;e&nbsp;**apriamo**&nbsp;la pagina “index.html”. Ecco che apparirà un&nbsp;**popup**&nbsp;con scritto “CIAO!”.

<div class="wp-block-image">
  <figure class="aligncenter size-full"><img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-10.png" alt="" class="wp-image-196" /></figure>
</div>

## Codice Javascript esterno

Per inserire il javascript esterno occorre&nbsp;**creare un file .js**&nbsp;e&nbsp;**importarlo**&nbsp;nell’html. Come per il CSS questo è**&nbsp;il metodo migliore**, quasi sempre.

**Esempio:**

Andiamo nella nostra cartella “**HTML**” sul desktop, la apriamo con code (guadra la guida&nbsp;[Le basi di HTML][1]) e creiamo un file (**CTRL+N**) e lo salviamo (**CTRL+S**) con il nome “_**scripts.js**_“.

All’interno di questo file scriviamo:

<pre class="wp-block-code"><code>alert("CIAO");</code></pre>

Ora&nbsp;**salviamo**&nbsp;“**_scripts.js_**” e apriamo “**_index.html_**“.

Qua, sempre prima del&nbsp;_</body>_, inseriamo questo:

<pre class="wp-block-code"><code>&lt;script src="scripts.js"&gt;&lt;/script&gt;</code></pre>

Ora&nbsp;**salviamo**&nbsp;e&nbsp;**aggiorniamo**&nbsp;il browser.

**Il risultato è uguale a prima**: il popup, solo che il modo con cui l’abbiamo fatto apparire è diverso.

## Un po’ di teoria

### Alert

Abbiamo appena utilizzato la funziona “**alert**“, che permette di far apparire un&nbsp;**popup**&nbsp;nella pagina web con del testo al suo interno. Raramente questo è utilizzato per i popup, perché l**‘estetica è un po’ bruttina**&nbsp;ed esistono metodi molto migliori per far comparire dei popup nelle pagine web, ma può essere molto utile&nbsp;**in fase di debugging**.

Se sto creando una funzione e non riesco a trovare l’errore, posso inserire un “alert” a metà funzione e vedere così se l’errore si verifica prima o dopo.

### Console.log

Un altro modo per visualizzare errori in Javascript è la funzione “**console.log**“. Questa permette di&nbsp;**inserire del testo nella console di Javascript**. Anche questa è molto utile in fase di debug e sviluppo.

**Ecco un esempio:**

<pre class="wp-block-code"><code>console.log("CIAO!");</code></pre>

Se inserisci questa in “_**scripts.js**_“, salvi e aggiorni, non vedrai accadere niente. Questo perché il&nbsp;**“CIAO!”&nbsp;**che abbiamo scritto&nbsp;**è inserito nella console di Javascript**, non nel body della pagina. Per vedere la console Javascript premi il tasto “**f12**“, oppure fai click con il tasto destro e clicca su “**ispeziona**” (Su google chrome, ma è molto simile su tutti i browser)

<div class="wp-block-image">
  <figure class="aligncenter size-large"><img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-11-1536x353-1-1024x235.png" alt="" class="wp-image-197" /></figure>
</div>

### Commenti

I&nbsp;**commenti**&nbsp;sono&nbsp;**importantissimi**&nbsp;in ogni linguaggio di programmazione.

Per inserire i commenti in Javascript esistono**&nbsp;due modi:**

Se il commento è su&nbsp;**una sola riga&nbsp;**puoi inserire un**&nbsp;doppio slash**&nbsp;prima della riga. In questo modo**&nbsp;tutta la riga sarà commentata.**

**Esempio**

<pre class="wp-block-code"><code>// Questo è un commento su una riga Javascript</code></pre>

Se invece&nbsp;**il commento è più lungo**, puoi usare la stessa sintassi del CSS:**_&nbsp;/\* Commento \*/_**

**Esempio:**

<pre class="wp-block-code"><code>/*
Questo è un commento
Javascript su più righe
*/</code></pre>

### Variabili

A differenza di HTML e CSS,&nbsp;**Javscript è un vero e proprio linguaggio di programmazione**, e non dei più semplici.

Come ogni linguaggio di prograammazione è possibile&nbsp;**utilizzare delle variabili per memorizzare i dati e fare calcoli.**

Inserire una variabile è molto semplice, basta inserire “**var**” prima della variabile, in questo modo:

<pre class="wp-block-code"><code>var anni = 30;</code></pre>

È fondamentale&nbsp;**inserire il punto e virgola**&nbsp;alla fine della variabile, per indicare che la regola finisce in quel punto. Senza il punto e virgola verranno generati degli errori.

Ora possiamo&nbsp;**richiamare la variabile dentro il console.log&nbsp;**oppure in un&nbsp;**alert**, in questo modo:

<pre class="wp-block-code"><code>console.log(anni);</code></pre>

oppure:

<pre class="wp-block-code"><code>alert(anni);</code></pre>

**Salviamo**&nbsp;e&nbsp;**aggiorniamo**&nbsp;e vedremo il numero “**30**” apparire nel popup oppure nella cosole.

**Ma possiamo fare di più!**

Impostiamo&nbsp;**una serie di variabili:**

<pre class="wp-block-code"><code>var nome = "Marco";
var altezza = "1.83";
var anni = 30;</code></pre>

Adesso possiamo c**reare una frase ed inserire al suo interno le nostre variabili,**&nbsp;oltre che utilizzarle per fare dei calcoli.

I&nbsp;**valori testuali devono essere inseriti fra virgolette**, mentre i&nbsp;**valori numerici senza**. In questo modo possiamo fare anche delle&nbsp;**operazioni aritmetiche.**

**Ecco un esempio:**

<pre class="wp-block-code"><code>console.log('Ciao, mi chiamo ' + nome + ' e sono alto ' + altezza + ' metri. In questo momento ho ' + anni + ' anni. Fra 5 anni avrò ' + (anni + 5) + ' anni.'); &lt;/script&gt;
</code></pre>

Per inserire una&nbsp;**variabile in un testo**&nbsp;occorre&nbsp;**concatenarla**, metterla insieme.

Per fare questo abbiamo utilizzato il segno**&nbsp;‘+’.**

### Funzioni

Le funzioni sono delle&nbsp;**parti di codice che svolgono una determinata azione**.

Isolando una parte di codice in una funzione, questa potrà essere&nbsp;**richiamata**&nbsp;più volte all’interno del progetto.

Le funzioni possono avere dei&nbsp;**parametri**, che ne personalizzano l’azione.

**Esempio:**

Andiamo sul file&nbsp;_**scripts.js&nbsp;**_e scriviamo:

<pre class="wp-block-code"><code>function ciao() {
   alert ("CIAO");
}</code></pre>

Ora andiamo sul file&nbsp;_**index.htm**_l e aggiungiamo un bottone, in questo modo:

<pre class="wp-block-code"><code>&lt;button onclick="ciao()"&gt;Salutami&lt;/button&gt;</code></pre>

**Salviamo**&nbsp;e&nbsp;**aggiorniamo**&nbsp;e vedremo che&nbsp;**cliccando sul nuovo bottone apparirà il popup con scritto “CIAO”.**

### Parametri

Adesso aggiungiamo un&nbsp;**parametro**. Andiamo nella funzione a la modifichiamo così:

<pre class="wp-block-code"><code>function ciao(nome) {
    alert ("CIAO "+nome);
 }</code></pre>

e sul file&nbsp;_**index.html**_&nbsp;modifichiamo così il bottone:

<pre class="wp-block-code"><code>&lt;button onclick="ciao('Marco')"&gt;Salutami&lt;/button&gt;</code></pre>

**Salviamo**&nbsp;e&nbsp;**aggiorniamo**&nbsp;e possiamo vedere che ora il saluto è rivolto al nome inserito nel parametro della funzione!

“Marco” è il nostro parametro

### If Else

Gli “If” sono&nbsp;**alla base di tutta la programmazione**. Ogni azione è fatta come conseguenza di un’altra. Vediamo cosa significa.

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

Ora possiamo andare a&nbsp;**modificare il parametro nel bottone**, da “Marco” a “Mark”, oppure inserire un nome totalmente diverso.

Se il nome è Marco allora il popup sarà “Ciao Marco”, se Mark allora “Hello Mark”, se altro sarà “Buongiorno + nome”.

Da notare come&nbsp;**ci siano due segni uguale**, questo perché nel Javascript un uguale assegna il valore, per confrontarli invece occorre usarne 2 o 3 a seconda dei casi. Per il momento ci basta sapere che quando dobbiamo connfrontare più valori bisogna inserire 2 segni uguale.

### Eventi

**Il Javascript può essere richiamato all’interno dell’HTML all’accadere di determinati eventi,&nbsp;**per esempio al click, al passaggio con il mouse etc.

Oggi esistono anche molti altri modi, ma per iniziare questi sono i più semplici ed immediati.

**Esempio:**

<pre class="wp-block-code"><code>&lt;button onclick="alert('CIAO!')"&gt;Salutami&lt;/button&gt;</code></pre>

In questo caso al click del bottone apparirà il&nbsp;**popup di saluto.**

## Creiamo il nostro primo effetto

Al di là della teoria,&nbsp;**a noi interessa soprattutto vedere come possiamo utilizzare Javascript per creare gli effetti per le nostre pagine web.**

Quindi ora andremo a&nbsp;**creare un semplice effetto che cambierà lo sfondo del body al click di un bottone.**

**Vediamo come fare:**

Iniziamo con il creare un bottone nella nostra_**&nbsp;index.html:**_

<pre class="wp-block-code"><code>&lt;button onclick="cambiaSfondo()"&gt; Cambia sfondo! &lt;/button&gt;</code></pre>

Ora andiamo nel nostro&nbsp;**_scripts.js_**&nbsp;e creiamo la funzione&nbsp;**cambiaSfondo()**:

<pre class="wp-block-code"><code>function cambiaSfondo(){
   document.body.style.backgroundColor='#000';
}</code></pre>

Se&nbsp;**salviamo**&nbsp;e&nbsp;**aggiorniamo**&nbsp;vedremo che ora**&nbsp;al click del bottone lo sfondo diventerà nero.**

Abbiamo detto al browser che al click del bottone deve selezionare il colore di sfondo del body (body.style.backgroundcolor) e impostarlo a nero.

Notiamo però che&nbsp;**è un’unica azione**, una volta che lo sfondo è nero non possiamo più tornare al bianco…

**Andiamo ad aggiungere ancora qualche linea di codice:**

<pre class="wp-block-code"><code>function cambiaSfondo(){
    var sfondo = document.body.style.backgroundColor;
    if(sfondo=="rgb(0, 0, 0)"){
        document.body.style.backgroundColor='#fff';
    }else{
        document.body.style.backgroundColor='#000';

    }
}</code></pre>

In questo modo facciamo un&nbsp;**controllo del colore di sfond**o. Se è nero lo impostiamo bianco, altrimento sarà nero.

Così facendo possiamo&nbsp;**cambiare colore di sfondo ogni volta che clicchiamo sul bottone.**

**Congratulazioni! Hai appena creato il tuo primo effetto Javascript!!!**

## Animazione di un componente

Se al posto dello sfondo intero volessimo modificare solamente un&nbsp;**componente**, possiamo farlo utilizzando gli&nbsp;**id**&nbsp;([Le basi di CSS][2]).

Iniziamo con il creare un&nbsp;**div con id=”box”**

<pre class="wp-block-code"><code>&lt;div id="box" onmouseover="cambiaBoxOver()" onmouseout="cambiaBoxOut()"&gt;
   Questo contenitore cambiarà colore al passaggio del mouse
&lt;/div&gt;</code></pre>

Ora&nbsp;**creiamo le due funzioni in scripts.js:**

<pre class="wp-block-code"><code> function cambiaBoxOver(){
    document.getElementById('box').style.backgroundColor="coral";
    document.getElementById('box').style.color="blue";
}

 function cambiaBoxOut(){
    document.getElementById('box').style.backgroundColor="white";
    document.getElementById('box').style.color="black";

}</code></pre>

**Salviamo**&nbsp;e&nbsp;**aggiorniamo**&nbsp;e vediamo che&nbsp;**il contenitore cambia colore e sfondo al passaggio del mouse.**

Molto bene,&nbsp;**queste sono le basi per iniziare a smanettare un po’ con il Javascript.**

**Cercando online potrai trovare moltissime guide e tutorial sull’argomento.**

**È però bene conoscere anche un po’ di Javascript**&nbsp;e soprattutto JQuery, per poter&nbsp;**evitare di installare un’infinità di plugin e crearci da soli tutti gli effetti e le funzioni che vogliamo!**

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
      <em><a href="https://albertoreineri.it/guide/le-basi-dellhtml/"><< Le basi di CSS</a></em>
    </p>
  </div>

  <div class="wp-block-column is-vertically-aligned-center is-layout-flow wp-block-column-is-layout-flow">
    <p class="has-text-align-right">
      <em><a href="https://albertoreineri.it/guide/le-basi-di-bootstrap/">Le basi di Bootstrap >></a></em>
    </p>
  </div>
</div>

 [1]: https://albertoreineri.it/guide/le-basi-dellhtml/
 [2]: https://albertoreineri.it/guide/le-basi-del-css/