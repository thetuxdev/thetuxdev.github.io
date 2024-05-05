---
title: Come creare un effetto Overlay in CSS
author: Alberto
type: post
date: 2022-02-22T20:02:00+00:00
url: /come-creare-un-effetto-overlay-in-css/
nectar_blog_post_view_count:
  - 93
tags:
  - Guide
  - Web Dev

---
Personalmente utilizzo moltissimo gli overlay per migliorare la leggibilità del testo sopra un&#8217;immagine,&nbsp;**ma che cos&#8217;è questo overlay?**

In poche parole non è nient&#8217;altro che un**&nbsp;livello intermedio fra l&#8217;immagine e il testo**, un livello che va &#8216;opacizzare&#8217; l&#8217;immagine per rendere più leggibile il testo.

Logicamente&nbsp;**con l&#8217;overlay il testo risulta molto più leggibile**, e secondo me l&#8217;immagnie è anche meno impattante, meno fastidiosa.

Farlo non è affatto difficile.<figure class="wp-block-embed is-type-rich is-provider-handler-delloggetto-incorporato wp-block-embed-handler-delloggetto-incorporato wp-embed-aspect-16-9 wp-has-aspect-ratio">

<div class="wp-block-embed__wrapper">
</div></figure>

## Come si fa {.wp-block-heading}

Basterà recarci all&#8217;interno del contenitore dell&#8217;immagine, in questo caso nel&nbsp;_div_&nbsp;con classe&nbsp;_sidebar&nbsp;_e aggiungere un elemento chiamato &#8220;_overlay_&#8220;

<pre class="wp-block-code"><code>&nbsp;&lt;div class="sidebar" style="background:url('https://images.unsplash.com/photo-1534067783941-51c9c23ecefd?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80')"&gt;&lt;br>
&nbsp; &nbsp; &nbsp; &nbsp; &lt;div class="overlay"&gt;&lt;/div&gt;&lt;br>
&nbsp; &nbsp; &nbsp; &nbsp; &lt;div class="sidebar-inner"&gt;&lt;br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &lt;div class="site-header"&gt;&lt;br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &lt;h2&gt;Nome Sito Web&lt;/h2&gt;&lt;br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &lt;i&gt;Lorem ipsum dolor sit amet&lt;/i&gt;&lt;br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &lt;/div&gt;&lt;br>
&nbsp; &nbsp; &nbsp; &nbsp; &lt;/div&gt;&lt;br>
&nbsp; &nbsp; &lt;/div&gt;</code></pre>

Con l&#8217;html siamo a posto, ora spostiamoci nel nostro file&nbsp;**CSS**&nbsp;e dobbiamo solamente creare questa classe:

<pre class="wp-block-code"><code>.overlay{&lt;br>
&nbsp; &nbsp; position: absolute;&lt;br>
&nbsp; &nbsp; top:0;&lt;br>
&nbsp; &nbsp; left: 0;&lt;br>
&nbsp; &nbsp; right: 0;&lt;br>
&nbsp; &nbsp; bottom:0;&lt;br>
&nbsp; &nbsp; background-color: rgba(0, 0, 0, 0.4);&lt;br>
&nbsp; &nbsp; z-index: 2;&lt;br>
&nbsp; &nbsp; width: 100%;&lt;br>
&nbsp; &nbsp; height: 100%;&lt;br>
}</code></pre>

_**E Voilà! Tutto finito!**_

Ora non resta che personalizzarla a piacere, cambiando il colore e il livello di opacità.

_Buon codice!_