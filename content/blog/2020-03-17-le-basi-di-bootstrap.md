---
title: 4. Le basi di Bootstrap
author: Alberto
type: post
date: 2020-03-17T20:42:49+00:00
url: /le-basi-di-bootstrap/
nectar_blog_post_view_count:
  - 28
tags:
  - Guide
  - Inizia Qui

---
<p class="has-cyan-bluish-gray-color has-text-color">
<em>Questa guida fa riferimento a Bootstrap 4, ora è uscita la versione 5… Appena avrò un attimo di tempo la aggiornerò!</em>
</p>
<hr class="wp-block-separator"/>

Se vuoi diventare uno **sviluppatore web** oggi non puoi fare a meno che scontrarti con **bootstrap**.

Come dice il <a href="https://getbootstrap.com/" rel="noreferrer noopener" target="_blank">sito web uffiliale</a>, **Bootstrap è il framework HTML, CSS e JS più popolare al mondo!**

Una vastissima parte dei layout web sono create attraverso **Bootstrap**, perché rende lo sviluppo responsive **semplice e veloce.**

Sebbene esisteno anche altre alternative, Bootstrap rimane un fondamento nei **layout del web**.

## Cos’è Bootstrap

Ma che cos’è praticamente **Bootstrap**?

Bootstrap è un insieme di** librerie css e js** che velocizzano la realizzazione dei layout delle pagine web.

È stato sviluppato da **Twitter **ed è un progetto **open source.**

## Come includere Bootstrap

Per poter utilizzare Bootstrap occorre includerlo nel progetto, **inserendo **le librerie css e js nella pagina web.

Questo può essere fatto in **2 modi:**

  * Tramite CDN
  * Scaricando i file

### CDN

Questo metodo consiste nel **richiamare Bootstrap dalla CDN**. È facile e veloce, non occorre scaricare nulla, basta inserire questo codice nell’**_<head>_**:

<pre class="wp-block-code"><code>&lt;link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous"&gt;
</code></pre>

e questo prima della fine del **_<body>_**:

<pre class="wp-block-code"><code>&lt;script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"&gt;&lt;/script&gt;
&lt;script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"&gt;&lt;/script&gt;
&lt;script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"&gt;&lt;/script&gt;</code></pre>

**_E voilà! _**Bootstrap è inserito sul sito ed è pronto a funzionare!

### Scaricando i file

Questo metodo consiste nello** scaricare i file di bootstrap**, inserirli nella cartella del sito web e **richiamarli**.

I file di Bootstrap sono **scaricabili** a questa pagina:

<https: 4.0="" docs="" download="" getbootstrap.com="" getting-started=""></https:>

Una volta scaricati occorrerà inserire il file **css nell'<head>** e il **js prima del </head></body>.**

Nel download saranno presenti **molte versioni** dei file, a noi interessano quelli minizzati:

  * bootstrap.min.css
  * bootstrap.min.js

Inseriamo quindi questo codice nell’_**<head>**_:

<pre class="wp-block-code"><code>&lt;link rel="stylesheet" href="css/bootstrap.min.css"&gt;</code></pre>

E questo prima del**_ _**:

<pre class="wp-block-code"><code>&lt;script src="js/bootstrap.min.css"&gt;&lt;/script&gt;</code></pre>

Proseguendo** utilizzeremo il metodo CDN**, per semplicità e velocità di configurazione.

**Ecco il template di base da cui partiremo:**

<pre class="wp-block-code"><code>&lt;!doctype html&gt;
&lt;html lang="it"&gt;
  &lt;head&gt;
    &lt;!-- Required meta tags --&gt;
    &lt;meta charset="utf-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"&gt;

    &lt;!-- Bootstrap CSS --&gt;
    &lt;link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous"&gt;

    &lt;!-- Ulteriore CSS --&gt;

    &lt;title&gt;Corso intensivo Bootstrap!&lt;/title&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;h1&gt;Corso intensivo Bootstrap!&lt;/h1&gt;

    &lt;!-- Ulteriore Javascript --&gt;

    &lt;!-- jQuery, Popper.js e Bootstrap JS **L'ordine è molto importante, non modificarlo** --&gt;
    &lt;script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"&gt;&lt;/script&gt;
    &lt;script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"&gt;&lt;/script&gt;
    &lt;script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;</code></pre>

## La griglia di Bootstrap

La **parte fondamentale** di Bootstrap è la sua griglia.

Bootstrap utilizza un sistema basato su **12 colonne**, che si **adattano **alla dimensione dello **schermo**.

La griglia è composta da un **contenitore **(_container_), al cui interno vengono inserite delle **righe **(_row_), al cui interno possono essere inserite delle **colonne **(_col_).

Le colonne possono essere configurate in modo che la loro** larghezza si adatti e cambi** a seconda della dimensione dello schermo.

**Ma è tutto più facile a farsi che a dirsi, quindi iniziamo!**

Creiamo un **layout **suddiviso su **2 colonne** che diventeranno 1 se lo schermo è più piccolo di un laptop!

