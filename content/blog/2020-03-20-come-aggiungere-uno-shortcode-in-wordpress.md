---
title: Come aggiungere uno shortcode in WordPress?
author: Alberto
type: post
date: 2020-03-20T13:40:00+00:00
url: /come-aggiungere-uno-shortcode-in-wordpress/
nectar_blog_post_view_count:
  - 36
tags:
  - Guide
  - WordPress Tricks

---
Gli shortcode sono un modo semplice per&nbsp;**aggiungere contenuti dinamici&nbsp;**nei post, nelle pagine e nelle barre laterali di WordPress.

Molti&nbsp;**plugin e temi WordPress utilizzano shortcode**&nbsp;per aggiungere contenuti particolari come moduli di contatto, gallerie di immagini, cursori e altro.

In questo articolo, ti mostreremo come&nbsp;**aggiungere facilmente uno shortcode in WordPress**.&nbsp;Ti mostreremo anche come creare i tuoi shortcode personalizzati in WordPress.

## COSA SONO GLI SHORTCODE?

Gli shortcode in ​​WordPress sono stringhe che ti aiutano ad aggiungere contenuti dinamici nei post, nelle pagine e nei widget della sidebar di WordPress.&nbsp;Sono visualizzati&nbsp;**tra parentesi quadre&nbsp;**quadre in questo modo:

_[shortcode]_

Per comprendere meglio gli shortcode, diamo un’occhiata al motivo per cui sono stati inseriti.

WordPress filtra tutto il contenuto per assicurarsi che nessuno utilizzi post e contenuto della pagina per inserire**&nbsp;codice dannoso**&nbsp;nel&nbsp;database&nbsp;.&nbsp;Ciò significa che&nbsp;**puoi scrivere HTML di base nei tuoi post, ma non puoi scrivere codice PHP.**

E se volessi eseguire un codice personalizzato all’interno dei tuoi post per visualizzare post correlati, banner pubblicitari, moduli di contatto, gallerie, ecc.?

Qui entra in gioco&nbsp;**l’API Shortcode.**

Fondamentalmente,**&nbsp;consente agli sviluppatori di aggiungere il loro codice all’interno di una funzione&nbsp;**e quindi di registrarla con WordPress come shortcode, in modo che gli utenti possano usarlo facilmente senza avere alcuna conoscenza di sviluppo web.

Quando WordPress trova lo shortcode, eseguirà automaticamente il codice ad esso associato.

Vediamo&nbsp;**come aggiungere facilmente&nbsp;**shortcode nei post e nelle pagine di WordPress.

## AGGIUNTA DI UNO SHORTCODE NEI POST E NELLE PAGINE DI WORDPRESS

Innanzitutto, è necessario**&nbsp;modificare il post e la pagina in cui si desidera aggiungere lo shortcode**.&nbsp;Successivamente, è necessario fare clic sul pulsante&nbsp;**Aggiungi blocco**&nbsp;per inserire un blocco&nbsp;_shortcode_.<figure class="wp-block-image size-large">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/shortcode-1024x513.gif" alt="" class="wp-image-434" /> </figure>

Dopo aver aggiunto il blocco&nbsp;_shortcode_, puoi semplicemente inserire il tuo shortcode nelle impostazioni del blocco.&nbsp;Lo shortcode sarà fornito da vari plugin di WordPress che potresti utilizzare.

Ora puoi salvare il tuo post o la pagina e visualizzare in anteprima le modifiche&nbsp;**per vedere lo shortcode in azione.**

## AGGIUNTA DI UNO SHORTCODE NEI WIDGET DELLA SIDEBAR DI WORDPRESS

Puoi anche usare gli shortcode nei&nbsp;widget della&nbsp;sidebar di WordPress&nbsp;.&nbsp;Basta visitare la&nbsp;pagina&nbsp;**Aspetto »Widget**&nbsp;e aggiungere il widget “Testo” a una sidebar.

Ora puoi**&nbsp;incollare il tuo shortcode**&nbsp;nell’area di testo del widget.<figure class="wp-block-image size-large">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-33-1-1024x438.png" alt="" class="wp-image-435" /> </figure>

Non dimenticare di fare clic sul pulsante “**Salva**” per memorizzare le impostazioni del widget.

