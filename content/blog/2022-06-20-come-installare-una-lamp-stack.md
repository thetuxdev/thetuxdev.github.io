---
title: Come installare una LAMP stack (Linux, Apache, MySQL, PHP) su Ubuntu
author: Alberto
type: post
date: 2022-06-20T12:59:37+00:00
url: /come-installare-una-lamp-stack/
nectar_blog_post_view_count:
  - 136
tags:
  - Guide
  - Linux
---
## Introduzione

Uno stack “LAMP” è un gruppo di software open source che viene generalmente installato insieme per consentire a un server di ospitare siti Web dinamici e app Web. Questo termine è in realtà un acronimo che rappresenta il sistema operativo **L**inux, con il web server **A**pache**. **I dati del sito vengono archiviati in un database **M**ySQL e il contenuto dinamico viene elaborato da **P**HP.

In questa guida, installeremo uno stack LAMP su un server Ubuntu.

## Prerequisiti

Questo tutorial è creato su Ubuntu, ma funziona su tutte le distro basate su Debian, come Pop!_OS, Elementary OS, Linux Mint etc.

## Passaggio 1: installazione di Apache

Il server Web Apache è un popolare server Web open source che può essere utilizzato insieme a [PHP][1] per ospitare siti Web dinamici. È ben documentato ed è stato ampiamente utilizzato per gran parte della storia del web.

Innanzitutto, assicurati che la tua `apt` cache sia aggiornata con:

<pre class="wp-block-code"><code>sudo apt update</code></pre>

Se è la prima volta che lo utilizzi `sudo` in questa sessione, ti verrà chiesto di fornire la password dell’utente per convalidare le tue autorizzazioni.

Una volta aggiornata la cache, puoi installare Apache lanciando:

<pre class="wp-block-code"><code>sudo apt install apache2</code></pre>

Dopo aver inserito questo comando, `apt` ti dirà quali pacchetti intende installare e quanto spazio su disco occuperà. Premi S (o Y se hai configurati il sistema in lingua inglese) e poi premi `ENTER` per confermare e l’installazione procederà.

<hr class="wp-block-separator has-alpha-channel-opacity"/>
<p class="has-white-color has-vivid-red-background-color has-text-color has-background">
  N.B.: in questa guida utilizzerò ‘<em>Y</em>‘ per procedere con l’installazione, perché ho l’abitudine di installare sempre Linux in inglese… Se usi l’italiano ricordati di premere ‘<em>S</em>‘
</p>
<hr class="wp-block-separator has-alpha-channel-opacity"/>

E voilà! Apache è bello che installato!

Puoi fare subito un controllo a campione per verificare che tutto sia andato come previsto visitando l’indirizzo IP pubblico del tuo server nel tuo browser web. Se sei il locale ti basterà aprire il browser e scrivere nella barra degli indirizzi:

<pre class="wp-block-code"><code>http://localhost
</code></pre>

Se invece stai configurando un web server remoto, allora dovrai inserire il tuo indirizzo IP

<pre class="wp-block-code"><code>http://<mark>your_server_ip</mark>
</code></pre>

Dovresti ora vedere nel browser la pagina Web predefinita di Apache, che è disponibile a scopo informativo e di test. Dovrebbe assomigliare a qualcosa di simile a questo:`<figure class="wp-block-image size-large">`
`<img alt="" class="wp-image-493" decoding="async" src="/img/uploads/2022/06/small_apache_default_1804-728x1024.png"/>` `</figure>`

Se vedi questa pagina, allora il tuo server web è ora installato correttamente e accessibile attraverso il tuo firewall.

### Come trovare l’indirizzo IP pubblico del tuo server

Se stai configurando un web server remoto e non sai qual è l’indirizzo IP pubblico del tuo server, ci sono diversi modi per trovarlo. Di solito è l’indirizzo che usi per connetterti al tuo server tramite SSH.

Esistono diversi modi per farlo dalla riga di comando. Innanzitutto, puoi utilizzare gli strumenti _iproute2_ per ottenere il tuo indirizzo IP digitando questo:

<pre class="wp-block-code"><code>ip addr show eth0 | grep inet | awk '{ print $2; }' | sed 's/\/.*$//'
</code></pre>

Questo ti restituirà due o tre righe. Sono tutti indirizzi corretti, ma il tuo computer potrebbe essere in grado di utilizzarne solo uno, quindi sentiti libero di provarli.

