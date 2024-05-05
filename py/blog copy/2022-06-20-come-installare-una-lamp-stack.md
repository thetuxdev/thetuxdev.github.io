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
## Introduzione {#introduction.wp-block-heading}

Uno stack &#8220;LAMP&#8221; è un gruppo di software open source che viene generalmente installato insieme per consentire a un server di ospitare siti Web dinamici e app Web.&nbsp;Questo termine è in realtà un acronimo che rappresenta il&nbsp;sistema operativo&nbsp;**L**inux, con il web server&nbsp;**A**pache**.&nbsp;**I dati del sito vengono archiviati in un&nbsp;database&nbsp;**M**ySQL e il contenuto dinamico viene elaborato da&nbsp;**P**HP.

In questa guida, installeremo uno stack LAMP su un server Ubuntu.

## Prerequisiti {#prerequisites.wp-block-heading}

Questo tutorial è creato su Ubuntu, ma funziona su tutte le distro basate su Debian, come Pop!_OS, Elementary OS, Linux Mint etc.

## Passaggio 1: installazione di Apache {#step-1-installing-apache-and-updating-the-firewall.wp-block-heading}

Il server Web Apache è un popolare server Web open source che può essere utilizzato insieme a [PHP][1] per ospitare siti Web dinamici.&nbsp;È ben documentato ed è stato ampiamente utilizzato per gran parte della storia del web.

Innanzitutto, assicurati che la tua&nbsp;`apt` cache sia aggiornata con:

<pre class="wp-block-code"><code>sudo apt update</code></pre>

Se è la prima volta che lo utilizzi&nbsp;`sudo` in questa sessione, ti verrà chiesto di fornire la password dell&#8217;utente per convalidare le tue autorizzazioni.

Una volta aggiornata la cache, puoi installare Apache lanciando:

<pre class="wp-block-code"><code>sudo apt install apache2</code></pre>

Dopo aver inserito questo comando,&nbsp;`apt` ti dirà quali pacchetti intende installare e quanto spazio su disco occuperà.&nbsp;Premi&nbsp;S (o Y se hai configurati il sistema in lingua inglese) e poi premi&nbsp;`ENTER` per confermare e l&#8217;installazione procederà.

<hr class="wp-block-separator has-alpha-channel-opacity" />

<p class="has-white-color has-vivid-red-background-color has-text-color has-background">
  N.B.: in questa guida utilizzerò &#8216;<em>Y</em>&#8216; per procedere con l&#8217;installazione, perché ho l&#8217;abitudine di installare sempre Linux in inglese&#8230; Se usi l&#8217;italiano ricordati di premere &#8216;<em>S</em>&#8216;
</p>

<hr class="wp-block-separator has-alpha-channel-opacity" />

E voilà! Apache è bello che installato!

Puoi fare subito un controllo a campione per verificare che tutto sia andato come previsto visitando l&#8217;indirizzo IP pubblico del tuo server nel tuo browser web. Se sei il locale ti basterà aprire il browser e scrivere nella barra degli indirizzi:

<pre class="wp-block-code"><code>http:&#47;&#47;localhost
</code></pre>

Se invece stai configurando un web server remoto, allora dovrai inserire il tuo indirizzo IP

<pre class="wp-block-code"><code>http://&lt;mark>your_server_ip&lt;/mark>
</code></pre>

Dovresti ora vedere nel browser la pagina Web predefinita di Apache, che è disponibile a scopo informativo e di test.&nbsp;Dovrebbe assomigliare a qualcosa di simile a questo:<figure class="wp-block-image size-large">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/06/small_apache_default_1804-728x1024.png" alt="" class="wp-image-493" /> </figure>

Se vedi questa pagina, allora il tuo server web è ora installato correttamente e accessibile attraverso il tuo firewall.

### Come trovare l&#8217;indirizzo IP pubblico del tuo server {#how-to-find-your-server-s-public-ip-address.wp-block-heading}

Se stai configurando un web server remoto e non sai qual è l&#8217;indirizzo IP pubblico del tuo server, ci sono diversi modi per trovarlo.&nbsp;Di solito è l&#8217;indirizzo che usi per connetterti al tuo server tramite SSH.

