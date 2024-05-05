---
title: 5. Come funziona WordPress
author: Alberto
type: post
date: 2020-03-20T21:28:14+00:00
url: /come-funziona-wordpress/
nectar_blog_post_view_count:
  - 26
tags:
  - Guide
  - WordPress Base

---
Hai seguito la guide per [configurare il tuo PC per lo sviluppo web][1], hai capito [come funziona un server locale][2] e [installato una copia di WordPress][3] sul tuo computer,** e ora?**

Ora **iniziamo a capire come funziona WordPress!**

Spiegare tutto il funzionamento di WordPress in un singolo articolo è impensabile… Sono troppe le possibilità che il CMS offre…<figure class="wp-block-image">

[<img alt="" decoding="async" src="/assets/img/uploads/2020/05/scarica-gratis-desk.jpg"/>][4]</figure>

Ma oggi vedremo** le cose principali**, butteremo le **fondamenta **per creare le nostre skills con WordPress!

In questo articolo ti insegnerò **nello specifico:**

  * come WordPress gestisce i contenuti
  * come creare Articoli e Pagine

## ACCEDERE AL BACKEND

Ora che hai [installato il tuo sito in WordPress in locale][3], iniziamo a capire come è possibile entrare nel **backend**.

Dopo aver [avviato **Apache **e **MySQL **da **XAMPP**][5], apriamo il **browser **e digitiamo “localhost/” + il nome del nostro sito.

Se hai seguito la lezione precedente dovrai digitare: <http: localhost="" wp-test=""></http:>

Dovresti vedere la **home page** del sito standard di **WordPress**.

Ora per entrare nel backend andiamo nella barra dell’**URL** e **aggiungiamo** “wp-admin”.

