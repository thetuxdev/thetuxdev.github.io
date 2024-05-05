---
title: SASS Tutorial – Che cos’è e perché non potrai più farne a meno
author: Alberto
type: post
date: 2019-11-10T20:07:00+00:00
url: /sass-tutorial-che-cose-e-perche-non-potrai-piu-farne-a-meno/
nectar_blog_post_view_count:
  - 39
tags:
  - Guide
  - Web Dev

---
Se vivi nel mondo dello **sviluppo web** allora sicuramente avrai già sentito parlare di **SASS**, il preprocessore di CSS più famoso! Questo è uno **strumento fantastico** che consente di **estendere di molto le possibilità del CSS** e creare e gestire i fogli di stile in maniera **veloce **e ben **organizzata**.

**SASS **è un **preprocessore CSS**, che aggiunge funzionalità speciali come **variabili**, **annidamenti**, **mixin **e molto altro ai normali CSS. L’obiettivo è rendere il processo di creazione del C**SS semplice ed efficace**, sia da scrivere che da leggere in futuro.

<blockquote class="wp-block-quote is-layout-flow wp-block-quote-is-layout-flow">
<p>
<em>Ma andiamo un po’ più nel dettaglio!</em>
</p>
</blockquote>

## Che cos’è un preprocessore CSS?

Un preprocessore CSS è un **linguaggio di scripting** che estende i CSS, consentendo agli sviluppatori di scrivere codice in un determinato linguaggio e quindi **compilarlo **in CSS. <a href="https://sass-lang.com/" rel="noreferrer noopener" target="_blank">Sass </a>è forse il preprocessore più popolare in circolazione in questo momento, ma altri esempi ben noti includono <a href="http://lesscss.org/" rel="noreferrer noopener" target="_blank">Less </a>e <a href="http://stylus-lang.com/" rel="noreferrer noopener" target="_blank">Stylus</a>.

**Prima di proseguire, è necessaria una rapida premessa:**_ la maggior parte dei web designer direbbe che se sei nuovo nel mondo del CSS, è meglio evitare Sass (o eventuali preprocessori, estensioni o framework) mentre sei ancora in fase di apprendimento. Sebbene questi tool offrono molti vantaggi in termini di velocità ed efficienza, è importante che conoscere a fondo le basi del CSS prima di affacciarsi ai preprocessori. Assicurati quindi di apprendere i concetti chiave prima di iniziare ad esplorare i vari tool a disposizione. Questo vale per ogni tecnologia ed ogni framework, prima è sempre buona norma imparare a dovere il linguaggio base e poi i vari strumenti su esso costruiti!_

<blockquote class="wp-block-quote is-layout-flow wp-block-quote-is-layout-flow">
<p>
<em>Finito il predicozzo torniamo a Sass!</em>
</p>
</blockquote>

## Che cos’è Sass?

**Sass **(che sta per “Syntactically awesome style sheets”) è un’**estensione del CSS** che consente di usare cose come variabili, regole nidificate, importazioni in linea e altro. Aiuta anche a mantenere il **codice organizzato **e consente di **creare fogli di stile molto più velocemente.**

**Sass è compatibile con tutte le versioni di CSS**. L’unico requisito per usarlo è avere installato Ruby. Gli sviluppatori che lo utilizzano sono inoltre invitati a seguire le <a href="https://sass-lang.com/community-guidelines" rel="noreferrer noopener" target="_blank">Linee guida della community di Sass</a>, è sempre un bene darci un’occhiata.

## Come usare Sass?

Nella sezione seguente, vedremo alcuni suggerimenti di base per l’utilizzo di Sass, usando esempi tratti dal sito Web ufficiale di Sass. Dai un’occhiata alla <a href="https://sass-lang.com/documentation" rel="noreferrer noopener" target="_blank">documentazione ufficiale</a> per ulteriori riferimenti ed esempi.

### Sintassi

Sass include **due opzioni di sintassi**:

  * **SCSS **(Sassy CSS): utilizza l’estensione del file .scss ed è pienamente conforme alla sintassi CSS. (la mia preferita!)
  * **SASS**: utilizza l’indentazione al posto delle parentesi ed ha estensione .sass; non è completamente conforme alla sintassi CSS, ma è più veloce da scrivere. (Per gli amanti di Python)

I file possono comunque essere convertiti da una sintassi all’altra utilizzando il comando **sass-convert**.

### Variabili

Proprio come altri linguaggi di programmazione, **Sass consente l’uso di variabili** che possono memorizzare informazioni che è possibile utilizzare in tutto il foglio di stile.

Ad esempio,** è possibile memorizzare un valore di colore in una variabile** nella parte superiore del file e quindi utilizzare questa variabile quando si imposta il colore dei propri elementi. Ciò consente di **cambiare rapidamente i colori senza dover modificare ciascuna riga separatamente**.

_Per esempio:_

<pre class="wp-block-code"><code>$font-stack:    Helvetica, sans-serif;
$primary-color: #333;

body {
  font: 100% $font-stack;
  color: $primary-color;
}</code></pre>

