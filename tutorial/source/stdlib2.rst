.. _tut-brieftourtwo:

*******************************************
Una breve visita alla libreria standard - 2
*******************************************

Questa seconda parte del tour presenta strumenti più avanzati che supportano le esigenze dei programmi professionali. Di rado ce n'è bisogno per i piccoli script. 

.. _tut-output-formatting:

Formattazione dell'output
=========================

Il modulo :mod:`reprlib` presenta una versione della funzione predefinita :func:`repr`, adattata per visualizzare in forma abbreviata le collezioni molto grandi o con molti livelli di annidamento::

   >>> import reprlib
   >>> reprlib.repr(set('supercalifragilisticexpialidocious'))
   "{'a', 'c', 'd', 'e', 'f', 'g', ...}"

:mod:`pprint` permette un controllo più raffinato sulla scrittura di oggetti predefiniti o creati dall'utente, in modo che l'output resti leggibile dall'interprete. Quando il risultato è più lungo di una riga, il *pretty printer* aggiunge interruzioni di riga e rientri per rendere più chiara la struttura dei dati::

   >>> import pprint
   >>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
   ...     'yellow'], 'blue']]]
   ...
   >>> pprint.pprint(t, width=30)
   [[[['black', 'cyan'],
      'white',
      ['green', 'red']],
     [['magenta', 'yellow'],
      'blue']]]

:mod:`textwrap` formatta i paragrafi di testo in modo che rispettino una determinata larghezza dello schermo::

   >>> import textwrap
   >>> doc = """Il metodo wrap() è come fill(), tranne che restituisce una 
   ... lista di stringhe, invece di una sola stringa lunga con gli a-capo 
   ... che separano le righe processate."""
   ...
   >>> print(textwrap.fill(doc, width=40))
   Il metodo wrap() è come fill(), tranne
   che restituisce una lista di stringhe,
   invece di una sola stringa lunga con gli
   a-capo che separano le righe processate.

Il modulo :mod:`locale` accede al database dei formati "culturali" specifici per i dati. Per esempio, l'attributo *grouping* della funzione localizzata *format* permette di formattare i numeri con i separatori di gruppo corretti::

   >>> import locale
   >>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
   'English_United States.1252'
   >>> conv = locale.localeconv()  # un mapping delle convenzioni applicabili
   >>> x = 1234567.8
   >>> locale.format("%d", x, grouping=True)
   '1,234,567'
   >>> locale.format_string("%s%.*f", (conv['currency_symbol'],
   ...                      conv['frac_digits'], x), grouping=True)
   '$1,234,567.80'

.. _tut-templating:

Template
========

Il modulo :mod:`string` include una versatile classe :class:`~string.Template`, con una sintassi semplice, adatta a essere modificata dagli utenti finali. In questo modo gli utenti possono personalizzare il programma senza doverne alterare il codice. 

Il formato utilizza dei nomi segnaposto composti da ``$`` con un identificatore Python valido (ovvero, caratteri alfanumerici e trattini bassi). Se il segnaposto è inserito tra parentesi, è possibile aggiungere dei caratteri immediatamente dopo, senza spazio in mezzo. Un ``$$`` è lo *escape* che produce un singolo ``$``::

   >>> from string import Template
   >>> t = Template('${village}folk send $$10 to $cause.')
   >>> t.substitute(village='Nottingham', cause='the ditch fund')
   'Nottinghamfolk send $10 to the ditch fund.'

Il metodo :meth:`~string.Template.substitute` emette un :exc:`KeyError` quando il segnaposto non è "alimentato" da un dizionario o un argomento *keyword*. Per le applicazioni di tipo "stampa unione", i dati forniti potrebbero essere incompleti e quindi potrebbe essere più appropriato il metodo :meth:`~string.Template.safe_substitute` che lascia semplicemente il segnaposto, quando il dato manca::

   >>> t = Template('Return the $item to $owner.')
   >>> d = dict(item='unladen swallow')
   >>> t.substitute(d)
   Traceback (most recent call last):
     ...
   KeyError: 'owner'
   >>> t.safe_substitute(d)
   'Return the unladen swallow to $owner.'

