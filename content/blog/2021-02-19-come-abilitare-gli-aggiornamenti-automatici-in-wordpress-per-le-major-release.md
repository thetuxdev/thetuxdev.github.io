---
title: Come abilitare gli aggiornamenti automatici in WordPress per le Major Release
author: Alberto
type: post
date: 2021-02-19T10:37:00+00:00
url: /come-abilitare-gli-aggiornamenti-automatici-in-wordpress-per-le-major-release/
nectar_blog_post_view_count:
  - 44
tags:
  - Guide
  - WordPress Tricks

---
Sapevi che WordPress include&nbsp;**aggiornamenti automatici**&nbsp;abilitati per le versioni minori?&nbsp;Ciò significa che il team di WordPress.org può&nbsp;**installare automaticamente gli aggiornamenti di sicurezza**&nbsp;senza richiedere nulla dell’utente.

Tuttavia,&nbsp;**non aggiorna automaticamente il tuo sito Web quando è disponibile una nuova versione del sistema**.&nbsp;A meno che tu non faccia parte di un&nbsp;servizio di&nbsp;hosting WordPress gestito&nbsp;, dovrai avviare manualmente l’aggiornamento da solo.

In questo articolo, ti mostreremo come a**bilitare facilmente gli aggiornamenti automatici anche per le major release.**

## Come funzionano gli aggiornamenti automatici di WordPress

WordPress ha introdotto la funzione di aggiornamento automatico in&nbsp;WordPress 3.7&nbsp;(24 ottobre 2013).&nbsp;Ciò ha permesso a WordPress di installare automaticamente le nuove versioni minori per migliorare la sicurezza del tuo sito web.

C’è un’opzione per&nbsp;disabilitare gli aggiornamenti automatici&nbsp;in WordPress.&nbsp;Tuttavia, ti consigliamo di&nbsp;**mantenere abilitati gli aggiornamenti automatici&nbsp;**perché in genere risolvono importanti problemi di sicurezza e vulnerabilità.

I provider di hosting WordPress gestiti aggiornano automaticamente WordPress per tutte le nuove versioni, non solo per quelle minori.

Ora, se gestisci solo uno o due siti Web WordPress, puoi aggiornarli manualmente senza grossi problemi.

D’altra parte,&nbsp;**se gestisci più siti WordPress**, l’aggiornamento di tutti questi può richiedere molto tempo.

Diamo un’occhiata a come impostare facilmente gli aggiornamenti automatici per le principali versioni di WordPress.

## Preparazione agli aggiornamenti automatici in WordPress

Il livello più importante di sicurezza che è possibile aggiungere a qualsiasi sito Web è la configurazione di un sistema di&nbsp;**backup**.&nbsp;Che tu attivi gli aggiornamenti automatici o meno, dovresti sempre avere un sistema di backup automatico in atto per ogni sito Web WordPress.

Esistono diversi&nbsp;plug-in di backup WordPress&nbsp;utili&nbsp;che puoi utilizzare per impostare backup automatici sul tuo sito WordPress.

Ti consigliamo di utilizzare il&nbsp;plug-in&nbsp;<a href="https://it.wordpress.org/plugins/updraftplus/" target="_blank" rel="noreferrer noopener">UpdraftPlus&nbsp;</a>perché è il plug-in di WordPress più popolare sul mercato ed è gratuito.&nbsp;**UpdraftPlus&nbsp;**consente di impostare facilmente backup automatici dell’intero sito Web WordPress.

Inoltre, consente di archiviare automaticamente i file di backup in una posizione remota come&nbsp;**Google Drive**, Dropbox, ecc.

Dopo aver impostato i backup automatici di WordPress, puoi andare avanti e attivare l’aggiornamento automatico di WordPress per le versioni principali.

## Metodo 1. Abilita gli aggiornamenti automatici di WordPress per le versioni principali utilizzando un plug-in

Questo metodo è più&nbsp;**semplice&nbsp;**e consigliato a tutti gli utenti.

Innanzitutto, è necessario installare e attivare il&nbsp;plug-in&nbsp;<a href="https://wordpress.org/plugins/stops-core-theme-and-plugin-updates/" target="_blank" rel="noreferrer noopener">Easy Updates Manager</a>&nbsp;.&nbsp;

Al momento dell’attivazione, è necessario visitare&nbsp;**Dashboard »**&nbsp;**Update Options**&nbsp;per configurare il plug-in.<figure class="wp-block-image size-large">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-27-1-1024x200.png" alt="" class="wp-image-422" /> </figure>

Nella sezione “**WordPress core updates**“, fai clic sull’opzione “**Auto update all releases**“.

Il plugin memorizzerà automaticamente le tue impostazioni e consentirà&nbsp;**l’aggiornamento automatico delle principali versioni di WordPress.**

Questo plugin consente anche di**&nbsp;impostare altri aggiornamenti automatici**&nbsp;o disabilitarli.&nbsp;

## Metodo 2. Abilita manualmente l’aggiornamento

Questo metodo richiede di&nbsp;**aggiungere codice**&nbsp;ai tuoi file WordPress.

Innanzitutto, devi aggiungere la seguente riga di codice al&nbsp;file&nbsp;_wp-config.php_&nbsp;del&nbsp;tuo sito&nbsp;.

<pre class="wp-block-code"><code>define( 'WP_AUTO_UPDATE_CORE', true );</code></pre>

C’è un piccolo problema con questo codice: consente aggiornamenti&nbsp;**notturni**.

Per&nbsp;**disabilitare build notturni&nbsp;**e aggiornamenti di sviluppo, è necessario aggiungere il seguente codice nel file_&nbsp;functions.php_

<pre class="wp-block-code"><code>add_filter( 'allow_dev_auto_core_updates', '__return_false' );</code></pre>

Questo filtro disabiliterà gli aggiornamenti automatici per build notturne o aggiornamenti di sviluppo.

Il tuo sito WordPress è ora pronto per aggiornarsi automaticamente, senza il tuo input, ogni volta che è disponibile una nuova versione di WordPress.

## Domande frequenti sugli aggiornamenti automatici di WordPress

### **1. Perché devo installare gli aggiornamenti di WordPress?**

**WordPress è un software regolarmente gestito**.&nbsp;Migliaia di sviluppatori contribuiscono a rendere WordPress migliore e sicuro.

Devi installare gli aggiornamenti di WordPress non appena sono disponibili.&nbsp;Ciò&nbsp;**garantisce che il tuo sito Web disponga delle ultime patch di sicurezza**, nuove funzionalità per&nbsp;velocità e prestazioni&nbsp;ottimali.

### **2. Gli aggiornamenti sono sicuri per il mio sito Web?**

Gli aggiornamenti di WordPress diventano immediatamente disponibili per milioni di siti Web.&nbsp;**Il team principale lavora molto duramente per garantire che siano assolutamente sicuri**&nbsp;per l’installazione di tutti i siti Web.

Tuttavia, consigliamo a tutti di&nbsp;**eseguire sempre il backup del sito Web WordPress prima degli aggiornamenti**.&nbsp;Ciò consente di tornare rapidamente indietro nel caso in cui qualcosa vada storto dopo un aggiornamento.

### **3. Posso anche aggiornare automaticamente i plugin di WordPress?**

Per impostazione predefinita, WordPress richiede l’installazione manuale degli aggiornamenti dei plug-in.&nbsp;Tuttavia,&nbsp;**puoi abilitare gli aggiornamenti automatici anche per i plugin**.&nbsp;

Speriamo che questo articolo ti abbia aiutato a imparare come**&nbsp;abilitare gli aggiornamenti automatici in WordPress&nbsp;**per le&nbsp;