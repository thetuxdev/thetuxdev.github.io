---
title: Usare la riga di comando con WordPress grazie a WP-CLI
author: Alberto
type: post
date: 2022-06-27T09:35:51+00:00
url: /usare-la-riga-di-comando-con-wordpress-grazie-a-wp-cli/
nectar_blog_post_view_count:
  - 50
tags:
  - Guide
  - WordPress DEV

---
Se sei uno sviluppatore WordPress, probabilmente hai installato il CMS, l&#8217;hai aggiornato e hai attivato temi e plugin centinaia di volte.&nbsp;E sebbene queste attività di routine di sviluppo e manutenzione siano abbastanza facili da eseguire con l&#8217;interfaccia utente grafica di WordPress, eseguirle più e più volte non è molto efficiente.

La buona notizia è che puoi velocizzare facilmente ed efficacemente lo sviluppo e la manutenzione di&nbsp;[WordPress con l&#8217;interfaccia a riga di comando di WordPress (WP-CLI)][1]&nbsp;.&nbsp;In questo post esploreremo i diversi modi in cui puoi utilizzare WP-CLI e vedremo alcuni utili comandi WP-CLI per aiutarti a iniziare con un passo nella giusta direzione.

## UN&#8217;INTRODUZIONE A WP-CLI {.wp-block-heading}

Se sei nello sviluppo web da un po&#8217; di tempo, probabilmente hai familiarità con l&#8217;interfaccia da riga di comando.&nbsp;WP-CLI è l&#8217;interfaccia della riga di comando di WordPress.&nbsp;E per quelli di voi che non si sono dilettati molto nella programmazione, WP-CLI è uno strumento che consente di gestire le installazioni di WordPress senza utilizzare un browser web.

WP-CLI ti consente di fare qualsiasi cosa, dall&#8217;installazione del CMS WordPress su un sito Web nuovo di zecca all&#8217;esecuzione di operazioni a livello di sito su un sito Web WordPress esistente.&nbsp;E la parte migliore è che l&#8217;insieme di passaggi che devi seguire per completare tali attività sarà, nella maggior parte dei casi, ridotto a una&nbsp;singola riga di codice&nbsp;.

Ora che abbiamo visto a grandi linee cos&#8217;è WP-CLI e come può aiutarti ad accelerare lo sviluppo del tuo prossimo progetto, diamo un&#8217;occhiata a come puoi iniziare con questo potente strumento.

## INSTALLAZIONE DI WP-CLI SUL TUO AMBIENTE DI HOSTING {.wp-block-heading}

La prima cosa che devi fare per iniziare con WP-CLI è assicurarti che il tuo ambiente di hosting soddisfi i requisiti minimi:

  * Ambiente UNIX.
  * PHP 5.3.29 (o successivo).
  * WordPress 3.7 (o successivo).
  * Secure Shell (SSH) abilitato sul tuo server web.

Dopo aver verificato quegli elementi essenziali, vai avanti e scarica il file&nbsp;_wp-cli.phar_&nbsp;usando il seguente comando:

<pre class="wp-block-code"><code>$ curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar</code></pre>

E voilà!&nbsp;WP-CLI dovrebbe ora essere installato nel tuo ambiente di hosting.&nbsp;Se desideri assicurarti che funzioni correttamente, esegui semplicemente il seguente comando:

<pre class="wp-block-code"><code>$ php wp-cli.phar -info</code></pre>

Se tutto va bene, dovresti vedere qualcosa di simile sulla riga di comando che specifica quale versione di WP-CLI è in esecuzione nel tuo ambiente di hosting:

<pre class="wp-block-code"><code>PHP binary: /usr/bin/php5
PHP version: 5.5.9-1ubuntu4.14
php.ini used: /etc/php5/cli/php.ini
WP-CLI root dir: /home/wp-cli/.wp-cli
WP-CLI packages dir: /home/wp-cli/.wp-cli/packages/
WP-CLI global config: /home/wp-cli/.wp-cli/config.yml
WP-CLI project config:
WP-CLI version: 1.3.0</code></pre>

Tuttavia, se scopri che WP-CLI non è stato installato correttamente sul tuo sistema, ti consiglio di controllare alcuni metodi di&nbsp;[installazione alternativi][2]&nbsp;per ulteriori informazioni su come configurarlo.

Infine, creeremo un file eseguibile per WP-CLI e lo sposteremo nella sua directory in modo da poterlo eseguire da qualsiasi luogo:

<pre class="wp-block-code"><code>$ chmod +x wp-cli.phar
$ sudo mv wp-cli.phar /usr/local/bin/wp</code></pre>

Per semplicità, abbiamo chiamato la directory&nbsp;_wp_&nbsp;.&nbsp;Ora, ogni volta che devi usare WP-CLI, tutto ciò che devi fare è eseguire il comando&nbsp;_wp_&nbsp;dalla riga di comando.

## SVILUPPO WORDPRESS E MANUTENZIONE DEL SITO CON WP-CLI {.wp-block-heading}

Ora che WP-CLI è installato e pronto per l&#8217;uso, esaminiamo alcune delle cose più utili che puoi fare per accelerare le attività di routine di sviluppo e manutenzione di WordPress.

### INSTALLAZIONE DI WORDPRESS {.wp-block-heading}

Entra nella directory in cui desideri installare il CMS WordPress ed esegui la seguente riga di codice:

<pre class="wp-block-code"><code>$ wp core download</code></pre>

Dovrai creare un file&nbsp;_wp-config.php_&nbsp;per proseguire con la tua installazione.&nbsp;Ecco come puoi farlo:

<pre class="wp-block-code"><code>$ wp core config --dbname=databasename --dbuser=databaseuser --dbpass=databasepassword --dbhost=localhost --dbprefix=prfx_</code></pre>

_(Ho utilizzato del testo di esempio per il nome del database e le credenziali dell&#8217;utente del database. Assicurati di sostituirli con le informazioni del tuo database prima di eseguire il codice.)_

Infine, puoi iniziare l&#8217;installazione vera e propria eseguendo il comando di&nbsp;_installazione principale_&nbsp;indicato di seguito.&nbsp;Ricorda di sostituire i parametri di esempio con le informazioni del tuo sito prima di eseguire il codice.

<pre class="wp-block-code"><code>$ wp core install –-url=yoursite.com -–title="Your WordPress Site's Title" –-admin_user=admin_username –-admin_password=admin_password –-admin_email=admin@yoursite.com</code></pre>

### AGGIORNAMENTO DI WORDPRESS {.wp-block-heading}

Prima o poi verrà lanciata una nuova versione di WordPress e dovrai aggiornare la tua installazione all&#8217;ultima versione.&nbsp;Se non sei sicuro di quale versione di WordPress è attualmente in esecuzione sul tuo sito, esegui semplicemente il seguente comando:

<pre class="wp-block-code"><code>$ wp core version</code></pre>

Se ritieni che il tuo sito abbia effettivamente bisogno di essere aggiornato, è meglio eseguire un backup completo del suo database prima di procedere.&nbsp;Ecco come puoi farlo con WP-CLI:

<pre class="wp-block-code"><code>$ wp db export my-db-backup.sql</code></pre>

L&#8217;esecuzione di questo comando creerà un backup completo del database del tuo sito e lo salverà nella directory principale in un file chiamato&nbsp;_my-db-backup.sql_&nbsp;.

Infine, puoi aggiornare i file core del tuo sito e il relativo database eseguendo le seguenti righe di codice:

<pre class="wp-block-code"><code>$ wp core update
$ wp core update –db</code></pre>

Per quelli di voi che gestiscono più siti o reti multisito, eseguire il seguente script per aggiornare tutti i siti in una volta sola:

<pre class="wp-block-code"><code>$ declare -a sites_to_update=('/var/www/wordpress_site_1' '/var/www/wordpress_site_2' '/var/www/wordpress_site_n')
for site in "${sites_to_update&#91;@]}";
do
wp --path=$site core update
done</code></pre>

_(Ricordati di sostituire il testo di esempio con i nomi delle directory principali dei tuoi siti Web WordPress.)_

### GESTIONE DI TEMI E PLUGIN {.wp-block-heading}

Una delle cose migliori di WP-CLI è che collega il tuo server web alle directory ufficiali di WordPress&nbsp;[Theme][3]&nbsp;e&nbsp;[Plugin][4].&nbsp;Ciò significa che puoi gestire le installazioni di temi e plug-in utilizzando solo la riga di comando.

**Comandi del tema WordPress:**

  * **Per installare un tema:&nbsp;**__wp theme install theme_name__
  * **Per attivare un tema installato:&nbsp;**__wp theme activate theme_name__
  * **Per aggiornare un tema installato:&nbsp;**__wp theme update theme_name__
  * **Per aggiornare tutti i temi installati:&nbsp;**__wp theme update –all__

**Comandi del plugin di WordPress:**

  * **Per installare un plugin:&nbsp;**__wp plugin install plugin_name__
  * **Per attivare un plugin installato:&nbsp;**__wp plugin activate plugin_name__
  * **Per aggiornare un plugin installato:&nbsp;**__wp plugin update plugin_name__
  * **Per aggiornare tutti i plugin installati:&nbsp;**__wp plugin update –all__

_(Ricordati di sostituire il testo di esempio con il nome del tema o del plugin con cui desideri interagire.)_

### CREAZIONE DI CUSTOM POST PERSONALIZZATI {.wp-block-heading}

WP-CLI elimina il lavoro pesante dalla creazione di custom post type in WordPress e lo riduce a una semplice riga di codice.&nbsp;Invece di scaricare un plug-in per aiutarti a portare a termine il lavoro, perché non provare la seguente riga di codice:

<pre class="wp-block-code"><code>$ wp scaffold post-type cpt_slug --label=CPT_Label --theme=theme_name</code></pre>

Tutto quello che devi fare è sostituire il testo di esempio con lo slug, l&#8217;etichetta e il nome del tema del tuo custom post type e voilà!

### CREAZIONE DI TEMI CHILD {.wp-block-heading}

Se ti è già capitato di creare un tema child, avrai dovuto accedere al pannello di controllo e creareti cartella e file relativi dentro al sito.&nbsp;WP-CLI ti consente di creare un tema child con una singola riga di codice:

<pre class="wp-block-code"><code>$ wp scaffold child-theme name-of-child-theme --parent_theme=name_of_parent_theme --theme_name='My Child Theme' --author='Your Name' --author_uri=http://www.yoursite.com --theme_uri=http://www.themesite.com --activate</code></pre>

_(Come sempre, ricorda di sostituire il testo di esempio con il tema child e le informazioni sul tema genitore.)_

## CONCLUSIONE {.wp-block-heading}

Con WP-CLI puoi ottenere di più facendo di meno.&nbsp;Se desideri aumentare la tua produttività accelerando le operazioni di routine di sviluppo e manutenzione di WordPress, allora vale sicuramente la pena provare WP-CLI.

Ti ho mostrato come installare lo strumento nel tuo ambiente di hosting e abbiamo visto alcuni scenari in cui WP-CLI batte la GUI di WordPress in termini di efficienza.&nbsp;Ora non ti resta che provarlo!

Ah, sembra scontato, ma NON FARE MAI TEST IN AMBIENTE DI PRODUZIONE, usa lo STAGING o falli in LOCALE.

Buon codice!

 [1]: http://wp-cli.org/
 [2]: https://make.wordpress.org/cli/handbook/installing/#alternative-installation-methods
 [3]: https://wordpress.org/themes/
 [4]: https://wordpress.org/plugins/