Un metodo alternativo consiste nell’utilizzare l’utility `curl` per contattare una parte esterna per dirti come _vede_ il tuo server. Questo viene fatto chiedendo a un server specifico qual è il tuo indirizzo IP:

<pre class="wp-block-code"><code>sudo apt install curl
curl http://icanhazip.com</code></pre>

Indipendentemente dal metodo utilizzato per ottenere il tuo indirizzo IP, digitalo nella barra degli indirizzi del tuo browser web per visualizzare la pagina Apache predefinita.

## Passaggio 2: installazione di MySQL

Ora che hai il tuo server web attivo e funzionante, è il momento di installare MySQL. MySQL è un sistema di gestione di database. Fondamentalmente, organizzerà e fornirà l’accesso ai database in cui il tuo sito può archiviare informazioni.

Ancora una volta, utilizziamo `apt` per acquisire e installare questo software:

<pre class="wp-block-code"><code>sudo apt install mysql-server</code></pre>

**Nota** : in questo caso, non è necessario eseguire `sudo apt update` prima del comando. Questo perché di recente l’hai eseguito nei comandi sopra per installare Apache. L’indice del pacchetto sul tuo computer dovrebbe essere già aggiornato.

Anche questo comando ti mostrerà un elenco dei pacchetti che verranno installati, insieme alla quantità di spazio su disco che occuperanno. Entra `Y` (o _S_) per continuare.

Al termine dell’installazione, esegui un semplice script di sicurezza preinstallato con MySQL che rimuoverà alcune pericolose impostazioni predefinite e bloccherà l’accesso al tuo sistema di database (Se sei in locale non è necessario). Avvia lo script interattivo eseguendo:

<pre class="wp-block-code"><code>sudo mysql_secure_installation</code></pre>

Questo ti chiederà se vuoi configurare il `VALIDATE PASSWORD PLUGIN`.

**Nota:** l’abilitazione di questa funzione è una sorta di chiamata di giudizio. Se abilitato, le password che non corrispondono ai criteri specificati verranno rifiutate da MySQL con un errore. Ciò causerà problemi se si utilizza una password debole insieme al software che configura automaticamente le credenziali utente di MySQL, come i pacchetti Ubuntu per phpMyAdmin. È sicuro lasciare la convalida disabilitata, ma dovresti sempre usare password complesse e univoche per le credenziali del database.

Rispondi `Y` per sì o per qualsiasi altra cosa per continuare senza abilitare.

<pre class="wp-block-code"><code>VALIDATE PASSWORD PLUGIN can be used to test passwords
and improve security. It checks the strength of password
and allows the users to set only those passwords which are
secure enough. Would you like to setup VALIDATE PASSWORD plugin?

Press y|Y for Yes, any other key for No:
</code></pre>

Se rispondi “sì”, ti verrà chiesto di selezionare un livello di convalida della password. Tieni presente che se inserisci `2`, il livello più forte, riceverai errori quando tenti di impostare una password che non contenga numeri, lettere maiuscole e minuscole e caratteri speciali o che sia basata su parole comuni del dizionario.

<pre class="wp-block-code"><code>There are three levels of password validation policy:

LOW    Length >= 8
MEDIUM Length >= 8, numeric, mixed case, and special characters
STRONG Length >= 8, numeric, mixed case, special characters and dictionary                  file

Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG: <mark>1</mark>
</code></pre>

Indipendentemente dal fatto che tu abbia scelto di impostare `VALIDATE PASSWORD PLUGIN`, il tuo server ti chiederà successivamente di selezionare e confermare una password per l’ utente **root** MySQL. Questo non deve essere confuso con il **root di sistema**. L’ utente **root del database** è un utente amministrativo con privilegi completi sul sistema del database. Anche se il metodo di autenticazione predefinito per l’utente root MySQL dispensa l’uso di una password, **anche quando ne è impostata una** , dovresti definire qui una password complessa come misura di sicurezza aggiuntiva. Ne parleremo tra un momento.

Se hai abilitato la convalida della password, ti verrà mostrata la sicurezza della password per la password di root che hai appena inserito e il tuo server ti chiederà se vuoi cambiare quella password. Se sei soddisfatto della tua password attuale, digita `N`:

<pre class="wp-block-code"><code>Using existing password for root.

