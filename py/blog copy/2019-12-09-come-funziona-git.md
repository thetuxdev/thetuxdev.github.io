---
title: Come funziona GIT
author: Alberto
type: post
date: 2019-12-09T10:26:00+00:00
url: /come-funziona-git/
nectar_blog_post_view_count:
  - 43
tags:
  - Guide
  - Web Dev

---
Poco tempo fa ho scritto un [articolo ][1]elogiando **Git**, questo software di controllo versione del quale ormai **non posso più fare a meno**, quindi ho pensato di scrivere una guida per spiegare come funziona GIT!

## MA COME SI USA CONCRETAMENTE GIT? E’ DIFFICILE DA USARE?

Partiamo dal fatto che “Git” può essere tradotto con “_idiota_“, questo quasi a dirci che è un software a prova di scemo…

Scherzi a parte no, è&nbsp;**molto semplice**&nbsp;da utilizzare, inoltre può essere un buon&nbsp;**punto di inizio per imparare ad utilizzare la CLI,**&nbsp;l’interfaccia a riga di comando!

## INSTALLAZIONE

Per&nbsp;**scaricare&nbsp;**Git è sufficiente andare su questo sito:&nbsp;<https://git-scm.com/>

Una volta aperto il link cliccate su “Download”, selezionate il vostro sistema operativo ed effettuate l’installazione.

Se utilizzate Windows vi consiglio di installare anche Git Bash, una CLI molto carina che utilizzo anche per molto altro.

## UTILIZZO

Una volta installato git potete aprire Git Bash e spostarvi nella cartella di un vostro progetto (tramite il comando&nbsp;_cd_. Es:&nbsp;_cd C:/Users/alby/progetti/app_)

Qui inserite il comando

<pre class="wp-block-code"><code>git init</code></pre>

e git sarà presente nel vostro progetto con una cartella nascosta chiamata .git. Non aprite mai questa cartella, lasciatela semplicemente lì dove si trova, non vi farà del male.

Ora potete digitare, sempre su Git Bash, il seguente comando:

<pre class="wp-block-code"><code>git add .</code></pre>

Questo&nbsp;**caricherà&nbsp;**tutti i file del progetto nella staging area, in attesa di essere approvati.

Dopodiché basterà scrivere

<pre class="wp-block-code"><code>git commit -m “nome del commit”</code></pre>

Questo comando&nbsp;_committerà&nbsp;_i vostri file, creerà cioè una versione del vostro progetto. Fra virgolette potete scrivere ad esempio “Primo commit”, nei successivi andrete ad indicare le modifiche effettuate (Es: Inserito login)

## GIT HUB

E’ anche possibile salvare i commit su github, in modo da poterli consultare e scaricare ovunque e permettere ad altri sviluppatori di consultare il nostro codice e migliorarlo!

Per fare questo bisogna avere un account GitHub e creare un nuovo Repository.

Dopo aver creato un nuovo repository GitHub vi indica già i comandi da eseguire per “riempirlo” con il vostro progetto in locale.

Per fare questo dovere inserire:

<pre class="wp-block-code"><code>git remote add origin https://github.com&#91;link al repository]</code></pre>

<pre class="wp-block-code"><code>git push -u origin master</code></pre>

In questo modo avete il vostro progetto anche su GitHub. Per scaricarlo basterà usare il comando

<pre class="wp-block-code"><code>git pull https://github.com&#91;link al repository]</code></pre>

Questi sono i&nbsp;**comandi base**. Una volta creato il commit si possono fare altre modifiche al progetto e ridare i comandi add e commit.

Esistono&nbsp;**molti altri comandi**&nbsp;per utilizzare questo software.&nbsp;**Il modo migliore per impararli tutti è utilizzarli**, quindi inizia a sporcarti le mani e provali!&nbsp;**Non potrai più farne a meno**.

Qua di seguito inserisco una lista dei&nbsp;**comandi più utilizzat**i spiegati rapidamente.

## COMANDI PER GIT

### git config

Utilizzo:&nbsp;git config –global user.name “[name]”&nbsp;&nbsp;

Utilizzo :&nbsp;git config –global user.email “[email address]”&nbsp;&nbsp;

Questo comando imposta rispettivamente il nome dell’autore e l’indirizzo e-mail da utilizzare per i tuoi commit.<figure class="wp-block-image">

<img decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/1-9.png" alt="Git Config Command - Git Commands - Edureka" /> </figure>

### git init

Utilizzo:&nbsp;git init [repository name]

Questo comando viene utilizzato per avviare un nuovo repository (progetto).<figure class="wp-block-image">

<img decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/2-6.png" alt="GitInit Command - Git Commands - Edureka" /> </figure>

### git clone

Utilizzo:&nbsp;git clone [url]&nbsp;&nbsp;

Questo comando viene utilizzato per clonare un repository da un URL esistente.<figure class="wp-block-image">

<img decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/4-4.png" alt="Git Clone Command - Git Commands - Edureka" /> </figure>

### git add

Utilizzo:&nbsp;git add [file]&nbsp;&nbsp;

Questo comando aggiunge un file all’area di gestione temporanea.<figure class="wp-block-image">

