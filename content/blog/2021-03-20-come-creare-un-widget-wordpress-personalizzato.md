---
title: Come creare un widget WordPress personalizzato
author: Alberto
type: post
date: 2021-03-20T13:45:00+00:00
url: /come-creare-un-widget-wordpress-personalizzato/
nectar_blog_post_view_count:
  - 50
tags:
  - Guide
  - WordPress Tricks

---
Vuoi**&nbsp;creare i tuoi widget&nbsp;**personalizzati in WordPress?&nbsp;I widget ti consentono di aggiungere elementi non contenuti in una sidebar o in qualsiasi area predisposta per i widget del tuo sito web.

Puoi utilizzare i widget per&nbsp;**aggiungere banner, pubblicità, moduli di iscrizione alla newsletter e altri elementi**&nbsp;sul tuo sito web.

In questo articolo, ti mostreremo come creare un widget WordPress personalizzato, passo dopo passo.

## CHE COS’È UN WIDGET WORDPRESS?

I widget di WordPress contengono&nbsp;**parti di codice che puoi aggiungere alle sidebar del tuo sito Web o alle aree predisposte per accogliere i widget.**

Pensali come moduli che puoi usare per aggiungere diversi elementi usando una semplice**&nbsp;interfaccia drag and drop.**

Per impostazione predefinita,&nbsp;**WordPress viene fornito con un set standard di widget**&nbsp;che è possibile utilizzare con qualsiasi tema WordPress.&nbsp;Consulta la nostra guida per principianti su&nbsp;[come utilizzare i widget in WordPress][1]&nbsp;.<figure class="wp-block-image size-large">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-1-2-1-1024x484.png" alt="" class="wp-image-440" /> </figure>

WordPress consente inoltre agli sviluppatori di&nbsp;**creare i propri widget personalizzati.**

Molti temi e plugin premium di WordPress sono dotati di widget personalizzati che puoi aggiungere alle sidebar.

Ad esempio, puoi aggiungere un&nbsp;modulo di contatto&nbsp;, un&nbsp;modulo di accesso personalizzato&nbsp;o una&nbsp;galleria fotografica&nbsp;a una sidebar senza scrivere alcun codice.

Detto questo, vediamo come creare facilmente i tuoi widget personalizzati in WordPress.

## CREAZIONE DI UN WIDGET PERSONALIZZATO IN WORDPRESS

Se stai imparando a sviluppare in WordPress, avrai bisogno di un&nbsp;**ambiente di sviluppo locale**.&nbsp;Puoi&nbsp;[installare WordPress][2]&nbsp;sul tuo computer (Mac o Windows).

Esistono&nbsp;**diversi modi&nbsp;**per aggiungere il codice del widget personalizzato in WordPress.

Puoi&nbsp;creare un**&nbsp;plug-in**&nbsp;specifico per il sito&nbsp;e incollare qui il codice del tuo widget.

Puoi anche incollare il codice nel**&nbsp;file&nbsp;Functions.php&nbsp;**del tuo tema&nbsp;.&nbsp;Tuttavia, sarà disponibile solo quando quel particolare tema è attivo.

In questo tutorial, creeremo un semplice widget che saluta i visitatori.&nbsp;L’obiettivo è familiarizzare con la classe del widget WordPress.

_**Iniziamo**_.

## CREAZIONE DI UN WIDGET WORDPRESS DI BASE

WordPress viene fornito con una classe Widget WordPress integrata.&nbsp;**Ogni nuovo widget WordPress estende la classe del widget WordPress.**

Esistono&nbsp;**18 metodi&nbsp;**menzionati nel manuale dello sviluppatore di WordPress che possono essere utilizzati con la&nbsp;<a rel="noreferrer noopener" href="http://developer.wordpress.org/reference/classes/wp_widget/" target="_blank">classe Widget WP</a>&nbsp;.

Tuttavia, per il bene di questo tutorial,&nbsp;**ci concentreremo sui seguenti metodi.**

  * __construct (): questa è la parte in cui creiamo l’ID del widget, il titolo e la descrizione.
  * widget: Qui è dove definiamo l’output generato dal widget.
  * modulo: questa parte del codice è dove creiamo il modulo con le opzioni del widget per il backend.
  * aggiornamento: questa è la parte in cui salviamo le opzioni del widget nel database.

Studiamo il seguente codice in cui abbiamo usato questi quattro metodi all’interno della classe&nbsp;**WP_Widget**.

<pre class="wp-block-code"><code>// Creo il widget
class swp_widget extends WP_Widget {

// Construct
function __construct() {

}

// Widget front-end
public function widget( $args, $instance ) {

}

// Widget Backend
public function form( $instance ) {

}

// Updating widget replacing old instances with new
public function update( $new_instance, $old_instance ) {

}

// Fine Classe swp_widget ends here
} </code></pre>

