---
title: 6. Le basi di PHP
author: Alberto
type: post
date: 2020-03-17T18:44:55+00:00
url: /le-basi-di-php/
nectar_blog_post_view_count:
  - 26
tags:
  - Guide
  - Inizia Qui

---
**PHP**&nbsp;è uno dei linguaggi di programmazione&nbsp;**più utilizzati al mondo**&nbsp;in ambito web.

Moltissime&nbsp;**grandi aziende**&nbsp;lo utilizzano per i loro progetti, tra cui

  * Facebook
  * Wikipedia
  * Yahoo
  * Mailchimp
  * Slack
  * Dailymotion
  * Etsy

Fra queste c’è anche Automattic, l’azienda che ha realizzato e gestisce&nbsp;**WordPress**.

Il nostro&nbsp;**CMS**&nbsp;è infatti realizzato utilizzando il&nbsp;**PHP**.

Come per ogni Framework è sempre bene conoscere, almeno in linea generale, il linugaggio su cui è costruito. In questo caso a noi interessa&nbsp;**WordPress**, perciò&nbsp;**è bene sapere un po’ di PHP**&nbsp;per riuscire a comprenderlo a fondo.

Vediamo quindi&nbsp;**come funziona il PHP**

## Il PHP

Il php è un linguaggio&nbsp;**lato server,**&nbsp;cioè non può funzionare semplicemente sul browser, come avviene per HTML, CSS e Javascript, ma&nbsp;**ha bisogno di un server&nbsp;**per poter funzionare.

La particolarità del PHP è che&nbsp;**può essere eseguito all’interno delle pagine HTML,**&nbsp;può essere inserito direttamente in mezzo ai vari tag html.

**Esempio:**

<pre class="wp-block-code"><code>&lt;html&gt;
   &lt;head&gt;&lt;/head&gt;
   &lt;body&gt;
      &lt;?php echo "CIAO"; ?&gt;
   &lt;/body&gt;
&lt;/html&gt;</code></pre>

In questo caso puoi notare come**&nbsp;il PHP sia inserito direttamente nel body della pagina HTML.**

Questo rende il suo utilizzo molto&nbsp;**semplice**&nbsp;ed immediato.

### Server locale

Per poter iniziare a utilizzare PHP sul nostro computer dobbiamo&nbsp;**utilizzare un server locale.**

Come già detto prima, se HTML, CSS e Javascript possono girare nel browser, il PHP ha bisogno di un server.

Esistono molti server locali. In questa guida utilizzeremo [XAMPP][1], perché è semplice e disponibile per tutti i sistemi operativi.

Se vuoi sapere come installare XAMPP guarda [qui][1].

### Sintassi di base

Come già detto il PHP viene eseguito nelle pagine HTML, ma occorre&nbsp;**separare ciò che è PHP da ciò che non lo è.**

Il codice PHP va inserito all’interno di questi tag:**_&nbsp;<?php_**&nbsp;e&nbsp;_?>_

<pre class="wp-block-code"><code>&lt;?php
    //Codice php
?&gt;</code></pre>

Tutto ciò inserito fra questi tag sarà php, il resto sarà HTML.

### Fine riga

Come per il Javascript, anche il PHP necessita del&nbsp;**punto e virgola**&nbsp;alla fine di ogni riga, per poter capire dove termina una regola e ne inizia un’altra. Ricordati perciò semprio di inserire il punto e virgola dopo ogni riga

<pre class="wp-block-code"><code>echo "CIAO";</code></pre>

### Commenti

I commenti possono essere di&nbsp;**due tipi:**

**Una riga:&nbsp;**Se si vuole commentare l’intera riga basta inserire un&nbsp;**doppio slash**&nbsp;all’inizio della riga

<pre class="wp-block-code"><code>// Commento di una riga</code></pre>

**Più righe:&nbsp;**Per commentare più righe occorre utilizzare&nbsp;**_/\* commento \*/._**