Una sotto-classe di *Template* può specificare un delimitatore arbitrario. Per esempio, un tool per la rinomina automatica di una collezione di foto potrebbe decidere di usare il simbolo di percentuale per segnaposti come la data corrente, un numero progressivo, un formato di file e così via::

   >>> import time, os.path
   >>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
   >>> class BatchRename(Template):
   ...     delimiter = '%'
   >>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
   Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

   >>> t = BatchRename(fmt)
   >>> date = time.strftime('%d%b%y')
   >>> for i, filename in enumerate(photofiles):
   ...     base, ext = os.path.splitext(filename)
   ...     newname = t.substitute(d=date, n=i, f=ext)
   ...     print('{0} --> {1}'.format(filename, newname))

   img_1074.jpg --> Ashley_0.jpg
   img_1076.jpg --> Ashley_1.jpg
   img_1077.jpg --> Ashley_2.jpg

Un altro scenario in cui i template sono utili è per separare la logica del programma dai dettagli di ciascun formato di output. In questo modo è possibile per esempio sostituire template personalizzati per file XML, output di solo testo o report in HTML. 

.. _tut-binary-formats:

Formati per campi di dati binari
================================

Il modulo :mod:`struct` ha le funzioni :func:`~struct.pack` e :func:`~struct.unpack` che consentono di lavorare con record di dati binari di lunghezza variabile. Questo esempio mostra come iterare sullo *header* di un file ZIP, senza usare il modulo :mod:`zipfile`.  I codici ``"H"`` e ``"I"`` indicano un numero di due e quattro byte senza segno. Il segno ``"<"`` indica che si tratta di numeri di larghezza standard e ordinamento *little-endian*::

   import struct

   with open('myfile.zip', 'rb') as f:
       data = f.read()

   start = 0
   for i in range(3):                      # mostra i primi 3 headers
       start += 14
       fields = struct.unpack('<IIIHH', data[start:start+16])
       crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

       start += 16
       filename = data[start:start+filenamesize]
       start += filenamesize
       extra = data[start:start+extra_size]
       print(filename, hex(crc32), comp_size, uncomp_size)

       start += extra_size + comp_size     # salta allo header successivo

.. _tut-multi-threading:

Multi-threading
===============

Il *threading* è una tecnica per separare *task* che non dipendono da un'esecuzione sequenziale. Si possono usare i thread per migliorare la reattività delle applicazioni che devono ricevere input dall'utente mentre svolgono altri compiti in background. Un caso d'uso simile è la necessità di compiere operazioni di input/output in parallelo con dei calcoli in un altro thread. 

Questo esempio mostra come l'interfaccia di alto livello del modulo :mod:`threading` permette di eseguire compiti in background mentre il programma principale continua a essere attivo::

   import threading, zipfile

   class AsyncZip(threading.Thread):
       def __init__(self, infile, outfile):
           threading.Thread.__init__(self)
           self.infile = infile
           self.outfile = outfile

       def run(self):
           f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
           f.write(self.infile)
           f.close()
           print('Finished background zip of:', self.infile)

   background = AsyncZip('mydata.txt', 'myarchive.zip')
   background.start()
   print('The main program continues to run in foreground.')

   background.join()    # aspetta che i compiti in background finiscano
   print('Main program waited until background was done.')

La sfida principale dei programmi multi-threading è di coordinare i thread che devono condividere dati o altre risorse. Per questo, il modulo *threading* mette a disposizione diverse primitive di sincronizzazione come lock, eventi, condizioni e semafori.