Esistono diversi modi per farlo dalla riga di comando.&nbsp;Innanzitutto, puoi utilizzare gli&nbsp;strumenti _iproute2_ per ottenere il tuo indirizzo IP digitando questo:

<pre class="wp-block-code"><code>ip addr show eth0 | grep inet | awk '{ print $2; }' | sed 's/\/.*$//'
</code></pre>

Questo ti restituirà due o tre righe.&nbsp;Sono tutti indirizzi corretti, ma il tuo computer potrebbe essere in grado di utilizzarne solo uno, quindi sentiti libero di provarli.

Un metodo alternativo consiste nell&#8217;utilizzare l&#8217;utility&nbsp;`curl` per contattare una parte esterna per dirti come&nbsp;_vede_&nbsp;il tuo server.&nbsp;Questo viene fatto chiedendo a un server specifico qual è il tuo indirizzo IP:

<pre class="wp-block-code"><code>sudo apt install curl
curl http://icanhazip.com</code></pre>

Indipendentemente dal metodo utilizzato per ottenere il tuo indirizzo IP, digitalo nella barra degli indirizzi del tuo browser web per visualizzare la pagina Apache predefinita.

## Passaggio 2: installazione di MySQL {#step-2-installing-mysql.wp-block-heading}

Ora che hai il tuo server web attivo e funzionante, è il momento di installare MySQL.&nbsp;MySQL è un sistema di gestione di database.&nbsp;Fondamentalmente, organizzerà e fornirà l&#8217;accesso ai database in cui il tuo sito può archiviare informazioni.

Ancora una volta, utilizziamo&nbsp;`apt` per acquisire e installare questo software:

<pre class="wp-block-code"><code>sudo apt install mysql-server</code></pre>

**Nota**&nbsp;: in questo caso, non è necessario eseguire&nbsp;`sudo apt update` prima del comando.&nbsp;Questo perché di recente l&#8217;hai eseguito nei comandi sopra per installare Apache.&nbsp;L&#8217;indice del pacchetto sul tuo computer dovrebbe essere già aggiornato.

Anche questo comando ti mostrerà un elenco dei pacchetti che verranno installati, insieme alla quantità di spazio su disco che occuperanno.&nbsp;Entra&nbsp;`Y` (o _S_) per continuare.

Al termine dell&#8217;installazione, esegui un semplice script di sicurezza preinstallato con MySQL che rimuoverà alcune pericolose impostazioni predefinite e bloccherà l&#8217;accesso al tuo sistema di database (Se sei in locale non è necessario).&nbsp;Avvia lo script interattivo eseguendo:

<pre class="wp-block-code"><code>sudo mysql_secure_installation</code></pre>

Questo ti chiederà se vuoi configurare il&nbsp;`VALIDATE PASSWORD PLUGIN`.

**Nota:**&nbsp;l&#8217;abilitazione di questa funzione è una sorta di chiamata di giudizio.&nbsp;Se abilitato, le password che non corrispondono ai criteri specificati verranno rifiutate da MySQL con un errore.&nbsp;Ciò causerà problemi se si utilizza una password debole insieme al software che configura automaticamente le credenziali utente di MySQL, come i pacchetti Ubuntu per phpMyAdmin.&nbsp;È sicuro lasciare la convalida disabilitata, ma dovresti sempre usare password complesse e univoche per le credenziali del database.

Rispondi&nbsp;`Y` per sì o per qualsiasi altra cosa per continuare senza abilitare.

<pre class="wp-block-code"><code>VALIDATE PASSWORD PLUGIN can be used to test passwords
and improve security. It checks the strength of password
and allows the users to set only those passwords which are
secure enough. Would you like to setup VALIDATE PASSWORD plugin?

Press y|Y for Yes, any other key for No:
</code></pre>

Se rispondi &#8220;sì&#8221;, ti verrà chiesto di selezionare un livello di convalida della password.&nbsp;Tieni presente che se inserisci&nbsp;`2`, il livello più forte, riceverai errori quando tenti di impostare una password che non contenga numeri, lettere maiuscole e minuscole e caratteri speciali o che sia basata su parole comuni del dizionario.

