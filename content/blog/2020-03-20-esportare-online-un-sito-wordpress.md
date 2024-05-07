---
title: 9. Esportare online un sito WordPress
author: Alberto
type: post
date: 2020-03-20T21:24:56+00:00
url: /esportare-online-un-sito-wordpress/
nectar_blog_post_view_count:
  - 35
tags:
  - Guide
  - WordPress Base

---
Finora abbiamo creato il nostro sito web **in locale**, ma adesso è arrivato il momento di **pubblicarlo finalmente online!**

Finalmente potrai **mostrare al mondo** intero il risultato del tuo lavoro e vantarti con amici e conoscenti della tua nuova creazione.

Non perdiamo altro tempo e** diamoci da fare** con la parte finale di questo corso.<figure class="wp-block-image">

[<img alt="" decoding="async" src="/img/uploads/2020/05/scarica-gratis-desk.jpg"/>][1]</figure>
<hr class="wp-block-separator"/>
<p class="has-text-align-center has-vivid-red-color has-text-color">
<em>Questa è la parte più complicata di tutte. Prenditi il tempo necessario per capirla a fondo!</em>
</p>
<hr class="wp-block-separator"/>

## DI COSA ABBIAMO BISOGNO

Per poter pubblicare un sito online abbiamo bisogno fondamentalmente di **due cose:**

  * **Nome dominio:** il nome attraverso il quale gli utenti possono collegarsi al sito, il famoso www.nomesito.it
  * **Hosting:** uno spazio su cui inserire il nostro nuovo sito.

Sono molte le aziende che offrono questo tipo di servizi, dalle più economiche alle più care. Molte di queste hanno un servizio dedicato proprio a WordPress, ma **è possibile installare WordPress da soli e risparmiare qualche euro**.

**Ecco alcune aziende che offrono spazi di hosting:**

  * Aruba
  * Register.it
  * TopHost
  * SiteGround
  * Keliweb
  * Serverplan
  * etc.

Alcuni preferiscono una all’altra. La mia opinione è che **non ci sia troppa differenza** fra i gestori di hosting. Logicamente non si può paragonare un hosting annuale da 15€ con uno da 500€. Come in ogni cosa **più si spende migliore è il servizio che si riceve.**

### SPECIFICHE TECNICHE

Se stai scegliendo un piano di hosting per il tuo sito web in **WordPress **devi sapere che ti serviranno queste **2 cose:**

  * Hosting LINUX
  * Database MySQL

**WordPress **è realizzato con un linguaggio di programmazione che si chiama **PHP **e che per funzionare ha bisogno di un server con sistema operativo **LINUX**.

Inoltre senza **database **WordPress non può funzionare, quindi ricorda di acquistarne anche uno.

### HOSTING GRATIS

Ma dato che questo è un corso rivolto ai **principianti**, è sempre meglio cercare di spendere il meno possibile all’inizio, quindi oggi ti indicherò un modo per avere un **hosting completamente gratuito.**

Andremo quindi ad installare il nostro sito web online in modo che possa essere raggiunto da tutti e lo faremo **senza spendere un euro!**

**_Non male no?_**

**Inziamo!!!**

## ALTERVISTA

Utilizzeremo il servizio gratuito di **altervista.org**, che ci permetterà di installare il nostro sito da zero su uno spazio di **hosting gratuito.**

Per prima cosa vai su <a href="http://it.altervista.org/" rel="noreferrer noopener" target="_blank">altervista.org</a>.

Aperto il sito troverai una schermata come questa:<figure class="wp-block-image size-full">
<img alt="" class="wp-image-285" decoding="async" src="/img/uploads/2022/03/image-1024x481-1.png"/> </figure>

Sebbene il tasto centrate “CREA SITO” sia molto invitante, clicca su “**HOSTING**” in alto a sinistra.<figure class="wp-block-image size-full">
<img alt="" class="wp-image-286" decoding="async" src="/img/uploads/2022/03/Senza-titolo-1.jpeg"/> <figcaption>Altervista Hosting</figcaption></figure>

Puoi installare anche WordPress cliccando su “CREA SITO” in maniera ancora più semplice di come sto per mostrarti, ma sarà una versione di WordPress personalizzata da altervista. Noi invece installeremo WordPress originale importando le modifiche effettuate in locale.

Dopo aver cliccato su “Hosting” ti troverai in questa schermata:<figure class="wp-block-image size-full">
<img alt="" class="wp-image-287" decoding="async" src="/img/uploads/2022/03/image-47-1024x485-1.png"/> </figure>