Anche con questi strumenti raffinati, piccoli errori di design possono causare problemi difficili da riprodurre. Di conseguenza, l'approccio più usato consiste nel concentrare tutte le operazioni di accesso alla risorsa in un solo thread, e quindi usare il modulo :mod:`queue` per fare arrivare a quel thread le richieste degli altri. Usare oggetti :class:`~queue.Queue` per le comunicazioni tra thread porta a scrivere applicazioni più semplici da progettare, più leggibili e affidabili.

.. _tut-logging:

Logging
=======

Il modulo :mod:`logging` offre un sistema di logging completo e flessibile. Nella forma più semplice, un messaggio di log è inviato a un file o a ``sys.stderr``::

   import logging
   logging.debug('Debugging information')
   logging.info('Informational message')
   logging.warning('Warning:config file %s not found', 'server.conf')
   logging.error('Error occurred')
   logging.critical('Critical error -- shutting down')

Questo produce l'output:

.. code-block:: none

   WARNING:root:Warning:config file server.conf not found
   ERROR:root:Error occurred
   CRITICAL:root:Critical error -- shutting down

I messaggi di informazione e debug sono soppressi di default, quando l'output è inviato allo *standard error*. Altre opzioni per l'output comprendono l'invio di messaggi tramite email, *datagram*, socket, o a un server HTTP. Un filtro può scegliere la modalità di invio in base alla priorità del messaggio: :const:`~logging.DEBUG`,
:const:`~logging.INFO`, :const:`~logging.WARNING`, :const:`~logging.ERROR`,
e :const:`~logging.CRITICAL`.

Il sistema di logging è configurabile direttamente da Python, o può essere inizializzato da un file di configurazione modificabile dall'utente, per personalizzare il sistema senza alterare il codice dell'applicazione. 

.. _tut-weak-references:

Weak References
===============

Python gestisce automaticamente la memoria, facendo *reference counting* per gli oggetti e usando il :term:`garbage collection` per eliminarli. La memoria viene liberata poco dopo che l'ultimo riferimento all'oggetto è stato cancellato. 

Questo approccio funziona bene nella maggior parte dei casi, ma talvolta si rende necessario tracciare un oggetto per tutto il tempo in cui è usato da qualcun altro. Purtroppo, questo tracciamento comporta la creazione di un riferimento, cosa che rende l'oggetto permanente. Il modulo :mod:`weakref` permette invece di tracciare oggetti senza per questo dover creare riferimenti. Quando non c'è più bisogno dell'oggetto, questo viene automaticamente rimosso dal registro delle *weak references* e un callback viene invocato per l'oggetto *weakref*. Questo meccanismo viene usato, per esempio, per conservare in cache gli oggetti costosi da creare::

   >>> import weakref, gc
   >>> class A:
   ...     def __init__(self, value):
   ...         self.value = value
   ...     def __repr__(self):
   ...         return str(self.value)
   ...
   >>> a = A(10)                   # crea un riferimento
   >>> d = weakref.WeakValueDictionary()
   >>> d['primary'] = a            # non crea un riferimento
   >>> d['primary']                # raggiunge l'oggetto se è ancora in vita
   10
   >>> del a                       # elimina il riferimento
   >>> gc.collect()                # aziona subito il garbage collector
   0
   >>> d['primary']                # la chiave è stata rimossa automaticamente
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       d['primary']                # la chiave è stata rimossa automaticamente
     File "C:/python39/lib/weakref.py", line 46, in __getitem__
       o = self.data[key]()
   KeyError: 'primary'

.. _tut-list-tools:

Strumenti per lavorare con le liste
===================================

Il tipo predefinito "lista" può soddisfare le esigenze di molte strutture-dati. Tuttavia occasionalmente c'è bisogno di un'implementazione alternativa con altri vantaggi e svantaggi in termini di performance. 

Il modulo :mod:`array` ha una classe :class:`~array.array()` simile a una lista che conserva i dati in modo più compatto, ma solo se sono di un medesimo tipo. L'esempio che segue mostra un array i cui elementi sono conservati come numeri binari di due byte senza segno (codice ``"H"``), invece dei consueti 16 byte che sarebbero impiegati da una normale lista Python::

   >>> from array import array
   >>> a = array('H', [4000, 10, 700, 22222])
   >>> sum(a)
   26932
   >>> a[1:3]
   array('H', [10, 700])

