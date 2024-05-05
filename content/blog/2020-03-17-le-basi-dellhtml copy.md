---
title: 1. Le basi dell’HTML
author: Alberto
type: post
date: 2020-03-17T23:50:00+00:00
url: /le-basi-dellhtml/
nectar_blog_post_view_count:
  - 19
tags:
  - Guide
  - Inizia Qui

---
**L’HTML è la base del web**, c’è dappertutto! Ogni pagina internet che visualizzi ha del codice HTML al suo interno. Se vuoi diventare uno sviluppatore web quindi la prima cosa da fare è un corso intensivo di HTML!

<hr class="wp-block-separator"/>

_Questo corso è rivolto ai **principianti**, pertanto se conosci già l’HTML questo articolo non fa per te, se invece sei agli inizi **BENVENUTO **e buono studio! Vedrai che** imparerai presto** a cerare fantastici contenuti web!_

<hr class="wp-block-separator"/>

L’HTML non è proprio un linguaggio di programmazione, ma è un **linguaggio di markup,** infatti HTML è l’acronimo di _HyperText Markup Language_.

Ciò significa che l’HTML non fa operazioni di calcolo, ma sostanzialmente indica al browser **come _montare _la pagina**, cosa posizionare e come posizionarlo.

## Cosa serve per iniziare

Per iniziare a scrivere codice HTML** non servono super computer** nè programmi pesanti e costosi.

Se vuoi iniziare a sviluppare contenuti per il web inizialmente** ti bastano 2 cose:**

  * web browser
  * editor di testo

### Web Browser

Sviluppando qualcosa che sarà fruibile attraverso un browser,** il browser è fondamentale**. Ne esistono veramente molti e tutti validi, ma il mio consiglio è di utilizzare** <a href="https://www.google.com/intl/it_it/chrome/" rel="noreferrer noopener" target="_blank">Google Chrome</a>**.

Se non sei un fan del browser di google eccoti alcune alternative:

  * <a href="https://www.microsoft.com/it-it/edge" rel="noreferrer noopener" target="_blank">Microsoft Edge</a> (Windows)
  * <a href="https://www.apple.com/it/safari/" rel="noreferrer noopener" target="_blank">Safari</a> (Mac)
  * <a href="https://www.mozilla.org/it/firefox/new/" rel="noreferrer noopener" target="_blank">Mozilla Firefox</a>

### Editor di testo

L’altro software **fondamentale **per sviluppare per il web è un editor di testo.

Un editor di testo è un programma che **consente di scrivere il codice.** Si potrebbe utilizzare banalmente il classico editor di testo del sistema operativo (Blocco note o Text edit), ma fortunatamente esistono software dedicati allo sviluppo che rendono la scrittura del codice molto più semplice.

Il mio consiglio è di utilizzare **<a href="https://code.visualstudio.com/" rel="noreferrer noopener" target="_blank">VS Code</a>**, a mio avviso in questo momento è il migliore in assoluto.

Anche qui hai comunque molta scelta! Ecco alcune delle migliori **alternative **a VS Code:

  * <a href="https://www.sublimetext.com/" rel="noreferrer noopener" target="_blank">Sublime Text</a>
  * <a href="https://atom.io/" rel="noreferrer noopener" target="_blank">Atom</a>
  * <a href="http://brackets.io/" rel="noreferrer noopener" target="_blank">Brackets</a>
  * <a href="https://notepad-plus-plus.org/downloads/" rel="noreferrer noopener" target="_blank">Notepad++</a>

## Creiamo il nostro primo file HTML

Ora che hai scaricato un browser e un editor di testo, possiamo crerare il nostro primo file HTML.

Creiamo una **cartella **sul desktop chiamata “**HTML**“. Ora apriamo questa cartella con **VS Code**, facendo click con il tasto destro del mouse all’interno della cartella e cliccando “**Apri con Code**“

{{&lt; image src="/assets/img/uploads/https://albertoreineri.it/wp-content/uploads/2022/03/Group-5-1.jpeg" >}}

Ora possiamo creare il nostro file con VS Code.

Clicchiamo “**CTRL+N**” per creare un nuovo file e poi “**CTRL+S**” per salvarlo, con il nome “**_index.html_**“.

Tutti i file HTML devono avere estensione .html, cioè finire con .html, questo farà capire al browser il tipo di file che sta leggendo.