Il pezzo finale del codice è dove registreremo effettivamente il widget e lo cariceremo all’interno di WordPress.

<pre class="wp-block-code"><code>// Registrazione e caricamento widget
function swp_load_widget()
{
	register_widget('swp_widget');
}
add_action('widgets_init', 'swp_load_widget');</code></pre>

Ora mettiamo tutto insieme per**&nbsp;creare un widget WordPress di base.**

Puoi&nbsp;**copiare e incollare il seguente codice&nbsp;**nel tuo plugin personalizzato o nel file Functions.php del tema.

<pre class="wp-block-code"><code>// Creo il widget
class swp_widget extends WP_Widget
{

	function __construct()
	{
		parent::__construct(

			// Base ID del widget
			'swp_widget',

			// Nome del Widget
			__('Specialista WP Widget', 'swp_widget_domain'),

			// Descrizione Widget
			array('description' =&gt; __('Widget di esempio di Specialista WP!', 'swp_widget_domain'),)
		);
	}

	// Widget front-end

	public function widget($args, $instance)
	{
		$title = apply_filters('widget_title', $instance&#91;'title']);

		// Gli argomenti before and after widget sono definiti dal tema
		echo $args&#91;'before_widget'];
		if (!empty($title))
			echo $args&#91;'before_title'] . $title . $args&#91;'after_title'];

		// Qua è dove vediamo l'output
		echo __('Ciao mondo!', 'swp_widget_domain');
		echo $args&#91;'after_widget'];
	}

	// Widget Backend
	public function form($instance)
	{
		if (isset($instance&#91;'title'])) {
			$title = $instance&#91;'title'];
		} else {
			$title = __('Titolo', 'swp_widget_domain');
		}
		// Widget admin form
	?&gt;
		&lt;p&gt;
			&lt;label for="&lt;?php echo $this-&gt;get_field_id('title'); ?&gt;"&gt;&lt;?php _e('Title:'); ?&gt;&lt;/label&gt;
			&lt;input class="widefat" id="&lt;?php echo $this-&gt;get_field_id('title'); ?&gt;" name="&lt;?php echo $this-&gt;get_field_name('title'); ?&gt;" type="text" value="&lt;?php echo esc_attr($title); ?&gt;" /&gt;
		&lt;/p&gt;
&lt;?php
	}

	// Aggiorniamo il widget sostituendo le vecchie istanze con le nuove
	public function update($new_instance, $old_instance)
	{
		$instance = array();
		$instance&#91;'title'] = (!empty($new_instance&#91;'title'])) ? strip_tags($new_instance&#91;'title']) : '';
		return $instance;
	}

	// Fine classe swp_widget
}


// Registrazione e caricamento widget
function swp_load_widget()
{
	register_widget('swp_widget');
}
add_action('widgets_init', 'swp_load_widget');
</code></pre>

Dopo aver aggiunto il codice, devi andare alla&nbsp;pagina&nbsp;**Aspetto »Widget**&nbsp;.&nbsp;Noterai il nuovo widget SpecialistaWP nell’elenco dei widget disponibili.&nbsp;Devi trascinare questo widget su una barra laterale.<figure class="wp-block-image size-large">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-2-1-1-1024x678.png" alt="" class="wp-image-441" /> </figure>

Questo widget ha solo un campo modulo da compilare, puoi&nbsp;**aggiungere il tuo testo e fare clic sul pulsante Salva&nbsp;**per memorizzare le modifiche.

Ora puoi&nbsp;**visitare il tuo sito Web per vederlo in azione.**<figure class="wp-block-image size-large">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/image-3-1-2-1024x626.png" alt="" class="wp-image-442" /> </figure>

Ora&nbsp;**studiamo di nuovo il codice.**

Innanzitutto&nbsp;**abbiamo registrato “swp_widget” e caricato il nostro widget personalizzato**.&nbsp;Successivamente abbiamo definito cosa fa quel widget e come visualizzare il back-end del widget.

Infine, abbiamo definito come&nbsp;**gestire le modifiche apportate al widget**.

Ora ci sono alcune cose che potresti voler chiedere.&nbsp;Ad esempio, qual è lo scopo&nbsp;`swp_text_domain`?

WordPress utilizza gettext per gestire la traduzione e la localizzazione.&nbsp;Questo&nbsp;`swp_text_domain`&nbsp;e&nbsp;dice a gettext di rendere disponibile una stringa per la traduzione.

Se stai creando un widget personalizzato per il tuo tema, puoi sostituirlo&nbsp;`swp_text_domain`&nbsp;con il&nbsp;**text_domain del tuo tema.**

Speriamo che questo articolo ti abbia&nbsp;**aiutato a imparare come creare facilmente un widget WordPress personalizzato**.&nbsp;

Buono sviluppo!

 [1]: http://specialistawp.local/widget-in-wordpress-come-utilizzarli/
 [2]: http://specialistawp.local/installare-wordpress-in-locale/