<pre class="wp-block-code"><code>/* Commento su
più righe
Commento
Commento*/</code></pre>

### Variabili

Le variabili in PHP sono precedute da&nbsp;**$**, in questo modo:

<pre class="wp-block-code"><code>$saluto = "CIAO";
echo $saluto;</code></pre>

**Iniziamo!**

Per prima cosa andando nella cartella&nbsp;**htdocs**&nbsp;di XAMPP e creando una nuova cartella “**php_test**“.

## Stampare testo in HTML

Iniziamo con un semplice esercizio: stampiamo il classico “**Ciao mondo!**” su una pagina HTML.

Creiamo un file&nbsp;**“index.php**” e apriamolo con&nbsp;**VS Code.**

Ora possiamo premere&nbsp;**Punto esclamativo&nbsp;**seguito da&nbsp;**tab**, in questo modo&nbsp;**VS Code&nbsp;**ci fornirà lo&nbsp;**scheletro**&nbsp;html di base.

Ora procediamo a&nbsp;**stampare la nostra scritta.**

La funzione PHP per stampare del testo è&nbsp;**echo();**

Scriviamo quindi questo nel body:

<pre class="wp-block-code"><code>&lt;?php
   echo("Ciao mondo!");
?&gt;</code></pre>

Ora&nbsp;**salviamo**, apriamo il browser e&nbsp;**andiamo a questo link:**

<http://localhost/php_test>

Se tutto è andato liscio dovremmo vedere scritto “**Ciao mondo!**“.

**Perfetto**! Hai iniziato ad usare il PHP. Ma ora andiamo un po’ più a fondo.

## Variabili

In php possiamo&nbsp;**definire una variabile&nbsp;**con questa sintassi:

<pre class="wp-block-code"><code>$x = 1;
$y = "ciao";
$z = True;</code></pre>

Abbiamo appena definito una variabile denominata&nbsp;_x_&nbsp;con il numero 1, una variabile denominata&nbsp;_y_&nbsp;con la stringa “ciao” e un nome variabile&nbsp;_z_&nbsp;con il valore booleano True.&nbsp;Una volta definiti, possiamo usarli nel codice.

PHP ha molti tipi di variabili, ma i tipi di variabili più basilari sono numeri interi (numeri interi), float (numeri decimali), stringhe e valori booleani.

PHP può utilizzare anche&nbsp;**array**&nbsp;e oggetti che spiegheremo più avanti.

Le variabili possono anche essere impostate su&nbsp;**NULL**, il che significa che le variabili esistono, ma non contengono alcun valore.

## Operatori aritmetici

Possiamo usare semplici operatori aritmetici per&nbsp;**aggiungere**,&nbsp;**sottrarre**&nbsp;o&nbsp;**concatenare**&nbsp;le variabili.

Possiamo anche&nbsp;**stampare**&nbsp;le variabili PHP usando il comando&nbsp;_echo_&nbsp;(come abbiamo visto poco fa).

Proviamo per esempio a sommare due numeri, inserire il risultato in una nuova variabile e stamparla.

<pre class="wp-block-code"><code>$x = 1;
$y = 2;
$somma = $x + $y;
echo $somma;       // Stampa 3</code></pre>

## Concatenare stringhe

In PHP è possibile concatenare variabili e stringhe utilizzando il pungo (_._), in questo modo:

<pre class="wp-block-code"><code>$anni = 30;
$nome = "Marco";
echo $nome . " ha " . $anni . " anni!";</code></pre>

## Stringhe

Le stringhe sono&nbsp;**variabili che contengono testo**.&nbsp;Ad esempio, una stringa che contiene un nome è definita come segue:

<pre class="wp-block-code"><code>$nome = "Marco";
echo $nome;</code></pre>

Possiamo&nbsp;**formattare facilmente le stringhe usando le variabili**.&nbsp;Per esempio:

<pre class="wp-block-code"><code>$nome = "Marco";
$frase = "Ciao $nome";
echo $frase;</code></pre>

