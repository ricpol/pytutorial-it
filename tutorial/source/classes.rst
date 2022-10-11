.. _tut-classes:

******
Classi
******

Le classi servono a unire insieme dati e funzionalità. Creare una classe 
equivale a creare un nuovo *tipo*, a partire dal quale possono essere create 
nuove *istanze* (oggetti). Ciascuna istanza può avere degli attributi suoi 
propri, che ne *mantengono* lo stato. Le istanze possono anche avere dei 
metodi (definiti nella classe) che ne *modificano* lo stato. 

A differenza di altri linguaggi di programmazione, il meccanismo delle classi 
in Python aggiunge pochissima sintassi e semantica: è un misto delle classi 
che si possono trovare in C++ e in Modula-3. Le classi Python forniscono tutti 
gli strumenti standard della programmazione a oggetti (OOP): il meccanismo 
dell'ereditarietà consente di avere più di una classe-base, una sotto-classe 
può sovrascrivere i metodi della sua classe-madre, e un metodo può invocare il 
metodo della classe-madre con lo stesso nome. Gli oggetti possono contenere 
quanti dati si desidera. Proprio come i moduli, le classi partecipano della 
natura dinamica di Python: sono create a *runtime* e possono essere modificate 
ulteriormente dopo la loro creazione. 

