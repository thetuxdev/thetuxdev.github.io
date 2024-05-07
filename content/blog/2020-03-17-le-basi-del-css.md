---
title: 2. Le basi del CSS
author: Alberto
type: post
date: 2020-03-17T22:31:00+00:00
url: /le-basi-del-css/
nectar_blog_post_view_count:
  - 30
tags:
  - Guide
  - Inizia Qui

---
Il CSS è il linguaggio di **formattazione **del web. Sta per _Cascading Style Sheets_ ed è utilizzato per **assegnare uno stile alle pagine html**.

Ha una sintassi specifica e permette di separare l’html dal suo stile, mantene do così il **codice pulito ed ordinato**.

Come l’HTML, anche il css **non è un linguaggio di programmazione**, è un linguaggio utilizzato per creare i layout delle pagine web. Consente di gestire gli spazi, modificare i colori, creare i layout e tutto ciò che ha a che fare con la parte grafica di un contenuto web.

<hr class="wp-block-separator"/>

_Questo corso è rivolto ai **principianti**, pertanto se conosci già il CSS questo articolo non fa per te, se invece sei agli inizi **BENVENUTO **e buono studio! Vedrai che** imparerai presto** a cerare fantastici contenuti web!_

<hr class="wp-block-separator"/>

Questo articolo è una continuazione del la guida [Le basi di][1] [HTML][2], che puoi trovare [qui][1].

Se ti perdi durante l’articolo sul fondo di questo articolo potrai trovare il codice di tutto ciò che andremo a creare.

## Come inserire il CSS in una pagina HTML

Il CSS da solo quindi non serve a nulla, ma **deve essere inserito in una pagina html.**

Esistono **3 modi** per inserire del codice CSS in una pagina HTML

  * **Inline CSS**
  * **CSS Interno**
  * **CSS Esterno**

### Inline CSS

Consente di inserire del codice CSS **direttamente all’interno del codice HTML.**

Con questo metodo **i linguaggi HTML e CSS restano mischiati insieme**. Un esempio di questa tipologia di codice è quello che abbiamo inserito nel corso intensivo di HTML, quando abbiamo impostato lo sfondo verde al div, o il rosso alla parola nello span.

**Esempio**:

<pre class="wp-block-code"><code>&lt;div style="background-color:green&gt;Ciao Mondo&lt;/div&gt;</code></pre>

Sebbene sia molto veloce da applicare, **è il modo peggiore** per inserire del codice CSS.

**Mischiare i linguaggi di programmazione non è mai un bene**, è meglio imparare fin da subito che l’ordine è una caratteristica fondamentale per un buon sviluppatore.

Vediamo quindi gli altri metodi.

### CSS Interno

Questo metodo consiste nell’inserire il codice CSS **all’interno dell’head **della pagina HTML.

In questo modo il CSS è all’interno della pagina HTML ma **non in mezzo al contenuto HTML.** È una scelta sicuramente migliore rispetto all’Inline CSS ma non ancora ottimale.

Per inserire del CSS interno occorre andare **fra i tag <head></head>** e indicare che stiamo per scrivere del codice CSS, in questo modo:

<pre class="wp-block-code"><code>&lt;style type="text/css"&gt;


&lt;/style&gt;</code></pre>

All’interno del tag <style> possiamo inserire il codice CSS.

**Esempio:**

<pre class="wp-block-code"><code>&lt;style type="text/css"&gt;
   h1{
      color:red
   }
&lt;/style&gt;</code></pre>

In questo caso**&nbsp;tutti gli h1 della pagina saranno rossi.**

### CSS Esterno

Questo è&nbsp;**il modo migliore**&nbsp;e più efficiente di gestire i file CSS.

Consiste nel&nbsp;**creare un file esterno**, che deve avere estensione .css, e&nbsp;**richiamarlo nell’head della pagina HTML.**

In questo modo&nbsp;**i linguaggi sono ben separati**, ognuno nel suo file.

**Esempio:**