Possiamo anche&nbsp;**concatenare**&nbsp;le stringhe usando l’&nbsp;_._&nbsp;operatore&nbsp;punto&nbsp;.&nbsp;Per esempio:

<pre class="wp-block-code"><code>$nome = "Marco";
$cognome = "Rossi";
$nome_completo = $nome . " " . $cognome;
echo $nome_completo;</code></pre>

Per misurare la&nbsp;**lunghezza**&nbsp;di una stringa, utilizziamo la funzione&nbsp;_strlen_:

<pre class="wp-block-code"><code>$string = "Misuriamo quanti caratteri ha questa stringa";
echo strlen($string);</code></pre>

Per tagliare una parte di una stringa e restituirla come nuova stringa, possiamo usare la funzione&nbsp;_substr_:

<pre class="wp-block-code"><code>$filename = "image.png";
$extension = substr($filename, strlen($filename) - 3);
echo "L'estensione di questo file è $extension";</code></pre>

## Matrici semplici

Le matrici sono un tipo speciale di v**ariabile che può contenere molte variabili**&nbsp;e tenerle in un elenco.

Ad esempio, supponiamo di voler creare un elenco di tutti i numeri dispari tra 1 e 10. Una volta creato l’elenco, possiamo assegnare nuove variabili che faranno riferimento a una variabile nell’array, utilizzando l’indice della variabile.

Per utilizzare la prima variabile nell’elenco (in questo caso il numero 1), dovremo fornire&nbsp;**il primo indice**, che è&nbsp;****, poiché PHP utilizza indici basati su zero, come quasi tutti i linguaggi di programmazione oggi.

<pre class="wp-block-code"><code>$numeri_dispari = &#91;1,3,5,7,9];
$primo_numero_dispari = $numeri_dispari&#91;0];
$secondo_numero_dispari = $numeri_dispari&#91;1];

echo "Il primo numero dispari è $primo_numero_dispari\n";
echo "Il secondo numero dispari è $secondo_numero_dispari\n";
</code></pre>

Ora possiamo aggiungere nuove variabili usando un indice.&nbsp;Per aggiungere un elemento alla fine dell’elenco, possiamo assegnare l’array con l’indice 5 (la sesta variabile):

<pre class="wp-block-code"><code>$numeri_dispari = &#91;1,3,5,7,9];
$numeri_dispari&#91;5] = 11;
print_r($numeri_dispari);
</code></pre>

## Loop

I loop ci aiutano a scorrere su una variabile utilizzando un indice.&nbsp;Esistono&nbsp;**due tipi di loop**:&nbsp;**semplice**&nbsp;(stile C) e un loop&nbsp;**foreach**.

### Loop semplice

I loop sono molto utili quando dobbiamo&nbsp;**scorrere su un array e fare riferimento al membro dell’array usando un indice che cambia**.&nbsp;Ad esempio, supponiamo di avere un elenco di numeri dispari.&nbsp;Per stamparli, dobbiamo fare riferimento a ciascun articolo singolarmente.&nbsp;Il codice che scriviamo nel ciclo for può usare l’indice&nbsp;_i_, che cambia in ogni iterazione del ciclo for.

<pre class="wp-block-code"><code>$numeri = &#91;1,3,5,7,9];
for ($i = 0; $i &lt; count($numeri); $i=$i+1) {
    $numero = $numeri&#91;$i];
    echo $numero . "\n";
}
</code></pre>

**La prima riga del ciclo for definisce 3 parti:**

  * La dichiarazione di inizializzazione – nel nostro caso, inizializziamo la variabile&nbsp;_$i_&nbsp;su 0.
  * L’istruzione condizionale – questa istruzione viene valutata in ogni ciclo.&nbsp;Il loop si interrompe quando questa condizione non è soddisfatta.&nbsp;Questo accadrà quando la variabile&nbsp;_$i_&nbsp;sarà più grande della lunghezza dell’array.
  * L’istruzione incrementale: questa istruzione viene eseguita ogni volta per aumentare la variabile indice della quantità necessaria.&nbsp;Di solito aumenteremo&nbsp;_$i_&nbsp;di 1. Esistono anche due modi più brevi per aumentare una variabile di 1.&nbsp;

