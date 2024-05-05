---
title: Functions.php – Cos’è e come modificarlo
author: Alberto
type: post
date: 2021-03-20T13:42:00+00:00
url: /functions-php-cose-e-come-modificarlo/
nectar_blog_post_view_count:
  - 19
tags:
  - Guide
  - WordPress Tricks

---
In WordPress,**&nbsp;Functions.php&nbsp;**è uno dei file più&nbsp;**importanti&nbsp;**presenti all’interno di un tema.

Racchiude**&nbsp;tutte le funzioni necessarie al funzionamento del tema**. Funziona come un**&nbsp;plugin per il tuo sito WordPress&nbsp;**che viene attivato automaticamente con il tuo tema attuale.&nbsp;Il file&nbsp;functions.php&nbsp;utilizza&nbsp;il&nbsp;codice&nbsp;[PHP&nbsp;][1]per&nbsp;**aggiungere funzionalità**&nbsp;o modificare funzionalità predefinite su un sito WordPress.

Ad esempio, un tema WordPress potrebbe aggiungere un po’ di codice al file functions.php del tema per&nbsp;**aggiungere una nuova&nbsp;area&nbsp;widget&nbsp;**al piè di pagina o aggiungere un messaggio di benvenuto personalizzato alla&nbsp;dashboard di WordPress.&nbsp;Le possibilità sono infinite!

Il file Functions.php**&nbsp;si carica automaticamente**&nbsp;quando&nbsp;installi e attivi un tema&nbsp;sul tuo sito WordPress.

La modifica del file Functions.php utilizzando codici personalizzati ti consente di&nbsp;**aggiungere&nbsp;custom post type,&nbsp;tassonomie&nbsp;,&nbsp;shortcodes**&nbsp;e altro per migliorare il tuo sito web.

## Dove si trova il file Functions? {.wp-block-heading}

Il percorso del file Functions.php si trova&nbsp;**nella cartella del tema.**

Se vuoi aggiungere uno&nbsp;**snippet&nbsp;**di codice al tuo sito WordPress, puoi aggiungerlo al file Functions.php.

Ma di solito non è il modo migliore per farlo.&nbsp;WordPress cerca di separare design e funzionalità quando possibile.&nbsp;Questo è il motivo per cui abbiamo&nbsp;**temi&nbsp;**che determinano il&nbsp;**design&nbsp;**e&nbsp;**plugin**, che determinano le&nbsp;**funzioni**.

È meglio poter**&nbsp;cambiare il tema di WordPress&nbsp;senza cambiare il modo in cui funziona&nbsp;**il tuo sito o cambiare i tuoi plugin senza influire sulla progettazione del tuo sito.

Esistono molti&nbsp;tutorial di WordPress&nbsp;che ti diranno di aggiungere frammenti di codice al file Functions.php del tuo tema, ma**&nbsp;non sempre è la cosa migliore da fare**. Occorre analizzare bene il caso.

Se decidi di modificare il tuo file Functions.php, usa la massima&nbsp;**cautela**.&nbsp;Ecco 3 motivi per cui modificare il tuo file Functions.php non è una buona idea:

  * Le modifiche al file delle funzioni andranno perse quando il tema viene aggiornato.
  * Le modifiche andranno perse se cambi il tema di WordPress.
  * Fare errori di codifica nel file delle funzioni può bloccare fuori dal tuo sito.

Anche qualcosa di semplice come un punto e virgola mancante potrebbe far scomparire tutto il tuo sito…&nbsp;

Perché i plugin specifici del sito sono migliori (alternativa a Functions.php)

Quindi, se non vuoi modificare Functions.php, dove dovresti aggiungere le nuove funzioni del tuo sito?

La risposta è creare il tuo [plugin WordPress][2] .

Questo sarà un**&nbsp;plugin specifico per il tuo sito**, perché è specifico per il tuo sito e non verrà mai condiviso nella directory dei plug-in di WordPress.

L’uso di un plug-in specifico per il sito è la&nbsp;**soluzione migliore**&nbsp;perché i frammenti di codice vengono archiviati separatamente dal file Functions.php del tuo tema.&nbsp;Ciò significa che possono essere attivati â€‹â€‹o disattivati, proprio come qualsiasi altro plugin.&nbsp;Questo garantisce che**&nbsp;il tuo codice non scomparirà se cambi tema.**

Speriamo che questo articolo ti abbia aiutato a conoscere tutto sul file Functions.php in WordPress e su come aggiungere frammenti di codice al tuo sito!&nbsp;

 [1]: https://albertoreineri.it/categoria_guide/php
 [2]: https://albertoreineri.it/guide/creare-un-plugin-wordpress/