Sotto l'<h1> del nostro file inseriamo questo:

<pre class="wp-block-code"><code>    &lt;!-- Layout 2 colonne Laptop, 1 colonna da tablet in giù --&gt;
    &lt;div class="container bg-secondary"&gt;
        &lt;div class="row"&gt;
            &lt;div class="col-lg-6 bg-success"&gt;
                Colonna 1
            &lt;/div&gt;
            &lt;div class="col-lg-6 bg-warning"&gt;
                Colonna 2
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/div&gt;</code></pre>

Il codice si spiega da solo!

Ecco che abbiamo un layout con 2 colonne su **desktop**:


E di 1 colonna da **tablet **in giù:

{{< image src="/assets/img/uploads/2022/03/image-17.png" >}}

Vedrai che la larghezza è minore dell’intero schermo del desktop.

Se vuoi una larghezza del layout al 100% sostituisci “**container**” con “**container-fluid**“.

## Come visualizzare la modalità mobile da pc

Per avere un’idea di come il sito sarà sui vari **dispositivi **puoi utilizzare la funzione “**Toggle Device**” di Chrome.

Su google chrome premi **f12 **e poi questa **icona** sulla sinistra:

{{< image src="/assets/img/uploads/2022/03/image-18.png" >}}

Dopodiché in alto potrai scegliere un dispositivo mobile oppure selezionare le **dimensioni **che preferisci attraverso l’opzione “**Responsive**“

{{< image src="/assets/img/uploads/2022/03/image-20.png" >}}

## Breakpoints

Bootstrap ha già preimpostati vari **breakpoints**, dal **desktop **al **mobile**.

Indicando **col-lg-6** significa che il contenuto occuperà** 6 colonne delle 12 **disponibili finché la larghezza è maggiore di lg, dopodiché il contenuto occuperà l’intera larghezza dello schermo.

Ecco una tabella delle **dimensioni **e delle colonne di bootstrap:<figure class="wp-block-table">
<table>
<tr>
<th>
       
    </th>
<th>
      Extra small<br/><small>&lt;576px</small>
</th>
<th>
      Small<br/><small>≥576px</small>
</th>
<th>
      Medium<br/><small>≥768px</small>
</th>
<th>
      Large<br/><small>≥992px</small>
</th>
<th>
      Extra large<br/><small>≥1200px</small>
</th>
</tr>
<tr>
<th scope="row">
      Max container width
    </th>
<td>
      None (auto)
    </td>
<td>
      540px
    </td>
<td>
      720px
    </td>
<td>
      960px
    </td>
<td>
      1140px
    </td>
</tr>
<tr>
<th scope="row">
      Class prefix
    </th>
<td>
<code>.col-</code>
</td>
<td>
<code>.col-sm-</code>
</td>
<td>
<code>.col-md-</code>
</td>
<td>
<code>.col-lg-</code>
</td>
<td>
<code>.col-xl-</code>
</td>
</tr>
</table></figure>

È possibile creare** layout complessi in modo semplice**, grazie a questo sistema di suddivisione delle colonne.

Ecco un **esempio**:

<pre class="wp-block-code"><code>    &lt;!-- Layout 2 colonne Laptop, 3 colonna da tablet, 1 colonna da smartphone --&gt;
    &lt;div class="container bg-secondary"&gt;
        &lt;div class="row"&gt;
            &lt;div class="col-lg-6 col-md-4 bg-success"&gt;
                Colonna
            &lt;/div&gt;
            &lt;div class="col-lg-6 col-md-4 bg-warning"&gt;
                Colonna
            &lt;/div&gt;
            &lt;div class="col-lg-6 col-md-4 bg-success"&gt;
                Colonna
            &lt;/div&gt;
            &lt;div class="col-lg-6 col-md-4 bg-warning"&gt;
                Colonna
            &lt;/div&gt;
            &lt;div class="col-lg-6 col-md-4 bg-success"&gt;
                Colonna
            &lt;/div&gt;
            &lt;div class="col-lg-6 col-md-4 bg-warning"&gt;
                Colonna
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/div&gt;</code></pre>

In questo caso abbiamo 2 colonne da desktop, 3 da tablet e 1 da smartphone.

Ora** prova anche tu **a creare dei layout utilizzando la tabella qua sopra! Il modo migliore per imparare è** provare, provare e provare!**

## Componenti

Bootstrap, oltre alla griglia, comprende una serie di **componenti già belli e pronti **da utilizzare sui nostri siti, basta copiare il componente, **incollarlo **nel nostro sito e poi andarlo a modificare come più ci piace!

Tutti i componenti sono visibili a questo **link**:

<https: 4.3="" alerts="" components="" docs="" getbootstrap.com=""></https:>

Sulla sinistra vedrai un menù con l’elenco dei componenti.

**Vediamo adesso quelli più utilizzati!**

### Navbar

Andiamo a creare una **navbar **per il nostro sito!

Nulla di più semplice con Bootstrap, ci basterà andare a cercare “**Navbar**” fra i vari componenti (<https: 4.3="" components="" docs="" getbootstrap.com="" navbar=""></https:>) e **copiare il codice **per inserirla, nel nostro caso questo:

<pre class="wp-block-code"><code>&lt;nav class="navbar navbar-expand-lg navbar-light bg-light"&gt;
  &lt;a class="navbar-brand" href="#"&gt;Navbar&lt;/a&gt;
  &lt;button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"&gt;
    &lt;span class="navbar-toggler-icon"&gt;&lt;/span&gt;
  &lt;/button&gt;

  &lt;div class="collapse navbar-collapse" id="navbarSupportedContent"&gt;
    &lt;ul class="navbar-nav mr-auto"&gt;
      &lt;li class="nav-item active"&gt;
        &lt;a class="nav-link" href="#"&gt;Home &lt;span class="sr-only"&gt;(current)&lt;/span&gt;&lt;/a&gt;
      &lt;/li&gt;
      &lt;li class="nav-item"&gt;
        &lt;a class="nav-link" href="#"&gt;Link&lt;/a&gt;
      &lt;/li&gt;
      &lt;li class="nav-item dropdown"&gt;
        &lt;a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"&gt;
          Dropdown
        &lt;/a&gt;
        &lt;div class="dropdown-menu" aria-labelledby="navbarDropdown"&gt;
          &lt;a class="dropdown-item" href="#"&gt;Action&lt;/a&gt;
          &lt;a class="dropdown-item" href="#"&gt;Another action&lt;/a&gt;
          &lt;div class="dropdown-divider"&gt;&lt;/div&gt;
          &lt;a class="dropdown-item" href="#"&gt;Something else here&lt;/a&gt;
        &lt;/div&gt;
      &lt;/li&gt;
      &lt;li class="nav-item"&gt;
        &lt;a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true"&gt;Disabled&lt;/a&gt;
      &lt;/li&gt;
    &lt;/ul&gt;
    &lt;form class="form-inline my-2 my-lg-0"&gt;
      &lt;input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search"&gt;
      &lt;button class="btn btn-outline-success my-2 my-sm-0" type="submit"&gt;Search&lt;/button&gt;
    &lt;/form&gt;
  &lt;/div&gt;
&lt;/nav&gt;</code></pre>

Vogliamo però apportare qualche **modifica**, per esempio non ci serve la ricerca sulla navbar, ma vogliamo che il nome del sito sia a sinistra, mente il menù a destra.

Ci basterà quindi **eliminare il form** di ricerca e modificare il margine del menù, da “**mr-auto**” a “**ml-auto**“, nell’ul “navbar-nav”:

<pre class="wp-block-code"><code>    &lt;nav class="navbar navbar-expand-lg navbar-light bg-light"&gt;
        &lt;a class="navbar-brand" href="#"&gt;Navbar&lt;/a&gt;
        &lt;button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"&gt;
          &lt;span class="navbar-toggler-icon"&gt;&lt;/span&gt;
        &lt;/button&gt;

        &lt;div class="collapse navbar-collapse" id="navbarSupportedContent"&gt;
          &lt;ul class="navbar-nav ml-auto"&gt;
            &lt;li class="nav-item active"&gt;
              &lt;a class="nav-link" href="#"&gt;Home &lt;span class="sr-only"&gt;(current)&lt;/span&gt;&lt;/a&gt;
            &lt;/li&gt;
            &lt;li class="nav-item"&gt;
              &lt;a class="nav-link" href="#"&gt;Link&lt;/a&gt;
            &lt;/li&gt;
            &lt;li class="nav-item dropdown"&gt;
              &lt;a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"&gt;
                Dropdown
              &lt;/a&gt;
              &lt;div class="dropdown-menu" aria-labelledby="navbarDropdown"&gt;
                &lt;a class="dropdown-item" href="#"&gt;Action&lt;/a&gt;
                &lt;a class="dropdown-item" href="#"&gt;Another action&lt;/a&gt;
                &lt;div class="dropdown-divider"&gt;&lt;/div&gt;
                &lt;a class="dropdown-item" href="#"&gt;Something else here&lt;/a&gt;
              &lt;/div&gt;
            &lt;/li&gt;
            &lt;li class="nav-item"&gt;
              &lt;a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true"&gt;Disabled&lt;/a&gt;
            &lt;/li&gt;
          &lt;/ul&gt;
        &lt;/div&gt;
      &lt;/nav&gt;</code></pre>

Vediamo che abbiamo la nostra bella** navbar pronta e responsiva!**

Prova a visualizzare in modalità smartphone, vedrai che il menù scompare e apparirà **l’hamburgher **che mostrerà il menù al click:

**Desktop:**

**Mobile:**

{{< image src="/assets/img/uploads/2022/03/image-22.png" >}}

### Bottoni

Un altro componente utilissimo sono i **bottoni**! Bootstrap fornisce un insieme di bottoni già pronti e **ben formattati**, disponibili nei colori più utilizzati, eccoli qui:

