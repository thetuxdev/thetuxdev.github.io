---
title: Nano Editor, Guida per principianti
author: Alberto
type: post
date: 2022-06-27T13:15:00+00:00
url: /nano-editor-guida-per-principianti/
nectar_blog_post_view_count:
  - 165
tags:
  - Guide
  - Linux

---
Gli utenti [Linux][1] hanno molte opzioni tra cui scegliere quando si tratta di editor di testo.&nbsp;Da base ad avanzato, esistono un sacco di editor di testo, ma alcuni come Vim ed Emacs possono risultare molto complicati per gli utenti meno avanzati.

In questo casi ci viene in aiuto Nano, forse il miglior editor di testo per principianti.

## Nano: {.wp-block-heading}

Nano è un editor di testo semplice e leggero sviluppato appositamente per sistemi UNIX e ambienti desktop che utilizzano un&#8217;interfaccia a riga di comando.&nbsp;Nano è concesso in licenza sotto la GNU General Public License ed emula l&#8217;editor di testo Pico.

## Come installare Nano: {.wp-block-heading}

Sto usando Ubuntu per questo tutorial e il processo di installazione sarà lo stesso su altre distribuzioni Linux.

Prima di procedere con il processo di installazione, sarebbe una buona idea verificare se l&#8217;editor di testo Nano è già installato o meno sul tuo sistema.&nbsp;Alcune distribuzioni Linux vengono fornite con l&#8217;editor Nano preinstallato.

Per controllare, esegui il seguente comando in Terminale.

<pre class="wp-block-code"><code>&lt;em>$&nbsp;&lt;/em>nano&nbsp;--version</code></pre>

Se ottieni un output con l&#8217;attuale versione di nano, puoi saltare l&#8217;installazione poiché l&#8217;editor di testo Nano è già installato sul tuo sistema.

L&#8217;installazione di Nano Text Editor è semplice, basta eseguire il seguente comando da Terminale e attendere il completamento dell&#8217;installazione.

<pre class="wp-block-code"><code>&lt;em>$&nbsp;&lt;/em>sudo&nbsp;apt-get install&nbsp;nano</code></pre>

Gli utenti CentOS/Red Hat Enterprise Linux (RHEL) possono utilizzare il comando seguente per installare l&#8217;editor Nano.

<pre class="wp-block-code"><code>&lt;em>$&nbsp;&lt;/em>yum installa&nbsp;nano</code></pre>

Ora che l&#8217;editor nano è stato installato correttamente sul tuo sistema e pronto per l&#8217;uso, possiamo iniziare con una guida per principianti all&#8217;uso dell&#8217;editor di testo Nano.

## Guida all&#8217;uso dell&#8217;editor di testo Nano {.wp-block-heading}

Vediamo ora come utilizzare l&#8217;editor di testo Nano.

### Come aprire/chiudere il Nano Text Editor {.wp-block-heading}

Il comando per aprire l&#8217;editor di testo Nano è il seguente.

<pre class="wp-block-code"><code>&lt;em>$&lt;/em>&nbsp;nano nomefile&nbsp;</code></pre>

Puoi aprire vari tipi di file nell&#8217;editor di testo Nano, inclusi .txt, .php, .html e molti altri.&nbsp;Devi solo digitare il nome del file seguito da un&#8217;estensione per aprire il file particolare nell&#8217;editor Nano.&nbsp;Ad esempio, supponiamo di dover aprire il file denominato il\_mio\_file.txt, il comando sarà il seguente.

<pre class="wp-block-code"><code>&lt;em>$&nbsp;&lt;/em>nano&nbsp;il_mio_file.txt</code></pre>

Devi assicurarti di essere nella directory in cui è stato salvato il file.&nbsp;Se il file non è presente nella directory, l&#8217;editor di testo Nano creerà un nuovo file nella directory attuale.