Ora&nbsp;**creiamo un nuovo file**&nbsp;(CTRL+N) e salviamolo (CTRL+S) con il nome “**_style.css_**“.

In questo file possiamo inserire questo:

<pre class="wp-block-code"><code>h1{
   color:red;
}</code></pre>

Ora&nbsp;**salviamo**&nbsp;“**_style.css_**” e apriamo “_**index.html**_“.

Andiamo&nbsp;**nell’head**&nbsp;di “index.html” e inseriamo questo sotto al title:

<pre class="wp-block-code"><code>&lt;link rel="stylesheet" href="style.css"&gt;</code></pre>

Se apri il file “**_index.html_**” nel tuo browser noterai che&nbsp;**l’h1 ora è rosso.**

Questi sono&nbsp;**i tre metodi&nbsp;**per inserire del codice CSS in una pagina HTML. Come avrai potuto capire&nbsp;**il metodo migliore è il terzo**, ma ci sono alcune occasioni nelle quali può essere utile applicare uno dei primi due metodi.

Ora che abbiamo imparato a inserire il CSS in una pagina HTML iniziamo a parlare proprio di CSS!

## Sintassi CSS

Il CSS è un linguaggio con una&nbsp;**sintassi specifica**. Se si commette un&nbsp;**errore**&nbsp;nella scrittura della sintassi il codice&nbsp;**non funzionerà.**

Ecco uno&nbsp;**schema**&nbsp;che raccoglie gli&nbsp;**elementi**&nbsp;del linguaggio CSS:

{{< image src="/img/uploads/schema-CSS.jpeg" >}}


<div class="wp-block-image">
  <figure class="aligncenter size-full"><img decoding="async" src="/img/uploads/2022/03/schema-CSS.jpeg" alt="" class="wp-image-189" /></figure>
</div>

### Selettore

Indica&nbsp;**l’oggetto a cui applicare lo stile**. Questo può essere un tag html, come <h1>, <p> etc., oppure una classe o un id (approfondiremo classi e id fra poco).

### Proprietà

Una proprietà è una&nbsp;**regola che si applica al selettore**. Il CSS ha moltissime proprietà, man mano che imparerai questo linguaggio ne scoprirai sempre di più. Fortunatamente VS Code offre una lista di tutte le proprietà, visibile premendo “CTRL+Space Bar”.

Nell’esempio di prima la proprietà è “_**color**_“, altre fra le più utilizzate sono “background-color”, “margin”, “padding”, “border” etc.

### Valore

È il&nbsp;**valore da assegnare alla proprietà**. Può essere un colore, un numero in pixel o altro ancora. Imparerai ad utilizzare i valori corretti man mano che utilizzerai il CSS.

Proprietà e Valore devono essere racchiusi in una&nbsp;**parentesi graffa.**

Al termine di ogni Valore occorre inserire un “**punto e virgola**“.

**Esempio:**

<pre class="wp-block-code"><code>h1{
   color:red;
}</code></pre>

  * **h1**&nbsp;è il&nbsp;**selettore**
  * sopo il selettore apro la&nbsp;**graffa**
  * **color**&nbsp;è la&nbsp;**Proprietà**
  * **red**&nbsp;è il&nbsp;**Valore**
  * alla fine del valore inserisco il&nbsp;**punto e virgola**
  * chiudo la&nbsp;**graffa**.

Dopo questa piccola introduzione teorica&nbsp;**iniziamo a fare sul serio!**

## **Iniziamo a sporcarci le mani**

Andiamo nel nostro file “style.css” e iniziamo a scrivere del codice CSS!

Iniziamo con il dare uno stile generale alla nostra pagina, utilizzando il selettore “body”, in questo modo:

<pre class="wp-block-code"><code>body{
   color:#444;
   background-color:#f2f2f2
}</code></pre>

In questo modo abbiamo inserito un colore grigio scuro al testo e un bianco leggermente sporco allo sfondo.

## I colori

Nel codice CSS ci sono&nbsp;**vari modi con i quali inserire i colori:**

  * Nome del colore
  * Esadecimale
  * RGB