<img decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/5-4.png" alt="Git Add Command - Git Commands - Edureka" /> </figure>

Utilizzo:&nbsp;git add *&nbsp;&nbsp;

Questo comando aggiunge uno o più file all’area di gestione temporanea.<figure class="wp-block-image">

<img decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/6-3.png" alt="Git Add Command - Git Commands - Edureka" /> </figure>

### git commit

Utilizzo:&nbsp;git commit -m “[ Type in the commit message]”&nbsp;&nbsp;

Questo comando registra o l’istantanea dei file in modo permanente nella cronologia delle versioni.<figure class="wp-block-image">

<img decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/7-3.png" alt="Git Commit Command - Git Commands - Edureka" /> </figure>

### git status

Utilizzo:&nbsp;git status&nbsp;&nbsp;

Questo comando elenca tutti i file che devono essere committati.<figure class="wp-block-image">

<img decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/15-1.png" alt="Git Status Command - Git Commands - Edureka" /> </figure>

### git rm

Utilizzo:&nbsp;git rm [file]&nbsp;&nbsp;

Questo comando cancella il file dalla directory di lavoro e mette in scena l’eliminazione.<figure class="wp-block-image">

<img decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/16-2.png" alt="Git Rm Command - Git Commands - Edureka" /> </figure>

### git log

Utilizzo :&nbsp;git log&nbsp;&nbsp;

Questo comando viene utilizzato per elencare la cronologia delle versioni per il ramo corrente.<figure class="wp-block-image">

<img decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/18.png" alt="Git Log Command - Git Commands - Edureka" /> </figure>

### git branch

Utilizzo:&nbsp;git branch&nbsp;&nbsp;

Questo comando elenca tutti i branch locali nel repository corrente.<figure class="wp-block-image">

<img decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/23.png" alt="Git Branch Command - Git Commands - Edureka" /> </figure>

Utilizzo :&nbsp;git branch [branch name]&nbsp;&nbsp;

Questo comando crea un nuovo branch.<figure class="wp-block-image">

<img decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/24.png" alt="Git Branch Command - Git Commands - Edureka" /> </figure>

Utilizzo :&nbsp;git branch -d [branch name]&nbsp;&nbsp;

Questo comando elimina il branch.<figure class="wp-block-image">

<img decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/25.png" alt="Git Branch Command - Git Commands - Edureka" /> </figure>

### git checkout

Utilizzo :&nbsp;git checkout [branch name]&nbsp;&nbsp;

Questo comando viene utilizzato per passare da un branch all’altro.<figure class="wp-block-image">

<img decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/27.png" alt="Git Checkout Command - Git Commands - Edureka" /> </figure>

Utilizzo :&nbsp;git checkout -b [branch name]&nbsp;&nbsp;

Questo comando crea un nuovo branch e passa anche a esso.<figure class="wp-block-image">

<img decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/28.png" alt="Git Checkout Command - Git Commands - Edureka" /> </figure>

### git merge

Utilizzo :&nbsp;git merge [branch name]&nbsp;&nbsp;

Questo comando unisce la cronologia del branch specificato nel branch corrente.<figure class="wp-block-image">

<img decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/31-1.png" alt="Git Merge Command - Git Commands - Edureka" /> </figure>

### git remote

Utilizzo :&nbsp;git remote add \[variable name\] \[Remote Server Link\]&nbsp;&nbsp;

Questo comando viene utilizzato per connettere il repository locale al server remoto.<figure class="wp-block-image">

<img decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/32.png" alt="Git Remote Command - Git Commands - Edureka" /> </figure>

### git push

Utilizzo :&nbsp;git push [variable name] master&nbsp;&nbsp;

Questo comando invia le modifiche da locale al repository remoto.<figure class="wp-block-image">

<img decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/33.png" alt="Git Push Command - Git Commands - Edureka" /> </figure>

Utilizzo :&nbsp;git push \[variable name\] \[branch\]&nbsp;&nbsp;

Questo comando invia i commit dei branch al repository remoto.<figure class="wp-block-image">

<img decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/34.png" alt="Git Push Command - Git Commands - Edureka" /> </figure>

Utilizzo :&nbsp;git push –all [variable name]&nbsp;&nbsp;

Questo comando invia tutti i branch al repository remoto.<figure class="wp-block-image">

<img decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/36.png" alt="Git Push Command - Git Commands - Edureka" /> </figure>

Utilizzo :&nbsp;git push [variable name] :[branch name]&nbsp;&nbsp;

Questo comando elimina un branch sul repository remoto.<figure class="wp-block-image">

<img decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/37.png" alt="Git Push Command - Git Commands - Edureka" /> </figure>

### git pull

Utilizzo :&nbsp;git pull [Repository Link]&nbsp;&nbsp;

Questo comando recupera e unisce le modifiche sul server remoto alla directory di lavoro.<figure class="wp-block-image">

<img decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/38.png" alt="Git Pull Command - Git Commands - Edureka" /> </figure>

### &nbsp;

 [1]: https://albertoreineri.it/guide/che-cose-git/