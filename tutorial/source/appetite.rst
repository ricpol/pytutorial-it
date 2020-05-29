
.. topic:: Nota per la traduzione italiana.

    Questa è una traduzione del `Tutorial ufficiale <https://docs.python.org/3/tutorial/index.html>`_ della documentazione di Python, mantenuta in sincrono con il testo della `repository GitHub <https://github.com/python/cpython/tree/master/Doc/tutorial>`_.

    Questa è la traduzione della **versione "di sviluppo" del Tutorial**, corrispondente al "master branch" della repository, ed è aggiornata al `28 maggio 2020 <https://github.com/python/cpython/commit/eaca2aa117d663acf8160a0b4543ee2c7006fcc7#diff-8f5d4d54eb7fab60cb04633e721f6328>`_.

    Gli esempi *non* sono tradotti, perché il codice dovrebbe sempre essere scritto in Inglese. Tuttavia i commenti all'interno del codice sono tradotti e così pure le stringhe, quando il loro contenuto è utile alla comprensione del tutorial.
    
    *(traduzione a cura di Riccardo Polignieri)*

.. il testo del topic che segue stava in index.rst, precedendo la toc. 
.. al builder html non da fastidio, ma il builder latex non riesce a concepirlo

.. topic:: Introduzione

    Python è un linguaggio di programmazione molto produttivo e semplice da imparare. È dotato di efficienti strutture-dati di alto livello e propone un approccio alla programmazione a oggetti semplice ma efficace. La sua sintassi elegante e la tipizzazione dinamica, oltre al fatto di essere un linguaggio interpretato, ne fanno uno strumento ideale per lo *scripting* e lo sviluppo rapido di applicazioni, in molti campi e su molte piattaforme. 

    L'interprete di Python e la sua vasta libreria standard sono disponibili sul sito web https://www.python.org/, sotto forma sia di codice sorgente sia di eseguibile binario, per tutte le piattaforme più diffuse, e possono essere liberamente redistribuiti. Il sito, inoltre, ospita direttamente o indirizza verso molti altri moduli Python, programmi e strumenti sviluppati da terze parti e documentazione aggiuntiva. 

    L'interprete Python si può estendere facilmente con nuove funzioni e tipi di dati implementati in C o C++ (o altri linguaggi interfacciabili con C). Python è inoltre adatto come linguaggio integrato per estendere e personalizzare altre applicazioni. 

    Questo tutorial introduce il lettore in modo informale ai concetti e alle funzioni di base del linguaggio e del suo ambiente. Può essere utile avere sotto mano un interprete Python per provare direttamente il codice, ma tutti gli esempi mostrano anche il loro output: è quindi possibile leggere il tutorial anche a sé stante. 

    Per una descrizione delle funzionalità e dei moduli, si veda la documentazione della :ref:`libreria standard<library-index>`. :ref:`La guida di riferimento del linguaggio<reference-index>` approfondisce in modo formale la struttura di Python. Per scrivere estensioni in C o C++ si può consultare la guida su come :ref:`estendere e incorporare Python <extending-index>` e il manuale delle :ref:`API C di Python<c-api-index>`. Ci sono poi molti libri dedicati all'approfondimento di Python.

    Questo tutorial non vuole essere una descrizione esauriente che copre ogni singola funzionalità, o anche solo quelle comuni. Piuttosto, è un'introduzione agli aspetti più notevoli di Python e può dare un'idea dello stile e del "gusto" del linguaggio. Dopo averlo letto, sarete in grado di leggere e scrivere moduli e programmi in Python, e sarete pronti ad approfondire i diversi moduli contenuti nella :ref:`libreria standard<library-index>`.

    Vale anche la pena di dare un'occhiata al :ref:`glossario<glossary>`.

.. _tut-intro:

**************************
Per stuzzicare l'appetito.
**************************

Se lavorate molto al computer, prima o poi vi troverete davanti a un compito che vi piacerebbe automatizzare. Per esempio, fare un trova-e-sostituisci su molti file contemporaneamente, o rinominare e riordinare un gruppo di foto secondo una regola complicata. Magari vi piacerebbe creare un piccolo database personale, o un'applicazione grafica per uno scopo specifico, o un semplice gioco. 