### Nome del colore

Questo modo consente di indicare il colore semplicemente scrivendo il&nbsp;**nome del colore in inglese**.

Per esempio se voglio un colore bianco basterà scrivere “white”, e così via.

**Esempio:**

<pre class="wp-block-code"><code>color:blue;</code></pre>

### Esadecimale

Il colore è indicato utilizzando un codice esadecimale, chiamato anche&nbsp;**Hex code**. Per utilizzare questo metodo occorre inserire un # seguito dal codice a 6 cifre. È di gran lunga il metodo più utilizzato.

**Esempio:**

<pre class="wp-block-code"><code>color:#f4f4f4;</code></pre>

### RGB

Consiste nell’indicare il colore utilizzando il&nbsp;**metodo RGB**. È possibile anche utilizzare delle trasparenze con l’RGBA.

**Esempi:**

**RGB:**

<pre class="wp-block-code"><code>rgb(243, 163, 44)</code></pre>

**RGBA**:

<pre class="wp-block-code"><code>rgba(243, 163, 44,.7)</code></pre>

In questo caso il “.7” indica che la trasparenza sarà al 70%.

## Font

Una delle prime cose da fare quando si personalizza un layout è&nbsp;**scegliere un bel font.**

Per inserire un font in un sito web occorre&nbsp;**importarlo**, per essere certi che qualsiasi utente su qualsiasi computer visualizzi il font corretto.

Fortunatamente&nbsp;**google&nbsp;**mette a disposizione moltissimi&nbsp;**font&nbsp;**in maniera&nbsp;**gratuita&nbsp;**e semplicissima da utilizzare. Vediamo come.

Per prima cosa andiamo su&nbsp;**google fonts**, a questo link:&nbsp;<https://fonts.google.com/>

Qua possiamo cercare il font che più ci piace. In questa guida utilizzeremo il “**Source Sans Pro**“.

Inseriamo quindi “**Source Sans Pro**” nella barra di ricerca di Google Fonts

<div class="wp-block-image">
  <figure class="aligncenter size-full"><img decoding="async" src="/img/uploads/2022/03/image-5.png" alt="" class="wp-image-190" /></figure>
</div>

e lo&nbsp;**selezioniamo**.

Ora ci troveremo di fronte ad una schermata come questa:

<div class="wp-block-image">
  <figure class="aligncenter size-large"><img decoding="async" src="/img/uploads/2022/03/image-6-1536x725-1-1024x483.png" alt="" class="wp-image-192" /></figure>
</div>

Sulla destra possiamo cliccare su “**+ Select this style**” in corrispondenza del carattere che vogliamo. Possiamo selezionarli tutti per avere tutte le variabili possibili del font, ma per ottimizzare i tempo di caricamento della pagina è meglio selezionare solo l’essenziale.

In questa guida selezioniamo solo il “**regular 400**” e il “**bold 700**“.

Ora si aprirà sulla destra una finestra come questa:

<div class="wp-block-image">
  <figure class="aligncenter size-full"><img decoding="async" src="/img/uploads/2022/03/image-7.png" alt="" class="wp-image-193" /></figure>
</div>

Qua clicchiamo su “**Embed**” e successivamente su “**@import**“

<div class="wp-block-image">
  <figure class="aligncenter size-full"><img decoding="async" src="/img/uploads/2022/03/image-8.png" alt="" class="wp-image-194" /></figure>
</div>

Adesso possiamo copiare il contenuto fra&nbsp;_<style>_&nbsp;e&nbsp;_</style>_ e incollarlo nel nostro **“style.css**“, cancellando tutto il resto.

Ora aggiungiamo questo codice:

<pre class="wp-block-code"><code>body{
    font-family: 'Source Sans Pro', sans-serif;
    font-size: 22px;
    font-weight: 400;
    font-style: normal;
    line-height: 35px;
}</code></pre>

In questo modo abbiamo impostato **“Source Sans Pro” come font primario **del sito.

