---
title: Rimuovere Virus da WordPress
author: Alberto
type: post
date: 2019-09-01T10:35:00+00:00
url: /rimuovere-virus-da-wordpress/
nectar_blog_post_view_count:
  - 38
tags:
  - Guide
  - WordPress Tricks

---
WordPress è una delle piattaforme&nbsp;**più utilizzate la mondo**&nbsp;per la&nbsp;**creazione di siti web ma a volte può essere facile imbattersi in un virus, ma come si possono rimuovere?**

WordPRess permette a chiunque di&nbsp;**tirar su un sito internet**&nbsp;funzionante**&nbsp;in pochissimo tempo**&nbsp;e con&nbsp;**costi molto bassi.**

Questo però significa anche avere&nbsp;**moltissimi siti web creati da estranei ai lavori&nbsp;**che installato temi e plugin&nbsp;_a caso_&nbsp;senza sapere realmente cosa stanno facendo… Finché il sito è piccolino e con un numero esigui di utenti non c’è problema, quando invece raggiunge una audience più alta allora**&nbsp;la probabilità di essere bersagliati da qualche hacker diventa elevata.**

Si stima che almeno&nbsp;**il 30% dei siti web in WordPress abbia delle vulnerabilità.**&nbsp;Se pensiamo che&nbsp;**più di 75 milioni di siti web utilizzano questa piattaforma**&nbsp;allora le vulnerabilità sono moltissime.

Vedremo ora come**&nbsp;mantenere al sicuro il proprio sito WordPress e come eliminare eventuali virus.**

## Mettere in sicurezza WordPress {.wp-block-heading}

WordPress utilizza un sistema molto intelligente di&nbsp;**temi e plugin**, ma occorre&nbsp;**fare attenzione a ciò che si installa.**

Esistono alcune&nbsp;**regole fondamentali:**

  * **Controllo sulla provenienza di temi e plugin**
  * **Installare il minor numero di plugin possibili**
  * **Avere un buon hosting**

### 1. Controllo sulla provenienza di temi e plugin {.wp-block-heading}

Ogni volta che si installa qualcosa su un sito in WordPress si va ad inserire del codice sul proprio progetto. Questo codice se ben scritto porterà funzionalità utili e migliorerà il sito, se invece è scritto male o contiene&nbsp;**bug**&nbsp;può causare molti problemi.

Quando si installa qualcosa su WordPress bisogna fare&nbsp;**molta molta attenzione alla fonte.**

**MAI**&nbsp;installare plugin o temi scaricati da&nbsp;**fonti non chiare.**

La cosa migliore è attenersi alla&nbsp;**repository ufficiale di WordPress**&nbsp;oppure ai grandi store garantiti.

### 2. Installare il minor numero di plugin possibili {.wp-block-heading}

Esistono plugin per ogni cosa ormai, ma&nbsp;**ogni plugin è un oggetto in più da gestire e mantenere.**

Avere plugin specifici per funzionalità pressoché inutili rischia di portarci&nbsp;**falle nel sistema**, oltre che appesantire inutilmente il sito.

Installare 20 plugin gestiti da sviluppatori diversi aumenta notevolmente il rischio di attacchi. Se uno di questi sviluppatori non corregge un bug oppure viene scoperta una falla, allora è a rischio l’intero sito.

**_Il trucco è questo: “Pochi ma buoni”._**

### 3. Avere un buon hosting {.wp-block-heading}

Parliamo di hosting e non di server perché la stragrande maggioranza dei siti web è ospitata su hosting condiviso.

Questi servizi sono&nbsp;**migliorati moltissimo&nbsp;**e offrono servizi che in passato erano disponibili solamente sui server dedicati, come accessi&nbsp;**SSH**,&nbsp;**cache**&nbsp;e&nbsp;**sicurezza**.

Poter contare su un buon servizio è molto importante per&nbsp;**proteggersi dagli attacchi e gestirli**&nbsp;nel malaugurato caso in cui si venga infettati.

## Rimuovere un virus da un sito WordPress {.wp-block-heading}

**Non c’è un modo unico per rimuovere un virus,**&nbsp;perché questi agiscono in maniera molto diversa gli uni dagli altri.

Questo complica un pochino le cose… È difficile quindi spiegare come rimuovere un virus in un semplice articolo, ma cercherò di&nbsp;**indicare alcune vie per gestire il problema**