Puoi creare i file anche tramite il menù in alto, cliccando su “File-New File” oppure con l’icona specifica nella barra laterale sulla sinistra.

**PERFETTO! Abbiamo creato il nostro primo file HTML!**

## Struttura base

Ogni pagina HTML è diversa, ma tutte hanno una **struttura base comune**, uno _**scheletro **_sul quale sono costruite.

_VS Code_ ci permette di creare questo scheletro in maniera **semplicissima e molto veloce.**

Ci basterà aprire il file, inserire un **punto esclamativo** e cliccare il tasto “**tab**“. In questo modo VS Code creerà la struttura base della nostra pagina HTML in automatico.

Se hai fatto questa operazione dovresti vedere comparire questo codice all’interno del file:

<pre class="wp-block-code"><code>&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;Document&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;

&lt;/body&gt;
&lt;/html&gt;</code></pre>

Questo è lo _**scheletro **_di ogni pagina HTML. Andiamo ad analizzarlo!

## I tag HTML

L’HTML è un linguaggio basato sui **tag**.

Ogni tag indica una** tipologia di contenuto.**

**Struttura base**: <nometag>contenuto</nometag>

Qualsiasi contenuto è sempre inserito all’interno di un **tag**, che **indica al browser come trattare quel tipo di contenuto**.

Generalmente i tag hanno un inizio e una fine, il tag di fine inizia con uno slash(/).

Esistono però alcuni tag senza tag di chiusura, come il tag <br/>, che è utilizzato per andare a capo.

## Esempi di tag:

<pre class="wp-block-code"><code>&lt;html&gt;&lt;/html&gt;</code></pre>

Questi tag indicano dove inizia e dove finisce la pagina HTML. Tutto il contenuto va inserito fra questi due!

<pre class="wp-block-code"><code>&lt;head&gt;&lt;/head&gt;</code></pre>

Questo tag permette di inserire delle informazioni relative alla pagina, come il titolo, gli stili da inserire, gli script etc. (Questo ti sarà più chiaro man mano che andrai avanti)

<pre class="wp-block-code"><code>&lt;body&gt;&lt;/body&gt;</code></pre>

All’interno di questi tag c’è il vero e proprio contenuto della pagina

<pre class="wp-block-code"><code>&lt;h1&gt;La mia prima pagina web&lt;/h1&gt;</code></pre>

I titoli sono inseriti dentro i tag heading, che vanno dall’1 al 6, in ordine di importanza. Il titolo della pagina deve essere inserito fra i tag <h1></h1>, il sottotitolo <h2></h2> e così via.

<pre class="wp-block-code"><code>&lt;br&gt;</code></pre>

Questo tag indica al browser di andare a capo.

<pre class="wp-block-code"><code>&lt;!-- Questo è un commento --&gt;</code></pre>

In qualiasi tipo di codice è molto importante inserire i commenti. Questi permettono di inserire delle note all’interno del codice, per poter capire meglio cosa si sta scrivendo o per inserire delle frasi rivolte ai colleghi etc.

<pre class="wp-block-code"><code>&lt;ul&gt;

    &lt;li&gt;Questo è un item di un elenco&lt;/li&gt;

    &lt;li&gt;Questo è un altro item&lt;/li&gt;

&lt;/ul&gt;</code></pre>

Il tag <ul> permette di inserire un elenco. Per inserire un elenco numerato c’è il tag <ol> (Unordered List e Ordered List).

Ogni elemento di un elenco deve essere inserito con il tag <li> (List Item)

## Sporchiamoci le mani

Iniziamo ora a **modificare lo** **_scheletro _**della nostra pagina HTML.

Iniziamo a modificare la **lingua**, modificando “en” con “it” nella **riga 2 **del nostro file.

La riga 2 sarà quindi così:

<pre class="wp-block-code"><code>&lt;html lang="en"&gt;</code></pre>

Ora andiamo sulla riga 6 e modifichiamo il titolo, nel tag **_<title>_**.

Chiamiamo questa pagina “**La mia prima pagina web**“

<pre class="wp-block-code"><code>&lt;title&gt;La mia prima pagina web&lt;/title&gt;</code></pre>

Ora salviamo il file e apriamolo, semplicemente aprendo la cartella “**HTML**” e facendoci **doppio click** sopra.