Estimated strength of the password: <mark>100</mark>
Change the password for root ? ((Press y|Y for Yes, any other key for No) : <mark>n</mark>
</code></pre>

Per il resto delle domande, premere `Y` e premere `ENTER` ad ogni prompt. Ciò rimuoverà alcuni utenti anonimi e il database di test, disabiliterà gli accessi root remoti e caricherà queste nuove regole in modo che MySQL rispetti immediatamente le modifiche apportate.

Al termine, verifica se riesci ad accedere alla console MySQL digitando:

<pre class="wp-block-code"><code>sudo mysql</code></pre>

Questo si collegherà al server MySQL come utente **root** del database amministrativo, che viene dedotto dall’uso di `sudo` quando si esegue questo comando. Dovresti vedere un output come questo:

<pre class="wp-block-code"><code>OutputWelcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 5
Server version: 5.7.34-0ubuntu0.18.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
</code></pre>

Per uscire dalla console MySQL, digita:

<pre class="wp-block-code"><code>exit</code></pre>

Tieni presente che non è necessario fornire una password per connettersi come utente **root** , anche se ne è stata definita una durante l’esecuzione dello  `mysql_secure_installation`. Questo perché il metodo di autenticazione predefinito per l’utente MySQL amministrativo è `unix_socket` invece di `password`. Anche se all’inizio potrebbe sembrare un problema di sicurezza, rende il server del database più sicuro perché gli unici utenti autorizzati ad accedere come utente **root** MySQL sono gli utenti del sistema con privilegi sudo che si connettono dalla console o tramite un’applicazione in esecuzione con gli stessi privilegi. In termini pratici, ciò significa che non sarai in grado di utilizzare l’utente **root** del database amministrativo per connetterti dalla tua applicazione PHP. L’account MySQL funge da salvaguardia, nel caso in cui il metodo di autenticazione predefinito venga modificato da `unix_socket` a `password`.

Per una maggiore sicurezza, è meglio disporre di account utente dedicati con privilegi meno estesi impostati per ogni database, soprattutto se prevedi di avere più database ospitati sul tuo server, ma su questo creerò altre guide più dettagliate in futuro.

Il tuo server MySQL è ora installato e protetto. Vediamo ora come installare PHP, il componente finale nello stack LAMP.

## Passaggio 3: installazione di PHP

PHP è il componente della configurazione che elaborerà il codice per visualizzare il contenuto dinamico. Può eseguire script, connettersi ai tuoi database MySQL per ottenere informazioni e consegnare il contenuto elaborato al tuo server web in modo che possa mostrare i risultati ai tuoi visitatori.

Ancora una volta, sfrutta il sistema apt per installare PHP. Oltre al pacchetto php, dovrai anche integrare libapache2-mod-php in Apache e il pacchetto php-mysql per consentire a PHP di connettersi ai database MySQL. Esegui il comando seguente per installare tutti e tre i pacchetti e le relative dipendenze:

<pre class="wp-block-code"><code>sudo apt install php libapache2-mod-php php-mysql</code></pre>

Questo dovrebbe installare PHP senza problemi. Lo testeremo tra un momento.

### Modifica dell’indice della directory di Apache (opzionale)

In alcuni casi, vorrai modificare il modo in cui Apache serve i file quando viene richiesta una directory. Di default, se un utente richiede una directory dal server, Apache cercherà prima un file chiamato `index.html`. Ma noi vogliamo dire al server web di preferire i file PHP rispetto ad altri, per fare in modo che Apache cerchi `index.php` come primoo file. In caso contrario, un `index.html` inserito nella radice del documento dell’applicazione avrà sempre la precedenza su un `index.php`.

Per apportare questa modifica, apri il file di configurazione `dir.conf` in un editor di testo a tua scelta. Qui useremo `nano`:

<pre class="wp-block-code"><code>sudo nano /etc/apache2/mods-enabled/dir.conf</code></pre>

Dovresti vedere una cosa del genere:

<pre class="wp-block-code"><code><IfModule mod_dir.c>
    DirectoryIndex index.html index.cgi index.pl <mark>index.php</mark> index.xhtml index.htm
</IfModule></code></pre>

Sposta il file di indice PHP (evidenziato sopra) nella prima posizione dopo la `DirectoryIndex`, in questo modo:

<pre class="wp-block-code"><code><IfModule mod_dir.c>
    DirectoryIndex <mark>index.php</mark> index.html index.cgi index.pl index.xhtml index.htm
</IfModule></code></pre>

Al termine, salva e chiudi il file premendo `CTRL+X`. Conferma il salvataggio digitando `Y` e quindi premi `ENTER` per verificare la posizione di salvataggio del file.

Successivamente, riavvia il server Web Apache in modo che le modifiche vengano riconosciute. Puoi farlo con il seguente comando:

<pre class="wp-block-code"><code>sudo systemctl restart apache2</code></pre>

Puoi anche controllare lo stato del `apache2`servizio utilizzando `systemctl`:

<pre class="wp-block-code"><code>sudo systemctl status apache2</code></pre>

<pre class="wp-block-code"><code>Sample Output● apache2.service - The Apache HTTP Server
   Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset: enabled)
  Drop-In: /lib/systemd/system/apache2.service.d
           └─apache2-systemd.conf
   Active: active (running) since Thu 2021-07-15 09:22:59 UTC; 1h 3min ago
 Main PID: 3719 (apache2)
    Tasks: 55 (limit: 2361)
   CGroup: /system.slice/apache2.service
           ├─3719 /usr/sbin/apache2 -k start
           ├─3721 /usr/sbin/apache2 -k start
           └─3722 /usr/sbin/apache2 -k start