<pre class="wp-block-code"><code>There are three levels of password validation policy:

LOW    Length &gt;= 8
MEDIUM Length &gt;= 8, numeric, mixed case, and special characters
STRONG Length &gt;= 8, numeric, mixed case, special characters and dictionary                  file

Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG: &lt;mark>1&lt;/mark>
</code></pre>

Indipendentemente dal fatto che tu abbia scelto di impostare&nbsp;`VALIDATE PASSWORD PLUGIN`, il tuo server ti chiederà successivamente di selezionare e confermare una password per l&#8217; utente&nbsp;**root**&nbsp;MySQL.&nbsp;Questo non deve essere confuso con il&nbsp;**root di sistema**. L&#8217; utente&nbsp;**root del database**&nbsp;è un utente amministrativo con privilegi completi sul sistema del database.&nbsp;Anche se il metodo di autenticazione predefinito per l&#8217;utente root MySQL dispensa l&#8217;uso di una password,&nbsp;**anche quando ne è impostata una**&nbsp;, dovresti definire qui una password complessa come misura di sicurezza aggiuntiva.&nbsp;Ne parleremo tra un momento.

Se hai abilitato la convalida della password, ti verrà mostrata la sicurezza della password per la password di root che hai appena inserito e il tuo server ti chiederà se vuoi cambiare quella password.&nbsp;Se sei soddisfatto della tua password attuale, digita&nbsp;`N`:

<pre class="wp-block-code"><code>Using existing password for root.

