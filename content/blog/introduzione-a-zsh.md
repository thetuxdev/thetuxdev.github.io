---
title: Introduzione a Zsh e Oh My Zsh - Migliorare il Terminale Linux
author: Alberto
type: post
date: 2024-05-19T08:26:00+00:00
tags:
  - Guide
  - Linux
---

Benvenuti alla guida alla configurazione e utilizzo di Zsh e Oh My Zsh per ottimizzare la vostra esperienza con il terminale! Navigare efficacemente attraverso il sistema operativo e eseguire operazioni complesse può diventare molto più semplice e piacevole con l'aiuto di questi tool.

### Cos'è Zsh e perché dovresti usarlo?

Zsh, acronimo di "Z shell", è una shell avanzata per i sistemi Unix-like, che offre una vasta gamma di funzionalità rispetto alla shell predefinita del vostro sistema. Con una sintassi intuitiva, un potente sistema di completamento automatico e una ricca collezione di plugin, Zsh è diventata la scelta preferita per molti sviluppatori e amministratori di sistema.

### Oh My Zsh: semplificare la gestione di Zsh

Oh My Zsh è un framework open-source che semplifica la configurazione e l'utilizzo di Zsh. Con una vasta selezione di temi preconfigurati, plugin e strumenti di personalizzazione, Oh My Zsh rende facile adattare Zsh alle vostre esigenze specifiche. Che si tratti di migliorare la produttività con il completamento automatico dei comandi o di aggiungere funzionalità avanzate con plugin personalizzati, Oh My Zsh offre tutto il necessario per rendere Zsh la vostra shell definitiva.

In questa guida, esploreremo insieme come installare, configurare e utilizzare Zsh e Oh My Zsh per sfruttare al meglio il vostro terminale. Dalle basi della configurazione iniziale ai trucchi avanzati per ottimizzare la vostra produttività, sarete guidati passo dopo passo attraverso tutto ciò che c'è da sapere per diventare dei veri esperti di Zsh.

Se siete pronti a dare una svolta alla vostra esperienza con il terminale, allora accomodatevi e preparatevi ad esplorare il meraviglioso mondo di Zsh e Oh My Zsh!

## 1. Installazione

Prima di poter godere dei vantaggi di Zsh e Oh My Zsh, è necessario installarli correttamente sul vostro sistema. Fortunatamente, l'installazione è un processo relativamente semplice e può essere completata in pochi passaggi.

### Installazione di Zsh

Se Zsh non è già presente sul vostro sistema, è possibile installarlo utilizzando il gestore di pacchetti appropriato per il vostro sistema operativo.

- **Linux (Ubuntu/Debian)**:

  Utilizzando apt:

  ```bash
  sudo apt-get install zsh
  ```
- **macOS**:

  Utilizzando Homebrew:

  ```bash
  brew install zsh
  ```
- **Altre distribuzioni Linux**:

  Utilizzate il gestore di pacchetti della vostra distribuzione, come yum o pacman, per installare Zsh.

### Installazione di Oh My Zsh

Oh My Zsh può essere installato tramite il terminale utilizzando uno dei seguenti comandi:

- **Utilizzando curl**:

  ```bash
  sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
  ```
- **Utilizzando wget**:

  ```bash
  sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
  ```

Una volta completata l'installazione, il terminale vi chiederà se desiderate impostare Zsh come shell predefinita. Accettate questa opzione per continuare con la configurazione di Zsh e Oh My Zsh.

Ora che Zsh e Oh My Zsh sono installati sul vostro sistema, potete procedere con la configurazione e l'utilizzo per personalizzare la vostra esperienza con il terminale.

## 2. Configurazione Iniziale

Una volta completata l'installazione di Zsh e Oh My Zsh, è il momento di configurare la vostra shell per adattarla alle vostre preferenze e esigenze specifiche. Questa sezione vi guiderà attraverso i passaggi necessari per eseguire una configurazione iniziale di base.

### Selezione di un Tema

Oh My Zsh offre una vasta gamma di temi che modificano l'aspetto del vostro terminale. Per selezionare un tema, modificate la variabile `ZSH_THEME` nel vostro file di configurazione Zsh, di solito situato in `~/.zshrc`. Ecco come farlo:

