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
Personalmente utilizzo moltissimo gli overlay per migliorare la leggibilità del testo sopra un’immagine, **ma che cos’è questo overlay?**

In poche parole non è nient’altro che un** livello intermedio fra l’immagine e il testo**, un livello che va ‘opacizzare’ l’immagine per rendere più leggibile il testo.

Logicamente **con l’overlay il testo risulta molto più leggibile**, e secondo me l’immagnie è anche meno impattante, meno fastidiosa.

Farlo non è affatto difficile.<figure class="wp-block-embed is-type-rich is-provider-handler-delloggetto-incorporato wp-block-embed-handler-delloggetto-incorporato wp-embed-aspect-16-9 wp-has-aspect-ratio">
<div class="wp-block-embed__wrapper">
</div></figure>

## Come si fa

Basterà recarci all’interno del contenitore dell’immagine, in questo caso nel _div_ con classe _sidebar _e aggiungere un elemento chiamato “_overlay_“

<pre class="wp-block-code"><code> &lt;div class="sidebar" style="background:url('https://images.unsplash.com/photo-1534067783941-51c9c23ecefd?ixlib=rb-1.2.1&amp;ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&amp;auto=format&amp;fit=crop&amp;w=774&amp;q=80')"&gt;&lt;br&gt;
        &lt;div class="overlay"&gt;&lt;/div&gt;&lt;br&gt;
        &lt;div class="sidebar-inner"&gt;&lt;br&gt;
            &lt;div class="site-header"&gt;&lt;br&gt;
                &lt;h2&gt;Nome Sito Web&lt;/h2&gt;&lt;br&gt;
                &lt;i&gt;Lorem ipsum dolor sit amet&lt;/i&gt;&lt;br&gt;
            &lt;/div&gt;&lt;br&gt;
        &lt;/div&gt;&lt;br&gt;
    &lt;/div&gt;</code></pre>

Con l’html siamo a posto, ora spostiamoci nel nostro file **CSS** e dobbiamo solamente creare questa classe:

<pre class="wp-block-code"><code>.overlay{&lt;br&gt;
    position: absolute;&lt;br&gt;
    top:0;&lt;br&gt;
    left: 0;&lt;br&gt;
    right: 0;&lt;br&gt;
    bottom:0;&lt;br&gt;
    background-color: rgba(0, 0, 0, 0.4);&lt;br&gt;
    z-index: 2;&lt;br&gt;
    width: 100%;&lt;br&gt;
    height: 100%;&lt;br&gt;
}</code></pre>

_**E Voilà! Tutto finito!**_

Ora non resta che personalizzarla a piacere, cambiando il colore e il livello di opacità.

_Buon codice!_