Ora clicca su “**Inizia subito**“.<figure class="wp-block-image size-full">
<img alt="" class="wp-image-288" decoding="async" src="/img/uploads/2022/03/image-48-1024x479-1.png"/> </figure>

Adesso lasciamo selezionato “**Attiva un Hosting**” e premiamo “**Prosegui**“<figure class="wp-block-image size-full">
<img alt="" class="wp-image-290" decoding="async" src="/img/uploads/2022/03/image-49-1024x483-1.png"/> </figure>

Ora devi inserire **il nome del tuo sito**. Io in questo caso ho inserito “_albydev_“.

Ricordati che con altervista non potrai avere un sito con il “.it” o “.com”, ma solamente con “.altervista.org”. Può essere una **limitazione **ma considerando la gratuità del servizio penso possa andar bene lo stesso, almeno all’inizio per effettuare test senza spendere nulla!

Dopo che avrai compilato i tuoi dati pesonali clicca su “**Prosegui**” in fondo alla pagina.<figure class="wp-block-image size-full">
<img alt="" class="wp-image-291" decoding="async" src="/img/uploads/2022/03/image-50-1024x482-1.png"/> </figure>

**_E Voilà!_**<figure class="wp-block-image size-full">
<img alt="" class="wp-image-292" decoding="async" src="/img/uploads/2022/03/image-51-1024x486-1.png"/> </figure>

Abbiamo il nostro spazio di hosting gratuito!

Ora non resta che **aspettare la mail di altervista** con le credenziali per accedere all’hosting. Prima di poter accedere è necessario **confermare la creazione dell’account**, dopo aver cliccato sul relativo link della email abbiamo terminato la procedura di creazione!

Se non la vedi nella posta in arrivo controlla anche nella spam.

Una volta creato lo spazio web possiamo **entrare nella sezione di configurazione.**<figure class="wp-block-image size-full">
<img alt="" class="wp-image-293" decoding="async" src="/img/uploads/2022/03/image-52-1024x697-1.png"/> </figure>

## CREARE IL DATABASE

Come ormai saprai bene, **WordPress per funzionare ha bisogno di un database** nel quale salvare i dati.

Quindi per prima cosa **attiviamo il database su altervista.**

È molto semplice, basta cliccare sul bottone “**Attiva Database**” presente nella schermata del backend di altervista e poi “**Attiva database gratis**“

Dopo aver attivato il database dovresti vedere questi campi nella pagina di altervista:<figure class="wp-block-image size-full">
<img alt="" class="wp-image-294" decoding="async" src="/img/uploads/2022/03/image-52-1024x697-2.png"/> </figure>

**Ora inizia la parte più complicata di tutte!**

Certo potevamo creare il nostro sito** direttamente online**, ma noi vogliamo diventare degli **Specialisti WP**, gente che ne sa di WordPress, e dobbiamo **imparare anche come funzionano le cose!** Saper importare ed esportare un sito manualmente è una capacità molto importante** se vuoi diventare uno sviluppatore web!**

## CARICARE IL SITO WORDPRESS ONLINE

### FILEZILLA

Per poter _**uploadare **_il nostro sito su altervista non possiamo semplicemente fare un copia/incolla, ma dobbiamo inviarlo al server tramite un **Client FTP**.

Il software migliore per questo tipo di operazioni è **FileZilla**!

Procedi quindi con il download di questo software tramite questo link: <http: download.php="" filezilla-project.org="">

L’installazione è semplicissima, basta seguire la guida e cliccare su “**Avanti**” fino alla fine!

Dopo averlo installato dobbiamo inserire il nostro account FTP per collegarci al server di altervista.

_Non spaventarti per questi paroloni, man mano che vedremo le cose diventeranno sempre più semplici._

Per prima cosa **cerca fra le tue email quella che ti ha inviato Altervista **contentente i dati per loggarti, che inizia così:<figure class="wp-block-image size-full">
<img alt="" class="wp-image-295" decoding="async" src="/img/uploads/2022/03/image-14.png"/> </figure>

Ora** lanciamo FileZilla **e clicchiamo sulla prima icona sotto al menù (apri il gestore siti):<figure class="wp-block-image size-full">
<img alt="" class="wp-image-296" decoding="async" src="/img/uploads/2022/03/image-13-1.png"/> </figure>

Si aprirà una schermata come questa:<figure class="wp-block-image size-full">
<img alt="" class="wp-image-297" decoding="async" src="/img/uploads/2022/03/Untitled-1024x576-1.jpeg"/> </figure>

Qui clicchiamo su “**Nuovo sito**“.

Sulla sinistra apparirà un nuovo campo con scritto”**Nuovo sito**“, puoi rinominare questo campo come vuoi, io per esempio inserisco “**albydev.altervista.org**“.