Una volta aperto il file noterai che l&#8217;interfaccia nano presenta il nome del file nella parte superiore, mentre nella parte inferiore noterai principalmente scorciatoie come taglia, sostituisci, vai alla riga e giustifica.&nbsp;Qui ˄ significa il tasto&nbsp;**CTRL**&nbsp;sulla tastiera.

Ad esempio, per&nbsp;**scrivere**&nbsp;o salvare le modifiche, devi premere i pulsanti CTRL + O sulla tastiera.

Se stai aprendo un file di configurazione, assicurati di utilizzare l&#8217; opzione&nbsp;**–w**&nbsp;, questo comanderà a Nano editor di aprire il file di configurazione in un formato standard.&nbsp;Se non si utilizza questa opzione, l&#8217;editor Nano avvolgerà il testo del file per adattarlo alla finestra, che alla fine sarà difficile da leggere.

## Come cercare / sostituire il testo {.wp-block-heading}

**CTRL + W**&nbsp;è la scorciatoia per cercare la parola nell&#8217;editor.&nbsp;Ora devi inserire il testo che vuoi cercare e quindi premere il tasto Invio.&nbsp;Per continuare a cercare lo stesso testo, usa il&nbsp;tasto&nbsp;**ALT + W.**

Per sostituire il testo, devi usare&nbsp;**CTRL + R**, l&#8217;editor ti porterà alla prima istanza del testo che desideri sostituire;&nbsp;per sostituire tutto il testo, devi premere&nbsp;**A**&nbsp;.&nbsp;Ma se vuoi sostituire un solo testo, devi premere&nbsp;**Y**.

## Come copiare e incollare il testo {.wp-block-heading}

L&#8217;operazione di copia incolla non è così semplice come altri editor di testo nell&#8217;editor Nano.&nbsp;Se desideri tagliare e incollare una riga particolare, devi prima portare il cursore all&#8217;inizio di quella riga.

Ora devi premere&nbsp;**CTRL + K**&nbsp;per tagliare la linea, quindi spostare il cursore nel punto in cui vuoi incollarlo, ora infine, premere&nbsp;**CTRL + U**&nbsp;per incollare la linea.

Per copiare e incollare una particolare stringa o parola, devi selezionare quella parola o stringa premendo&nbsp;**CTRL + 6**&nbsp;o&nbsp;**ALT + A**&nbsp;, assicurati che il cursore sia all&#8217;inizio della parola.

Ora puoi usare&nbsp;**CTRL + K**&nbsp;e&nbsp;**CTRL + U**&nbsp;per tagliare e incollare la parola o la stringa.

Ecco come puoi iniziare a utilizzare l&#8217;editor di testo Nano. Modificare un file di testo utilizzando la riga di comando non è facile, ma l&#8217;editor di testo Nano lo rende più semplice.&nbsp;È affidabile e uno degli strumenti più facili da usare.

Dagli utenti inesperti ai professionisti, tutti trovano l&#8217;editor di testo Nano un utile strumento da riga di comando.&nbsp;Spero che questa guida ti abbia sicuramente aiutato a iniziare con l&#8217;editor Nano.

Di seguito ti lascio una serie di comandi spesso utilizzati:

## Scoriatoie utili per nano: {.wp-block-heading}<figure class="wp-block-table">

| Command  | Action                                 |
| -------- | -------------------------------------- |
| CTRL + A | Vai all&#8217;inizio della riga        |
| CTRL + E | Vai alla fine della riga               |
| CTRL + Y | Scorri in basso nella pagina           |
| CTRL + V | Scorri in alto nella pagina            |
| CTRL + _ | Scorri fino alla riga speficina        |
| CTRL + C | Scopri dov&#8217;è il cursore          |
| CTRL + V | Scorri verso l&#8217;alto              |
| CTRL + W | Cerca un testo                         |
| CTRL + D | Cancella il carattere sotto al cursore |
| CTRL + K | Cancella l&#8217;intera riga           |
| CTRL + \ | Sostituisci una stringa                |
| CTRL + O | Salva il contenuto senza uscire        |
|          |                                        |</figure>

 [1]: /argomento/linux/