Estimated strength of the password: &lt;mark>100&lt;/mark>
Change the password for root ? ((Press y|Y for Yes, any other key for No) : &lt;mark>n&lt;/mark>
</code></pre>

Per il resto delle domande, premere&nbsp;`Y` e premere `ENTER` ad ogni prompt.&nbsp;Ciò rimuoverà alcuni utenti anonimi e il database di test, disabiliterà gli accessi root remoti e caricherà queste nuove regole in modo che MySQL rispetti immediatamente le modifiche apportate.

Al termine, verifica se riesci ad accedere alla console MySQL digitando:

<pre class="wp-block-code"><code>sudo mysql</code></pre>

Questo si collegherà al server MySQL come utente&nbsp;**root**&nbsp;del database amministrativo, che viene dedotto dall&#8217;uso di&nbsp;`sudo` quando si esegue questo comando.&nbsp;Dovresti vedere un output come questo:

<pre class="wp-block-code"><code>OutputWelcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 5
Server version: 5.7.34-0ubuntu0.18.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql&gt;
</code></pre>

Per uscire dalla console MySQL, digita:

<pre class="wp-block-code"><code>exit</code></pre>

Tieni presente che non è necessario fornire una password per connettersi come utente&nbsp;**root**&nbsp;, anche se ne è stata definita una durante l&#8217;esecuzione dello&nbsp; `mysql_secure_installation`.&nbsp;Questo perché il metodo di autenticazione predefinito per l&#8217;utente MySQL amministrativo è&nbsp;`unix_socket` invece di&nbsp;`password`.&nbsp;Anche se all&#8217;inizio potrebbe sembrare un problema di sicurezza, rende il server del database più sicuro perché gli unici utenti autorizzati ad accedere come utente&nbsp;**root**&nbsp;MySQL sono gli utenti del sistema con privilegi sudo che si connettono dalla console o tramite un&#8217;applicazione in esecuzione con gli stessi privilegi.&nbsp;In termini pratici, ciò significa che non sarai in grado di utilizzare l&#8217;utente&nbsp;**root**&nbsp;del database amministrativo per connetterti dalla tua applicazione PHP.&nbsp;L&#8217;account MySQL funge da salvaguardia, nel caso in cui il metodo di autenticazione predefinito venga modificato da&nbsp;`unix_socket` a&nbsp;`password`.

Per una maggiore sicurezza, è meglio disporre di account utente dedicati con privilegi meno estesi impostati per ogni database, soprattutto se prevedi di avere più database ospitati sul tuo server, ma su questo creerò altre guide più dettagliate in futuro.

Il tuo server MySQL è ora installato e protetto.&nbsp;Vediamo ora come installare PHP, il componente finale nello stack LAMP.

## Passaggio 3: installazione di PHP {#step-3-installing-php.wp-block-heading}

PHP è il componente della configurazione che elaborerà il codice per visualizzare il contenuto dinamico.&nbsp;Può eseguire script, connettersi ai tuoi database MySQL per ottenere informazioni e consegnare il contenuto elaborato al tuo server web in modo che possa mostrare i risultati ai tuoi visitatori.

Ancora una volta, sfrutta il&nbsp;sistema apt per installare PHP.&nbsp;Oltre al&nbsp;pacchetto php, dovrai anche&nbsp;integrare libapache2-mod-php in Apache e il&nbsp;pacchetto php-mysql per consentire a PHP di connettersi ai database MySQL.&nbsp;Esegui il comando seguente per installare tutti e tre i pacchetti e le relative dipendenze:

<pre class="wp-block-code"><code>sudo apt install php libapache2-mod-php php-mysql</code></pre>

Questo dovrebbe installare PHP senza problemi.&nbsp;Lo testeremo tra un momento.

### Modifica dell&#8217;indice della directory di Apache (opzionale) {#changing-apache-s-directory-index-optional.wp-block-heading}

In alcuni casi, vorrai modificare il modo in cui Apache serve i file quando viene richiesta una directory.&nbsp;Di default, se un utente richiede una directory dal server, Apache cercherà prima un file chiamato&nbsp;`index.html`.&nbsp;Ma noi vogliamo dire al server web di preferire i file PHP rispetto ad altri, per fare in modo che Apache cerchi&nbsp;`index.php` come primoo file.&nbsp;In caso contrario, un&nbsp;`index.html` inserito nella radice del documento dell&#8217;applicazione avrà sempre la precedenza su un&nbsp;`index.php`.

Per apportare questa modifica, apri il file di configurazione&nbsp;`dir.conf` in un editor di testo a tua scelta.&nbsp;Qui useremo&nbsp;`nano`:

<pre class="wp-block-code"><code>sudo nano /etc/apache2/mods-enabled/dir.conf</code></pre>

Dovresti vedere una cosa del genere:

<pre class="wp-block-code"><code>&lt;IfModule mod_dir.c&gt;
    DirectoryIndex index.html index.cgi index.pl &lt;mark>index.php&lt;/mark> index.xhtml index.htm
&lt;/IfModule&gt;</code></pre>

Sposta il file di indice PHP (evidenziato sopra) nella prima posizione dopo la&nbsp;`DirectoryIndex`, in questo modo:

<pre class="wp-block-code"><code>&lt;IfModule mod_dir.c&gt;
    DirectoryIndex &lt;mark>index.php&lt;/mark> index.html index.cgi index.pl index.xhtml index.htm
&lt;/IfModule&gt;</code></pre>

Al termine, salva e chiudi il file premendo&nbsp;`CTRL+X`.&nbsp;Conferma il salvataggio digitando&nbsp;`Y` e quindi premi&nbsp;`ENTER` per verificare la posizione di salvataggio del file.

Successivamente, riavvia il server Web Apache in modo che le modifiche vengano riconosciute.&nbsp;Puoi farlo con il seguente comando:

<pre class="wp-block-code"><code>sudo systemctl restart apache2</code></pre>

Puoi anche controllare lo stato del&nbsp;`apache2`servizio utilizzando&nbsp;`systemctl`:

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

Jul 15 09:22:59 ubuntu1804 systemd&#91;1]: Starting The Apache HTTP Server...
Jul 15 09:22:59 ubuntu1804 apachectl&#91;3694]: AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.1.1. Set the 'ServerName' di
Jul 15 09:22:59 ubuntu1804 systemd&#91;1]: Started The Apache HTTP Server.
</code></pre>

Premi&nbsp;`Q` per uscire da questo stato.

## Passaggio 4: configurazione di un host virtuale (consigliato) {#step-4-setting-up-a-virtual-host-recommended.wp-block-heading}

Quando si utilizza il server Web Apache, è possibile utilizzare&nbsp;_host virtuali_ per incapsulare i dettagli di configurazione e ospitare più di un dominio da un singolo server.&nbsp;Imposteremo ora un dominio di esempio chiamato&nbsp;****il\_mio\_dominio****, potrai sostituirlo con il nome del dominio che desideri utilizzare.

Apache su ha un blocco server abilitato per impostazione predefinita che è configurato per servire i documenti dalla cartella&nbsp;`/var/www/html`.&nbsp;Sebbene funzioni bene per un singolo sito, può diventare ingombrante se ospiti più siti.&nbsp;Invece di modificare&nbsp;`/var/www/html`, creiamo una struttura di directory all&#8217;interno&nbsp;`/var/www` per&nbsp;**il sito il\_mio\_dominio**, lasciando&nbsp;`/var/www/html` come directory predefinita da servire se una richiesta del client non corrisponde a nessun altro sito.

Crea la directory per&nbsp;****il\_mio\_dominio****&nbsp;come segue:

<pre class="wp-block-code"><code>sudo mkdir /var/www/il_mio_dominio</code></pre>

Quindi, assegna la proprietà della directory con la variabile di ambiente&nbsp;`$USER`, che fa riferimento all&#8217;utente registrato corrente:

<pre class="wp-block-code"><code>sudo chown -R $USER:$USER /var/www/il_mio_dominio</code></pre>

I permessi della tua directory principale web dovrebbero essere corretti se non hai modificato il suo valore umask, ma puoi comunque digitare:

<pre class="wp-block-code"><code>sudo chmod -R 755 /var/www/il_mio_dominio</code></pre>

Ora crea una pagina di esempio&nbsp;`index.html` utilizzando&nbsp;`nano` o il tuo editor preferito:

<pre class="wp-block-code"><code>nano /var/www/il_mio_dominio/index.html</code></pre>

All&#8217;interno, aggiungi il seguente codice HTML di esempio:

<pre class="wp-block-code"><code>&lt;html&gt;
    &lt;head&gt;
        &lt;title&gt;Il Mio Dominio&lt;/title&gt;
    &lt;/head&gt;
    &lt;body&gt;
        &lt;h1&gt;Il mio dominio FUNZIONA!!!&lt;/h1&gt;
    &lt;/body&gt;
&lt;/html&gt;
</code></pre>

Salva e chiudi il file quando hai finito.

Affinché Apache possa servire questo contenuto, è necessario creare un file host virtuale con le direttive corrette.&nbsp;Invece di modificare il file di configurazione predefinito che si trova&nbsp;`/etc/apache2/sites-available/000-default.conf` direttamente in, creiamone uno nuovo in&nbsp;:`/etc/apache2/sites-available/<mark>il_mio_dominio</mark>.conf`

<pre class="wp-block-code"><code>sudo nano /etc/apache2/sites-available/il_mio_dominio.conf</code></pre>

Incolla il seguente blocco di configurazione, che è simile a quello predefinito, ma aggiornato per la nostra nuova directory e nome di dominio:/etc/apache2/sites-available/il\_mio\_dominio.conf

<pre class="wp-block-code"><code>&lt;VirtualHost *:80&gt;
    ServerAdmin webmaster@localhost
    ServerName il_mio_dominio
    ServerAlias &lt;mark>www.&lt;/mark>il_mio_dominio
    DocumentRoot /var/www/il_mio_dominio
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
&lt;/VirtualHost&gt;
</code></pre>

Nota che abbiamo aggiornato il&nbsp;`DocumentRoot` alla nostra nuova directory e&nbsp;`ServerAdmin` a un&#8217;e-mail a cui l&#8217; amministratore del sito&nbsp;****il\_mio\_dominio****&nbsp;può accedere.&nbsp;Abbiamo anche aggiunto due direttive:&nbsp;`ServerName`, che stabilisce il dominio di base che dovrebbe corrispondere a questa definizione di host virtuale e&nbsp;`ServerAlias`, che definisce altri nomi che dovrebbero corrispondere come se fossero il nome di base.

Salva e chiudi il file quando hai finito.

Abilitiamo ora il file con lo strumento&nbsp;`a2ensite`:

<pre class="wp-block-code"><code>sudo a2ensite il_mio_dominio.conf</code></pre>

Disabilita infine il sito predefinito definito in&nbsp;`000-default.conf`:

<pre class="wp-block-code"><code>sudo a2dissite 000-default.conf</code></pre>

Quindi, testiamo gli errori di configurazione:

<pre class="wp-block-code"><code>sudo apache2ctl configtest</code></pre>

Dovresti vedere il seguente output:

<pre class="wp-block-code"><code>OutputSyntax OK</code></pre>

Riavvia Apache per implementare le modifiche:

<pre class="wp-block-code"><code>sudo systemctl restart apache2</code></pre>

Apache dovrebbe ora servire il tuo nome di dominio.&nbsp;Puoi testarlo navigando su&nbsp;`http://<mark>il_mio_dominio</mark>`, dovresti vedere la pagina HTML creata poco fa funzionare correttamente.

Con ciò, il tuo host virtuale è completamente configurato.&nbsp;Prima di apportare ulteriori modifiche o distribuire un&#8217;applicazione, tuttavia, sarebbe utile testare in modo proattivo la configurazione PHP nel caso in cui ci siano problemi che dovrebbero essere risolti.

## Passaggio 5: testare l&#8217;elaborazione PHP sul server Web {#step-5-testing-php-processing-on-your-web-server.wp-block-heading}

Per verificare che il tuo sistema sia configurato correttamente per PHP, crea uno script PHP chiamato&nbsp;`info.php`.&nbsp;Affinché Apache possa trovare questo file e servirlo correttamente, deve essere salvato nella directory principale del Web.

Crea il file nella radice web che hai creato nel passaggio precedente eseguendo:

<pre class="wp-block-code"><code>sudo nano /var/www/il_mio_dominio/info.php</code></pre>

Questo aprirà un file vuoto.&nbsp;Aggiungi il seguente testo, che è un codice PHP valido, all&#8217;interno del file:

<pre class="wp-block-code"><code>&lt;?php
phpinfo();
</code></pre>

Al termine, salva e chiudi il file.

Ora puoi verificare se il tuo server web è in grado di visualizzare correttamente il contenuto generato da questo script PHP.&nbsp;Per provarlo, visita questa pagina nel tuo browser web.&nbsp;Avrai bisogno di nuovo dell&#8217;indirizzo IP pubblico o del nome di dominio del tuo server.

L&#8217;indirizzo che vorrai visitare è:

<pre class="wp-block-code"><code>http:&#47;&#47;il_mio_dominio/info.php
</code></pre>

La pagina a cui vieni dovrebbe assomigliare a questa:<figure class="wp-block-image size-large">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/06/small_php_info_1804-796x1024.png" alt="" class="wp-image-494" /> </figure>

Questa pagina fornisce alcune informazioni di base sul tuo server dal punto di vista di PHP.&nbsp;È utile per il debug e per garantire che le impostazioni vengano applicate correttamente.

Se riesci a vedere questa pagina nel tuo browser, il tuo PHP funziona come previsto.

Probabilmente vorrai rimuovere questo file dopo questo test perché potrebbe effettivamente fornire informazioni sul tuo server a utenti non autorizzati.&nbsp;Per fare ciò, esegui il seguente comando:

<pre class="wp-block-code"><code>sudo rm /var/www/il_mio_dominio/info.php</code></pre>

Puoi sempre ricreare questa pagina se hai bisogno di accedere nuovamente alle informazioni in un secondo momento.

## Conclusione {#conclusion.wp-block-heading}

Ora che hai installato uno stack LAMP, hai molte scelte su cosa fare dopo.&nbsp;Hai installato una piattaforma che ti consentirà di installare la maggior parte dei tipi di siti Web e software Web sul tuo server.

Non ti resta che iniziare a installare o sviluppare i tuoi siti in PHP sul tuo nuovo LAMP stack!

Buon codice!

 [1]: https://albertoreineri.it/guide/le-basi-di-php/