Jul 15 09:22:59 ubuntu1804 systemd[1]: Starting The Apache HTTP Server...
Jul 15 09:22:59 ubuntu1804 apachectl[3694]: AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.1.1. Set the 'ServerName' di
Jul 15 09:22:59 ubuntu1804 systemd[1]: Started The Apache HTTP Server.
</code></pre>

Premi `Q` per uscire da questo stato.

## Passaggio 4: configurazione di un host virtuale (consigliato)

Quando si utilizza il server Web Apache, è possibile utilizzare _host virtuali_ per incapsulare i dettagli di configurazione e ospitare più di un dominio da un singolo server. Imposteremo ora un dominio di esempio chiamato ****il\_mio\_dominio****, potrai sostituirlo con il nome del dominio che desideri utilizzare.

Apache su ha un blocco server abilitato per impostazione predefinita che è configurato per servire i documenti dalla cartella `/var/www/html`. Sebbene funzioni bene per un singolo sito, può diventare ingombrante se ospiti più siti. Invece di modificare `/var/www/html`, creiamo una struttura di directory all’interno `/var/www` per **il sito il\_mio\_dominio**, lasciando `/var/www/html` come directory predefinita da servire se una richiesta del client non corrisponde a nessun altro sito.

Crea la directory per ****il\_mio\_dominio**** come segue:

<pre class="wp-block-code"><code>sudo mkdir /var/www/il_mio_dominio</code></pre>

Quindi, assegna la proprietà della directory con la variabile di ambiente `$USER`, che fa riferimento all’utente registrato corrente:

<pre class="wp-block-code"><code>sudo chown -R $USER:$USER /var/www/il_mio_dominio</code></pre>

I permessi della tua directory principale web dovrebbero essere corretti se non hai modificato il suo valore umask, ma puoi comunque digitare:

<pre class="wp-block-code"><code>sudo chmod -R 755 /var/www/il_mio_dominio</code></pre>

Ora crea una pagina di esempio `index.html` utilizzando `nano` o il tuo editor preferito:

<pre class="wp-block-code"><code>nano /var/www/il_mio_dominio/index.html</code></pre>

All’interno, aggiungi il seguente codice HTML di esempio:

<pre class="wp-block-code"><code><html>
    <head>
        <title>Il Mio Dominio</title>
    </head>
    <body>
        <h1>Il mio dominio FUNZIONA!!!</h1>
    </body>
</html>
</code></pre>

Salva e chiudi il file quando hai finito.

Affinché Apache possa servire questo contenuto, è necessario creare un file host virtuale con le direttive corrette. Invece di modificare il file di configurazione predefinito che si trova `/etc/apache2/sites-available/000-default.conf` direttamente in, creiamone uno nuovo in :`/etc/apache2/sites-available/<mark>il_mio_dominio</mark>.conf`

<pre class="wp-block-code"><code>sudo nano /etc/apache2/sites-available/il_mio_dominio.conf</code></pre>

Incolla il seguente blocco di configurazione, che è simile a quello predefinito, ma aggiornato per la nostra nuova directory e nome di dominio:/etc/apache2/sites-available/il\_mio\_dominio.conf

