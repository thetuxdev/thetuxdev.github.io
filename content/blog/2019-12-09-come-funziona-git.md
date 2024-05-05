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

Scherzi a parte no, è **molto semplice** da utilizzare, inoltre può essere un buon **punto di inizio per imparare ad utilizzare la CLI,** l’interfaccia a riga di comando!

## INSTALLAZIONE

Per **scaricare **Git è sufficiente andare su questo sito: <https: git-scm.com=""></https:>

Una volta aperto il link cliccate su “Download”, selezionate il vostro sistema operativo ed effettuate l’installazione.

Se utilizzate Windows vi consiglio di installare anche Git Bash, una CLI molto carina che utilizzo anche per molto altro.

## UTILIZZO

Una volta installato git potete aprire Git Bash e spostarvi nella cartella di un vostro progetto (tramite il comando _cd_. Es: _cd C:/Users/alby/progetti/app_)

Qui inserite il comando

<pre class="wp-block-code"><code>git init</code></pre>

e git sarà presente nel vostro progetto con una cartella nascosta chiamata .git. Non aprite mai questa cartella, lasciatela semplicemente lì dove si trova, non vi farà del male.

Ora potete digitare, sempre su Git Bash, il seguente comando:

<pre class="wp-block-code"><code>git add .</code></pre>

Questo **caricherà **tutti i file del progetto nella staging area, in attesa di essere approvati.

Dopodiché basterà scrivere

<pre class="wp-block-code"><code>git commit -m “nome del commit”</code></pre>

Questo comando _committerà _i vostri file, creerà cioè una versione del vostro progetto. Fra virgolette potete scrivere ad esempio “Primo commit”, nei successivi andrete ad indicare le modifiche effettuate (Es: Inserito login)

## GIT HUB

E’ anche possibile salvare i commit su github, in modo da poterli consultare e scaricare ovunque e permettere ad altri sviluppatori di consultare il nostro codice e migliorarlo!

Per fare questo bisogna avere un account GitHub e creare un nuovo Repository.

Dopo aver creato un nuovo repository GitHub vi indica già i comandi da eseguire per “riempirlo” con il vostro progetto in locale.

Per fare questo dovere inserire:

<pre class="wp-block-code"><code>git remote add origin https://github.com[link al repository]</code></pre>
<pre class="wp-block-code"><code>git push -u origin master</code></pre>

In questo modo avete il vostro progetto anche su GitHub. Per scaricarlo basterà usare il comando

<pre class="wp-block-code"><code>git pull https://github.com[link al repository]</code></pre>

Questi sono i **comandi base**. Una volta creato il commit si possono fare altre modifiche al progetto e ridare i comandi add e commit.

Esistono **molti altri comandi** per utilizzare questo software. **Il modo migliore per impararli tutti è utilizzarli**, quindi inizia a sporcarti le mani e provali! **Non potrai più farne a meno**.

Qua di seguito inserisco una lista dei **comandi più utilizzat**i spiegati rapidamente.

## COMANDI PER GIT

### git config

Utilizzo: git config –global user.name “[name]”  

Utilizzo : git config –global user.email “[email address]”  

Questo comando imposta rispettivamente il nome dell’autore e l’indirizzo e-mail da utilizzare per i tuoi commit.<figure class="wp-block-image">
<img alt="Git Config Command - Git Commands - Edureka" decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/1-9.png"/> </figure>

### git init

Utilizzo: git init [repository name]

Questo comando viene utilizzato per avviare un nuovo repository (progetto).<figure class="wp-block-image">
<img alt="GitInit Command - Git Commands - Edureka" decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/2-6.png"/> </figure>

### git clone

Utilizzo: git clone [url]  

Questo comando viene utilizzato per clonare un repository da un URL esistente.<figure class="wp-block-image">
<img alt="Git Clone Command - Git Commands - Edureka" decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/4-4.png"/> </figure>

### git add

Utilizzo: git add [file]  

Questo comando aggiunge un file all’area di gestione temporanea.<figure class="wp-block-image">
<img alt="Git Add Command - Git Commands - Edureka" decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/5-4.png"/> </figure>

Utilizzo: git add *  

