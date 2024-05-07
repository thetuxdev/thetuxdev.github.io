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
Vuoi** creare i tuoi widget **personalizzati in WordPress? I widget ti consentono di aggiungere elementi non contenuti in una sidebar o in qualsiasi area predisposta per i widget del tuo sito web.

Puoi utilizzare i widget per **aggiungere banner, pubblicità, moduli di iscrizione alla newsletter e altri elementi** sul tuo sito web.

In questo articolo, ti mostreremo come creare un widget WordPress personalizzato, passo dopo passo.

## CHE COS’È UN WIDGET WORDPRESS?

I widget di WordPress contengono **parti di codice che puoi aggiungere alle sidebar del tuo sito Web o alle aree predisposte per accogliere i widget.**

Pensali come moduli che puoi usare per aggiungere diversi elementi usando una semplice** interfaccia drag and drop.**

Per impostazione predefinita, **WordPress viene fornito con un set standard di widget** che è possibile utilizzare con qualsiasi tema WordPress. Consulta la nostra guida per principianti su [come utilizzare i widget in WordPress][1] .<figure class="wp-block-image size-large">
<img alt="" class="wp-image-440" decoding="async" src="/img/uploads/2022/03/image-1-2-1-1024x484.png"/> </figure>

WordPress consente inoltre agli sviluppatori di **creare i propri widget personalizzati.**

Molti temi e plugin premium di WordPress sono dotati di widget personalizzati che puoi aggiungere alle sidebar.

Ad esempio, puoi aggiungere un modulo di contatto , un modulo di accesso personalizzato o una galleria fotografica a una sidebar senza scrivere alcun codice.

Detto questo, vediamo come creare facilmente i tuoi widget personalizzati in WordPress.

## CREAZIONE DI UN WIDGET PERSONALIZZATO IN WORDPRESS

Se stai imparando a sviluppare in WordPress, avrai bisogno di un **ambiente di sviluppo locale**. Puoi [installare WordPress][2] sul tuo computer (Mac o Windows).

Esistono **diversi modi **per aggiungere il codice del widget personalizzato in WordPress.

Puoi creare un** plug-in** specifico per il sito e incollare qui il codice del tuo widget.

Puoi anche incollare il codice nel** file Functions.php **del tuo tema . Tuttavia, sarà disponibile solo quando quel particolare tema è attivo.

In questo tutorial, creeremo un semplice widget che saluta i visitatori. L’obiettivo è familiarizzare con la classe del widget WordPress.

_**Iniziamo**_.

## CREAZIONE DI UN WIDGET WORDPRESS DI BASE

WordPress viene fornito con una classe Widget WordPress integrata. **Ogni nuovo widget WordPress estende la classe del widget WordPress.**

Esistono **18 metodi **menzionati nel manuale dello sviluppatore di WordPress che possono essere utilizzati con la <a href="http://developer.wordpress.org/reference/classes/wp_widget/" rel="noreferrer noopener" target="_blank">classe Widget WP</a> .

Tuttavia, per il bene di questo tutorial, **ci concentreremo sui seguenti metodi.**

  * __construct (): questa è la parte in cui creiamo l’ID del widget, il titolo e la descrizione.
  * widget: Qui è dove definiamo l’output generato dal widget.
  * modulo: questa parte del codice è dove creiamo il modulo con le opzioni del widget per il backend.
  * aggiornamento: questa è la parte in cui salviamo le opzioni del widget nel database.

Studiamo il seguente codice in cui abbiamo usato questi quattro metodi all’interno della classe **WP_Widget**.

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

Ora mettiamo tutto insieme per** creare un widget WordPress di base.**

Puoi **copiare e incollare il seguente codice **nel tuo plugin personalizzato o nel file Functions.php del tema.

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
		$title = apply_filters('widget_title', $instance['title']);

		// Gli argomenti before and after widget sono definiti dal tema
		echo $args['before_widget'];
		if (!empty($title))
			echo $args['before_title'] . $title . $args['after_title'];

		// Qua è dove vediamo l'output
		echo __('Ciao mondo!', 'swp_widget_domain');
		echo $args['after_widget'];
	}

	// Widget Backend
	public function form($instance)
	{
		if (isset($instance['title'])) {
			$title = $instance['title'];
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
		$instance['title'] = (!empty($new_instance['title'])) ? strip_tags($new_instance['title']) : '';
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

Dopo aver aggiunto il codice, devi andare alla pagina **Aspetto »Widget** . Noterai il nuovo widget SpecialistaWP nell’elenco dei widget disponibili. Devi trascinare questo widget su una barra laterale.<figure class="wp-block-image size-large">
<img alt="" class="wp-image-441" decoding="async" src="/img/uploads/2022/03/image-2-1-1-1024x678.png"/> </figure>

Questo widget ha solo un campo modulo da compilare, puoi **aggiungere il tuo testo e fare clic sul pulsante Salva **per memorizzare le modifiche.

Ora puoi **visitare il tuo sito Web per vederlo in azione.**<figure class="wp-block-image size-large">
<img alt="" class="wp-image-442" decoding="async" src="/img/uploads/2022/03/image-3-1-2-1024x626.png"/> </figure>

Ora **studiamo di nuovo il codice.**

Innanzitutto **abbiamo registrato “swp_widget” e caricato il nostro widget personalizzato**. Successivamente abbiamo definito cosa fa quel widget e come visualizzare il back-end del widget.

Infine, abbiamo definito come **gestire le modifiche apportate al widget**.

Ora ci sono alcune cose che potresti voler chiedere. Ad esempio, qual è lo scopo `swp_text_domain`?

WordPress utilizza gettext per gestire la traduzione e la localizzazione. Questo `swp_text_domain` e dice a gettext di rendere disponibile una stringa per la traduzione.

Se stai creando un widget personalizzato per il tuo tema, puoi sostituirlo `swp_text_domain` con il **text_domain del tuo tema.**

Speriamo che questo articolo ti abbia **aiutato a imparare come creare facilmente un widget WordPress personalizzato**. 

Buono sviluppo!

 [1]: /come-creare-un-widget-wordpress-personalizzato/
 [2]: /installare-wordpress-in-locale/