<pre class="wp-block-code"><code>&lt;button type="button" class="btn btn-primary"&gt;Primary&lt;/button&gt;
&lt;button type="button" class="btn btn-secondary"&gt;Secondary&lt;/button&gt;
&lt;button type="button" class="btn btn-success"&gt;Success&lt;/button&gt;
&lt;button type="button" class="btn btn-danger"&gt;Danger&lt;/button&gt;
&lt;button type="button" class="btn btn-warning"&gt;Warning&lt;/button&gt;
&lt;button type="button" class="btn btn-info"&gt;Info&lt;/button&gt;
&lt;button type="button" class="btn btn-light"&gt;Light&lt;/button&gt;
&lt;button type="button" class="btn btn-dark"&gt;Dark&lt;/button&gt;

&lt;button type="button" class="btn btn-link"&gt;Link&lt;/button&gt;</code></pre>
{{< image src="/assets/img/uploads/2022/03/image-24.png" >}}

La classe “**btn**” indica il bottone, mentre “**btn-primary**” indica la tipologia del bottone.

### Caroselli

Inserire dei caroselli non è mai stato così semplice! Anche qua basta andare a cercare il componente “**Carousel**” sul sito di bootstrap ed inserire il codice!

**Esempio:**

<pre class="wp-block-code"><code>&lt;div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel"&gt;
  &lt;ol class="carousel-indicators"&gt;
    &lt;li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"&gt;&lt;/li&gt;
    &lt;li data-target="#carouselExampleIndicators" data-slide-to="1"&gt;&lt;/li&gt;
    &lt;li data-target="#carouselExampleIndicators" data-slide-to="2"&gt;&lt;/li&gt;
  &lt;/ol&gt;
  &lt;div class="carousel-inner"&gt;
    &lt;div class="carousel-item active"&gt;
      &lt;img src="..." class="d-block w-100" alt="..."&gt;
    &lt;/div&gt;
    &lt;div class="carousel-item"&gt;
      &lt;img src="..." class="d-block w-100" alt="..."&gt;
    &lt;/div&gt;
    &lt;div class="carousel-item"&gt;
      &lt;img src="..." class="d-block w-100" alt="..."&gt;
    &lt;/div&gt;
  &lt;/div&gt;
  &lt;a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev"&gt;
    &lt;span class="carousel-control-prev-icon" aria-hidden="true"&gt;&lt;/span&gt;
    &lt;span class="sr-only"&gt;Previous&lt;/span&gt;
  &lt;/a&gt;
  &lt;a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next"&gt;
    &lt;span class="carousel-control-next-icon" aria-hidden="true"&gt;&lt;/span&gt;
    &lt;span class="sr-only"&gt;Next&lt;/span&gt;
  &lt;/a&gt;
&lt;/div&gt;</code></pre>

Logicamente dobbiamo** inserire un “src” alle immagini** per farle visualizzare, ma il carosello funziona fina da subito!

### Form

Anche creare **form graficamente accettabili** è velocissimo! Bootstrap consente di creare degli input carini e ben stilizzati senza perdere il minimo tempo!

Ecco un **esempio**:

<pre class="wp-block-code"><code>&lt;form&gt;
  &lt;div class="form-group"&gt;
    &lt;label for="exampleInputEmail1"&gt;Email address&lt;/label&gt;
    &lt;input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email"&gt;
    &lt;small id="emailHelp" class="form-text text-muted"&gt;We'll never share your email with anyone else.&lt;/small&gt;
  &lt;/div&gt;
  &lt;div class="form-group"&gt;
    &lt;label for="exampleInputPassword1"&gt;Password&lt;/label&gt;
    &lt;input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password"&gt;
  &lt;/div&gt;
  &lt;div class="form-group form-check"&gt;
    &lt;input type="checkbox" class="form-check-input" id="exampleCheck1"&gt;
    &lt;label class="form-check-label" for="exampleCheck1"&gt;Check me out&lt;/label&gt;
  &lt;/div&gt;
  &lt;button type="submit" class="btn btn-primary"&gt;Submit&lt;/button&gt;
&lt;/form&gt;</code></pre>

Questi sono solo **alcuni **dei **componenti **disponibili! Naviga un po’ fra la lista dei componenti e **prova ad inserirli per vedere come funzionano!**

Una volta che ti sarai impadronito della griglia potrai cerare siti web responsive in maniera rapida e veloce!

E non dimenticare che** Bootstrap è cross-browser**, cioè funziona sempre e ovunque senza problemi!

## Modificare Bootstrap

Puoi anche **aggiungere un tuo file css** personale per andare a sovrascrivere alcune classi di bootstrap e personalizzarle come vuoi!

Se per esempio vogliamo che il btn-primary sia arancione, possiamo creare un nostro file css con questo al suo interno:

<pre class="wp-block-code"><code>.btn-primary{
   background-color:orange !important;
}</code></pre>

Ricordati solamente di **inserire questo css dopo bootstrap**, in modo che vada a sovrascriverlo!

Così tutti i btn-primary saranno **arancione **anziché blu!

## Layout di esempio

Creiamo ora una **home page semplice utilizzando solo bootstrap!**

### **Template di base:**