Questo comando aggiunge uno o più file all’area di gestione temporanea.<figure class="wp-block-image">
<img alt="Git Add Command - Git Commands - Edureka" decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/6-3.png"/> </figure>

### git commit

Utilizzo: git commit -m “[ Type in the commit message]”  

Questo comando registra o l’istantanea dei file in modo permanente nella cronologia delle versioni.<figure class="wp-block-image">
<img alt="Git Commit Command - Git Commands - Edureka" decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/7-3.png"/> </figure>

### git status

Utilizzo: git status  

Questo comando elenca tutti i file che devono essere committati.<figure class="wp-block-image">
<img alt="Git Status Command - Git Commands - Edureka" decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/15-1.png"/> </figure>

### git rm

Utilizzo: git rm [file]  

Questo comando cancella il file dalla directory di lavoro e mette in scena l’eliminazione.<figure class="wp-block-image">
<img alt="Git Rm Command - Git Commands - Edureka" decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/16-2.png"/> </figure>

### git log

Utilizzo : git log  

Questo comando viene utilizzato per elencare la cronologia delle versioni per il ramo corrente.<figure class="wp-block-image">
<img alt="Git Log Command - Git Commands - Edureka" decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/18.png"/> </figure>

### git branch

Utilizzo: git branch  

Questo comando elenca tutti i branch locali nel repository corrente.<figure class="wp-block-image">
<img alt="Git Branch Command - Git Commands - Edureka" decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/23.png"/> </figure>

Utilizzo : git branch [branch name]  

Questo comando crea un nuovo branch.<figure class="wp-block-image">
<img alt="Git Branch Command - Git Commands - Edureka" decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/24.png"/> </figure>

Utilizzo : git branch -d [branch name]  

Questo comando elimina il branch.<figure class="wp-block-image">
<img alt="Git Branch Command - Git Commands - Edureka" decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/25.png"/> </figure>

### git checkout

Utilizzo : git checkout [branch name]  

Questo comando viene utilizzato per passare da un branch all’altro.<figure class="wp-block-image">
<img alt="Git Checkout Command - Git Commands - Edureka" decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/27.png"/> </figure>

Utilizzo : git checkout -b [branch name]  

Questo comando crea un nuovo branch e passa anche a esso.<figure class="wp-block-image">
<img alt="Git Checkout Command - Git Commands - Edureka" decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/28.png"/> </figure>

### git merge

Utilizzo : git merge [branch name]  

Questo comando unisce la cronologia del branch specificato nel branch corrente.<figure class="wp-block-image">
<img alt="Git Merge Command - Git Commands - Edureka" decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/31-1.png"/> </figure>

### git remote

Utilizzo : git remote add \[variable name\] \[Remote Server Link\]  

Questo comando viene utilizzato per connettere il repository locale al server remoto.<figure class="wp-block-image">
<img alt="Git Remote Command - Git Commands - Edureka" decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/32.png"/> </figure>

### git push

Utilizzo : git push [variable name] master  

Questo comando invia le modifiche da locale al repository remoto.<figure class="wp-block-image">
<img alt="Git Push Command - Git Commands - Edureka" decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/33.png"/> </figure>

Utilizzo : git push \[variable name\] \[branch\]  

Questo comando invia i commit dei branch al repository remoto.<figure class="wp-block-image">
<img alt="Git Push Command - Git Commands - Edureka" decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/34.png"/> </figure>

Utilizzo : git push –all [variable name]  

Questo comando invia tutti i branch al repository remoto.<figure class="wp-block-image">
<img alt="Git Push Command - Git Commands - Edureka" decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/36.png"/> </figure>

Utilizzo : git push [variable name] :[branch name]  

Questo comando elimina un branch sul repository remoto.<figure class="wp-block-image">
<img alt="Git Push Command - Git Commands - Edureka" decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/37.png"/> </figure>

### git pull

Utilizzo : git pull [Repository Link]  

Questo comando recupera e unisce le modifiche sul server remoto alla directory di lavoro.<figure class="wp-block-image">
<img alt="Git Pull Command - Git Commands - Edureka" decoding="async" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2018/07/38.png"/> </figure>

###  

 [1]: /che-cose-git/