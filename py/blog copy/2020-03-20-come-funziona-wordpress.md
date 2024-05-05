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
Hai seguito la guide per&nbsp;[configurare il tuo PC per lo sviluppo web][1], hai capito&nbsp;[come funziona un server locale][2]&nbsp;e&nbsp;[installato una copia di WordPress][3]&nbsp;sul tuo computer,**&nbsp;e ora?**

Ora&nbsp;**iniziamo a capire come funziona WordPress!**

Spiegare tutto il funzionamento di WordPress in un singolo articolo è impensabile… Sono troppe le possibilità che il CMS offre…<figure class="wp-block-image">

[<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2020/05/scarica-gratis-desk.jpg" alt="" />][4]</figure>

Ma oggi vedremo**&nbsp;le cose principali**, butteremo le&nbsp;**fondamenta&nbsp;**per creare le nostre skills con WordPress!

In questo articolo ti insegnerò&nbsp;**nello specifico:**

  * come WordPress gestisce i contenuti
  * come creare Articoli e Pagine

## ACCEDERE AL BACKEND

Ora che hai&nbsp;[installato il tuo sito in WordPress in locale][3], iniziamo a capire come è possibile entrare nel&nbsp;**backend**.

Dopo aver&nbsp;[avviato&nbsp;**Apache&nbsp;**e&nbsp;**MySQL&nbsp;**da&nbsp;**XAMPP**][5], apriamo il&nbsp;**browser&nbsp;**e digitiamo “localhost/” + il nome del nostro sito.

Se hai seguito la lezione precedente dovrai digitare: <http://localhost/wp-test/>

Dovresti vedere la&nbsp;**home page**&nbsp;del sito standard di&nbsp;**WordPress**.

Ora per entrare nel backend andiamo nella barra dell’**URL**&nbsp;e&nbsp;**aggiungiamo&nbsp;**“wp-admin”.

**L’URL finale** sarà quindi questo: [http://localhostal/][6][wp-test][7][/wp-admin/][8]

A questo punto ci troviamo la schermata di&nbsp;**login&nbsp;**di WordPress.

<div class="wp-block-image">
  <figure class="aligncenter size-full"><img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-13.png" alt="" class="wp-image-225" /></figure>
</div>

**Inseriamo&nbsp;**i nostri dati ed entriamo.

Ecco il**&nbsp;backend di WordPress**. Da qui potrai&nbsp;**gestire&nbsp;**tutti i contenuti presenti sul tuo sito web.

<div class="wp-block-image">
  <figure class="aligncenter size-full"><img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-14-1024x481-1.png" alt="" class="wp-image-224" /></figure>
</div>

## INDICAZIONI GENERALI SUL BACKEND

Ma&nbsp;**come funziona&nbsp;**questo backend?

È molto&nbsp;**semplice**. Sulla sinistra troverai tutte le sezioni per configurare il tuo sito, sulla destra invece vedrai ciò che stai attualmente modificando.

Prenditi un po’ di tempo per&nbsp;**scorrere tutti i punti nel menù laterale**&nbsp;del backend, in modo da farti un’idea generale del suo funzionamento.<figure class="wp-block-image size-full">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-22-1.png" alt="" class="wp-image-223" /> </figure>

## 1. GESTIONE DEI CONTENUTI

Ora iniziamo a capire come&nbsp;**vengono gestiti i contenuti in WordPress.**

Quando andiamo a creare una nuova pagina per il nostro sito possiamo scegliere fra**&nbsp;due possibilità:**

  * **Articoli**
  * **Pagine**

### ARTICOLI<figure class="wp-block-image size-full">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-23.png" alt="" class="wp-image-222" /> </figure>

Gli&nbsp;**Articoli**&nbsp;sono dei contenuti elencati in ordine cronologico inverso (dal più recente al più vecchio). Sono utilizzati per i&nbsp;**blog**, i giornali e tutti i siti che si aggiornano continuamente.

Gli&nbsp;**Articoli&nbsp;**possono essere suddivisi in&nbsp;**categorie**&nbsp;e possono contenere dei&nbsp;**tag**. In questo modo sono facilmente rintraciabili dagli utenti.

Inoltre invitano alla conversazione grazie alla presenza dei&nbsp;**commenti&nbsp;**in fondo.

Un&nbsp;**esempio&nbsp;**di Articolo è quello che stai leggendo ora!

### PAGINE<figure class="wp-block-image size-full">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-24-1.png" alt="" class="wp-image-221" /> </figure>

Le&nbsp;**Pagine&nbsp;**di WordPress sono contenuti&nbsp;**a sè stanti**, una tantum, senza particolari relazioni con altri contenuti del sito. Un esempio di una&nbsp;**Pagina&nbsp;**è la pagina di contatto del sito oppure la pagina “**chi siamo**“. Questa tipologia di contenuto non ha la sezione commenti solitamente.

Entrambe queste tipologie possono contenere&nbsp;**testi**, immagini,&nbsp;**link&nbsp;**e tutto ciò che puoi desiderare inserire all’interno dei tuoi&nbsp;**contenuti**.

### MEDIA<figure class="wp-block-image size-full">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-25.png" alt="" class="wp-image-220" /> </figure>

Se hai dato un’occhiata alla barra laterale del backend di WordPress avrai notato che, proprio fra&nbsp;**Articoli&nbsp;**e&nbsp;**Pagine**, c’è la sezione&nbsp;**Media**.

Questa sezione raccoglie&nbsp;**tutte le risorse**&nbsp;che caricherai sul tuo sito, come&nbsp;**foto**, immagini, pdf etc…

## 2. GESTIONE DELLA GRAFICA

La parte grafica del tuo sito è gestita tramite la sezione “**Aspetto**“.<figure class="wp-block-image size-full">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-26-1.png" alt="" class="wp-image-218" /> </figure>

All’interno di questa sezione&nbsp;**puoi trovare:**

  * **Temi:&nbsp;**è il “vestito” del tuo sito, ciò che circonda i tuoi contenuti. In parole povere la grafica. Tramite questa sezione puoi cercare e installare nuovi temi per il tuo sito.
  * **Personalizza:&nbsp;**questa sezione ti permette di personalizzare il tema che hai installato. Alcuni temi hanno personalizzazioni maggiori rispetto ad altri.
  * **Widget:**&nbsp;i widget sono dei blocchi che eseguono un’azione specifica (come un elenco o un menù) e possono essere aggiunti in un luogo preciso del sito, come la sidebar.
  * **Menu:**&nbsp;permette di creare e modificare i menù del tuo sito web. Un esempio di menù è solitamente la navbar del sito, che permette di spostarsi e trovare i contenuti desiderati
  * **Sfondo:**&nbsp;permette di modificare lo sfondo del sito. Questa voce è collegata con il tema di default di WordPress, se installerai un tema nuovo potrebbe sparire.
  * **Editor del tema:&nbsp;**permette di modificare il foglio di stile del tema. Qua le cose si fanno interessanti. Se provi ad aprirlo vedrai un foglio scritto in linguaggio CSS. Se continuerai a seguire questo sito imparerai a districarti senza problemi in mezzo a questi tipi di file.

## 3. GESTIONE DELLE FUNZIONALITÀ

Tutte le funzionalità che vuoi implementare nel tuo sito le puoi trovare nella sezione “**Plugin**“.<figure class="wp-block-image size-full">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-27.png" alt="" class="wp-image-217" /> </figure>

I plugin sono dei&nbsp;**piccoli software**&nbsp;che consentono al sito di fare una&nbsp;**determinata funzione.**

Se per esempio vuoi inserire un&nbsp;**modulo di contatto&nbsp;**al tuo sito, allora puoi cercare un plugin che gestisca questa funzione.

Esistono&nbsp;**migliaia di plugin**&nbsp;per infinite funzionalità, basta provare a cercare.

Tramite questa sezione puoi&nbsp;**cercare e installare nuovi pluign**.

I plugin dopo essere stati installati**&nbsp;devono essere attivati**&nbsp;per poter funzionare.

<hr class="wp-block-separator" />

Spero che questa&nbsp;**infarinatura generale**&nbsp;ti sia stata utile per capire a grandi linee&nbsp;**il funzionamento di WordPress!**

Ti consiglio di provare a&nbsp;**dedicare un po’ di tempo**&nbsp;a creare articoli e pagine, installare temi e plugin e vedere cosa succede!

**La pratica è il miglior modo per imparare!**

 [1]: https://albertoreineri.it/guide/configurare-il-pc-per-sviluppare-in-wordpress%ef%bf%bc/
 [2]: https://albertoreineri.it/guide/perche-installare-wordpress-in-locale/
 [3]: https://albertoreineri.it/guide/installare-wordpress-in-locale%ef%bf%bc/
 [4]: https://albertoreineri.it.local/risorse-gratuite//
 [5]: https://albertoreineri.it/guide/come-funziona-xampp/
 [6]: http://localhostalbertoreineri.it.local-test/wp-admin/
 [7]: http://localhost/wp-test/
 [8]: http://localhostal/wp-test/wp-admin/