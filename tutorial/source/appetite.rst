.. _tut-intro:

**************************
Per stuzzicare l'appetito.
**************************

Se lavorate molto al computer, prima o poi vi troverete davanti a un compito che vi piacerebbe automatizzare. Per esempio, fare un trova-e-sostituisci su molti file contemporaneamente, o rinominare e riordinare un gruppo di foto secondo una regola complicata. Magari vi piacerebbe creare un piccolo database personale, o un'applicazione grafica per uno scopo specifico, o un semplice gioco. 

Se siete un programmatore professionista, forse dovete lavorare con diverse librerie C, C++ o Java, ma il consueto ciclo di scrivere, compilare, testare, ricompilare vi sembra troppo lento. Forse state scrivendo una *suite* di test per una libreria di questo tipo e pensate che scrivere il codice dei test sia un compito noioso. O forse avete scritto un programma che potrebbe aver bisogno di un linguaggio interno per le estensioni, ma non avete voglia di progettarne e implementarne uno da zero per la vostra applicazione. 

Allora Python è proprio il linguaggio che fa per voi.

Per alcuni di questi compiti potrebbe bastare uno script della shell di Unix o un *batch file* di Windows: gli script però vanno bene per spostare i file e modificare i dati testuali, non sono adatti alle applicazioni grafiche o ai giochi. Potreste scrivere un programma in C, C++ o Java, ma questo richiederebbe molto tempo di sviluppo anche solo per arrivare a una prima bozza. Python è più semplice, è disponibile su Windows, Mac OS X e Unix, e vi aiuterà a finire il lavoro più in fretta.  

Python è semplice da usare, ma è un linguaggio di programmazione serio che offre molta più struttura e supporto per programmi di grandi dimensioni, rispetto a uno script della shell o un batch file. D'altra parte, Python ha anche molta più gestione delle eccezioni di C; essendo poi un linguaggio *particolarmente* "di alto livello", include tipi di dati di alto livello, con la flessibilità delle sue liste e dizionari. Grazie alle sue strutture-dati più astratte, Python si può usare in campi applicativi molto più vasti rispetto ad Awk o anche a Perl, pur mantenendo la stessa semplicità d'uso di questi linguaggi. 

Python vi consente di dividere il vostro programma in moduli che possono essere riutilizzati in altri programmi. Include già una vasta collezione di moduli standard, che potete usare come base per il vostro lavoro, o come esempi per imparare la programmazione in Python. Questi moduli, tra l'altro, offrono soluzioni per l'input/output dei file, le chiamate di sistema, i socket e perfino interfacce per *toolkit* grafici come Tk. 

Python è un linguaggio interpretato, cosa che fa risparmiare molto tempo durante lo sviluppo, perché non c'è bisogno di compilare e collegare nulla. L'interprete può essere usato in modalità interattiva ed è quindi facile sperimentare con le funzionalità del linguaggio, scrivere programmi usa-e-getta, testare i costrutti durante lo sviluppo *bottom-up*. Può essere anche una pratica calcolatrice da tenere sottomano. 

Python vi consente di scrivere codice compatto e leggibile. I programmi scritti in Python sono in genere molto più corti degli equivalenti in C, C++ o Java, per diverse ragioni:

* i tipi di dato di alto livello vi permettono di codificare operazioni complesse in una singola istruzione;

* il raggruppamento delle istruzioni avviene rientrando il codice, invece di racchiuderlo tra parentesi;

* non c'è bisogno di dichiarare le variabili. 

Python è *estensibile*: se conoscete il C, è facile aggiungere all'interprete una nuova funzione predefinita o un modulo, sia per aumentare la velocità di esecuzione in punti critici del codice, sia per collegare un programma Python a librerie disponibili solo in forma binaria (per esempio, librerie grafiche di terze parti). Una volta che siete diventati esperti, potete collegare l'interprete Python all'interno di un programma scritto in C e usarlo come un'estensione, o un linguaggio interno di quel programma. 

A proposito, il nome del linguaggio deriva dallo show della BBC "Monty Python's Flying Circus" e non ha niente a che vedere con i rettili. Ogni riferimento agli sketch dei Monty Python nella documentazione è non solo permesso ma anzi incoraggiato. 

Adesso che siete incuriositi da Python, avrete voglia di esaminarlo più nel dettaglio. Siccome il miglior modo di imparare un linguaggio è usarlo, vi invitiamo a sperimentare con l'interprete man mano che leggete il tutorial. 

Dedichiamo il prossimo capitolo a spiegare il meccanismo di funzionamento dell'interprete. Si tratta di concetti piuttosto semplici, ma sono importanti per consentirvi di provare gli esempi che verranno presentato più in là. 

I capitoli successivi descrivono e dimostrano diverse funzionalità di Python e del suo ambiente, a cominciare da semplici espressioni, istruzioni e tipi di dati, proseguendo poi con le funzioni e i moduli, fino ad accennare agli argomenti più avanzati come le eccezioni e la creazione di classi personalizzate. 