### 1. Cercare backup precedenti all’attacco {.wp-block-heading}

Se avete un buon hosting sicuramente avrete anche dei&nbsp;**backup giornalieri o almeno settimanali**. La prima cosa da fare è scaricarsi uno si questi backup e tenerlo da parte, per&nbsp;**avere una situazione “**_**pre-virus**_**“.**

Se il sito è&nbsp;**statico**, senza sezioni aggiornabili come blog o portfolio allora si può semplicemente ripristinare il backup alla versione pre-attacco e il gioco è fatto.

Se invece il sito ha subito&nbsp;**aggiornamenti**&nbsp;che non si vogliono perdere allora conviene tenersi una copia pre-virus per sicurezza e andare a cercare i file infetti.

### 2. Scansionare sito web con tool online {.wp-block-heading}

Esistono molti tool online in grado di analizzare il sito e individuare le criticità.

Si possono anche utilizzare alcuni plugin sviluppati per gestire la sicurezza, come&nbsp;**WordFence**&nbsp;o&nbsp;**Sucuri**&nbsp;e utilizzare il loro scan per analizzare tutti i file sul sito.

Questi non garantiscono un risultato ottimale al 100%, ma è comunque un buon punto di partenza.

Ecco una serie di link utili per effettuare le scansioni:

  * <https://wpsec.com/>
  * [https://sitecheck.sucuri.net/][1]
  * [https://hackertarget.com/wordpress-security-scan/][2]
  * [https://wprecon.com/][3]
  * <https://firstsiteguide.com/tools/free-fsg/wordpress-security-online-scanner/>

Se ve la cavate con la CLI potete anche utilizzare&nbsp;[WP Scan][4], il software per eccellenza per testare la sicurezza di un sito in WordPress.

### Disattivare Temi e Plugin {.wp-block-heading}

Per cercare di&nbsp;**isolare**&nbsp;il&nbsp;**virus**&nbsp;può essere utile procedere con la&nbsp;**disattivazione**&nbsp;di temi a plugin.

Se il sito senza plugin e con il tema di default di WordPress funziona allora si possono riattivare uno ad uno e capire dove si trova l’infezione.

### Copiare i file originali di temi e plugin {.wp-block-heading}

**ATTENZIONE!!!**&nbsp;Fai molta attenzione nel mettere in pratica questo punto, se non sei esperto potresti fare più danni di quelli già presenti!Se un tema o un plugin è stato infettato una soluzione per rimuovere il virus dal sito WordPress è quella di&nbsp;**sovrascrivere le cartelle contenenti il tema e i plugin**&nbsp;con le versioni scaricate dalle fonti ufficiali.

In questo caso se il virus era presente nella cartella verrà sovrascritto.

### Analizzare struttura WordPress {.wp-block-heading}

In ultima battuta si può**&nbsp;analizzare la struttura di file e cartelle di WordPress**&nbsp;per controllare che non ci siano file strani, non presenti nell’installazione originale.

Se si trovano file&nbsp;**strani**&nbsp;allora bisogna cancellarli, sempre prestando molta attenzione a ciò che si sta facendo.

## **Conclusione** {.wp-block-heading}

Questi sono alcuni passaggi&nbsp;**generici**&nbsp;da effettuare per controllare lo stato di un sito web.

Purtroppo&nbsp;**ogni virus è differente**, alcuni agiscono sul database, altri direttaemnte nei file di sistema, altri ancora in modi che non ci immaginiamo nemmeno.

In questo articolo ho provato a darti&nbsp;**alcuni consigli di base&nbsp;**da mettere in pratica per provare a rimuovere un virus da un&nbsp;**sito in WordPress.**

Se nessuno di questi ha funzionato ti consiglio di&nbsp;**rivolgerti ad un professionista.**

Se&nbsp;**hai un sito web hackerato e vuoi una consulenza o un intervento professionale&nbsp;**volto alla rimozione e alla messa in sicurezza del suo sito contattami tramite la pagina&nbsp;[contatti][5]

 [1]: https://sitecheck.sucuri.net/%E2%80%A8
 [2]: https://hackertarget.com/wordpress-security-scan/%E2%80%A8
 [3]: https://wprecon.com/%E2%80%A8
 [4]: https://wpscan.org/
 [5]: https://albertoreineri.it/contatti