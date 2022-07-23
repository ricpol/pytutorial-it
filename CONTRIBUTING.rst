Contribuire a questo progetto.
==============================

Se stai leggendo questo file, prima di tutto **grazie di cuore**: già solo 
per il fatto di considerare la possibilità di contribuire sei più generoso 
del novantanove virgola nove... nove... nove... ;-)

Errori, orrori e peccati in genere.
-----------------------------------

Se noti un errore di qualsiasi tipo, per cortesia *segnalalo*. Non esiste un 
errore abbastanza piccolo da essere trascurabile: inceppi tipografici, 
virgole fuori posto, qualsiasi cosa. A maggior ragione, se noti qualcosa di 
grave come un termine mal tradotto, una frase resa in modo fuorviante, una 
distrazione, una cantonata... 

Il modo migliore di segnalare un errore è aprire una "issue" nuova. Questo 
può essere fatto direttamente dall'interfaccia web di GitHub: semplicemente 
clicca sulla *tab* "Issues" e poi sul pulsante verde "New Issue". 

Nella segnalazione dovresti indicare: 

* la **versione** (o le versioni) della documentazione in cui hai visto 
  l'errore: quella per Python 3.7, 3.8, 3.9, 3.10, 3.11 o "latest";

* il numero del capitolo e paragrafo;

* la frase incriminata e il problema. 

Contribuire alla traduzione.
----------------------------

Per fortuna questo progetto di traduzione non è complicato da aggiornare. Le 
modifiche nei file originali del tutorial sono piuttosto rare e quasi sempre 
di modesta entità. 

Tuttavia è possibile che, in futuro, io possa distrarmi o essere occupato in 
altre faccende e che quindi la traduzione resti indietro. Inoltre restano 
comunque dei punti in sospeso: per esempio, 

* sarebbe molto bello tradurre anche qualche documento ulteriore, oltre al 
  tutorial: per esempio sono molto tentato dagli 
  `HowTo <https://docs.python.org/3/howto/index.html>`_ (almeno alcuni) o 
  dalle `FAQ <https://docs.python.org/3/faq/index.html>`_ e anche dal 
  `Python Setup and Usage <https://docs.python.org/3/using/index.html>`_.

* negli esempi del tutorial ho tradotto solo i commenti e le stringhe più 
  utili alla comprensione. Per completezza, tuttavia, sarebbe preferibile 
  avere *tutte* le stringhe degli esempi tradotte. 