Ecco cos’altro abbiamo impostato:

  * **Font-size** indica la **dimensione **del font, che abbiamo settato a 22 pixel.
  * **Font-weight** indica lo **spessore **del font, in questo caso è settato come regolare. In questo campo possiamo utilizzare sia i numeri da 100 a 900, sia il nome, da “lighter” a “bolder”. Logicamente occorrerà importare queste dimensioni da google fonts, per il momento abbiamo importato solo il 400 e il 700.
  * **Font-style** indica lo **stile **del font, in questo caso è normale. Puoi inserire per esempio “italiac” per avere un font in corsivo.
  * **Line-height **indica **l’altezza **del font, lo spazio fra le righe, in questo caso impostato a 35 pixel.

Prova a **salvare **il foglio di stile e **aggiornare **la pagina, vedrai che **il testo sarà cambiato!**

## Classi e id

Come abbiamo già accennato poco fa, è possibile impostare delle classi e degli id ai tag html, in modo da poterli **raggruppare **alcune regole di css.

Classi e id sono **attributi **che possiamo** aggiungere ai tag html** per distinguerli fra loro.

### Id

Un **id **è un** attributo univoco**, va utilizzato nel caso ci sia un elemento particolare che **non si ripeterà **mai. Se per esempio voglio che un titolo sia giallo, solo quel titolo, posso dargli un id particolare.

Per indicare un id nel CSS occorre farlo precedere da un **hashtag**

**Esempio:**

**_style.css_**

<pre class="wp-block-code"><code>#giallo{
   color:yellow
}</code></pre>

**_index.html_**

<pre class="wp-block-code"><code>&lt;h2 id="giallo"&gt;Questo titolo è giallo&lt;/h2&gt;</code></pre>

### Classi

Una classe è un** elemento che ritorna spesso**, e che quindi posso **riutilizzare**. Per esempio se voglio inserire una serie di bottoni con la stessa formattazione, posso dare loro la classe “**bottone**“, impostarla una sola volta nel CSS e questa verrà applicata a tutti gli elementi con la classe “bottone”

Per indicare una classe nel CSS occorre farla precedere da un **punto**.

**Esempio:**

_**style.css**_

<pre class="wp-block-code"><code>.bottone{
   background-color:coral;
   border-radius: 15px;
   color:white;
}</code></pre>

**_index.html_**

<pre class="wp-block-code"><code>&lt;div class="bottone"&gt;Premi qui!&lt;/div&gt;</code></pre>

## Margin e Padding

Per gestire gli spazi fra gli elementi si possono utilizzare “**margin**” e “**padding**“.

Ecco uno **schema **per spiegarti che differenza c’è fra i due:

{{< image src="/img/uploads/2022/03/margin-e-padding-1.jpeg" >}}

Il **margin **indica lo spazio **all’esterno** del contenuto, il **padding **lo spazio **all’interno**.

È possibile indicare la **direzione **dello spazio sia per il margin che per il padding, per esempio se si vuole inserire un margine superiore occorre utiilzzare “**margin-top**“.

Ecco alcuni **esempi**:

_**style.css**_

<pre class="wp-block-code"><code>.box-margin{
    background-color: coral;
    margin:50px
}
.box-padding{
    background-color: coral;
    padding:50px
}
.box-margin-top{
    margin-top: 50px;
    background-color: aquamarine;
}</code></pre>

**_index.html_**

<pre class="wp-block-code"><code>    &lt;h2&gt;Margin e Padding&lt;/h2&gt;
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
    &lt;/div&gt;</code></pre>

## Contenitore

Gli elementi del CSS possono essere** uno dentro l’altro**, in questo modo permettono di creare layout più elaborati.

Proviamo a rendere la nostra pagina HTML un po’ più carina inserendola in un **contenitore**.

Andiamo** sotto il tag body** e inseriamo un **div **con classe “**container**“, in questo modo:

<pre class="wp-block-code"><code>&lt;div class="container"&gt;</code></pre>

Ora andiamo prima del  e** chiudiamo questo div**, inserendo:

<pre class="wp-block-code"><code>&lt;/div&gt;</code></pre>

Ora aggiungiamo questo codice nel nostro “**style.css**“:

<pre class="wp-block-code"><code>.container{
    max-width: 800px;
    margin: 0 auto;
}</code></pre>

In questo modo abbiamo impostato una **larghezza massima del contenuto della nostra pagina a 800 pixel**, e impostato il margine del contenuto a 0 pixel dall’alto e dal basso e **automaticamente **da destra e sinistra.

Ora **salviamo **e **aggiorniamo **e vedremo il contenuto inserito a centro pagina, più carino no?

## Immagine come sfondo

Vediamo ancora un’ultima cosa prima di terminare questa prima carrellata generale di CSS: come inserire **un’immagine come sfondo** di un elemento.

Per poter inserire un’immagine come sfondo occorre utilizzare la proprietà “**background-image**“.

Creiamo un **div **che conterrà la nostra immagine nel file **html**:

<pre class="wp-block-code"><code>&lt;div class="immagine-sfondo"&gt;
    Questo div ha un'immagine di sfondo!
&lt;/div&gt;</code></pre>

E inseriamo l’url all’immagine tramite il **CSS **nel nostro “style.css”:

<pre class="wp-block-code"><code>.immagine-sfondo{
    background-image: url(img/immagine.jpg);
    height:500px;
    text-align: center;
    padding-top: 250px;
    color:white;
}</code></pre>

In questo modo abbiamo impostato **la nostra immagine come sfondo. **Abbiamo anche impostato **un’altezza **in modo da far vedere bene l’immagine.

Prova a **salvare **e **aggiornare **e vedrai cosa succede.

**Ora prova a smanettare un po’ **con queste classi e con queste regole, modificando dimensioni, font, colori, immagini e tutto ciò che hai in mente!

Ricorda che** il modo migliore per imparare e dedicare tanto tempo** alla pratica, quindi** inizia a darci dentro con il CSS!**

### Codice completo:

Qua puoi trovare il **codice completo** dei file index.html e style.css

**_index.html_**

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
    &lt;!-- Titolo --&gt;
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

    &lt;!-- Immagine --&gt;
    &lt;img src="img/immagine.jpg" width="200"&gt;

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

&lt;div class="immagine-sfondo"&gt;
    Questo div ha un'immagine di sfondo!
&lt;/div&gt;

&lt;/div&gt;
&lt;/body&gt;

&lt;/html&gt;</code></pre>

**_style.css_**

<pre class="wp-block-code"><code>@import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@400;700&amp;display=swap');
body{
    font-family: 'Source Sans Pro', sans-serif;
    font-size: 22px;
    font-weight: lighter;
    line-height: 35px;
    font-style: normal;
}
.box-margin{
    background-color: coral;
    margin:50px
}
.box-padding{
    background-color: coral;
    padding:50px
}
.box-margin-top{
    margin-top: 50px;
    background-color: aquamarine;
}
.container{
    max-width: 800px;
    margin: 0 auto;
}
.immagine-sfondo{
    background-image: url(img/immagine.jpg);
    height:500px;
    text-align: center;
    padding-top: 250px;
    color:white;
}</code></pre>
<div class="wp-block-columns are-vertically-aligned-center is-layout-flex wp-container-core-columns-is-layout-4 wp-block-columns-is-layout-flex">
<div class="wp-block-column is-vertically-aligned-center is-layout-flow wp-block-column-is-layout-flow">
<p>
<em><a href="/le-basi-dellhtml/">&lt;&lt; Le basi di HTML</a></em>
</p>
</div>
<div class="wp-block-column is-vertically-aligned-center is-layout-flow wp-block-column-is-layout-flow">
<p class="has-text-align-right">
<em><a href="/le-basi-di-javascript/">Le basi di Javascript &gt;&gt;</a></em>
</p>
</div>
</div>

 [1]: /le-basi-dellhtml/
 [2]: /le-basi-dellhtml/