<pre class="wp-block-code"><code>&lt;!DOCTYPE html&gt;
&lt;html lang="it"&gt;

&lt;head&gt;
    &lt;meta charset="utf-8"&gt;
    &lt;meta http-equiv="X-UA-Compatible" content="IE=edge"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1"&gt;
    &lt;!-- I 3 meta tags qua sopra DEVONO essere inseriti come primi --&gt;
    &lt;meta name="description" content="Corso intensivo di Bootstrap"&gt;
    &lt;meta name="author" content="Specialista WP!"&gt;

    &lt;title&gt;Corso intensivo di Bootstrap&lt;/title&gt;

    &lt;!-- Bootstrap CSS --&gt;
    &lt;link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet"&gt;

&lt;/head&gt;

&lt;body&gt;

    &lt;!-- JQuery e Bootstrap JavaScript  --&gt;
    &lt;script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"&gt;&lt;/script&gt;
    &lt;script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"&gt;&lt;/script&gt;
&lt;/body&gt;

&lt;/html&gt;</code></pre>

### Navbar:

Ora inseriamo una** navbar con il menù allineato a destra**, come abbiamo visto prima:

<pre class="wp-block-code"><code>    &lt;nav class="navbar navbar-expand-lg navbar-light bg-light"&gt;
        &lt;div class="container"&gt;
            &lt;a class="navbar-brand" href="#"&gt;Corso intensivo di Bootstrap&lt;/a&gt;
            &lt;button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"&gt;
                &lt;span class="navbar-toggler-icon"&gt;&lt;/span&gt;
            &lt;/button&gt;

            &lt;div class="collapse navbar-collapse" id="navbarSupportedContent"&gt;
                &lt;ul class="navbar-nav ml-auto"&gt;
                    &lt;li class="nav-item active"&gt;
                        &lt;a class="nav-link" href="#"&gt;Home &lt;span class="sr-only"&gt;(current)&lt;/span&gt;&lt;/a&gt;
                    &lt;/li&gt;
                    &lt;li class="nav-item"&gt;
                        &lt;a class="nav-link" href="#"&gt;Chi sono&lt;/a&gt;
                    &lt;/li&gt;
                    &lt;li class="nav-item"&gt;
                        &lt;a class="nav-link" href="#"&gt;Blog&lt;/a&gt;
                    &lt;/li&gt;
                    &lt;li class="nav-item"&gt;
                        &lt;a class="nav-link" href="#"&gt;Contatti&lt;/a&gt;
                    &lt;/li&gt;
                &lt;/ul&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/nav&gt;</code></pre>

### Contenuto

Ora creiamo il classico layout con il **contenuto sulla sinistra** e una **sidebar sulla destra**. Da smartphone invece la sidebar sarà sotto il contenuto.