Se siete un programmatore professionista, forse dovete lavorare con diverse librerie C, C++ o Java, ma il consueto ciclo di scrivere, compilare, testare, ricompilare vi sembra troppo lento. Forse state scrivendo una *suite* di test per una libreria di questo tipo e pensate che scrivere il codice dei test sia un compito noioso. O forse avete scritto un programma che potrebbe aver bisogno di un linguaggio interno per le estensioni, ma non avete voglia di progettarne e implementarne uno da zero per la vostra applicazione. 

Allora Python è proprio il linguaggio che fa per voi.

Per alcuni di questi compiti potrebbe bastare uno script della shell di Unix o un *batch file* di Windows: gli script però vanno bene per spostare i file e modificare i dati testuali, non sono adatti alle applicazioni grafiche o ai giochi. Potreste scrivere un programma in C, C++ o Java, ma questo richiederebbe molto tempo di sviluppo anche solo per arrivare a una prima bozza. Python è più semplice, è disponibile su Windows, Mac OS X e Unix, e vi aiuterà a finire il lavoro più in fretta.  

Python è semplice da usare, ma è un linguaggio di programmazione serio che offre molta più struttura e supporto per programmi di grandi dimensioni, rispetto a uno script della shell o un batch file. D'altra parte, Python ha anche molta più gestione delle eccezioni rispetto a C; essendo poi un linguaggio *particolarmente* "di alto livello", include tipi di dati di alto livello e flessibili, come le sue liste e dizionari. Grazie alle sue strutture-dati più astratte, Python si può usare in campi applicativi molto più vasti rispetto ad Awk o anche a Perl, pur mantenendo la stessa semplicità d'uso di questi linguaggi. 

Python vi consente di dividere il vostro programma in moduli che possono essere riutilizzati in altri programmi. Include già una vasta collezione di moduli standard, che potete usare come base per il vostro lavoro, o come esempi per imparare la programmazione in Python. Questi moduli, tra l'altro, offrono soluzioni per l'input/output dei file, le chiamate di sistema, i socket e perfino interfacce per *toolkit* grafici come Tk. 

Python è un linguaggio interpretato, cosa che fa risparmiare molto tempo durante lo sviluppo, perché non c'è bisogno di compilare e collegare nulla. L'interprete può essere usato in modalità interattiva ed è quindi facile sperimentare con le funzionalità del linguaggio, scrivere programmi usa-e-getta, testare i costrutti durante lo sviluppo *bottom-up*. Può essere anche una pratica calcolatrice da tenere sottomano. 

Python vi consente di scrivere codice compatto e leggibile. I programmi scritti in Python sono in genere molto più corti degli equivalenti in C, C++ o Java, per diverse ragioni:

* i tipi di dato di alto livello vi permettono di codificare operazioni complesse in una singola istruzione;

* il raggruppamento delle istruzioni avviene rientrando il codice, invece di racchiuderlo tra parentesi;

* non c'è bisogno di dichiarare le variabili. 

Python è *estensibile*: se conoscete il C, è facile aggiungere all'interprete una nuova funzione predefinita o un modulo, sia per aumentare la velocità di esecuzione in punti critici del codice, sia per collegare un programma Python a librerie disponibili solo in forma binaria (per esempio, librerie grafiche di terze parti). Una volta che siete diventati esperti, potete collegare l'interprete Python all'interno di un programma scritto in C e usarlo come un'estensione, o un linguaggio interno di quel programma. 

A proposito, il nome del linguaggio deriva dallo show della BBC "Monty Python's Flying Circus" e non ha niente a che vedere con i rettili. Ogni riferimento agli sketch dei Monty Python nella documentazione è non solo permesso ma anzi incoraggiato. 

Adesso che siete incuriositi da Python, avrete voglia di esaminarlo più nel dettaglio. Siccome il miglior modo di imparare un linguaggio è usarlo, vi invitiamo a sperimentare con l'interprete man mano che leggete il tutorial. 

Dedichiamo il prossimo capitolo a spiegare il meccanismo di funzionamento dell'interprete. Si tratta di informazioni di servizio, ma sono importanti per consentirvi di provare gli esempi che verranno presentati più in là. 

I capitoli successivi descrivono e dimostrano diverse funzionalità di Python e del suo ambiente, a cominciare da semplici espressioni, istruzioni e tipi di dati, proseguendo poi con le funzioni e i moduli, fino ad accennare agli argomenti più avanzati come le eccezioni e la creazione di classi personalizzate. 