{{&lt; image src="/assets/img/uploads/https://albertoreineri.it/wp-content/uploads/2022/03/image-1536x529-1-1024x353.png" >}}

Ci troveremo di fonte una **pagina completamente bianca**, perché non abbiamo ancora inserito nessun codice nel contenuto.

Possiamo vedere però che il nome della scheda in alto è “**La mia prima pagina web**“. Questo è il **_<title>_** della nostra pagina.

**Ora inseriamo un po’ di contenuto.**

Andiamo **fra i tag <body></body>** e inseriamo questo:

<pre class="wp-block-code"><code>   &lt;h1&gt;La mia prima pagina web&lt;/h1&gt;
    &lt;p&gt;Benvenuto nella mia prima pagina web!&lt;/p&gt;
    &lt;br&gt;&lt;!-- questo è un a capo--&gt;
    &lt;p&gt;Questo è il secondo paragrafo della mia prima pagina web&lt;/p&gt;
    &lt;br&gt;
    &lt;h2&gt;Elenco&lt;/h2&gt;
    &lt;ul&gt;
        &lt;li&gt;Primo Item&lt;/li&gt;
        &lt;li&gt;Secondo Item&lt;/li&gt;
    &lt;/ul&gt;</code></pre>

Ora** salva la pagina e aggiornala nel browser**, vedrai comparire del contenuto!

{{&lt; image src="/assets/img/uploads/https://albertoreineri.it/wp-content/uploads/2022/03/image-1.png" >}}

Non è difficile da capire, ogni tag spiega se stesso.

**CONGRATULAZIONI!**

**Hai appena creato la tua prima pagina web!**

Ma addentriamoci ancora un po’ nell’HTML.

## Inseriamo un’immagine

Per inserire un’immagine in una pagina HTML bisogna utilizzare il tag **<img/>**, con alcuni attributi.

Gli **attributi **forniscono **informazioni aggiuntive **ai tag html. Per esempio il tag <img/> indicherà al browser di inserire un’immagine, ma quale immagine? A questa domanda rispondiamo con l’attributo “**src**“, cioè la sorgente da cui il browser può attingere per inserire l’immagine.

Esempio:

<pre class="wp-block-code"><code>&lt;img src="immagini/foto.jpg"&gt;</code></pre>

In questo esempio il browser inserirà l’immagine** foto.jpg **presente nella cartella “**immagini**“.

Proviamo ora ad inserire un’immagine nella nostra pagina.

Andiamo nella nostra cartella “**HTML**” sul desktop e creiamo una cartella chiamata “**img**“, all’interno di questa cartella inseriamo ora una qualsiasi immagine in formato **JPG**.

Adesso** richiamiamo l’immagine nel nostro file _index.html_,** in questo modo:

<pre class="wp-block-code"><code>&lt;img src="img/immagine.jpg"&gt;</code></pre>

Ora **salviamo **il file e **aggiorniamo **il browser.

{{&lt; image src="/assets/img/uploads/https://albertoreineri.it/wp-content/uploads/2022/03/image-2-768x370-1.png" >}}

Vediamo che l’immagine viene visualizzata nella nostra pagina html.

Però è un po’** troppo grande!** Almeno nel mio caso, questo dipende dalle dimensioni dell’immagine.

Per visualizzare l’immagine in modo più carino possiamo aggiungere un altro attributo al nostro tag <img/>: **l’attributo height o width**

<pre class="wp-block-code"><code>    &lt;img src="img/immagine.jpg" width="200"&gt;</code></pre>

In questo modo sto **impostando la larghezza dell’immagine a 200px.** Ed ecco che si vede tutto decisamente meglio.

{{&lt; image src="/assets/img/uploads/https://albertoreineri.it/wp-content/uploads/2022/03/image-3.png" >}}

In questo modo posso **ridimensionare **l’immagine.

Ora **andiamo ancora più a fondo **nell’html.

## I contenitori

Nelle nostre pagine html possiamo inserire dei **contenitori**, nei quali inserire del contenuto. Questi sono molto utili per **suddividere le pagine e gestire i contenuti al meglio.**

### <div>

Un primo tipo di contenitore è il tag **<div>**. Questo crea una **sezione **nella pagina. È un **block element**, cioè il contenuto dopo questo tag è inserito** a capo**.

### <span>