### Ciclo foreach

Il ciclo&nbsp;**foreach**&nbsp;esegue il loop su un elemento come una matrice o un oggetto, fornendo i membri in una specifica variabile uno alla volta.

Ad esempio, supponiamo di voler creare un elenco di tutti i numeri dispari tra 1 e 10 e stamparli uno per uno, come nell’esempio precedente.&nbsp;Questa volta, useremo il&nbsp;_foreach_&nbsp;&nbsp; invece di un&nbsp;_for_&nbsp;&nbsp;regolare con&nbsp;una variabile.&nbsp;Invece di utilizzare la variabile come indice dell’array, otteniamo l’elemento dall’array direttamente nella variabile&nbsp;_$numeri_dispari_&nbsp;.

<pre class="wp-block-code"><code>$numeri_dispari = &#91;1,3,5,7,9];
foreach ($numeri_dispari as $numero) {
  echo $numero . "\n";
}
</code></pre>

## Ciclo di While

I cicli&nbsp;**While**&nbsp;sono semplici blocchi che vengono eseguiti ripetutamente fino a quando non viene soddisfatta la condizione del ciclo while.

Ecco un esempio di un ciclo che viene eseguito per un totale di 10 volte:

<pre class="wp-block-code"><code>$counter = 0;

while ($counter &lt; 10) {
    $counter += 1;
    echo "Funzione eseguita $counter\n volte.&lt;br&gt;";
}</code></pre>

## funzioni

Le funzioni sono semplici&nbsp;**blocchi di codice che possiamo chiamare da qualsiasi luogo**.&nbsp;Ad esempio, possiamo creare una funzione che somma un elenco di numeri e restituisce il risultato.&nbsp;Chiamiamo questa funzione&nbsp;_somma_.

Una funzione riceve un elenco di argomenti separati da virgole.&nbsp;Ogni argomento esiste solo nel contesto della funzione, nel senso che diventano variabili all’interno del blocco funzione, ma non sono definiti al di fuori di quel blocco funzione.

<pre class="wp-block-code"><code>// Definiamo una funzione chiamata "somma" che farà la somma di una lista di numeri
function somma($numeri) {
    // inizializziamo la variabile somma
    $somma = 0;

    // Sommiamo i numero
    foreach ($numeri as $numero) {
        $somma += $numero;
    }

    // restituiamo la somma
    return $somma;
}

// Esempio di utilizzo della funzione
echo somma(&#91;1,2,3,4,5,6,7,8,9,10]);</code></pre>

In questo caso abbiamo la funzione “_**somma**_” che sommerà tutti i numeri che passeremo al loro interno.

**Richiamiamo**&nbsp;quindi la funzione in un&nbsp;_echo_, in questo modo stamperemo la somma dei numeri inseriti nel’array dentro la funzione.

Come per ogni cosa il metodo migliore è sempre quello di&nbsp;**provare, provare e riprovare!**

**Prenditi quindi il tuo tempo**&nbsp;e prova a smanettare un po’ con le funzioni che hai imparato qui sopra!

Il PHP consente di fare ben altre cose, ma&nbsp;**per iniziare con WordPress questo può bastare!**

**Quando ti senti pronto prova** adare un’occhiata alle nostre guide per **[creare un tema WordPress da zero][2]**, così potra imettere in pratica quello che hai imparato

_[<< Le basi di jQuery][3]_

 [1]: https://albertoreineri.it/guide/come-funziona-xampp/
 [2]: https://albertoreineri.it/guide/creare-un-tema-wordpress-da-zero-parte-1/
 [3]: https://albertoreineri.it/guide/le-basi-di-jquery/