<pre class="wp-block-code"><code>    &lt;div class="container mt-5"&gt;

        &lt;div class="row"&gt;
            &lt;!-- CONTENUTO --&gt;
            &lt;div class="col-sm-8"&gt;

                &lt;!-- ARTICOLO --&gt;
                &lt;div&gt;
                    &lt;!-- TITOLO --&gt;
                    &lt;h2 class=""&gt;Il mio articolo&lt;/h2&gt;
                    &lt;!-- META --&gt;
                    &lt;p&gt;15 luglio 2020 - Scritto da &lt;a href="#"&gt;Alberto&lt;/a&gt;&lt;/p&gt;
                    &lt;!-- CONTENT --&gt;
                    &lt;p&gt;
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque et justo ultrices, blandit nulla in, convallis metus. Nullam et mollis orci.
                        Nulla magna augue, accumsan in metus ut, pulvinar facilisis libero. Aliquam erat volutpat. Nulla lectus tortor, lacinia id imperdiet ut, sagittis
                        consectetur magna. Maecenas laoreet sodales tristique. [...]
                    &lt;/p&gt;
                &lt;/div&gt;
                &lt;!-- /ARTICOLO --&gt;

                &lt;!-- ARTICOLO --&gt;
                &lt;div class="mt-5"&gt;
                    &lt;!-- TITOLO --&gt;
                    &lt;h2 class=""&gt;Il mio articolo 2&lt;/h2&gt;
                    &lt;!-- META --&gt;
                    &lt;p&gt;16 luglio 2020 - Scritto da &lt;a href="#"&gt;Alberto&lt;/a&gt;&lt;/p&gt;
                    &lt;!-- CONTENT --&gt;
                    &lt;p&gt;
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque et justo ultrices, blandit nulla in, convallis metus. Nullam et mollis orci.
                        Nulla magna augue, accumsan in metus ut, pulvinar facilisis libero. Aliquam erat volutpat. Nulla lectus tortor, lacinia id imperdiet ut, sagittis
                        consectetur magna. Maecenas laoreet sodales tristique. [...]
                    &lt;/p&gt;
                &lt;/div&gt;
                &lt;!-- /ARTICOLO --&gt;

                &lt;!-- ARTICOLO --&gt;
                &lt;div class="mt-5"&gt;
                    &lt;!-- TITOLO --&gt;
                    &lt;h2 class=""&gt;Il mio articolo 3&lt;/h2&gt;
                    &lt;!-- META --&gt;
                    &lt;p&gt;17 luglio 2020 - Scritto da &lt;a href="#"&gt;Alberto&lt;/a&gt;&lt;/p&gt;
                    &lt;!-- CONTENT --&gt;
                    &lt;p&gt;
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque et justo ultrices, blandit nulla in, convallis metus. Nullam et mollis orci.
                        Nulla magna augue, accumsan in metus ut, pulvinar facilisis libero. Aliquam erat volutpat. Nulla lectus tortor, lacinia id imperdiet ut, sagittis
                        consectetur magna. Maecenas laoreet sodales tristique. [...]
                    &lt;/p&gt;
                &lt;/div&gt;
                &lt;!-- /ARTICOLO --&gt;

                &lt;!-- NAVIGATION LINKS --&gt;
                &lt;nav aria-label="Page navigation example"&gt;
                    &lt;ul class="pagination justify-content-center mb-5"&gt;
                        &lt;li class="page-item disabled"&gt;
                            &lt;a class="page-link" href="#" tabindex="-1" aria-disabled="true"&gt;Precedente&lt;/a&gt;
                        &lt;/li&gt;
                        &lt;li class="page-item"&gt;&lt;a class="page-link" href="#"&gt;1&lt;/a&gt;&lt;/li&gt;
                        &lt;li class="page-item"&gt;&lt;a class="page-link" href="#"&gt;2&lt;/a&gt;&lt;/li&gt;
                        &lt;li class="page-item"&gt;&lt;a class="page-link" href="#"&gt;3&lt;/a&gt;&lt;/li&gt;
                        &lt;li class="page-item"&gt;
                            &lt;a class="page-link" href="#"&gt;Successivo&lt;/a&gt;
                        &lt;/li&gt;
                    &lt;/ul&gt;
                &lt;/nav&gt;
                &lt;!-- /NAVIGATION LINKS --&gt;
            &lt;/div&gt;
            &lt;!-- /CONTENUTO --&gt;

            &lt;!-- SIDEBAR --&gt;
            &lt;div class="col-sm-3 col-sm-offset-1"&gt;
                &lt;div&gt;
                    &lt;h4&gt;Chi sono&lt;/h4&gt;
                    &lt;p&gt;Etiam porta &lt;em&gt;sem malesuada magna&lt;/em&gt; mollis euismod. Cras mattis consectetur purus sit amet fermentum. Aenean lacinia bibendum nulla sed consectetur.&lt;/p&gt;
                &lt;/div&gt;
                &lt;div&gt;
                    &lt;h4&gt;Ultimi articoli&lt;/h4&gt;
                    &lt;ol class="list-unstyled"&gt;
                        &lt;li&gt;&lt;a href="#"&gt;Il mio articolo 1&lt;/a&gt;&lt;/li&gt;
                        &lt;li&gt;&lt;a href="#"&gt;Il mio articolo 2&lt;/a&gt;&lt;/li&gt;
                        &lt;li&gt;&lt;a href="#"&gt;Il mio articolo 3&lt;/a&gt;&lt;/li&gt;

                    &lt;/ol&gt;
                &lt;/div&gt;
                &lt;div&gt;
                    &lt;h4&gt;Social&lt;/h4&gt;
                    &lt;ol class="list-unstyled"&gt;
                        &lt;li&gt;&lt;a href="#"&gt;GitHub&lt;/a&gt;&lt;/li&gt;
                        &lt;li&gt;&lt;a href="#"&gt;Twitter&lt;/a&gt;&lt;/li&gt;
                        &lt;li&gt;&lt;a href="#"&gt;Facebook&lt;/a&gt;&lt;/li&gt;
                    &lt;/ol&gt;
                &lt;/div&gt;
            &lt;/div&gt;
            &lt;!-- /SIDEBAR --&gt;

        &lt;/div&gt;&lt;!-- /.row --&gt;

    &lt;/div&gt;&lt;!-- /.container --&gt;</code></pre>

Particolarità:

  * **mt-5 **sta per “margin-top:5rem”.
  * **offset** serve per lasciare colonne vuote prima del contenuto

### Footer

Infine inseriamo il footer:

<pre class="wp-block-code"><code>    &lt;footer&gt;
        &lt;div class="container text-center mb-5"&gt;
            &lt;p&gt;Sito realizzato da &lt;a href=""&gt;Specialista WP!&lt;/a&gt;&lt;/p&gt;
        &lt;/div&gt;
    &lt;/footer&gt;</code></pre>

Ed ecco un** layout classico semplice realizzato interamente con Bootstrap!**


Come vedi **Bootstrap è uno strumento fantastico **per creare layout web in pochissimo tempo!

**Prova ad utilizzarlo** modificando la pagina che abbiamo creato per **renderla più tua**, aggiungi un css esterno, cambia i colori,** crea una pagina “chi sono”** da linkare e utilizza lo stesso layout, insomma sbizzarrisciti come meglio credi!

**Il miglior modo per imparare è provare, provare, provare!**