Lo **<span>** è un contenitore ma **inline**, cioè **non va a capo** dopo di esso.

Se voglio creare un quadrato verde nel sito dovrò utilizzare un <div>, se invece voglio colorare una parola di rosso allora userò il tag <span>.

**Eccoti un esempio:**

Aggiungi questo codice a_** index.html**_

<pre class="wp-block-code"><code>    &lt;div style="background-color: green;"&gt;
        Questo è un contenitore con sfondo verde
    &lt;/div&gt;
    &lt;p&gt;
        Questo è un paragrafo con del testo inserito a caso. In questo testo voglio &lt;span style="color:red"&gt;colorare&lt;/span&gt; una parola di rosso
    &lt;/p&gt;</code></pre>

ed ecco il **risultato**

{{&lt; image src="/assets/img/uploads/https://albertoreineri.it/wp-content/uploads/2022/03/image-4-1536x666-1-1024x444.png" >}}

Per inserire i colori ho utilizzato l’attributo “style”, che permette di inserire del codice CSS all’interno dell’HTML, ma lo vedremo meglio nella[ guida][1] [al CSS.][2]

## I form

Un altro elemento molto importante di una pagina web è il **form**.

Navigando online avrai compilato moltissime volte dei **moduli**, che siano di contatto, di prenotazione etc.

Per inserire un form occorre utilizzare il tag **<form></form>** e al suo interno inserire **le tipologia di input **richieste.

**Esempio **di form:

<pre class="wp-block-code"><code>  &lt;form&gt;
        &lt;input type="text" placeholder="Nome"&gt;
        &lt;br&gt;&lt;br&gt;
        &lt;input type="text" placeholder="Cognome"&gt;
        &lt;br&gt;&lt;br&gt;
        &lt;select name="select" id=""&gt;
            &lt;option value="0"&gt;Opzione 1&lt;/option&gt;
            &lt;option value="1"&gt;Opzione 2&lt;/option&gt;
            &lt;option value="2"&gt;Opzione 3&lt;/option&gt;
        &lt;/select&gt;
        &lt;br&gt;&lt;br&gt;
        &lt;textarea name="" id="" cols="30" rows="10" placeholder="Inserisci il testo qui."&gt;&lt;/textarea&gt;
        &lt;br&gt;&lt;br&gt;
        &lt;input type="checkbox" name="privacy" value="0"&gt;Accetto la Privacy Policy
        &lt;br&gt;&lt;br&gt;
        &lt;button&gt;Invia&lt;/button&gt;
    &lt;/form&gt;</code></pre>

Prova a inserire questo codice in**_ index.html_**, salvare e aggiornare.

Vedrai comparire dei campi compilabili.

**Questi campi sono**

  * input di tipo text nel caso del nome e del cognome.
  * select nel caso del menù a tendina
  * textarea nel caso dell’area di testo
  * input di tipo checkbox per accettare la privacy
  * button per il bottone di invio

Premendo sul tasto “**Invia**” non succederà nulla. Per far svolgere un’azione alla nostra pagina html occorre integrarla con altri linguaggi. Ricordi che **l’HTML è solamente un linguaggio di markup**, non di programmazione.

Per questa guida è tutto. Ti lascio ancora **il codice per intero della nostra _index.html_ **con i **commenti **che spiegano cosa fa ogni cosa.

<pre class="wp-block-code"><code>&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;

&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;La mia prima pagina web&lt;/title&gt;&lt;!-- Il titolo della pagina che appare nella scheda del browser --&gt;
&lt;/head&gt;

&lt;body&gt;
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
&lt;/body&gt;

&lt;/html&gt;</code></pre>

**Ora puoi iniziare a smanettare un po’ con i tag** che hai imparato, provando a **creare e modificare qualche pagina HTML!**



<p class="has-text-align-right">
  Leggi anche <em><a href="https://albertoreineri.it/guide/le-basi-del-css/">Le basi del CSS &gt;&gt;</a></em>
</p>
<div class="wp-block-buttons is-content-justification-right is-layout-flex wp-container-core-buttons-is-layout-2 wp-block-buttons-is-layout-flex">
</div>

 [1]: https://albertoreineri.it/guide/le-basi-del-css/
 [2]: https://albertoreineri.it/corso-intensivo-di-css/</span></div></span></span></div></div></title></title></li></ol></ul>