Usando la terminologia di C++, di solito i membri di una classe (inclusi i 
dati) sono *pubblici* (a eccezione di quanto spiegato in :ref:`tut-private`) e 
tutte le funzioni interne sono *virtuali*. Come in Modula-3, non ci sono 
scorciatoie per referenziare i membri di un oggetto dall'interno dei suoi 
metodi: un metodo è chiamato con un primo argomento esplicito che rappresenta 
l'oggetto stesso, che è fornito implicitamente dalla chiamata. Le classi sono 
oggetti esse stesse, come in Smalltalk: questo permette la semantica per 
l'importazione e la rinomina. A differenza di C++ e Modula-3, i tipi 
predefiniti possono essere usati come classi-base che l'utente può estendere. 
Inoltre, come in C++, la maggior parte degli operatori predefiniti che godono 
di sintassi speciale (gli operatori aritmetici, l'indicizzazione, etc.) 
possono essere ridefiniti per le istanze delle classi. 

(Dal momento che non esiste una terminologia universale per le classi, 
utilizziamo occasionalmente il lessico di C++ e Smalltalk. Sarebbe preferibile 
usare il lessico di Modula-3 che, rispetto a C++, è più simile a Python per 
quel che riguarda gli oggetti: ma sospettiamo che pochi lettori abbiano 
familiarità con questo linguaggio.)

.. _tut-object:

A proposito di nomi e oggetti
=============================

Gli oggetti hanno una identità univoca e più di un nome (in più di uno 
*scope*) può essere collegato allo stesso oggetto: è ciò che in altri 
linguaggi si chiama *aliasing*. Questa caratteristica, a prima vista, non è 
sempre apprezzata in Python e può tranquillamente essere ignorata quando si 
gestiscono oggetti di tipo immutabile (numeri, stringhe, tuple). Tuttavia, lo 
*aliasing* può avere effetti imprevisti sulla semantica del codice Python che 
maneggia oggetti mutabili come liste, dizionari e la maggior parte degli altri 
tipi. Di solito questi effetti sono sfruttati positivamente dal programma, dal 
momento che lo *aliasing* è in qualche modo simile ai puntatori. Per esempio, 
passare un oggetto è più economico, dal momento che l'implementazione 
sottostante deve solo passare un puntatore; e se una funzione modifica un 
oggetto passato come argomento, il codice chiamante vedrà le modifiche: questo 
elimina la necessità di un doppio meccanismo di passaggio degli argomenti, 
come avviene in Pascal. 

.. _tut-scopes:

*Scope* e *namespace* in Python
===============================

Prima di affrontare le classi, dobbiamo parlare delle regole degli *scope* in 
Python. [#]_ Le classi manipolano i *namespace* in modo sottile ed è 
necessario sapere come funzionano *scope* e *namespace* per capire che cosa 
succede davvero. D'altra parte, la comprensione di questi argomenti è utile in 
qualsiasi applicazione avanzata di Python. 

Iniziamo con alcune definizioni.

Un *namespace* è una mappatura che collega nomi a oggetti. Di solito i 
*namespace* sono attualmente implementati come dizionari (per ragioni di 
performance), ma dall'esterno questo non si vede e potrebbe cambiare in 
futuro. Esempi di *namespace* sono l'insieme dei nomi predefiniti (che 
comprende funzioni come :func:`abs` e i nomi delle eccezioni predefinite); i 
nomi globali di un modulo; i nomi locali a una chiamata di funzione. In un 
certo senso, l'insieme degli attributi di un oggetto è anch'esso un 
*namespace*. La cosa fondamentale da capire sui *namespace* è che non c'è 
assolutamente nessuna relazione tra i nomi di diversi *namespace*. Per 
esempio, due moduli diversi potrebbero definire entrambi una funzione 
``maximize`` senza nessuna confusione: gli utenti dei due moduli devono 
riferirsi a questa funzione premettendo il nome del modulo. 

A proposito: usiamo il termine *attributo* per qualsiasi nome che segue un 
punto: per esempio, nell'espressione ``z.real``, ``real`` è un attributo 
dell'oggetto ``z``. Tecnicamente, un riferimento a un nome in un modulo è un 
riferimento a un *attributo* di quel modulo: nell'espressione 
``modname.funcname``, ``modname`` è un oggetto-modulo e ``funcname`` è un suo 
attributo. In questo caso c'è una corrispondenza ovvia tra gli attributi del 
modulo e i nomi globali definiti nel modulo: condividono lo stesso 
*namespace*! [#]_

Gli attributi possono essere di sola lettura o scrivibili: a questi ultimi è 
possibile assegnare dei valori. Gli attributi dei moduli sono scrivibili: 
potete scrivere ``modname.the_answer = 42``. Gli attributi scrivibili sono 
anche eliminabili con l'istruzione :keyword:`del`. Per esempio, 
``del modname.the_answer`` rimuoverà l'attributo :attr:`the_answer` 
dall'oggetto ``modname``.

I *namespace* sono creati in momenti diversi e hanno cicli di vita diversi. 
Il *namespace* che contiene i nomi predefiniti è creato dall'interprete Python 
all'avvio e non viene mai distrutto. Il *namespace* globale di un modulo è 
creato al momento della lettura delle definizioni del modulo; anche questi di 
solito durano fin quando l'interprete è in esecuzione. Le istruzioni eseguite 
all'invocazione dell'interprete, sia quelle che sono lette da un file *script* 
sia quelle eseguite in modalità interattiva, sono considerate parte di un 
modulo chiamato :mod:`__main__`, e quindi hanno un loro *namespace* globale. 
(I nomi predefiniti, in effetti, vivono anch'essi in un modulo: questo si 
chiama :mod:`builtins`.)

Il *namespace* locale di una funzione viene creato al momento di chiamare la 
funzione e distrutto quando la funzione restituisce il suo risultato o emette 
un'eccezione che non viene gestita all'interno della funzione. (In realtà, 
"dimenticato" è un termine più appropriato per descrivere quello che accade.) 
Naturalmente le invocazioni ricorsive hanno ciascuna il proprio *namespace*.

Uno *scope* è una regione di codice Python, all'interno del programma, dove il 
*namespace* è direttamente accessibile. Con "direttamente accessibile" 
intendiamo che un riferimento *non qualificato* (senza ricorrere alla notazione 
col punto) a un nome riesce effettivamente a raggiungere quel nome nel 
*namespace*. 

Anche se gli *scope* sono determinati in modo statico, sono usati in modo 
dinamico. In qualsiasi momento durante l'esecuzione del programma esistono tre 
o quattro *scope* annidati, i cui *namespace* sono direttamente accessibili:

* lo *scope* più interno, dove un nome è cercato per prima cosa, contiene i 
  nomi locali; 
* gli *scope* di ogni eventuale funzione di ordine superiore, che sono 
  ricercati dal più prossimo al più lontano, contengono nomi non-locali ma 
  anche non-globali;
* il penultimo *scope* più lontano contiene i nomi globali del modulo corrente;
* lo *scope* più generale (dove il nome è cercato per ultimo) è il *namespace* 
  che contiene i nomi predefiniti.

Se un nome è dichiarato *global*, allora tutti i riferimenti a questo puntano 
direttamente allo *scope* intermedio che contiene i nomi globali del moduli. 
Per ri-collegare variabili che si trovano fuori dallo *scope* più interno, 
potete usare l'istruzione :keyword:`nonlocal`. Se dichiarata *nonlocal*, una 
variabile è di sola lettura: tentare di scrivere in questa variabile non farà 
altro che creare un *nuova* variabile nello *scope* locale, lasciando immutata 
la variabile esterna con il medesimo nome. 

In genere lo *scope* locale "vede" i nomi locali al codice della funzione 
corrente. Al di fuori di una funzione, lo *scope* locale vede lo stesso 
*namespace* dello *scope* globale: ovvero, il *namespace* del modulo.  

È importante capire che gli *scope* sono determinati "dal testo del codice". 
Lo *scope* globale di una funzione definita in un modulo è il *namespace* di 
quel modulo: non importa da dove è chiamata la funzione, o con quale alias. Ma 
d'altro canto, la *ricerca* di un nome avviene dinamicamente, a *runtime*. È 
anche vero che l'architettura del linguaggio evolve verso la risoluzione 
statica dei nomi, a *compile time*, quindi non dovreste fare affidamento sulla 
risoluzione dinamica dei nomi (e in effetti, le variabili locali sono già 
determinate in modo statico).

Una peculiarità di Python è che, in assenza di istruzioni :keyword:`global` 
o :keyword:`nonlocal`, gli assegnamenti alle variabili sono sempre indirizzati 
allo *scope* più interno. Gli assegnamenti non copiano i dati, collegano 
semplicemente i nomi agli oggetti. Lo stesso vale per le eliminazioni: 
l'istruzione ``del x`` rimuove il collegamento di ``x`` dal *namespace* 
ricercato dallo *scope* locale. In effetti, tutte le operazioni che 
introducono nomi nuovi utilizzano lo *scope* locale: in particolare, le 
istruzioni :keyword:`import` e le definizioni di funzione collegano il nome 
del modulo o della funzione allo *scope* locale. 

L'istruzione :keyword:`global` può essere usata per indicare che una 
particolare variabile vive nello *scope* globale e dovrebbe essere 
ri-collegata lì; l'istruzione :keyword:`nonlocal` indica che una particolare 
variabile vive nel *namespace* di ordine superiore e dovrebbe essere 
ri-collegata lì. 

.. _tut-scopeexample:

Esempi di *scope* e *namespace*
-------------------------------

Questo esempio dimostra come riferirsi ai diversi *scope* e *namespace* e come 
:keyword:`global` e :keyword:`nonlocal` influiscono sul collegamento delle 
variabili. ::

   def scope_test():
       def do_local():
           spam = "local spam"

       def do_nonlocal():
           nonlocal spam
           spam = "nonlocal spam"

       def do_global():
           global spam
           spam = "global spam"

       spam = "test spam"
       do_local()
       print("Dopo un'assegnazione locale:", spam)
       do_nonlocal()
       print("Dopo un'assegnazione 'nonlocal':", spam)
       do_global()
       print("Dopo un'assegnazione 'global':", spam)

   scope_test()
   print("Nello scope globale:", spam)

L'output di questo esempio è:

.. code-block:: none

   Dopo un'assegnazione locale: test spam
   Dopo un'assegnazione 'nonlocal': nonlocal spam
   Dopo un'assegnazione 'global': nonlocal spam
   Nello scope globale: global spam

Si noti che l'assegnazione *locale* (che è il comportamento di default) non 
cambia il collegamento della variabile *spam* della funzione *scope_test*. 
D'altra parte l'assegnamento :keyword:`nonlocal` cambia il collegamento dello 
*spam* di *test_spam*, e l'assegnamento :keyword:`global` cambia il 
collegamento dello *spam* del modulo. 

Si noti inoltre che non esisteva un collegamento per la variabile *spam* prima 
dell'assegnamento :keyword:`global`.

.. _tut-firstclasses:

Introduzione alle classi
========================

Le classi introducono qualche nuovo aspetto nella sintassi, tre tipi di 
oggetto nuovi e della nuova semantica. 

.. _tut-classdefinition:

Sintassi della definizione di una classe
----------------------------------------

Questa è la forma più semplice di definizione di una classe::

   class ClassName:
       <statement-1>
       .
       .
       .
       <statement-N>

La definizione delle classi, come quella delle funzioni (l'istruzione 
:keyword:`def`) deve essere *eseguita* prima di avere qualsiasi effetto. (Si 
potrebbe anche collocare la definizione in un ramo di un'istruzione 
:keyword:`if`, o all'interno di una funzione.)

In pratica, le istruzioni all'interno di una definizione di classe sono in 
genere definizioni di funzione: ma sono permesse anche altre istruzioni, e 
talvolta sono anzi utili (ne riparleremo in seguito). Le definizioni di 
funzione all'interno della classe di solito hanno una particolare lista di 
parametri, dovuta alle convenzioni di chiamata per i metodi (di nuovo, ne 
riparleremo). 

Quando il flusso di esecuzione del codice entra nella definizione della 
classe, un nuovo *namespace* viene creato e usato come *scope* locale: ovvero, 
tutte le successive assegnazioni di variabili locali finiscono in questo nuovo 
*namespace*. In particolare, le definizioni di funzione collegano qui il nome 
della funzione. 

Quando si esce dalla definizione della classe nel modo normale (perché il 
flusso di esecuzione abbandona la classe), viene creato un *oggetto-classe*. 
Questo oggetto è in sostanza un "contenitore" per il contenuto del *namespace* 
creato dalla definizione della classe: diremo di più sugli oggetti-classe 
nella prossima sezione. Lo *scope* locale originario (quello che era attivo 
subito prima di entrare nella definizione della classe) viene ripristinato e 
l'oggetto-classe viene collegato in questo *namespace* al nome fornito 
nell'intestazione della definizione della classe (nel nostro esempio, 
:class:`ClassName`).

.. _tut-classobjects:

Gli oggetti-classe
------------------

Gli oggetti-classe supportano due tipi di operazione: il riferimento agli 
attributi e l'istanziamento. 

Il riferimento agli attributi utilizza la normale sintassi che si usa per 
queste operazioni in Python: ``obj.name``. Un nome di attributo è valido se 
era nel *namespace* della classe al momento della creazione 
dell'oggetto-classe. Quindi, se una definizione di classe è fatta così, ::

   class MyClass:
       """Un semplice esempio di classe."""
       i = 12345

       def f(self):
           return 'hello world'

allora ``MyClass.i`` e ``MyClass.f`` sono riferimenti validi agli attributi, e 
restituiscono un intero e un oggetto-funzione rispettivamente. Gli attributi 
della classe possono anche essere assegnati, ovvero potete cambiare il valore 
di ``MyClass.i`` con un assegnamento. Anche :attr:`__doc__` è un attributo 
valido, e restituisce la docstring della classe 
(``"Un semplice esempio di classe."``)

Lo *istanziamento* usa invece la notazione di chiamata di funzione. Fate finta 
che la classe sia una funzione senza parametri che restituisce una nuova 
istanza della classe. Per esempio, con riferimento alla classe dell'esempio 
precedente, ::

   x = MyClass()

crea una nuova *istanza* della classe e assegna questo oggetto alla variabile 
locale ``x``.

L'operazione di istanziamento ("invocare" un oggetto-classe) crea un oggetto 
vuoto. Molto spesso le classi preferiscono creare istanze predisposte con uno 
specifico stato iniziale. Per questo è possibile definire nella classe un 
metodo speciale chiamato :meth:`__init__`, così::

   def __init__(self):
       self.data = []

Se la classe definisce un metodo :meth:`__init__` allora l'operazione di 
istanziamento lo invoca automaticamente per l'istanza appena creata. Quindi 
nel nostro esempio, una nuova istanza già inizializzata può essere ottenuta 
con::

   x = MyClass()

Naturalmente il metodo :meth:`__init__` può essere reso più flessibile 
dotandolo di parametri. In questo caso gli argomenti passati all'istanziamento 
della classe sono trasferiti al metodo :meth:`__init__`. Per esempio::

   >>> class Complex:
   ...     def __init__(self, realpart, imagpart):
   ...         self.r = realpart
   ...         self.i = imagpart
   ...
   >>> x = Complex(3.0, -4.5)
   >>> x.r, x.i
   (3.0, -4.5)

.. _tut-instanceobjects:

Oggetti-istanza
---------------

Che cosa possiamo fare con gli oggetti-istanza? L'unica operazione possibile 
con questi oggetti è il riferimento agli attributi. Ci sono due tipi di nomi 
di attributo validi: i *dati* ("campi") e i *metodi*. 

I *dati* corrispondono alle "variabili di istanza" di Smalltalk e ai "data 
members" di C++. Gli attributi-dati non devono essere dichiarati: proprio come 
le variabili locali, iniziano a esistere nel momento in cui sono assegnati per 
la prima volta. Per esempio, se ``x`` è una istanza della classe 
:class:`MyClass` che abbiamo definito sopra, questo codice scriverà il valore 
"16" senza lasciar traccia::

   x.counter = 1
   while x.counter < 10:
       x.counter = x.counter * 2
   print(x.counter)
   del x.counter

L'altro tipo di attributo dell'istanza è il *metodo*. Un metodo è una funzione 
che "appartiene" all'oggetto-istanza. (In Python, il termine "metodo" non si 
usa solo in relazione alle istanze delle classi: anche altri tipi di oggetti 
possono avere dei metodi. Per esempio, gli oggetti-lista hanno metodi come 
*append*, *insert*, *remove*, *sort* e così via. In ogni caso, nel resto di 
questo capitolo, useremo "metodo" solo per riferirci ai metodi degli 
oggetti-istanza di una classe, a meno che non sia specificato diversamente.)

.. index:: object: method

I nomi validi per i metodi di un'istanza dipendono dalla sua classe. Per 
definizione, tutti gli attributi della classe che corrispondono a degli 
oggetti-funzione sono metodi della sua istanza. Quindi nel nostro esempio 
``x.f`` è un riferimento valido al metodo, dal momento che ``MyClass.f`` è una 
funzione; ma ``x.i`` non lo è, perché ``MyClass.i`` non è una funzione. 
Tuttavia ``x.f`` *non è* la stessa cosa di ``MyClass.f``: il primo è un 
oggetto-metodo, il secondo è un oggetto-funzione. 

.. _tut-methodobjects:

Oggetti-metodo
--------------

Di solito un metodo viene invocato non appena è stato collegato::

   x.f()

Nell'esempio di :class:`MyClass`, questa chiamata restituirà la stringa 
``'hello world'``. Tuttavia non è necessario invocare il metodo 
immediatamente: ``x.f`` è un oggetto-metodo che può essere "conservato" e 
chiamato più tardi. Per esempio, ::

   xf = x.f
   while True:
       print(xf())

continuerà a scrivere ``hello world`` fino alla fine del mondo.

Che cosa succede di preciso quando un metodo è invocato? Avrete notato che 
l'invocazione ``x.f()`` è stata fatta senza passare argomenti, anche se la 
definizione di :meth:`f` specifica in effetti un parametro. Che cosa succede a 
questo? Certamente Python dovrebbe emettere un'eccezione se una funzione che 
richiede un argomento è invocata senza passarlo, anche se poi l'argomento non 
dovesse essere usato nella funzione stessa...

In realtà probabilmente avrete indovinato la risposta: la peculiarità dei 
metodi è che l'oggetto-istanza è passato automaticamente come primo argomento 
della funzione. Nel nostro esempio, la chiamata ``x.f()`` è esattamente 
equivalente a ``MyClass.f(x)``. In generale, invocare un metodo con una lista 
di *n* argomenti è equivalente a chiamare la corrispondente funzione con una 
lista di argomenti identica, ma che inserisce al primo posto l'oggetto-istanza. 

Se non riuscite a comprendere esattamente come funziona, può essere utile dare 
un'occhiata all'implementazione. Quando referenziamo un attributo (che non sia 
un dato) di una classe, il nome viene cercato nell'istanza della classe. Se il 
nome corrisponde a un attributo che è un oggetto-funzione, allora un 
oggetto-metodo viene creato mettendo insieme (puntatori a) l'oggetto-istanza e 
l'oggetto-funzione appena trovato, per formare un nuovo oggetto astratto: 
l'oggetto-metodo, appunto. Quando l'oggetto-metodo è invocato con una lista di 
argomenti, una nuova lista viene creata unendola all'oggetto-istanza: 
l'oggetto-funzione viene chiamato con questa nuova lista di argomenti. 

.. _tut-class-and-instance-variables:

Variabili di classe e di istanza
--------------------------------

In generale, le variabili di istanza sono per i dati che devono restare unici 
per ciascuna istanza; le variabili di classe sono per attributi e metodi 
condivisi tra tutte le istanze della classe::

    class Dog:

        kind = 'canine'         # variabile di classe condivisa tra le istanze

        def __init__(self, name):
            self.name = name    # variabile di istanza unica per ciascuna istanza

    >>> d = Dog('Fido')
    >>> e = Dog('Buddy')
    >>> d.kind                  # condivisa tra tutti i cani
    'canine'
    >>> e.kind                  # condivisa tra tutti i cani
    'canine'
    >>> d.name                  # unica per d
    'Fido'
    >>> e.name                  # unica per e
    'Buddy'

Come abbiamo visto in :ref:`tut-object`, i dati condivisi possono avere 
comportamenti sorprendenti quando sono oggetti :term:`mutabili<mutable>` come 
liste e dizionari. Nell'esempio che segue, la lista *tricks* non dovrebbe 
essere utilizzata come una variabile di classe, perché una singola lista 
verrebbe condivisa tra tutte le istanze di *Dog*:: 

    class Dog:

        tricks = []             # uso sbagliato di una variabile di classe

        def __init__(self, name):
            self.name = name

        def add_trick(self, trick):
            self.tricks.append(trick)

    >>> d = Dog('Fido')
    >>> e = Dog('Buddy')
    >>> d.add_trick('roll over')
    >>> e.add_trick('play dead')
    >>> d.tricks                # inaspettata condivisione tra tutte le istanze
    ['roll over', 'play dead']

Il design corretto per la classe prevede l'uso di una variabile *di istanza*, 
invece::

    class Dog:

        def __init__(self, name):
            self.name = name
            self.tricks = []    # crea una lista vuota per ciascuna istanza

        def add_trick(self, trick):
            self.tricks.append(trick)

    >>> d = Dog('Fido')
    >>> e = Dog('Buddy')
    >>> d.add_trick('roll over')
    >>> e.add_trick('play dead')
    >>> d.tricks
    ['roll over']
    >>> e.tricks
    ['play dead']

.. _tut-remarks:

Osservazioni varie
==================

.. These should perhaps be placed more carefully...

Se lo stesso nome è usato per un attributo di classe e uno di istanza, allora 
il meccanismo di ricerca dà priorità all'attributo di istanza::

    >>> class Warehouse:
    ...     purpose = 'storage'
    ...     region = 'west'
    ...
    >>> w1 = Warehouse()
    >>> print(w1.purpose, w1.region)
    storage west
    >>> w2 = Warehouse()
    >>> w2.region = 'east'
    >>> print(w2.purpose, w2.region)
    storage east

Gli attributi che sono dati possono essere referenziati anche dai metodi, 
oltre che dai normali "clienti" (utilizzatori) di un oggetto. In altre parole, 
le classi non sono adatte a implementare tipi di dati astratti. In effetti, 
non è in alcun modo possibile in Python garantire la protezione di un dato: 
questo può essere solo basato su convenzioni. (D'altro canto, la 
*implementazione* di Python, scritta in C, può nascondere completamente i 
dettagli di implementazione e controllare l'accesso a un oggetto, se 
necessario: si può sfruttare questo aspetto scrivendo delle estensioni di 
Python in C.)

I "clienti" dovrebbero fare attenzione a usare gli attributi-dati: potrebbero 
scompaginare delle invarianti utilizzate dai metodi, sovrascrivendole con i 
loro attributi-dati. Si noti che i clienti possono aggiungere dati per conto 
proprio a un oggetto-istanza, senza compromettere il funzionamento dei metodi, 
fintanto che non ci sono conflitti tra i nomi. Ancora una volta, l'uso di una 
convenzione per i nomi può risparmiare molti grattacapi. 

Non ci sono particolari scorciatoie per referenziare dati (o metodi) 
dall'interno dei metodi. Riteniamo che in questo modo il codice sia più 
leggibile: non c'è la possibilità di confondere variabili locali e variabili 
di istanza quando si scorre con l'occhio il codice di un metodo. 

Di solito il primo parametro di un metodo viene chiamato ``self``. Si tratta 
solo di una convenzione: il nome di per sé non ha alcun significato speciale 
per Python. Notate tuttavia che non seguire questa convenzione rende il vostro 
codice meno leggibile per gli altri programmatori Python; è anche probabile 
che gli strumenti di introspezione del codice si basino sul rispetto di questa 
convenzione. 

Ogni oggetto-funzione che sia un attributo di classe definisce un 
oggetto-metodo per l'istanza di quella classe. Non è necessario che il codice 
della funzione sia fisicamente contenuto all'interno della definizione della 
classe: si può anche assegnare una variabile locale a un oggetto-funzione 
esterno. Per esempio::

   # Una funzione definita all'esterno della classe
   def f1(self, x, y):
       return min(x, x+y)

   class C:
       f = f1

       def g(self):
           return 'hello world'

       h = g

Adesso ``f``, ``g`` e ``h`` sono tutti attributi della classe :class:`C`, che 
si riferiscono a oggetti-funzione: di conseguenza sono anche tutti metodi 
delle istanze della classe; ``h`` sarà esattamente equivalente a ``g``. Si 
noti però che questa pratica in genere confonde solo le idee a chi deve 
leggere il codice.

I metodi possono invocare altri metodi usando gli attributi-metodo del loro 
parametro ``self``::

   class Bag:
       def __init__(self):
           self.data = []

       def add(self, x):
           self.data.append(x)

       def addtwice(self, x):
           self.add(x)
           self.add(x)

I metodi possono accedere ai nomi globali nello stesso modo delle funzioni 
ordinarie. Lo *scope* globale associato a un metodo è il modulo che contiene 
la definizione. (Una classe non è mai utilizzata come *scope* globale.) Anche 
se di rado esiste una ragione valida per accedere a un *dato* globale 
dall'interno di un metodo, ci sono comunque motivi validi per usare lo *scope* 
globale: per cominciare, le funzioni e i moduli importati nello *scope* 
globale possono essere usate dai metodi, così come le funzioni e le classi ivi 
definite. In genere la classe che contiene il metodo è essa stessa definita 
nello *scope* globale, e nella prossima sezione vedremo dei buoni motivi per 
cui un metodo potrebbe voler accedere al nome della sua stessa classe. 

Ogni valore è un oggetto e di conseguenza ha una *classe*, che è chiamata il 
suo *tipo*. Il nome della classe/tipo è conservato in ``object.__class__``.

.. _tut-inheritance:

Ereditarietà
============

Naturalmente una classe non sarebbe degna di questo nome se non supportasse 
l'ereditarietà. La sintassi per definire una sotto-classe è questa::

   class DerivedClassName(BaseClassName):
       <statement-1>
       .
       .
       .
       <statement-N>

Il nome della classe-madre :class:`BaseClassName` deve essere definito in un 
*namespace* accessible dallo *scope* che contiene la definizione della 
sotto-classe. Al posto del nome 
della classe-madre è anche consentito inserire un'espressione arbitraria. 
Questo è utile, per esempio, quando la classe-madre è definita in un altro 
modulo::

   class DerivedClassName(modname.BaseClassName):

L'esecuzione della definizione di una sotto-classe è simile a quella della 
classe-madre. Al momento della sua costruzione, l'oggetto-classe ricorda la 
sua classe-madre. In questo modo può risolvere i riferimenti agli attributi: 
se viene richiesto un attributo che non si trova nella classe, la ricerca 
procede nella classe-madre. Il meccanismo si applica ricorsivamente, se la 
classe-madre a sua volta deriva da qualche altra classe.

Non vi è nulla di speciale nell'istanziare una sotto-classe: 
``DerivedClassName()`` crea una nuova istanza della classe. I riferimenti ai 
metodi sono risolti così: si cerca il corrispondente attributo di classe, 
scendendo lungo la catena delle classi-madri se necessario; il riferimento al 
metodo è valido se il nome trovato corrisponde a un oggetto-funzione. 

Le sotto-classi possono sovrascrivere i metodi delle loro classi-madri. Dal 
momento che i metodi non hanno privilegi speciali quando chiamano altri metodi 
dello stesso oggetto, un metodo in una classe-madre che chiama un altro metodo 
definito nella stessa classe potrebbe finire per chiamare in realtà un metodo 
sovrascritto in una sotto-classe. (Per i programmatori C++: tutti i metodi in 
Python sono ``virtual``.)

Un metodo di una sotto-classe potrebbe voler *estendere* invece che 
semplicemente rimpiazzare il metodo della classe-madre con lo stesso nome. Per 
chiamare il metodo della classe-madre, semplicemente basta chiamare 
``BaseClassName.methodname(self, arguments)``. Talvolta questa tecnica può 
servire anche al codice "cliente". (Si noti però che questo funziona solo se 
la classe-madre è accessibile nello *scope* globale come ``BaseClassName``.)

Python ha due funzioni predefinite che si occupano di ereditarietà:

* :func:`isinstance` controlla il tipo di un'istanza: ``isinstance(obj, int)``
  restituirà ``True`` se ``obj.__class__`` è un :class:`int` o qualcosa 
  derivato da :class:`int`.

* :func:`issubclass` controlla l'ereditarietà di una classe: 
  ``issubclass(bool, int)`` restituisce ``True``, dal momento che la classe 
  :class:`bool` è una sotto-classe di :class:`int`.  Al contrario, 
  ``issubclass(float, int)`` è ``False`` perché :class:`float` non è una 
  sotto-classe di :class:`int`.

.. _tut-multiple:

Ereditarietà multipla
---------------------

Python supporta anche una forma di ereditarietà multipla. Una classe con più 
di una classe-madre si può scrivere così::

   class DerivedClassName(Base1, Base2, Base3):
       <statement-1>
       .
       .
       .
       <statement-N>

Nei casi più semplici e per la maggior parte dei casi d'uso, potete assumere 
che la ricerca di un attributo ereditato proceda da sinistra a destra, con una 
"ricerca in profondità", e senza cercare una seconda volta nella stessa classe 
quando le gerarchie si sovrappongono. Quindi, se un attributo non viene 
trovato in :class:`DerivedClassName`, lo si cerca in :class:`Base1`, quindi 
ricorsivamente nelle classi-madre di :class:`Base1`, quindi in :class:`Base2` 
e così via. 

In realtà le cose sono leggermente più complicate; il meccanismo di ricerca 
dei metodi cambia dinamicamente per supportare chiamate cooperative alla 
funzione :func:`super`. Questo approccio è noto come "call-next-method" in 
alcuni linguaggi dotati di ereditarietà multipla e offre più possibilità 
rispetto al *super* dei linguaggi con ereditarietà semplice. 

La ricerca con ordinamento dinamico si rende necessaria perché tutte le 
ereditarietà multiple finiscono per avere una o più gerarchie "a rombo": 
ovvero, almeno una delle classi-madre può essere raggiunta in più di un modo a 
partire dalla sotto-classe. Per esempio, in Python tutte le classi ereditano 
da :class:`object`, quindi tutti gli schemi di ereditarietà multipla hanno 
necessariamente più di un percorso per arrivare a :class:`object`. Per evitare 
di cercare più di una volta nelle classi-madre, l'algoritmo dinamico traccia 
un percorso di ricerca lineare tale da preservare il principio "da sinistra a 
destra", da raggiungere ciascuna classe-madre una sola volta, e da essere 
monotonico (ovvero, è possibile creare una sotto-classe senza influenzare il 
percorso di ricerca già esistente per la gerarchia superiore). Queste 
proprietà, nel loro insieme, rendono possibile la progettazione di classi 
affidabili ed estensibili in un contesto di ereditarietà multipla. Per 
ulteriori dettagli, si veda https://www.python.org/download/releases/2.3/mro/.

.. _tut-private:

Variabili private
=================

In Python non esiste il concetto di istanza "privata" di una variabile, che è 
accessibile solo dall'interno del suo oggetto. Tuttavia esiste una 
convenzione, adottata quasi ovunque nel codice scritto in Python: un nome che 
inizia con il "trattino basso" (per esempio ``_spam``) dovrebbe essere 
trattato come una componente non-pubblica della API (che sia una funzione, un 
metodo o un dato). Dovrebbe essere considerato come un dettaglio di 
implementazione, suscettibile di essere modificato in futuro senza preavviso. 

.. index::
   pair: name; mangling

Esiste almeno uno scenario reale in cui è desiderabile disporre di una 
variabile privata: quando si vogliono evitare conflitti con nomi definiti 
dalle sotto-classi. Python fornisce un supporto limitato per questa necessità, 
attraverso il :dfn:`name mangling`. Tutti i nomi che hanno almeno due 
"trattini bassi" iniziali e non più di un "trattino basso" finale (come 
``__spam``) sono rimpiazzati con ``_classname__spam``, dove ``classname`` è il 
nome della classe corrente senza trattini bassi iniziali. Questa manipolazione 
avviene per tutti gli identificatori di questo tipo, indipendentemente dalla 
loro posizione, purché siano definiti all'interno della classe. 

La manipolazione dei nomi permette alle sotto-classi di sovrascrivere un 
metodo senza comprometterne l'invocazione da un'altra classe. Per esempio::

   class Mapping:
       def __init__(self, iterable):
           self.items_list = []
           self.__update(iterable)

       def update(self, iterable):
           for item in iterable:
               self.items_list.append(item)

       __update = update   # una copia privata del metodo update()

   class MappingSubclass(Mapping):

       def update(self, keys, values):
           # sovrascrive update() con una nuova *signature*
           # ma non rompe il funzionamento della chiamata in __init__()
           for item in zip(keys, values):
               self.items_list.append(item)

Questo esempio funzionerebbe anche se ``MappingSubclass`` volesse introdurre 
un suo ``__update``, dal momento che sarebbe rimpiazzato con 
``_Mapping__update`` nella classe-madre e con ``_MappingSubclass__update`` 
nella sotto-classe.

Si noti che il meccanismo del *mangling* vuole essere soprattutto un modo per 
evitare conflitti di nomi: è comunque sempre possibile accedere o modificare 
una variabile "privata". Questo può essere anzi utile in talune circostanze, 
per esempio in un debugger. 

Si noti inoltre che il codice passato alle funzioni ``exec()`` o ``eval()`` 
non considera la classe che invoca il metodo come la classe "corrente" e 
quindi non usa quel nome per il *mangling*; è un effetto simile a quello 
dell'istruzione ``global``, che infatti, anch'essa, vale solo nel codice che è 
stato compilato insieme (nel senso di *byte-compiled*). Lo stesso vale per 
``getattr()``, ``setattr()`` e ``delattr()``, e anche quando si utilizza 
direttamente ``__dict__``.

.. _tut-odds:

Note varie
==========

Può essere utile talvolta disporre di una struttura-dati simile al "record" di 
Pascal o a "struct" in C, impacchettando insieme alcuni dati referenziati con 
variabili. Si può usare una classe vuota::

   class Employee:
       pass

   john = Employee()  # Crea una scheda di impiegato vuota

   # Riempie i campi della scheda
   john.name = 'John Doe'
   john.dept = 'computer lab'
   john.salary = 1000

Se una sezione di codice Python si aspetta di ricevere uno specifico tipo di 
dato astratto, le si può passare invece una classe che emula i metodi di quel 
tipo di dato. Per esempio, se avete una funzione che formatta dei dati 
provenienti da un file di testo, potete definire una classe con dei metodi 
:meth:`read` e :meth:`!readline` che invece prelevano i dati da una 
stringa-buffer, e passare questa alla funzione come argomento. 

.. (Unfortunately, this technique has its limitations: a class can't define
   operations that are accessed by special syntax such as sequence subscripting
   or arithmetic operators, and assigning such a "pseudo-file" to sys.stdin will
   not cause the interpreter to read further input from it.)

Gli oggetti-metodi di istanza hanno a loro volta degli attributi: 
``m.__self__`` è l'oggetto-istanza che possiede il metodo :meth:`m`, e 
``m.__func__`` è l'oggetto-funzione corrispondente al metodo.

.. _tut-iterators:

Iteratori
=========

Avrete probabilmente già notato che è possibile iterare su molti oggetti 
contenitori con l'istruzione :keyword:`for`::

   for element in [1, 2, 3]:
       print(element)
   for element in (1, 2, 3):
       print(element)
   for key in {'one':1, 'two':2}:
       print(key)
   for char in "123":
       print(char)
   for line in open("myfile.txt"):
       print(line, end='')

Questo modo di accesso è chiaro, sintetico, efficiente. L'uso degli iteratori 
è onnipresente in Python. Dietro le quinte, l'istruzione :keyword:`for` chiama 
la funzione :func:`iter` dell'oggetto contenitore. La funzione restituisce un 
oggetto iteratore, che a sua volta definisce il metodo 
:meth:`~iterator.__next__`, che accede agli elementi del contenitore, uno alla 
volta. Quando gli elementi sono finiti, :meth:`~iterator.__next__` emette 
un'eccezione :exc:`StopIteration`, che comunica all'istruzione :keyword:`!for` 
di terminare. Potete chiamare direttamente il metodo 
:meth:`~iterator.__next__` usando la funzione predefinita :func:`next`. Questo 
esempio spiega come funziona il meccanismo::

   >>> s = 'abc'
   >>> it = iter(s)
   >>> it
   <str_iterator object at 0x10c90e650>
   >>> next(it)
   'a'
   >>> next(it)
   'b'
   >>> next(it)
   'c'
   >>> next(it)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       next(it)
   StopIteration

Conoscendo il meccanismo che governa il comportamento degli iteratori, è 
facile aggiungere questa funzionalità alle vostre classi. Occorre definire un 
metodo :meth:`__iter__` che restituisce un oggetto a sua volta dotato di un 
metodo :meth:`~iterator.__next__`. Se la classe definisce già 
:meth:`__next__`, allora :meth:`__iter__` può limitarsi a restituire 
``self``::

   class Reverse:
       """Un iteratore che cicla all'indietro su una sequenza."""
       def __init__(self, data):
           self.data = data
           self.index = len(data)

       def __iter__(self):
           return self

       def __next__(self):
           if self.index == 0:
               raise StopIteration
           self.index = self.index - 1
           return self.data[self.index]

::

   >>> rev = Reverse('spam')
   >>> iter(rev)
   <__main__.Reverse object at 0x00A1DB50>
   >>> for char in rev:
   ...     print(char)
   ...
   m
   a
   p
   s

.. _tut-generators:

Generatori
==========

Un :term:`generatore<generator>` è uno strumento semplice e potente per creare 
iteratori. I generatori sono definiti come normali funzioni che però 
utilizzano l'istruzione :keyword:`yield` quando vogliono restituire dei dati. 
Ogni volta che la funzione :func:`next` viene chiamata su un generatore, 
questo riprende l'esecuzione da dove l'aveva interrotta (ricorda tutti i 
valori in sospeso e qual è stata l'ultima istruzione eseguita). Ecco un 
esempio che mostra come creare un generatore può essere molto semplice::

   def reverse(data):
       for index in range(len(data)-1, -1, -1):
           yield data[index]

::

   >>> for char in reverse('golf'):
   ...     print(char)
   ...
   f
   l
   o
   g

Tutto ciò che può essere fatto con un generatore può anche essere fatto con un 
iteratore in una classe, come visto nel paragrafo precedente. I generatori 
però sono più compatti grazie al fatto che i metodi :meth:`__iter__` e 
:meth:`~generator.__next__` vengono creati automaticamente.

Un altro vantaggio importante è che le variabili locali e lo stato 
dell'esecuzione vengono salvati tra una chiamata e l'altra. In questo modo 
scrivere la funzione è più facile e molto più chiaro, rispetto a dover usare 
variabili di istanza come ``self.index`` e ``self.data``.

Oltre alla creazione automatica dei metodi e alla persistenza dello stato del 
programma, un generatore emette automaticamente un'eccezione 
:exc:`StopIteration` quando termina. Combinate insieme, queste caratteristiche 
permettono di creare iteratori con la stessa facilità con cui si scrive una 
normale funzione. 

.. _tut-genexps:

Espressioni-generatore
======================

Alcuni semplici generatori possono essere scritti in modo sintetico come delle 
espressioni, usando una sintassi simile a quella delle *list comprehension*, 
ma con le parentesi tonde invece delle parentesi quadre. Queste espressioni 
sono adatte alle situazioni in cui il generatore è consumato immediatamente da 
una funzione di ordine superiore. Le espressioni-generatore sono più compatte, 
ma meno versatili rispetto a un normale generatore; tendono a consumare meno 
memoria dell'equivalente *list comprehension*. 

Esempi::

   >>> sum(i*i for i in range(10))                 # somma di quadrati
   285

   >>> xvec = [10, 20, 30]
   >>> yvec = [7, 5, 3]
   >>> sum(x*y for x,y in zip(xvec, yvec))         # prodotto scalare
   260

   >>> unique_words = set(word for line in page  for word in line.split())

   >>> valedictorian = max((student.gpa, student.name) for student in graduates)

   >>> data = 'golf'
   >>> list(data[i] for i in range(len(data)-1, -1, -1))
   ['f', 'l', 'o', 'g']


.. only:: html

    .. rubric:: Note

.. [#] ndT: in questa traduzione rifiutiamo con decisione la consueta, 
   orribile restituzione di *scope* (area in cui una variabile è visibile: dal 
   Greco *skopein*, osservare) con l'Italiano "scopo" (fine, proposito: dal 
   Latino *scopus*, bersaglio). Lasciamo inalterato *scope* e, per contiguità, 
   non traduciamo neppure *namespace* (che di solito è reso in modo più 
   accettabile con "spazio dei nomi").

.. [#] Tranne che per una cosa. Gli oggetti-modulo hanno un attributo di sola 
   lettura nascosto, che si chiama :attr:`~object.__dict__`: è il dizionario 
   usato per implementare il *namespace* del modulo. Il nome 
   :attr:`~object.__dict__` è un attributo del modulo, ma non un suo nome 
   globale. Naturalmente questa è un'eccezione nell'implementazione astratta 
   dei *namespace* e dovrebbe essere usata solo da strumenti come i *debugger* 
   post-mortem. 