**Questo codice genererà il seguente CSS:**

<pre class="wp-block-code"><code>body {
  font: 100% Helvetica, sans-serif;
  color: #333;
}</code></pre>

### Annidamento

_L’annidamento è un’arma a doppio taglio._ Sebbene fornisca un metodo eccellente per ridurre la quantità di codice da scrivere, può anche portare a CSS troppo “incasinati” se non eseguito con cura.

L’idea è di annidare i selettori CSS in modo tale da **imitare la gerarchia HTML.**

Ecco un **esempio **di menù di navigazione che utilizza l’annidamento:

<pre class="wp-block-code"><code>nav {
  ul {
    margin: 0;
    padding: 0;
    list-style: none;
  }

  li { display: inline-block; }

  a {
    display: block;
    padding: 6px 12px;
    text-decoration: none;
  }
}</code></pre>

**L’output CSS sarà il seguente:**

<pre class="wp-block-code"><code>nav ul {
  margin: 0;
  padding: 0;
  list-style: none;
}

nav li {
  display: inline-block;
}

nav a {
  display: block;
  padding: 6px 12px;
  text-decoration: none;
}</code></pre>

### Parzializzazione

I **parziali **sono **file Sass più piccoli** che possono essere importati (vedi la sezione successiva) in altri file Sass. Sono come** frammenti di codice**. Con questi frammenti il CSS può essere **modulare **e più **facile da mantenere**. Un parziale è designato come tale nominandolo con un carattere di underscore iniziale: **_partial.scss**.

### Importazione

Utilizzatato con i parziali (vedere la sezione precedente), il comando @import consente di **importare i file parziali nel file corrente**, per **creare un singolo file CSS.** In questo modo in fase di sviluppo è possibile **suddividere il codice per sezioni**, mentre in fase di caricamento del sito ci sarà solamente **un file .css **da caricare,** riducendo la richiesta al server**.

_Ecco un esempio:_

**_reset.scss**

<pre class="wp-block-code"><code>html,
body,
ul,
ol {
   margin: 0;
  padding: 0;
}</code></pre>

**basefile.scss**

<pre class="wp-block-code"><code>@import 'reset';

body {
  font: 100% Helvetica, sans-serif;
  background-color: #efefef;
}</code></pre>

**Output CSS:**

<pre class="wp-block-code"><code>html, body, ul, ol {
  margin: 0;
  padding: 0;
}

body {
  font: 100% Helvetica, sans-serif;
  background-color: #efefef;
}</code></pre>

**Importante**: quando si importano i parziali, non è necessario includere l’estensione del file o l’underscore.

### Mixins

Uno dei vantaggi dell’utilizzo dei preprocessori è la capacità di **prendere codice complesso e complicato e semplificarlo**. È qui che i mixin ci vengono in aiuto!

Ad esempio, se è necessario includere i **vendor prefixes**, è possibile utilizzare un mixin. Dai un’occhiata a questo esempio per border-radius:

<pre class="wp-block-code"><code>@mixin border-radius($radius) {
  -webkit-border-radius: $radius;
     -moz-border-radius: $radius;
      -ms-border-radius: $radius;
          border-radius: $radius;
}

.box { @include border-radius(10px); }</code></pre>

Da notare: il comando @mixin è in alto. È stato dato il nome “border-radius” e la variabile “$radius” come parametro. Questa variabile viene utilizzata per impostare il valore del raggio per ciascun elemento.

Successivamente, viene chiamato il comando @include, insieme al nome del mixin (“border-radius”) e un parametro (10px). Pertanto .box {@include border-radius (10px); }.

**Viene prodotto il seguente CSS:**

<pre class="wp-block-code"><code>.box {
  -webkit-border-radius: 10px;
  -moz-border-radius: 10px;
  -ms-border-radius: 10px;
  border-radius: 10px;
}</code></pre>

### Extend

Il comando @extend è stato definito una delle **funzionalità più potenti** di Sass. Dopo averlo visto in azione, è chiaro il perché.

L’idea è che con questa direttiva non dovrai includere più nomi di classe nei tuoi elementi HTML e puoi **mantenere il tuo codice DRY** (Don’t repeat yourself). I selettori possono ereditare gli stili di altri selettori e quindi essere facilmente estesi quando necessario.

### Operatori

La possibilità di e**seguire calcoli nel CSS** consente consente di ampliare le possibilità, come convertire i valori dei pixel in percentuali. Si può avere accesso a funzioni matematiche standard come **addizione, sottrazione, moltiplicazione e divisione**. Naturalmente, queste funzioni possono essere combinate per creare calcoli complessi.

Inoltre, Sass include alcune funzioni integrate per aiutare a manipolare i numeri. Funzioni come **percentage()**, **floor() **e **round()** per citarne alcuni.

Se ancora non conoscevi questo strumento inizia subito ad utilizzarlo nel progetto in corso, sicuramente non te ne pentirai!

Se invece lo conoscevi già spero di averti magari rivelato qualche caratteristica ulteriore di questo fantastico tool!

Buon codice!