Il modulo :mod:`collections` ha un oggetto :class:`~collections.deque()` simile a una lista, che permette *append* e *pop* rapidi a entrambi gli estremi, ma accessi più lenti al centro. Questi oggetti vanno bene per implementare code e ricerche in ampiezza nei grafi::

   >>> from collections import deque
   >>> d = deque(["task1", "task2", "task3"])
   >>> d.append("task4")
   >>> print("Handling", d.popleft())
   Handling task1

::

   unsearched = deque([starting_node])
   def breadth_first_search(unsearched):
       node = unsearched.popleft()
       for m in gen_moves(node):
           if is_goal(m):
               return m
           unsearched.append(m)

Oltre a implementazioni alternative per le liste, la libreria standard contiene anche altri strumenti, come il modulo :mod:`bisect` che può manipolare le liste ordinate::

   >>> import bisect
   >>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
   >>> bisect.insort(scores, (300, 'ruby'))
   >>> scores
   [(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]

Il modulo :mod:`heapq` implementa *heap* a partire da normali liste. Il valore più basso è sempre mantenuto all'inizio. Ciò è utile per le applicazioni che hanno bisogno di accedere spesso all'elemento più piccolo, senza dover ordinare tutta la lista per trovarlo::

   >>> from heapq import heapify, heappop, heappush
   >>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
   >>> heapify(data)                      # ordina la lista come heap
   >>> heappush(data, -5)                 # aggiunge un valore
   >>> [heappop(data) for i in range(3)]  # produce i tre valori più piccoli
   [-5, 0, 1]

.. _tut-decimal-fp:

Aritmetica decimale in virgola mobile
=====================================

Il modulo :mod:`decimal` offre un tipo :class:`~decimal.Decimal` per operare con i numeri decimali in virgola mobile. In confronto con il tipo predefinito :class:`float` che implementa un numero *binario* in virgola mobile, questa classe è conveniente per 

* le applicazioni finanziarie, o quando è richiesta una rappresentazione decimale esatta,
* avere più controllo sulla precisione,
* avere più controllo sull'arrotondamento per esigenze legali o normative,
* mantenere le cifre decimali significative, 
* le applicazioni dove il risultato deve essere uguale al calcolo fatto a mano.

Per esempio, calcolare il 5% di tasse su 70 centesimi di costo telefonico fornisce un risultato diverso in virgola mobile decimale o binaria. La differenza diventa importante se il risultato è arrotondato al centesimo più vicino::

   >>> from decimal import *
   >>> round(Decimal('0.70') * Decimal('1.05'), 2)
   Decimal('0.74')
   >>> round(.70 * 1.05, 2)
   0.73

I risultati in :class:`~decimal.Decimal` mantengono gli zero finali, conservando quattro decimali significativi da una moltiplicazione tra numeri con due decimali significativi. Il modulo *decimal* riproduce il risultato dei calcoli fatti a mano ed evita i problemi che nascono quando una quantità binaria in virgola mobile non può rappresentare esattamente una quantità decimale. 

Usare una rappresentazione esatta permette a :class:`~decimal.Decimal` di calcolare i resti precisamente e di effettuare test di uguaglianza che fallirebbero con la rappresentazione binaria in virgola mobile::

   >>> Decimal('1.00') % Decimal('.10')
   Decimal('0.00')
   >>> 1.00 % 0.10
   0.09999999999999995

   >>> sum([Decimal('0.1')]*10) == Decimal('1.0')
   True
   >>> sum([0.1]*10) == 1.0
   False

Il modulo :mod:`decimal` permette di svolgere calcoli con tutta la precisione richiesta::

   >>> getcontext().prec = 36
   >>> Decimal(1) / Decimal(7)
   Decimal('0.142857142857142857142857142857142857')