Successivamente, puoi visitare il tuo&nbsp;sito Web WordPress&nbsp;per vedere&nbsp;**l’anteprima dal vivo&nbsp;**dello shortcode nel widget della barra laterale.

## AGGIUNTA DI UNO SHORTCODE NEL VECCHIO EDITOR CLASSICO DI WORDPRESS

Se stai ancora utilizzando il vecchio&nbsp;**editor classico&nbsp;**in WordPress, ecco come aggiungere codici brevi ai tuoi post e alle tue pagine WordPress.

Modifica semplicemente il post e la pagina in cui desideri aggiungere lo shortcode.&nbsp;È possibile**&nbsp;incollare lo shortcode**&nbsp;in qualsiasi punto all’interno dell’editor dei contenuti nel punto in cui si desidera che venga visualizzato.&nbsp;Assicurati solo che lo shortcode sia nella sua stessa riga.<figure class="wp-block-image size-large">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-34-3-1024x316.png" alt="" class="wp-image-437" /> </figure>

Non dimenticare di&nbsp;**salvare&nbsp;**le modifiche.&nbsp;Successivamente puoi visualizzare l’anteprima del tuo post e della pagina per vedere lo shortcode in azione.

## COME AGGIUNGERE UN SHORTCODE NEL TEMA WORDPRESS

Gli shortcode sono pensati per essere utilizzati all’interno di post, pagine e widget di WordPress.&nbsp;Tuttavia, a volte potresti voler&nbsp;**usare un shortcode all’interno di un tema&nbsp;**di WordPress.

Fondamentalmente, puoi aggiungere uno shortcode a qualsiasi file del tuo tema WordPress semplicemente aggiungendo il seguente codice.

<pre class="wp-block-code"><code>&lt;?php echo do_shortcode("&#91;shortcode]"); ?&gt;</code></pre>

WordPress cercherà lo shortcode e visualizzerà il suo output nel file del tema.

## COME CREARE IL TUO SHORTCODE PERSONALIZZATO IN WORDPRESS

Gli shortcode possono essere davvero utili quando si desidera&nbsp;**aggiungere contenuto dinamico o codice personalizzato**&nbsp;all’interno del post e delle pagine di WordPress.&nbsp;Tuttavia, se vuoi&nbsp;**creare un tuo shortcode personalizzato**, dovrai scrivere un po’ di codice.

Se hai dimestichezza con la scrittura di codice PHP, ecco un esempio che puoi utilizzare come modello:

<pre class="wp-block-code"><code>// Funzione che viene eseguita quando è richiamato lo shortcode
function my_shortcode() {
    $messaggio = 'Ciao mondo!';  // Output
    return $messaggio;
}
// Registro lo shortcode
add_shortcode('saluto', 'my_shortcode'); // Lo shortcode sarà &#91;saluto]</code></pre>

Con questo codice abbiamo prima creato una funzione che esegue del codice e restituisce l’output.&nbsp;Successivamente, abbiamo creato un nuovo shortcode chiamato ‘saluto’ e abbiamo detto a WordPress di eseguire la funzione che abbiamo creato.

Ora puoi&nbsp;**usare aggiungi questo shortcode ai tuoi post**, pagine e widget usando il seguente codice:

_[saluto]_

Questo eseguirà la funzione creata e mostrerà l’output desiderato.

## SHORTCODE O BLOCCHI DI GUTENBERG?

Gli utenti ci chiedono spesso le differenze tra shortcode e nuovi blocchi di Gutenberg.

Fondamentalmente se trovi utili gli shortcode, adorerai i blocchi dell’editor di WordPress.&nbsp;I blocchi ti consentono di fare la stessa cosa ma&nbsp;**in modo più intuitivo.**

Invece di richiedere agli utenti di aggiungere uno shortcode per visualizzare contenuti dinamici, i blocchi consentono agli utenti di aggiungere contenuti dinamici all’interno di post / pagine con&nbsp;**un’interfaccia utente più intuitiva**.&nbsp;Molti&nbsp;plugin WordPress popolari&nbsp;stanno passando all’uso dei blocchi&nbsp;**Gutenberg&nbsp;**anziché degli shortcode perché sono&nbsp;**più adatti ai principianti.**

Speriamo che questo articolo ti abbia aiutato a imparare come aggiungere uno shortcode in WordPress.