```bash
ZSH_THEME="nome_del_tema"
```

Sostituite `"nome_del_tema"` con il nome del tema che desiderate utilizzare. Alcuni temi popolari includono "agnoster", "robbyrussell" e "powerlevel10k". Io per esempio uso [powerlevel10k](https://github.com/romkatv/powerlevel10k)

### Aggiunta di Plugin

I plugin di Oh My Zsh estendono le funzionalità della vostra shell aggiungendo nuove capacità e comandi. Per abilitare un plugin, aggiungetelo alla lista dei plugin nel vostro file di configurazione `~/.zshrc`. Ad esempio, per abilitare il plugin `git`, aggiungete `git` alla lista dei plugin come segue:

```bash
plugins=(git)
```

Potete elencare più plugin separandoli con spazi.

Ora che avete configurato il vostro tema e i plugin desiderati, salvate il file e chiudete il vostro editor di testo.

### Riavvio del Terminale

Per applicare le modifiche e far sì che Zsh e Oh My Zsh utilizzino la nuova configurazione, è necessario riavviare il terminale. Chiudete e riaprite il terminale, o eseguite il comando:

```bash
source ~/.zshrc
```

Una volta completati questi passaggi, la vostra shell Zsh dovrebbe essere configurata con il tema e i plugin che avete selezionato. Ora siete pronti per sfruttare appieno le potenzialità di Zsh e Oh My Zsh durante le vostre sessioni di lavoro al terminale.

## 3. I migliori Plugin di Oh My Zsh

I plugin di Oh My Zsh permettono di personalizzare e migliorare l'esperienza della shell Zsh. Essi possono migliorare sia l'aspetto della shell che la sua funzionalità. Tuttavia, cercando "Zsh plugin" su Internet, ci si imbatte in una vasta gamma di plugin disponibili.

Come scegliere quali plugin installare? Di seguito, vi mostrerò i 5 plugin essenziali di Zsh che vi renderanno più veloci nell'utilizzo della CLI.

### 1. Plugin Git

Il primo plugin è `git`, che viene pre-installato con Oh My Zsh. Fornisce utili alias (o scorciatoie) e alcune funzioni utili.

Ad esempio, invece di digitare lunghi comandi come `git push --set-upstream origin <branch>`, potete usare l'alias (scorciatoia) `gpsup`.

Digitare occasionalmente un lungo comando non è un problema. Tuttavia, come sviluppatori, interagiamo frequentemente con Git e spendiamo molto tempo a digitare comandi. Questo si accumula nel tempo, quindi perché non risparmiare qualche battitura?

Gli alias Git che uso più frequentemente sono:

- `ga` e `gaa` - alias per `git add` e `git add --all`
- `gco` e `gcb` - alias per `git checkout` e `git checkout -b`
- `gcmsg` - alias per `git commit --message`
- `gd` - alias per `git diff`
- `gl` - alias per `git pull`
- `gp` - alias per `git push`
- `gpsup` - alias per `git push --set-upstream origin $(git_current_branch)`
- `gst` - alias per `git status`

Potete vedere tutti gli alias disponibili [qui](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/git).

### 2. Plugin Zsh-autosuggestions

Probabilmente scrivete una considerevole quantità di comandi nel terminale e, molto spesso, ripetete molti di essi frequentemente.

Il plugin `zsh-autosuggestions` fornisce una funzionalità di autocompletamento. Suggerisce comandi basati sulla cronologia dei comandi precedenti e sui completamenti. Il completamento significa che offre suggerimenti basati su ciò che suggerirebbe il completamento con il tasto tab.

Per installare questo plugin con Oh My Zsh:

1. Clonate il repository del plugin nella cartella dei plugin di Zsh:
   ```bash
   git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
   ```
2. Aggiungete il plugin nel file `.zshrc`:
   ```bash
   plugins=(git zsh-autosuggestions)
   ```
3. Salvate il file e riavviate Zsh:
   ```bash
   source ~/.


### 3. Plugin Zsh-syntax-highlighting

Questo plugin fornisce l'evidenziazione della sintassi per i comandi che digitate nel terminale.

Senza questo plugin, l'intero comando ha lo stesso colore - bianco. Non solo sembra noioso, ma è anche più difficile individuare errori di battitura e altri errori.

Con l'evidenziazione della sintassi, il terminale ha un aspetto migliore e potete differenziare facilmente le diverse parti del comando.

Per installare questo plugin con Oh My Zsh:

1. Clonate il repository del plugin nella cartella dei plugin di Zsh:
   ```bash
   git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
   ```
2. Aggiungete il plugin nel file `.zshrc`:
   ```bash
   plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
   ```
3. Salvate il file e riavviate Zsh:
   ```bash
   source ~/.zshrc
   ```

### 4. Plugin You-should-use

È difficile ricordare tutti gli alias/scorciatoie dal plugin Git o quelli che avete impostato manualmente nel `.zshrc`. Ecco dove entra in gioco il plugin `you-should-use`.

Ogni volta che usate un comando che ha un alias, questo troverà la scorciatoia e la visualizzerà nel terminale. È utile e vi aiuta a memorizzare le scorciatoie.

Per installare questo plugin con Oh My Zsh:

1. Clonate il repository del plugin nella cartella dei plugin di Zsh:
   ```bash
   git clone https://github.com/MichaelAquilina/zsh-you-should-use.git $ZSH_CUSTOM/plugins/you-should-use
   ```
2. Aggiungete il plugin nel file `.zshrc`:
   ```bash
   plugins=(git zsh-autosuggestions zsh-syntax-highlighting you-should-use)
   ```
3. Salvate il file e riavviate Zsh:
   ```bash
   source ~/.zshrc
   ```

### 5. Plugin Zsh-bat

Se utilizzate frequentemente il comando `cat`, amerete questo plugin. L'output del comando `cat` è piuttosto semplice e può essere difficile da navigare.

Il plugin `zsh-bat` sostituisce il comando `cat` e vi offre un output migliore. Invece di usare il comando `cat`, userete `bat`, che restituisce un output con evidenziazione della sintassi e integrazione con Git.

Per installare questo plugin con Oh My Zsh:

1. Clonate il repository del plugin nella cartella dei plugin di Zsh:
   ```bash
   git clone https://github.com/fdellwing/zsh-bat.git $ZSH_CUSTOM/plugins/zsh-bat
   ```
2. Aggiungete il plugin nel file `.zshrc`:
   ```bash
   plugins=(git zsh-autosuggestions zsh-syntax-highlighting you-should-use zsh-bat)
   ```
3. Salvate il file e riavviate Zsh:
   ```bash
   source ~/.zshrc
   ```

**Nota importante**: per far funzionare questo plugin, dovete installare `bat` sulla vostra macchina.

Questi sono i 5 plugin che rendono la mia vita più facile e mi rendono più produttivo. Migliorano sia l'aspetto che la funzionalità della vostra shell Zsh. Continuate a sperimentare e trovare nuovi plugin per ottimizzare ulteriormente la vostra esperienza al terminale.

## Risorse Aggiuntive

Per ulteriori informazioni su comandi e funzionalità di Zsh e Oh My Zsh, consultate la documentazione ufficiale e le risorse online disponibili. Esplorare e sperimentare con le varie opzioni vi permetterà di scoprire nuovi modi per ottimizzare la vostra esperienza con il terminale.

Con questa conoscenza di base su come utilizzare Zsh e Oh My Zsh, siete pronti per iniziare a esplorare e sfruttare appieno le potenzialità di queste potenti tool durante le vostre sessioni al terminale. Continuate a praticare e ad esplorare per diventare sempre più esperti nell'utilizzo di Zsh e Oh My Zsh!

### Docs 
1. **Zsh Official Documentation**:
   - [Zsh Manual](http://zsh.sourceforge.net/Doc/Release/zsh_toc.html)

2. **Oh My Zsh Official Documentation**:
   - [Oh My Zsh GitHub Repository](https://github.com/ohmyzsh/ohmyzsh)
   - [Oh My Zsh Wiki](https://github.com/ohmyzsh/ohmyzsh/wiki)