* varie ed eventuali: sono aperto a suggerimenti (apri una "issue" se hai 
  un'idea...)

Che cosa serve per contribuire.
-------------------------------

Purtroppo per contribuire al progetto occorre avere una discreta conoscenza 
degli strumenti di lavoro: 

* Git e GitHub, 

* ReStructuredText e Sphinx. 

Per prepararsi al lavoro occorre:

* clonare la repository; 

* installare Sphinx (versione 3 o superiore) con Pip.

Come funziona questa traduzione.
--------------------------------

Le traduzioni sono fatte direttamente sui file ``.rst`` della repository 
originale di Python. Ogni volta che viene fatto un *commit* nell'originale, 
dovrebbe essere fatto anche  un *commit* per aggiornare la traduzione (a meno 
che, come capita spesso, la modifica non sia solo una questione di ortografia 
nell'originale). 

In particolare, ci sono (attualmente) quattro versioni della traduzione, che 
corrispondono ad altrettanti *branch* sia in questo progetto sia ovviamente 
nella repository originale: 

* la versione "legacy" per Python 3.7: l'elenco di *commit* su questo *branch* 
  può essere visto 
  `qui <https://github.com/python/cpython/commits/3.7/Doc/tutorial>`_;

* la versione "legacy" per Python 3.8: l'elenco dei *commit* relativi si trova 
  `qui <https://github.com/python/cpython/commits/3.8/Doc/tutorial>`_;

* la versione "stabile" per Python 3.9: l'elenco dei *commit* 
  relativi è 
  `questo <https://github.com/python/cpython/commits/3.9/Doc/tutorial>`_;

* la versione "stabile" per Python 3.10: l'elenco dei *commit* 
  relativi è 
  `questo <https://github.com/python/cpython/commits/3.10/Doc/tutorial>`_;

* la versione "in sviluppo" per Python 3.11: l'elenco dei *commit* 
  relativi è 
  `questo <https://github.com/python/cpython/commits/3.11/Doc/tutorial>`_;

* la versione "in sviluppo" per Python 3.12 è semplicemente il *main branch* e può essere seguito 
  `qui <https://github.com/python/cpython/commits/main/Doc/tutorial>`_. 

Naturalmente i *branch* più vecchi sono aggiornati sempre più sporadicamente, 
mentre il *main* può ricevere più attenzione, specialmente in prossimità di 
una nuova release. 

Ciascuna versione della traduzione riporta esattamente la data e il nome del 
*commit* con cui è attualmente sincronizzata. Questa informazione si può 
trovare all'inizio del file ``appetite.rst`` ("Per stuzzicare l'appetito"), 
nel box iniziale "Nota alla traduzione italiana", per esempio 
`così <https://pytutorial-it.readthedocs.io/it/python3.8/appetite.html>`_.

Come fare un aggiornamento.
---------------------------

Se trovi uno o più nuovi *commit* nell'originale che non sono ancora stati 
sincronizzati (tradotti), questa è la procedura da seguire: 

* per **prima cosa**, apri una "issue" per dire che vuoi occuparti di questo 
  pezzo di traduzione. Se non lo fai, rischi che qualcun altro (io!) faccia 
  lo stesso lavoro nel frattempo;
  
* controlla il *diff* del *commit* originale (puoi farlo nell'interfaccia web 
  di GitHub) per scoprire che cosa è cambiato esattamente; 

* nella tua repository locale clonata, apri un nuovo *topic branch* a partire 
  dal *branch* corrispondente alla versione che ha subito modifiche, per es.: 

  .. code-block:: bash

    $ git checkout python3.9
    $ git pull
    $ git checkout -b syncXXXXXX

  dove "XXXXXX" è il nome del *commit* nell'originale che intendi tradurre; 

* in questo *topic branch*, fai le modifiche necessarie per la traduzione;

* ricordati *sempre* di modificare anche ``appetite.rst`` per riportare la 
  data e il nome del *commit* originale che hai sincronizzato; 

* produci l'output di Sphinx (per es. ``make html``) per essere sicuro che 
  le tue modifiche siano corrette nella visualizzazione; controlla bene 
  l'ortografia etc.; 
  
* fai *commit* delle tue modifiche: ricorda, *un solo* commit per ciascuna 
  sincronizzazione. Il messaggio di *commit* **deve** essere così:

  .. code-block:: bash

    $ git commit -am "sync with commit XXXXXX"

  dove, di nuovo "XXXXXX" è il nome del *commit* originale che hai 
  appena sincronizzato;

* se devi sincronizzare più di un *commit*, fai sempre una modifica alla 
  volta, non fare un solo commit per tutto quanto. In questo modo nel log 
  di Git resterà traccia di ogni singola sincronizzazione; 

* quando hai finito, fai un ``git push`` del tuo *topic branch* per 
  pubblicarlo sulla tua repository clonata su GitHub;

* infine, non ti resta che aprire una *pull request*. Commenta la 
  *pull request* con le informazioni che ritieni necessarie; è importante 
  che tu menzioni sempre anche il numero della "issue" da cui sei partito, 
  in modo che GitHub faccia in automatico il collegamento necessario. 
  Non dimenticare di mettere il tuo nome e cognome per esteso per essere 
  inserito nella lista dei *contributors*. 

Come tradurre.
^^^^^^^^^^^^^^

Traduci in Italiano chiaro e piano per quanto possibile. 

Cerca di rispettare la terminologia già utilizzata nella traduzione. Alcune 
cose, lo ammetto, sono dei capricci personali ma **devi rispettarli** 
ugualmente (non perché ho ragione io, ma solo per uniformità). Per esempio, 
non troverai mai "sollevare un'eccezione" ma sempre "emettere". Non troverai 
mai e poi mai "lo scopo di una variabile", ma sempre "lo *scope*". E così via.

Non rompere mai i link (``:ref:`` etc.) che trovi nell'originale! Se hai dei 
dubbi, guarda come sono resi dei link simili in altri punti della traduzione. 

Lascia sempre *inalterate* queste cose:

* le note e i metadati (``.. blabla``, ``.. index::``, ``.. sectionauthor::`` 
  e così via);

* tutti i titoli (devi tradurli, certo: ma non aggiungerne e non toglierne);

* tutti gli esempi di codice (devono restare identici). 

In particolare, negli esempi di codice: 

* lascia sempre il codice (nomi di variabili etc.) inalterato;

* traduci sempre commenti e docstring;

* traduci le altre eventuali stringhe *solo* se sono importanti a chiarire 
  l'esempio; se sono solo "di colore", non tradurle. 

Solo se traduci una intera sezione nuova (capita raramente...), allora puoi 
aggiungere il tuo nome direttamente nel testo: immediatamente prima della 
nuova sezione, aggiungi una nota così ``.. traduttore: Tizio Caio``. In ogni 
caso i nomi di *tutti* i collaboratori saranno ricordati in 
``CONTRIBUTORS.txt``.

Grazie.
=======

Non riesco a credere che tu sia arrivato a leggere fin qui. 

Davvero, grazie di tutto il contributo che vorrai dare. 
