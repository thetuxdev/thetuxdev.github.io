---
title: Collegare PHP e MySQL con PDO
author: Alberto
type: post
date: 2021-06-30T17:56:00+00:00
url: /collegare-php-e-mysql-con-pdo/
nectar_blog_post_view_count:
  - 52
tags:
  - Guide
  - PHP

---
Collegare un database MySQL ad un progetto&nbsp;[PHP][1]&nbsp;è quasi sempre fondamentale, vediamo come farlo utilizzando PDO.

È possibile continuare ad utilizzare MySQLi, ma <a href="https://www.html.it/pag/63991/pdo-vs-mysqli/" target="_blank" rel="noreferrer noopener">PDO</a> garantisce livelli di sicurezza maggiori.<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio">

<div class="wp-block-embed__wrapper">
</div></figure>

La procedura è molto semplice, vediamo come fare:

Per prima cosa definiamo le variabili di connessione al nostro database:

<pre class="wp-block-code"><code>$servername = "localhost";
$username="root";
$passworddb="root";
$dbname="dbname";</code></pre>

Ora non ci resta che effettuare la connessione vera e propria, in questo modo:

<pre class="wp-block-code"><code>try{
    $db = new PDO("mysql:=$servername;dbname=$dbname", $username, $passworddb);
    $db-&gt;setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e){
    print "Errore! ". $e-&gt;getMessage() ." &lt;br/&gt;";
    die();
}</code></pre>

Con questo effettueremo la connessione al nostro DB e genereremo un messaggio in caso di errore, in modo da velocizzare il debug.

Ora non ci resta che testare la connessione. Aprendo il file contenente questo codice dovrete vedere una pagina completamente bianca, se è così allora la connessione funziona, altrimenti dovrete vedere un messaggio di errore.

Per essere ancora più sicuri della connessione proviamo a inserire dei dati nel nostro db e andarli a prendere e stampare sulla pagina PHP.

In questo esempio ho creato una tabella “Users” con all’interno un campo “Nome”. Ora andiamo a stampare tutti i dati all’interno di questa tabella:

<pre class="wp-block-code"><code>// Seleziono da DB
$query = $db-&gt;prepare("SELECT * FROM Users");
$query-&gt;execute();
$query-&gt;setFetchMode(PDO::FETCH_ASSOC);
while($row = $query-&gt;fetch()){
    echo $row&#91;'nome']. "&lt;br&gt;;
}</code></pre>

E Voilà! Se vi appare l’elenco dei nomi che avete inserito nel DB allora la connessione del php con MySQL attraverso PDO è fatta, non resta che svilupparci la web app intorno!

_Buon codice!_

 [1]: /argomento/php/