Come avrai potuto capire **Bootstrap utilizza JQuery**, una libreria Javascript!

Vuoi sapere come funziona?

[Vai alla guida Le basi di JQuery &gt;&gt;][1]

Per maggior chiarezza ecco il **codice completo** del layout base con Bootstrap!

I **commenti **ti aiuteranno a capire le varie sezioni!

<pre class="wp-block-code"><code>&lt;!DOCTYPE html&gt;
&lt;html lang="it"&gt;

&lt;head&gt;
    &lt;meta charset="utf-8"&gt;
    &lt;meta http-equiv="X-UA-Compatible" content="IE=edge"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1"&gt;
    &lt;!-- I 3 meta tags qua sopra DEVONO essere inseriti come primi --&gt;
    &lt;meta name="description" content="Corso intensivo di Bootstrap"&gt;
    &lt;meta name="author" content="Specialista WP!"&gt;

    &lt;title&gt;Corso intensivo di Bootstrap&lt;/title&gt;

    &lt;!-- Bootstrap CSS --&gt;
    &lt;link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet"&gt;

&lt;/head&gt;

&lt;body&gt;

    &lt;nav class="navbar navbar-expand-lg navbar-light bg-light"&gt;
        &lt;div class="container"&gt;
            &lt;a class="navbar-brand" href="#"&gt;Il mio primo tema&lt;/a&gt;
            &lt;button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"&gt;
                &lt;span class="navbar-toggler-icon"&gt;&lt;/span&gt;
            &lt;/button&gt;

            &lt;div class="collapse navbar-collapse" id="navbarSupportedContent"&gt;
                &lt;ul class="navbar-nav ml-auto"&gt;
                    &lt;li class="nav-item active"&gt;
                        &lt;a class="nav-link" href="#"&gt;Home &lt;span class="sr-only"&gt;(current)&lt;/span&gt;&lt;/a&gt;
                    &lt;/li&gt;
                    &lt;li class="nav-item"&gt;
                        &lt;a class="nav-link" href="#"&gt;Chi sono&lt;/a&gt;
                    &lt;/li&gt;
                    &lt;li class="nav-item"&gt;
                        &lt;a class="nav-link" href="#"&gt;Blog&lt;/a&gt;
                    &lt;/li&gt;
                    &lt;li class="nav-item"&gt;
                        &lt;a class="nav-link" href="#"&gt;Contatti&lt;/a&gt;
                    &lt;/li&gt;
                &lt;/ul&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/nav&gt;


    &lt;div class="container mt-5"&gt;

        &lt;div class="row"&gt;
            &lt;!-- CONTENUTO --&gt;
            &lt;div class="col-sm-8"&gt;

                &lt;!-- ARTICOLO --&gt;
                &lt;div&gt;
                    &lt;!-- TITOLO --&gt;
                    &lt;h2 class=""&gt;Il mio articolo&lt;/h2&gt;
                    &lt;!-- META --&gt;
                    &lt;p&gt;15 luglio 2020 - Scritto da &lt;a href="#"&gt;Alberto&lt;/a&gt;&lt;/p&gt;
                    &lt;!-- CONTENT --&gt;
                    &lt;p&gt;
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque et justo ultrices, blandit nulla in, convallis metus. Nullam et mollis orci.
                        Nulla magna augue, accumsan in metus ut, pulvinar facilisis libero. Aliquam erat volutpat. Nulla lectus tortor, lacinia id imperdiet ut, sagittis
                        consectetur magna. Maecenas laoreet sodales tristique. [...]
                    &lt;/p&gt;
                &lt;/div&gt;
                &lt;!-- /ARTICOLO --&gt;

                &lt;!-- ARTICOLO --&gt;
                &lt;div class="mt-5"&gt;
                    &lt;!-- TITOLO --&gt;
                    &lt;h2 class=""&gt;Il mio articolo 2&lt;/h2&gt;
                    &lt;!-- META --&gt;
                    &lt;p&gt;16 luglio 2020 - Scritto da &lt;a href="#"&gt;Alberto&lt;/a&gt;&lt;/p&gt;
                    &lt;!-- CONTENT --&gt;
                    &lt;p&gt;
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque et justo ultrices, blandit nulla in, convallis metus. Nullam et mollis orci.
                        Nulla magna augue, accumsan in metus ut, pulvinar facilisis libero. Aliquam erat volutpat. Nulla lectus tortor, lacinia id imperdiet ut, sagittis
                        consectetur magna. Maecenas laoreet sodales tristique. [...]
                    &lt;/p&gt;
                &lt;/div&gt;
                &lt;!-- /ARTICOLO --&gt;

                &lt;!-- ARTICOLO --&gt;
                &lt;div class="mt-5"&gt;
                    &lt;!-- TITOLO --&gt;
                    &lt;h2 class=""&gt;Il mio articolo 3&lt;/h2&gt;
                    &lt;!-- META --&gt;
                    &lt;p&gt;17 luglio 2020 - Scritto da &lt;a href="#"&gt;Alberto&lt;/a&gt;&lt;/p&gt;
                    &lt;!-- CONTENT --&gt;
                    &lt;p&gt;
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque et justo ultrices, blandit nulla in, convallis metus. Nullam et mollis orci.
                        Nulla magna augue, accumsan in metus ut, pulvinar facilisis libero. Aliquam erat volutpat. Nulla lectus tortor, lacinia id imperdiet ut, sagittis
                        consectetur magna. Maecenas laoreet sodales tristique. [...]
                    &lt;/p&gt;
                &lt;/div&gt;
                &lt;!-- /ARTICOLO --&gt;

                &lt;!-- NAVIGATION LINKS --&gt;
                &lt;nav aria-label="Page navigation example"&gt;
                    &lt;ul class="pagination justify-content-center mb-5"&gt;
                        &lt;li class="page-item disabled"&gt;
                            &lt;a class="page-link" href="#" tabindex="-1" aria-disabled="true"&gt;Precedente&lt;/a&gt;
                        &lt;/li&gt;
                        &lt;li class="page-item"&gt;&lt;a class="page-link" href="#"&gt;1&lt;/a&gt;&lt;/li&gt;
                        &lt;li class="page-item"&gt;&lt;a class="page-link" href="#"&gt;2&lt;/a&gt;&lt;/li&gt;
                        &lt;li class="page-item"&gt;&lt;a class="page-link" href="#"&gt;3&lt;/a&gt;&lt;/li&gt;
                        &lt;li class="page-item"&gt;
                            &lt;a class="page-link" href="#"&gt;Successivo&lt;/a&gt;
                        &lt;/li&gt;
                    &lt;/ul&gt;
                &lt;/nav&gt;
                &lt;!-- /NAVIGATION LINKS --&gt;
            &lt;/div&gt;
            &lt;!-- /CONTENUTO --&gt;

            &lt;!-- SIDEBAR --&gt;
            &lt;div class="col-sm-3 col-sm-offset-1"&gt;
                &lt;div&gt;
                    &lt;h4&gt;Chi sono&lt;/h4&gt;
                    &lt;p&gt;Etiam porta &lt;em&gt;sem malesuada magna&lt;/em&gt; mollis euismod. Cras mattis consectetur purus sit amet fermentum. Aenean lacinia bibendum nulla sed consectetur.&lt;/p&gt;
                &lt;/div&gt;
                &lt;div&gt;
                    &lt;h4&gt;Ultimi articoli&lt;/h4&gt;
                    &lt;ol class="list-unstyled"&gt;
                        &lt;li&gt;&lt;a href="#"&gt;Il mio articolo 1&lt;/a&gt;&lt;/li&gt;
                        &lt;li&gt;&lt;a href="#"&gt;Il mio articolo 2&lt;/a&gt;&lt;/li&gt;
                        &lt;li&gt;&lt;a href="#"&gt;Il mio articolo 3&lt;/a&gt;&lt;/li&gt;

                    &lt;/ol&gt;
                &lt;/div&gt;
                &lt;div&gt;
                    &lt;h4&gt;Social&lt;/h4&gt;
                    &lt;ol class="list-unstyled"&gt;
                        &lt;li&gt;&lt;a href="#"&gt;GitHub&lt;/a&gt;&lt;/li&gt;
                        &lt;li&gt;&lt;a href="#"&gt;Twitter&lt;/a&gt;&lt;/li&gt;
                        &lt;li&gt;&lt;a href="#"&gt;Facebook&lt;/a&gt;&lt;/li&gt;
                    &lt;/ol&gt;
                &lt;/div&gt;
            &lt;/div&gt;
            &lt;!-- /SIDEBAR --&gt;

        &lt;/div&gt;&lt;!-- /.row --&gt;

    &lt;/div&gt;&lt;!-- /.container --&gt;

    &lt;footer&gt;
        &lt;div class="container text-center mb-5"&gt;
            &lt;p&gt;Sito realizzato da &lt;a href=""&gt;Specialista WP!&lt;/a&gt;&lt;/p&gt;
        &lt;/div&gt;
    &lt;/footer&gt;


    &lt;!-- JQuery e Bootstrap JavaScript  --&gt;
    &lt;script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"&gt;&lt;/script&gt;
    &lt;script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"&gt;&lt;/script&gt;
&lt;/body&gt;

&lt;/html&gt;</code></pre>
<div class="wp-block-columns are-vertically-aligned-center is-layout-flex wp-container-core-columns-is-layout-2 wp-block-columns-is-layout-flex">
<div class="wp-block-column is-vertically-aligned-center is-layout-flow wp-block-column-is-layout-flow">
<p>
<em><a href="/le-basi-di-javascript/">&lt;&lt; Le basi di Javascript</a></em>
</p>
</div>
<div class="wp-block-column is-vertically-aligned-center is-layout-flow wp-block-column-is-layout-flow">
<p class="has-text-align-right">
<em><a href="/le-basi-di-jquery/">Le basi di jQuery &gt;&gt;</a></em>
</p>
</div>
</div>

 [1]: /le-basi-di-jquery/