<pre class="wp-block-code"><code><VirtualHost *:80>
    ServerAdmin webmaster@localhost
    ServerName il_mio_dominio
    ServerAlias <mark>www.</mark>il_mio_dominio
    DocumentRoot /var/www/il_mio_dominio
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
</code></pre>

Nota che abbiamo aggiornato il `DocumentRoot` alla nostra nuova directory e `ServerAdmin` a un’e-mail a cui l’ amministratore del sito ****il\_mio\_dominio**** può accedere. Abbiamo anche aggiunto due direttive: `ServerName`, che stabilisce il dominio di base che dovrebbe corrispondere a questa definizione di host virtuale e `ServerAlias`, che definisce altri nomi che dovrebbero corrispondere come se fossero il nome di base.

Salva e chiudi il file quando hai finito.

Abilitiamo ora il file con lo strumento `a2ensite`:

<pre class="wp-block-code"><code>sudo a2ensite il_mio_dominio.conf</code></pre>

Disabilita infine il sito predefinito definito in `000-default.conf`:

<pre class="wp-block-code"><code>sudo a2dissite 000-default.conf</code></pre>

Quindi, testiamo gli errori di configurazione:

<pre class="wp-block-code"><code>sudo apache2ctl configtest</code></pre>

Dovresti vedere il seguente output:

<pre class="wp-block-code"><code>OutputSyntax OK</code></pre>

Riavvia Apache per implementare le modifiche:

<pre class="wp-block-code"><code>sudo systemctl restart apache2</code></pre>

Apache dovrebbe ora servire il tuo nome di dominio. Puoi testarlo navigando su `http://<mark>il_mio_dominio</mark>`, dovresti vedere la pagina HTML creata poco fa funzionare correttamente.

Con ciò, il tuo host virtuale è completamente configurato. Prima di apportare ulteriori modifiche o distribuire un’applicazione, tuttavia, sarebbe utile testare in modo proattivo la configurazione PHP nel caso in cui ci siano problemi che dovrebbero essere risolti.

## Passaggio 5: testare l’elaborazione PHP sul server Web

Per verificare che il tuo sistema sia configurato correttamente per PHP, crea uno script PHP chiamato `info.php`. Affinché Apache possa trovare questo file e servirlo correttamente, deve essere salvato nella directory principale del Web.

Crea il file nella radice web che hai creato nel passaggio precedente eseguendo:

<pre class="wp-block-code"><code>sudo nano /var/www/il_mio_dominio/info.php</code></pre>

Questo aprirà un file vuoto. Aggiungi il seguente testo, che è un codice PHP valido, all’interno del file:

<pre class="wp-block-code"><code><?php
phpinfo();
</code></pre>

Al termine, salva e chiudi il file.

Ora puoi verificare se il tuo server web è in grado di visualizzare correttamente il contenuto generato da questo script PHP. Per provarlo, visita questa pagina nel tuo browser web. Avrai bisogno di nuovo dell’indirizzo IP pubblico o del nome di dominio del tuo server.

L’indirizzo che vorrai visitare è:

<pre class="wp-block-code"><code>http://il_mio_dominio/info.php
</code></pre>

La pagina a cui vieni dovrebbe assomigliare a questa:`<figure class="wp-block-image size-large">`
`<img alt="" class="wp-image-494" decoding="async" src="/img/uploads/2022/06/small_php_info_1804-796x1024.png"/>` `</figure>`

Questa pagina fornisce alcune informazioni di base sul tuo server dal punto di vista di PHP. È utile per il debug e per garantire che le impostazioni vengano applicate correttamente.

Se riesci a vedere questa pagina nel tuo browser, il tuo PHP funziona come previsto.

Probabilmente vorrai rimuovere questo file dopo questo test perché potrebbe effettivamente fornire informazioni sul tuo server a utenti non autorizzati. Per fare ciò, esegui il seguente comando:

<pre class="wp-block-code"><code>sudo rm /var/www/il_mio_dominio/info.php</code></pre>

Puoi sempre ricreare questa pagina se hai bisogno di accedere nuovamente alle informazioni in un secondo momento.

## Conclusione

Ora che hai installato uno stack LAMP, hai molte scelte su cosa fare dopo. Hai installato una piattaforma che ti consentirà di installare la maggior parte dei tipi di siti Web e software Web sul tuo server.

Non ti resta che iniziare a installare o sviluppare i tuoi siti in PHP sul tuo nuovo LAMP stack!

Buon codice!

 [1]: /le-basi-di-php/