**L’URL finale** sarà quindi questo: [http://localhost/wp-admin/][6]

A questo punto ci troviamo la schermata di **login **di WordPress.

{{< image src="/assets/img/uploads/2022/03/image-13.png" >}}

**Inseriamo **i nostri dati ed entriamo.

Ecco il** backend di WordPress**. Da qui potrai **gestire **tutti i contenuti presenti sul tuo sito web.

{{< image src="/assets/img/uploads/2022/03/image-14-1024x481-1.png" >}}

## INDICAZIONI GENERALI SUL BACKEND

Ma **come funziona **questo backend?

È molto **semplice**. Sulla sinistra troverai tutte le sezioni per configurare il tuo sito, sulla destra invece vedrai ciò che stai attualmente modificando.

Prenditi un po’ di tempo per **scorrere tutti i punti nel menù laterale** del backend, in modo da farti un’idea generale del suo funzionamento.<figure class="wp-block-image size-full">
<img alt="" class="wp-image-223" decoding="async" src="/assets/img/uploads/2022/03/image-22-1.png"/> </figure>

## 1. GESTIONE DEI CONTENUTI

Ora iniziamo a capire come **vengono gestiti i contenuti in WordPress.**

Quando andiamo a creare una nuova pagina per il nostro sito possiamo scegliere fra** due possibilità:**

  * **Articoli**
  * **Pagine**

### ARTICOLI<figure class="wp-block-image size-full">
<img alt="" class="wp-image-222" decoding="async" src="/assets/img/uploads/2022/03/image-23.png"/> </figure>

Gli **Articoli** sono dei contenuti elencati in ordine cronologico inverso (dal più recente al più vecchio). Sono utilizzati per i **blog**, i giornali e tutti i siti che si aggiornano continuamente.

Gli **Articoli **possono essere suddivisi in **categorie** e possono contenere dei **tag**. In questo modo sono facilmente rintraciabili dagli utenti.

Inoltre invitano alla conversazione grazie alla presenza dei **commenti **in fondo.

Un **esempio **di Articolo è quello che stai leggendo ora!

### PAGINE<figure class="wp-block-image size-full">
<img alt="" class="wp-image-221" decoding="async" src="/assets/img/uploads/2022/03/image-24-1.png"/> </figure>

Le **Pagine **di WordPress sono contenuti **a sè stanti**, una tantum, senza particolari relazioni con altri contenuti del sito. Un esempio di una **Pagina **è la pagina di contatto del sito oppure la pagina “**chi siamo**“. Questa tipologia di contenuto non ha la sezione commenti solitamente.

Entrambe queste tipologie possono contenere **testi**, immagini, **link **e tutto ciò che puoi desiderare inserire all’interno dei tuoi **contenuti**.

### MEDIA<figure class="wp-block-image size-full">
<img alt="" class="wp-image-220" decoding="async" src="/assets/img/uploads/2022/03/image-25.png"/> </figure>

Se hai dato un’occhiata alla barra laterale del backend di WordPress avrai notato che, proprio fra **Articoli **e **Pagine**, c’è la sezione **Media**.

Questa sezione raccoglie **tutte le risorse** che caricherai sul tuo sito, come **foto**, immagini, pdf etc…

## 2. GESTIONE DELLA GRAFICA

La parte grafica del tuo sito è gestita tramite la sezione “**Aspetto**“.<figure class="wp-block-image size-full">
<img alt="" class="wp-image-218" decoding="async" src="/assets/img/uploads/2022/03/image-26-1.png"/> </figure>

All’interno di questa sezione **puoi trovare:**

  * **Temi: **è il “vestito” del tuo sito, ciò che circonda i tuoi contenuti. In parole povere la grafica. Tramite questa sezione puoi cercare e installare nuovi temi per il tuo sito.
  * **Personalizza: **questa sezione ti permette di personalizzare il tema che hai installato. Alcuni temi hanno personalizzazioni maggiori rispetto ad altri.
  * **Widget:** i widget sono dei blocchi che eseguono un’azione specifica (come un elenco o un menù) e possono essere aggiunti in un luogo preciso del sito, come la sidebar.
  * **Menu:** permette di creare e modificare i menù del tuo sito web. Un esempio di menù è solitamente la navbar del sito, che permette di spostarsi e trovare i contenuti desiderati
  * **Sfondo:** permette di modificare lo sfondo del sito. Questa voce è collegata con il tema di default di WordPress, se installerai un tema nuovo potrebbe sparire.
  * **Editor del tema: **permette di modificare il foglio di stile del tema. Qua le cose si fanno interessanti. Se provi ad aprirlo vedrai un foglio scritto in linguaggio CSS. Se continuerai a seguire questo sito imparerai a districarti senza problemi in mezzo a questi tipi di file.

## 3. GESTIONE DELLE FUNZIONALITÀ

Tutte le funzionalità che vuoi implementare nel tuo sito le puoi trovare nella sezione “**Plugin**“.<figure class="wp-block-image size-full">
<img alt="" class="wp-image-217" decoding="async" src="/assets/img/uploads/2022/03/image-27.png"/> </figure>

I plugin sono dei **piccoli software** che consentono al sito di fare una **determinata funzione.**

Se per esempio vuoi inserire un **modulo di contatto **al tuo sito, allora puoi cercare un plugin che gestisca questa funzione.

Esistono **migliaia di plugin** per infinite funzionalità, basta provare a cercare.

Tramite questa sezione puoi **cercare e installare nuovi pluign**.

I plugin dopo essere stati installati** devono essere attivati** per poter funzionare.

<hr class="wp-block-separator"/>

Spero che questa **infarinatura generale** ti sia stata utile per capire a grandi linee **il funzionamento di WordPress!**

Ti consiglio di provare a **dedicare un po’ di tempo** a creare articoli e pagine, installare temi e plugin e vedere cosa succede!

**La pratica è il miglior modo per imparare!**

 [1]: /configurare-il-pc-per-sviluppare-in-wordpress%ef%bf%bc/
 [2]: /perche-installare-wordpress-in-locale/
 [3]: /installare-wordpress-in-locale%ef%bf%bc/
 [4]: .local/risorse-gratuite//
 [5]: /come-funziona-xampp/
 [6]: http://localhost/wp-admin/
 [7]: http://localhost/wp-test/
 [8]: http://localhostal/wp-test/wp-admin/