Ora concentriamoci sulla **parte a destra**, quella più importante:<figure class="wp-block-image size-full">
<img alt="" class="wp-image-298" decoding="async" src="/img/uploads/2022/03/image-15-1.png"/> </figure>

Qua dobbiamo andare ad inserire** i dati inviatici dalla mail di altervista.**

Dopo i dati di accesso al pannello, c’è un riquadro intitolato “Login via FTP”. Compiliamo quindi i campi “**Host**“, “**Utente**” e “**Password**” con i dati della mail e clicchiamo su “**Connetti**“.

_Il campo “Porta” possiamo lasciarlo vuoto._

Dovrebbe comparire una schermata come questa:<figure class="wp-block-image size-full">
<img alt="" class="wp-image-299" decoding="async" src="/img/uploads/2022/03/image-16.png"/> </figure>

**È tutto normale **non preoccuparti, puoi flaggare “Considera sempre sicuro il certificato…” e cliccare su “**OK**“.

**A questo punto sei connesso al tuo server altervista.**

Inizia subito con il cancellare il file “index.html” sulla destra, così non ci darà fastidio dopo.<figure class="wp-block-image size-full">
<img alt="" class="wp-image-300" decoding="async" src="/img/uploads/2022/03/image-20-1.png"/> </figure>

### COPIARE IL NOSTRO SITO SU ALTERVISTA

Ora possiamo caricare il nostro sito su altervista. Per prima cosa dobbiamo **raggiungere il nostro sito in locale**.

Tutti i nostri siti in locale sono nella cartella “C:\XAMPP\htdocs”, percui il nostro sito sarà in “_C:\XAMPP\htdocs/wp-test_“.

Filezilla ci fa vedere **sulla sinistra il nostro computer in locale **e** sulla destra il nostro server altervista**.<figure class="wp-block-image size-full">
<img alt="" class="wp-image-301" decoding="async" src="/img/uploads/2022/03/image-17-1024x554-1.png"/> </figure>

Nel riquadro a destra andiamo quindi in “_C:\XAMPP\htdoc\wp-test_“. Dovresti vedere una schermata come questa:<figure class="wp-block-image size-full">
<img alt="" class="wp-image-302" decoding="async" src="/img/uploads/2022/03/image-18-1.png"/> </figure>

Ora non ti resta che **selezionare tutti i file** (CTRL+A) **e trascinarli su altervista** (sulla parte destra), con un Drag&amp;Drop!<figure class="wp-block-image size-full">
<img alt="" class="wp-image-303" decoding="async" src="/img/uploads/2022/03/image-19-1024x553-1.png"/> </figure>

Questa operazione può **durare un po’ di tempo**…

Ma noi** non ci annoieremo**! Dobbiamo anche importare online il nostro database!

## IMPORTARE ONLINE IL DATABASE WORDPRESS

Questa è **_la parte più complicata di tutte_**… Ma non ti scoraggiare, **è finalmente l’ultima!**

Andremo a esportare il nostro database locale, lo modificheremo e lo uploderemo online su altervista!

### INIZIAMO!

Per prima cosa dobbiamo andare a **scaricarci il nostro database locale**. Per fare questo è necessario **avviare XAMPP**, avviare **Apache** e **MySQL **e cliccare su “**Admin**” **in corrispondenza di MySQL**:<figure class="wp-block-image size-full">
<img alt="" class="wp-image-304" decoding="async" src="/img/uploads/2022/03/image-21.png"/> </figure>

Si aprirà **PhpMyAdmin**, un software per gestire facilmente i database MySQL.<figure class="wp-block-image size-full">
<img alt="" class="wp-image-305" decoding="async" src="/img/uploads/2022/03/Untitled-1-1024x470-1.jpeg"/> </figure>

Qua andiamo nella **barra sulla sinistra** e selezioniamo il database del nostro sito:**wp-test** e poi clicchiamo su “**Esporta**“.<figure class="wp-block-image size-full">
<img alt="" class="wp-image-306" decoding="async" src="/img/uploads/2022/03/image-22-1024x338-1.png"/> </figure>

Possiamo lasciare “Rapido” e cliccare direttamente su “**Esegui**“

Scaricheremo quindi il nostro database, potete salvarlo dove volete.

Una volta salvato lo dobbiamo **aprire**. Non serve un programma specifico, basta il classico “**Blocco note**” o “**Text editor**“.<figure class="wp-block-image size-full">
<img alt="" class="wp-image-307" decoding="async" src="/img/uploads/2022/03/image-23-1024x695-1.png"/> </figure>

