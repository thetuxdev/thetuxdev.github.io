---
title: Organizzare il lavoro con Python
author: Alberto
type: post
date: 2020-01-26T21:46:00+00:00
url: /organizzare-il-lavoro-con-python/
nectar_blog_post_view_count:
  - 54
tags:
  - Personal

---
Da qualche tempo sto sviluppando **piccoli progettini in Python**. Non per lavoro, ma perché nella **community degli sviluppatori** online se ne parla molto spesso e sembra che questo linguaggio sia veramente fantastico.

Così ho deciso di dedicarci qualche oretta alla settimana, in modo da avere un’**infarinatura generale**&nbsp;casomai dovessi realizzare qualcosa in questo linguaggio in futuro.

Mentre studiavo e sviluppavo, mi è venuta in mente un’idea per un**&nbsp;piccolo software realizzabile**&nbsp;molto semplicemente proprio**&nbsp;con Python.**

**Tutte le mattine**&nbsp;quando inizio a lavorare&nbsp;**lancio una serie di software&nbsp;**e pagine web, sempre le stesse, tutti i giorni…

Così ho pensato di&nbsp;**automatizzare questo passaggio**, creando uno script che mi permetta di organizzarmi il computer appena acceso, aprendo tutto ciò di cui ho bisogno con un solo click.

<div class="wp-block-image">
  <figure class="aligncenter size-full"><img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2022/03/ezgif-6-6f58fa3bf18b.gif" alt="" class="wp-image-143" /></figure>
</div>



## Aprire browser web con Python {.wp-block-heading}

Per prima cosa apro&nbsp;**google chrome**&nbsp;(o Microsoft Edge, dalla nuova versione è veramente migliorato).

Per prima cosa occorre importare il modulo&nbsp;_webbrowser_

<pre class="wp-block-code"><code>import webbrowser</code></pre>

Dopodiché è sufficiente indicare quali siti vogliamo visualizzare. Io per esempio apro&nbsp;**Gmail&nbsp;**e poi Google&nbsp;**Calendar**&nbsp;e Google&nbsp;**Keep&nbsp;**in due tab separate, in questo modo:

<pre class="wp-block-code"><code># Apro una nuova finestra del browser
webbrowser.open_new("https://mail.google.com/mail/u/0/#inbox")

# Apro url in nuovo tab
webbrowser.open_new_tab("https://keep.google.com/u/0/#home")
webbrowser.open_new_tab("https://calendar.google.com/calendar/r")</code></pre>

E’ anche possibile raggruppare gli url in variabili da richiamare successivamente, in questo modo:

<pre class="wp-block-code"><code># Variabili
website1 = "https://mail.google.com/mail/u/0/#inbox"
website2 = "https://calendar.google.com/calendar/r"
website3 = "https://keep.google.com/u/0/#home"

# Apro una nuova finestra del browser
webbrowser.open_new(website1)

# Apro url in nuovo tab
webbrowser.open_new_tab(website2)
webbrowser.open_new_tab(website3)
</code></pre>

In questo modo il codice è più semplice da capire e più pulito.

## Aprire software esterni con Python {.wp-block-heading}

Oltre al browser solitamente apro anche alcuni software. Uno in particolare è&nbsp;**XAMPP**, per poter lavorare comodamente in locale con i miei progetti in&nbsp;**PHP**.

Per aprire un software con&nbsp;**Python&nbsp;**è necessario importare il modulo&nbsp;_os_&nbsp;in questo modo:

<pre class="wp-block-code"><code>import os</code></pre>

E successivamente richiamare il percorso nel quale risiede il file eseguibile del programma.

Io lavoro su Windows quindi sarà un file .exe

Ecco il codice:

<pre class="wp-block-code"><code>path = "C:/xampp/xampp-control.exe"
os.system(path)</code></pre>

## Aprire una cartella con Python {.wp-block-heading}

Infine voglio aprire anche la cartella&nbsp;_htdocs_, nella quale risiedono tutti i miei progetti. Per questa operazione utilizzeremo sempre il modulo os, quindi non sarà più necessario importarlo.

Basterà indicare il percorso della cartella e utilizzare il metodo&nbsp;_startfile_, in questo modo:

<pre class="wp-block-code"><code>path = "C:/xampp/htdocs"
path = os.path.realpath(path)
os.startfile(path)</code></pre>

## Nascondere la console di Python {.wp-block-heading}

Questo è lo script. Ma c’è ancora una cosa che non mi piace:**&nbsp;la console di python che rimane aperta**&nbsp;sotto i software appena lanciati.

Fortunatamente si può nascondere in maniera molto semplice, basta inserire il seguente codice per&nbsp;**Windows**:

<pre class="wp-block-code"><code># Nascondere python console
import win32gui, win32con

The_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)</code></pre>

Ecco qua, lo script è terminato.

Se volete poi lanciarlo semplicemente cliccando su un’icona sarà sufficiente trasformarlo in .exe tramite pyinstaller.

Per fare ciò installate pyinstaller sul pc e poi lanciate questo comando da terminale:

<pre class="wp-block-code"><code>pyinstaller nomefile.py</code></pre>

In questo modo potrete avere un link sul desktop che lancerà il vostro script, che aprirà tutti i software necessari per realizzare i vostri lavori.

Spero che questo articolo possa esserti stato utile. Se hai consigli o suggerimenti per migliorarlo o eventuali bug da segnalare fammelo sapere nei commenti!

### Codice completo: {.wp-block-heading}

<pre class="wp-block-code"><code>import win32gui, win32con # Nascondere python console
import webbrowser #Aprire browser
import os #Aprire Software e Cartelle

# Nascondere python console
The_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)


#Aprire browser
# Variabili
website1 = "https://mail.google.com/mail/u/0/#inbox"
website2 = "https://calendar.google.com/calendar/r"
website3 = "https://keep.google.com/u/0/#home"

# Apro una nuova finestra del browser
webbrowser.open_new(website1)

# Apro url in nuovo tab
webbrowser.open_new_tab(website2)
webbrowser.open_new_tab(website3)


#Aprire Cartella
path = "C:/xampp/htdocs"
path = os.path.realpath(path)
os.startfile(path)

#Aprire Software
xamppPath= "C:/xampp/xampp-control.exe"
os.system(xamppPath)

</code></pre>