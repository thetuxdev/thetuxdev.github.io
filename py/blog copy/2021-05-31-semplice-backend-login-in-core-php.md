---
title: Semplice Backend Login in Core PHP
author: Alberto
type: post
date: 2021-05-31T18:00:00+00:00
url: /semplice-backend-login-in-core-php/
nectar_blog_post_view_count:
  - 73
tags:
  - Guide
  - PHP

---
<p class="has-vivid-red-color has-text-color">
  <em>Ho effettuato un nuovo commit a questo progetto, aggiornandolo a PDO, inserendo i bindparam per aumentare la sicurezza e variando leggermente l’architettura software. Il codice aggiornato è nella repository github indicata nell’articolo.</em>
</p>

È vero, oggi esistono una&nbsp;**miriade di CMS e framework**&nbsp;in giro già belli che pronti, basta installarli e voilà! Il gioco è fatto!

Tutti hanno un sistema di login per poter accedere ad un’area riservata!

Però io sono sempre stato uno di quelli che non si accontentano della&nbsp;_pappa pronta_&nbsp;ma vogliono&nbsp;_**imparare**&nbsp;a cucinare_.

Per questo ho deciso di&nbsp;**creare un CMS tutto mio**, partendo da zero e utilizzando solamente HTML, CSS, JS e PHP.

Una delle prime cose che ho dovuto realizzare con il mio CMS è stato proprio un&nbsp;**sistema di login**&nbsp;per accedere all’area riservata.

## Sistema di login in core PHP

Ho deciso ora di rendere&nbsp;**open source&nbsp;**un piccolo sistema di accesso ad un’area riservata.

Puoi trovare il codice sorgente di questo progettino sul&nbsp;<a href="https://github.com/alby-dev" target="_blank" rel="noreferrer noopener">mio profilo github&nbsp;</a>a questo indirizzo:&nbsp;[ht][1]<a href="https://github.com/alby-dev/Simple-login-and-registration-in-php" target="_blank" rel="noreferrer noopener">tps://github.com/alby-dev/Simple-login-and-registration-in-php</a>

Tralasciamo sistemi di routing e architettura software e&nbsp;**facciamola semplice,**&nbsp;parliamo solo del login nudo e crudo.

### Area riservata

Innanzitutto ho creato una cartella “**login**“, dentro la quale ci saranno i file dell’area riservata.

Se non ho ancora effettuato l’accesso allora vedrò il&nbsp;**form di login.**<figure class="wp-block-image">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2020/04/image.png" alt="" /> </figure>

Nella&nbsp;**index.php**&nbsp;nella cartella login ho quindi inserito il&nbsp;**form**&nbsp;per effettuale l’accesso all’area riservata, con il form che rimanda al file&nbsp;**access.php,**&nbsp;contenente le funzioni di controllo dei dati di accesso.

<pre class="wp-block-code"><code>      &lt;!-- Login form --&gt;
      &lt;form class="" action="access.php" method="POST"&gt;
        &lt;!-- Action --&gt;
        &lt;input type="hidden" name="action" value="login"&gt;
        &lt;!-- Email or Username --&gt;
        &lt;label for="email"&gt;Email or Username&lt;/label&gt;
        &lt;input autofocus name="email" type="text"&gt;
        &lt;!-- Password --&gt;
        &lt;label for="password"&gt;Password&lt;/label&gt;
        &lt;input name="password" id="password" placeholder="" type="password"&gt;
        &lt;!-- Login Button --&gt;
        &lt;button type="submit"&gt;Login&lt;/button&gt;
      &lt;/form&gt;
      &lt;!-- /Login form --&gt;</code></pre>

**Access.php**&nbsp;si occupa sia del&nbsp;**login**&nbsp;che della&nbsp;**registrazione**&nbsp;dei nuovi utenti. È un file che continene solo PHP, esegue i controlli e poi rimanda alla pagina corretta, in base al tipo di richiesta.

Se ho inserito i dati corretti allora rimanda nel&nbsp;**backend**.

Invece se ho inserito i dati sbagliati mi rimanda al form di login con messaggio di&nbsp;**errore**.

Se sto&nbsp;**creando un nuovo utente segue la prassi della registrazione**, inviando un’email di conferma con un link cliccando sul quale si confermerà il proprio account.<figure class="wp-block-image">

<img decoding="async" src="https://albertoreineri.it/wp-content/uploads/2020/04/image-1.png" alt="" /> </figure>

**access.php**

<pre class="wp-block-code"><code>&lt;?php
//Config File
include("config.php");

//Control Action
if ($_POST&#91;'action'] == "login") {
    /*------------------------------------------------------
                        LOGIN
    -------------------------------------------------------*/
    ///$_Post variables
    $email = $_POST&#91;'email'];
    $password = $_POST&#91;'password'];


    //Query
    $sql = "SELECT * FROM users WHERE email = '" . $email . "' OR username ='" . $email . "'";
    $result = $conn-&gt;query($sql);
    if ($result-&gt;num_rows &gt; 0) {
        while ($row = $result-&gt;fetch_assoc()) {

            //Password control
            if (!(password_verify($password, $row&#91;"password"]))) {
                header("location: error.php?error=Wrong Password");
                die();
            }

            //Start Session
            session_start();

            //Save user id in session
            $_SESSION&#91;'id'] = $row&#91;"id"];

            //Redirect to backend homepage
            header("location: welcome.php");
            die();
        }
    } else {
        header("location: error.php?error=Wrong Email or Username");
        die();
    }
} elseif ($_POST&#91;'action'] == "register") {
     /*------------------------------------------------------
                        REGISTER
    -------------------------------------------------------*/
    $email = $_POST&#91;'email'];
    $username = $_POST&#91;'username'];
    $password = $_POST&#91;'password'];

    //Control if the user or email are already in the database
    $sql = "SELECT * FROM users WHERE email = '" . $email . "' OR username = '" . $username . "'";
    $result = $conn-&gt;query($sql);
    if ($result-&gt;num_rows &gt; 0) {
        while ($row = $result-&gt;fetch_assoc()) {
            header("location: error.php?error=Email or Username already register!");
        }
    }


    //Insert new user in DB
    $password = password_hash($password, PASSWORD_DEFAULT);
    $sql = "INSERT INTO users (username,email,password)
    VALUES (
    '" . $username . "',
    '" . $email . "',
    '" . $password . "'
    )";
    if ($conn-&gt;query($sql) === TRUE) {
        header("location: index.php");
    } else {
        header("location: error.php?error=" . $conn-&gt;error);
    }
}
$conn-&gt;close();</code></pre>

### Database

Il database è un MySQL molto semplice, con una tabella “**users**” contenente i dati dell’utente e la&nbsp;**password criptata.**

Per&nbsp;**bloccare gli utenti non loggati&nbsp;**e consentire l’accesso solamente ai loggati è possibile utilizzare le variabili&nbsp;**session**, da includere in ogni file del backend. In questo modo l’accesso viene consentito solamente a chi è passato tramite il form di login. Questo passaggio non è presente su github ma è molto semplice da integrare, forse lo aggiungerò quando avrò tempo!

Spero possa essere stato&nbsp;**utile**&nbsp;e&nbsp;**interessante**.

Se vuoi&nbsp;**utilizzare**&nbsp;questo form o provarelo e&nbsp;**migliorarlo**&nbsp;segui le&nbsp;**istruzioni**&nbsp;nel file readme.txt presente su github.

_Buon codice!_

 [1]: https://github.com/alby-dev/Simple-login-and-registration-in-php