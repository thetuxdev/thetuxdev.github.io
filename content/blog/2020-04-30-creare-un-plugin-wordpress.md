---
title: 4. Creare un plugin WordPress
author: Alberto
type: post
date: 2020-04-30T22:15:56+00:00
url: /creare-un-plugin-wordpress/
nectar_blog_post_view_count:
  - 26
tags:
  - Guide
  - WordPress DEV

---
Hai imparato a**[ creare un tema WordPress da zero ][1]**e vuoi impratichirti anche con i **plugin**?

Sei nel posto giusto!

Creare un plugin per WordPress può essere una cosa semplicissima e molto veloce come complicatissima e molto lenta…

In questa guida vediamo semplicemente come **creare un plugin per WordPress funzionante.**

Creeremo un plugin che aggiunge il **back on top **del sito. Andremo a inserire una freccia verso l’alto nell’angolo in basso a destra della pagina. Cliccando su questa freccia avvieremo uno smooth scroll verso il top della pagina!

## CREARE IL PLUGIN

Creare un nuovo plugin** non è difficile.**

Per prima cosa rechiamoci nella **cartella dei plugin **di WordPress: _/wp-content/pluigns._

Ora qui dentro **creiamo una nuova cartella **con il nome “**back-on-top**” e apriamo la cartella con** VS Code**.

Creiamo adesso un **file **in questa cartella chiamato “_**back-on-top.php**_” e inseriamo questo codice al suo interno:

<pre class="wp-block-code"><code>&lt;?php

/**
 * Plugin Name: Back on top
 * Plugin URI: /
 * Description: Un semplice link al top della pagina
 * Version: 1
 * Author: The TUX Dev
 * Author URI: https://thetuxdev.github.io/
 * Text Domain: back-on-top
 */</code></pre>

Questo codice **indicherà a WordPress l’esistenza del plugin.**

Se salviamo e andiamo nel backend in “**Plugins**” vedremo apparire “**Back on top**” nell’elenco. Possiamo quindi **attivarlo**.<figure class="wp-block-image size-full">
<img alt="" class="wp-image-331" decoding="async" src="/img/uploads/2022/03/image-41-1024x48-1.png"/> </figure>

Il plugin al momento **non fa assolutamente nulla**, ma l’abbiamo creato.

Vediamo ora come aggiungere una funzionalità al plugin.

## AGGIUNGERE FUNZIONALITÀ AL PLUGIN

Per poter aggiungere una funzionalità al nostro plugin occorre** agganciarsi ai vari hook di WordPress**. Nel nostro caso dobbiamo inserire una freccia in fondo alla pagina, quindi ci attaccheremo al footer.

Possiamo considerare il file back-on-top.php come un’**estensione del functions.php**. Ogni funzione che agguingiamo nel plugni verrà aggiunta al tema corrente.

### INSERIAMO IL CONTENUTO NEL FOOTER

<pre class="wp-block-code"><code>add_action('wp_footer', 'back_on_top');
function back_on_top()
{
    ob_start();
?&gt;
    &lt;div class="back-on-top" onclick="scrollToTop()"&gt;
        &lt;?php
        echo file_get_contents(plugin_dir_url(__FILE__) . "up.svg");
        ?&gt;
    &lt;/div&gt;
&lt;?php
    $output = ob_get_contents();
    ob_end_clean();
    echo $output;
}
</code></pre>

In questo modo abbiamo inserito sul fondo della nostra pagina** l’immagine up.svg** presente nella cartella del plugin.

**Puoi inserire l’immagine che preferisci**. Se inserisci un jpg o un png al posto di un svg puoi usare semplicemente il tag <img src="…"/>.

**_on_start _**è una funzione che permette di inserire codice html e considerarlo come una **variabile php.**

Ora aggiungiamo un po’ di **CSS **per rendere sensata la grafica. Per semplificare inseriamo il CSS direttamente nel file php, giusto sopra il div “**back-on-top**“:

<pre class="wp-block-code"><code>&lt;style&gt;
        .back-on-top {
            position: fixed;
            z-index: 99999;
            bottom: 30px;
            right: 30px;
            cursor: pointer
        }

        .back-on-top svg {
            width: 30px;
            height: 30px;
            fill: #444;
            transition: .3s;
        }

        .back-on-top svg:hover {
            fill: lightblue;
        }
    &lt;/style&gt;</code></pre>

Adesso non ci resta che inserire un po’ di **Javascript **per effettuare lo smooth scroll al top della pagina. Questo può essere fatto in molti modi, da vanilla Javascript a JQuery.

Per rendere le cose minimali inseriamo del **vanilla Javascript** dopo il div “**back-on-top**“:

<pre class="wp-block-code"><code>&lt;script&gt;
        // Smooth scroll to top
        const scrollToTop = () =&gt; {
            const c = document.documentElement.scrollTop || document.body.scrollTop;
            if (c &gt; 0) {
                window.requestAnimationFrame(scrollToTop);
                window.scrollTo(0, c - c / 8);
            }
        };
        scrollToTop();
    &lt;/script&gt;</code></pre>

**_E voilà!_**

**Il plugin è bello che pronto.** Puoi salvare e se tutto è andato a buon fine dovresti vedere una freccia verso l’alto nell’angolo in basso a destra del sito. Cliccando sulla freccia dovresti tornare al top della pagina.<figure class="wp-block-image size-full">
<img alt="" class="wp-image-332" decoding="async" src="/img/uploads/2022/03/image-39-1.png"> </img></figure>

**_Complimenti! Hai appena creato il tuo primo plugin!!!_**



<pre class="wp-block-code"><code>&lt;?php

/**
 * Plugin Name: Back on top
 * Plugin URI: /
 * Description: Un semplice link al top della pagina
 * Version: 1
 * Author: The TUX Dev
 * Author URI: https://thetuxdev.github.io/i
 * Text Domain: back-on-top
 */

add_action('wp_footer', 'back_on_top');
function back_on_top()
{
    ob_start();
?&gt;
    &lt;style&gt;
        .back-on-top {
            position: fixed;
            z-index: 99999;
            bottom: 30px;
            right: 30px;
            cursor: pointer
        }

        .back-on-top svg {
            width: 30px;
            height: 30px;
            fill: #444;
            transition: .3s;
        }

        .back-on-top svg:hover {
            fill: lightblue;
        }
    &lt;/style&gt;
    &lt;div class="back-on-top" onclick="scrollToTop()"&gt;
        &lt;?php
        echo file_get_contents(plugin_dir_url(__FILE__) . "up.svg");
        ?&gt;
    &lt;/div&gt;

    &lt;script&gt;
        // Smooth scroll to top
        const scrollToTop = () =&gt; {
            const c = document.documentElement.scrollTop || document.body.scrollTop;
            if (c &gt; 0) {
                window.requestAnimationFrame(scrollToTop);
                window.scrollTo(0, c - c / 8);
            }
        };
        scrollToTop();
    &lt;/script&gt;
&lt;?php
    $output = ob_get_contents();
    ob_end_clean();
    echo $output;
}
</code></pre>

_[&lt;&lt; Parte 3][2]_[]

 [1]: /creare-un-tema-wordpress-da-zero-parte-1/
 [2]: /creare-un-tema-wordpress-da-zero-parte-3/