Il file aperto è simile a questo, un insieme di stringhe. **Questo è il nostro database.**

Ora dobbiamo fare **un’operazione abbastanza delicata**: **sostituire l’url del sito in locale con l’url del sito online.**

Per far ciò andiamo su “**Modifica – Sostituisci**“.<figure class="wp-block-image size-full">
<img alt="" class="wp-image-308" decoding="async" src="/img/uploads/2022/03/image-24-2.png"/> </figure>

In Trova dovremmo inserire l’url al nostro sito in locale, cioè “_http://localhost/nome-sito_“, mentre in Sostituisci con dovremo inserire l’url di altervista, nel mio caso “_http://albydev.altervista.org_“.

Dopo avere compilato possiamo premere su** Sostituisci tutto** e infine **salvare **il file.

**Ora il nostro Database è pronto per essere importato su altervista.**

### IMPORTARE IL DATABASE SU ALTERVISTA

Torniamo ora nel backend di altervista e clicchiamo su **Accedi a PhpMyAdmin**<figure class="wp-block-image size-full">
<img alt="" class="wp-image-309" decoding="async" src="/img/uploads/2022/03/image-12.png"/> </figure>

Si aprirà il **phpmyadmin **del nostro server **altervista**.

Clicchiamo sul nostro database sulla sinistra, chiamato **my_nomesito** e poi su “**Importa**“<figure class="wp-block-image size-full">
<img alt="" class="wp-image-310" decoding="async" src="/img/uploads/2022/03/image-25-1024x416-1.png"/> </figure>

Ora clicchiamo su “**Scegli file**“, andiamo a selezionare il database locale che abbiamo appena modificato e infine premiamo “**Esegui**“.

Alla fine dovremmo visualizzare un messaggio come il seguente su sfondo verde:

_Importazione eseguita con successo, 86 query eseguite._ (wp-test.sql)

_**E voilà!**_

Il database è importato!

Ora non ci resta che **aspettare che FileZilla termini di caricare online** il nostro sito.

### L’ULTIMA OPERAZIONE

Quando FileZilla avrà terminato l’upload occorrerà fare ancora **un’ultimissima modifica!**

Andiamo ad aprire il file “**wp-config.php**” su altervista facendo click con il tasto destro sul file e cliccando su “**Visualizza / Modifica**“<figure class="wp-block-image size-full">
<img alt="" class="wp-image-311" decoding="async" src="/img/uploads/2022/03/image-26-1024x552-1.png"/> </figure>

Si aprirà il blocco note con il file wp-config.php al suo interno.<figure class="wp-block-image size-full">
<img alt="" class="wp-image-312" decoding="async" src="/img/uploads/2022/03/image-27-1024x555-1.png"/> </figure>

Qua dobbiamo solamente andare a modificare i dati relativi al database, che non è più quello di XAMPP ma quello di altervista.

Cerca questi campi:

<pre class="wp-block-code"><code>// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wp-test' );

/** MySQL database username */
define( 'DB_USER', 'root' );

/** MySQL database password */
define( 'DB_PASSWORD', '' );

/** MySQL hostname */
define( 'DB_HOST', 'localhost' );</code></pre>

Su **DB_NAME **dobbiamo indicare il nuovo nome del database, che sarà “**my_nomesito**“. Per sicurezza torna sul **PhpMyAdmin **di altervista e guarda nel menù laterale a sinistra, c’è un unico database che inizia con “my_”, quello è il nome da inserire.

Gli altri dati restano uguali fortunatamente. Ora non ci resta che **salvare **il file, riaprire **FileZilla **e cliccare su “**Si**” per apportare le modifiche online!<figure class="wp-block-image size-full">
<img alt="" class="wp-image-313" decoding="async" src="/img/uploads/2022/03/image-28.png"/> </figure>

A questo punto **basterà andare all’URL del nostro sito Altervista e ce lo troveremo online, bello e funzionante!**

Un’ultima operazione che è bene fare è quella di **risalvare i permalink **di WordPress, in modo che tutti i link funzionino correttamente.

Per fare ciò basterà loggarsi nel backend ed andare in “**Impostazioni – Permalink**” e semplicemente cliccare su “**Salva** **le modifiche**“, senza modificare nulla!<figure class="wp-block-image size-full">
<img alt="" class="wp-image-314" decoding="async" src="/img/uploads/2022/03/image-29-1024x481-1.png"/> </figure>

**_CONGRATULAZIONI_**!!!

**Hai terminato la serie per principianti! Ora puoi iniziare a dedicarti a qualcosa di più complesso!**

 [1]: https://github.com/thetuxdev