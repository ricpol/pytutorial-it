.. _tut-io:

**************
Input e Output
**************

Ci sono diversi modi per presentare l'output di un programma: i dati possono 
essere "stampati" in un formato leggibile per l'utente, o conservati in un 
file per uso futuro. In questo capitolo prenderemo in esame alcune possibilità.

.. _tut-formatting:

Formattazione gradevole dell'output
===================================

Finora abbiamo visto due modi di scrivere un valore: le espressioni e la 
funzione :func:`print`. (Un terzo modo è quello di usare il metodo 
:meth:`write` degli oggetti-file: lo standard output può essere raggiunto con 
``sys.stdout``. Si veda la documentazione della libreria standard per maggiori 
informazioni.)

Spesso si desidera avere un maggior controllo sulla formattazione dell'output, 
piuttosto di limitarsi a scrivere valori separati da spazi. Ci sono diversi 
modi per formattare l'output. 

* Usare le :ref:`formattazioni di stringa<tut-f-strings>`, mettendo una ``f`` 
  o ``F`` prima degli apici iniziali: in questo modo è possibile includere 
  nella stringa un'espressione tra parentesi graffe, che può fare riferimento 
  a variabili o valori. 

  ::

     >>> year = 2016
     >>> event = 'Referendum'
     >>> f'Results of the {year} {event}'
     'Results of the 2016 Referendum'

* Il metodo delle stringhe :meth:`str.format` richiede più lavoro manuale. 
  Potete usare le parentesi graffe per marcare il posto dove una variabile 
  sarà sostituita e potete specificare delle indicazioni dettagliate di 
  formattazione, ma dovete anche indicare quali informazioni formattare. 

  ::

     >>> yes_votes = 42_572_654
     >>> no_votes = 43_132_495
     >>> percentage = yes_votes / (yes_votes + no_votes)
     >>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
     ' 42572654 YES votes  49.67%'

* Infine, potete gestire la stringa "manualmente", usando gli operatori di 
  concatenamento e sezionamento per creare qualunque layout vi venga in mente. 
  Il tipo di dato stringa ha alcuni metodi utili in questo senso, che "mettono 
  in colonna" il testo allineandolo alla spaziatura voluta.

Quando non vi serve un output raffinato, ma vi basta dare un'occhiata ad 
alcune variabili a scopo di debug, potete convertire qualsiasi valore a una 
stringa con le funzioni :func:`repr` o :func:`str`.

La funzione :func:`str` restituisce una rappresentazione leggibile del valore, 
mentre :func:`repr` genera una rappresentazione che può essere consumata 
dall'interprete, o che forza un :exc:`SyntaxError` se non esiste una sintassi 
equivalente. Se un oggetto non ha una rappresentazione leggibile, :func:`str` 
restituisce lo stesso valore di :func:`repr`. Per molti valori, come i numeri 
o costrutti come le liste e i dizionari, entrambe le funzioni producono la 
stessa rappresentazione. Le stringhe, d'altra parte, hanno due 
rappresentazioni diverse. 

Alcuni esempi::

   >>> s = 'Hello, world.'
   >>> str(s)
   'Hello, world.'
   >>> repr(s)
   "'Hello, world.'"
   >>> str(1/7)
   '0.14285714285714285'
   >>> x = 10 * 3.25
   >>> y = 200 * 200
   >>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
   >>> print(s)
   The value of x is 32.5, and y is 40000...
   >>> # repr() aggiunge apici e backslash:
   ... hello = 'hello, world\n'
   >>> hellos = repr(hello)
   >>> print(hellos)
   'hello, world\n'
   >>> # possiamo passare a repr() qualsiasi oggetto come argomento:
   ... repr((x, y, ('spam', 'eggs')))
   "(32.5, 40000, ('spam', 'eggs'))"

Il modulo :mod:`string` contiene una classe :class:`~string.Template` che 
presenta ancora un altro metodo per integrare valori dentro una stringa, 
usando dei segnaposto come ``$x`` e rimpiazzandoli con valori da un 
dizionario; offre però meno controllo sulla formattazione. 

.. _tut-f-strings:

Stringhe formattate
-------------------

Le :ref:`stringhe formattate<f-strings>`, chiamate anche *f-string*, hanno il 
prefisso ``f`` o ``F`` e consentono di inserire delle espressioni Python nella 
stringa, racchiudendole dentro parentesi graffe.

L'espressione può essere seguita da una sintassi che specifica la 
formattazione da applicare: questo permette un maggiore controllo su come il 
valore verrà formattato. Nell'esempio che segue arrotondiamo pi greco a tre 
cifre decimali::

   >>> import math
   >>> print(f'The value of pi is approximately {math.pi:.3f}.')
   The value of pi is approximately 3.142.

Per espandere un "campo" a un numero minimo di caratteri, basta mettere un 
numero intero dopo il ``':'``. Questo è utile per creare incolonnamenti::

   >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
   >>> for name, phone in table.items():
   ...     print(f'{name:10} ==> {phone:10d}')
   ...
   Sjoerd     ==>       4127
   Jack       ==>       4098
   Dcab       ==>       7678

Altri modificatori servono a convertire il valore prima di formattarlo. 
``'!a'`` converte in :func:`ascii`, ``'!s'`` applica la funzione :func:`str`, 
e ``'!r'`` applica :func:`repr`::

   >>> animals = 'eels'
   >>> print(f'My hovercraft is full of {animals}.')
   My hovercraft is full of eels.
   >>> print(f'My hovercraft is full of {animals!r}.')
   My hovercraft is full of 'eels'.

Informazioni complete su come specificare la formattazione si trovano nella 
guida di riferimento nella sezione 
:ref:`Linguaggio di specifica della formattazione<formatspec>`.

.. _tut-string-format:

Il metodo format() delle stringhe
---------------------------------

L'uso più semplice del metodo :meth:`str.format` è qualcosa del genere::

   >>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
   We are the knights who say "Ni!"

Le parentesi graffe e i caratteri che contengono (i "campi da formattare") 
vengono sostituiti dai valori passati al metodo :meth:`str.format`. 
All'interno delle parentesi, è possibile usare un numero per riferirsi alla 
posizione degli argomenti passati a :meth:`str.format`. ::

   >>> print('{0} and {1}'.format('spam', 'eggs'))
   spam and eggs
   >>> print('{1} and {0}'.format('spam', 'eggs'))
   eggs and spam

Se a :meth:`str.format` vengono passati degli argomenti keyword, è possibile 
usare il nome dell'argomento per riferirsi al rispettivo valore::

   >>> print('This {food} is {adjective}.'.format(
   ...       food='spam', adjective='absolutely horrible'))
   This spam is absolutely horrible.

Argomenti posizionali e keyword possono essere usati insieme::

   >>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
   ...                                                    other='Georg'))
   The story of Bill, Manfred, and Georg.

.. l'originale è scritto male e quindi lexato in modo non corretto. 

Quando avete una stringa da formattare molto lunga e volete dividerla, può far 
comodo riferirsi alle variabili da formattare per nome, non per posizione. Ciò 
può essere fatto semplicemente passando un dizionario e usando la notazione 
con le parentesi quadre ``'[]'`` per accedere alle sue chiavi::

   >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
   >>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
   ...       'Dcab: {0[Dcab]:d}'.format(table))
   Jack: 4098; Sjoerd: 4127; Dcab: 8637678

Un'alternativa è passare il dizionario della tabella come argomento keyword, 
con la notazione '**'. ::

   >>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
   >>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
   Jack: 4098; Sjoerd: 4127; Dcab: 8637678

Questo metodo è particolarmente utile in combinazione con la funzione 
predefinita :func:`vars`, che restituisce un dizionario che contiene tutte le 
variabili locali.

Per esempio, questo produce delle colonne bene allineate che mostrano i numeri 
interi, i loro quadrati e cubi::

   >>> for x in range(1, 11):
   ...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
   ...
    1   1    1
    2   4    8
    3   9   27
    4  16   64
    5  25  125
    6  36  216
    7  49  343
    8  64  512
    9  81  729
   10 100 1000

Per una discussione completa della formattazione con :meth:`str.format`, si 
veda :ref:`Sintassi della formattazione delle stringhe<formatstrings>`.

Formattazione manuale delle stringhe
------------------------------------

Ecco lo stesso esempio dei quadrati e dei cubi, formattato manualmente::

   >>> for x in range(1, 11):
   ...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
   ...     # notare l'uso di 'end' nella riga precedente
   ...     print(repr(x*x*x).rjust(4))
   ...
    1   1    1
    2   4    8
    3   9   27
    4  16   64
    5  25  125
    6  36  216
    7  49  343
    8  64  512
    9  81  729
   10 100 1000

Si noti che il singolo spazio aggiunto tra le colonne è dovuto al modo in cui 
funziona :func:`print`, che aggiunge sempre uno spazio tra i suoi argomenti.

Il metodo :meth:`str.rjust` giustifica a destra una stringa rispetto a un 
campo di determinata lunghezza, aggiungendo gli spazi necessari a sinistra. 
Esistono metodi analoghi :meth:`str.ljust` e :meth:`str.center`. Questi metodi 
non producono output, si limitano a restituire una nuova stringa. Se la 
stringa da giustificare è troppo lunga rispetto al campo, non la troncano ma 
si limitano a restituirla inalterata: questo scompaginerà il vostro output, ma 
è senz'altro meglio dell'alternativa, ovvero alterare il dato. (Se davvero 
preferite troncare, potete fare un sezionamento, per esempio 
``x.ljust(n)[:n]``.)

Un altro metodo, :meth:`str.zfill`, completa una stringa numerica con degli 
"0" a sinistra. Inoltre capisce quando trova il segno positivo o negativo::

   >>> '12'.zfill(5)
   '00012'
   >>> '-3.14'.zfill(7)
   '-003.14'
   >>> '3.14159265359'.zfill(5)
   '3.14159265359'

Vecchio metodo di formattazione
-------------------------------

L'operatore ``%`` (modulo) può anche essere usato per la formattazione delle 
stringhe. Data la sintassi ``'stringa' % valori``, le occorrenze di ``%`` in 
``'stringa'`` sono rimpiazzate da zero o più elementi di ``valori``. Questa 
operazione viene chiamata comunemente "interpolazione di stringa". Per 
esempio::

   >>> import math
   >>> print('The value of pi is approximately %5.3f.' % math.pi)
   The value of pi is approximately 3.142.

Per ulteriori informazioni, si veda la sezione :ref:`Formattazione di stringa 
in stile printf<old-string-formatting>`.

.. _tut-files:

Leggere e scrivere files
========================

.. index::
   builtin: open
   object: file

La funzione :func:`open` restituisce un :term:`oggetto-file<file object>` e si 
usa in genere con due argomenti posizionali e uno *keyword*: 
``open(filename, mode, encoding=None)``.

::

   >>> f = open('workfile', 'w', encoding='utf-8')

.. XXX str(f) is <io.TextIOWrapper object at 0x82e8dc4>

   >>> print(f)
   <open file 'workfile', mode 'w' at 80a0960>

Il primo parametro è una stringa che indica il nome del file. Il secondo è una 
stringa che descrive il modo in cui il file verrà usato. Il *modo* può essere 
``'r'`` quando il file verrà solo letto, ``'w'`` per le operazioni di sola 
scrittura (un eventuale file pre-esistente verrà cancellato), e ``'a'`` che 
aggiunge alla fine del file tutti i dati che vengono scritti. ``'r+'`` 
consente sia la lettura sia la scrittura. Passare un *modo* è opzionale: se 
l'argomento è omesso, il file è aperto in modalità ``'r'`` di default. 

In genere i file sono aperti in modalità testuale (:dfn:`text mode`), il che 
significa leggere e scrivere delle *stringhe* di testo con un encoding 
specificato. Se l'encoding non è indicato, il default dipende dalla 
piattaforma (si veda la documentazione della funzione :func:`open`). 
Dal momento che UTF-8 è ormai lo standard di fatto, ``encoding='utf-8'`` è 
raccomandato, a meno di essere certi di aver bisogno di un altro encoding. 
Se si aggiunge una ``'b'`` all'argomento *mode*, il file è aperto in modalità 
binaria (:dfn:`binary mode`): i dati sono letti e scritti in forma di *bytes*. 
Tutti i file che non contengono testo dovrebbero essere aperti con questa 
modalità. 

In modalità testuale, Python, in lettura, converte a ``\n`` gli "a-capo" 
caratteristici della piattaforma (``\n`` su Unix, ``\r\n`` su Windows). In 
scrittura, tutti gli ``\n`` sono ri-convertiti secondo la convenzione della 
piattaforma. Queste modifiche dietro le quinte vanno bene per i file di testo, 
ma corrompono i dati binari di un file :file:`JPEG` o :file:`EXE`. Occorre 
prestare attenzione ad aprire questi file solo in modalità binaria. 

È buona pratica usare l'istruzione :keyword:`with` quando si deve gestire un 
oggetto-file. In questo modo il vantaggio è che il file verrà sempre chiuso al 
termine delle operazioni, anche se nel frattempo dovesse essere emessa 
un'eccezione. Usare :keyword:`!with` è anche più sintetico del corrispondente 
blocco :keyword:`try`\ -\ :keyword:`finally`::

    >>> with open('workfile', encoding='utf-8') as f:
    ...     read_data = f.read()

    >>> # In effetti il file è stato chiuso automaticamente:
    >>> f.closed
    True

Se non usate :keyword:`with`, allora dovreste chiamare ``f.close()`` per 
chiudere il file e liberare immediatamente le risorse di sistema collegate. 

.. warning::
   Chiamare ``f.write()`` senza usare :keyword:`!with` o chiamare 
   ``f.close()`` **potrebbe** comportare che gli argomenti di ``f.write()`` 
   non siano scritti completamente nel file su disco, anche se il programma 
   dovesse terminare senza problemi. 

.. See also https://bugs.python.org/issue17852 

Una volta chiuso il file, sia con un'istruzione :keyword:`with` sia chiamando 
``f.close()``, ogni tentativo di usarlo di nuovo fallirà automaticamente::

   >>> f.close()
   >>> f.read()
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ValueError: I/O operation on closed file.

.. _tut-filemethods:

Metodi degli oggetti-file
-------------------------

In ciascuno degli esempi seguenti assumiamo che un oggetto-file ``f`` sia 
stato appena creato.

Per leggere il contenuto di un file, chiamate ``f.read(size)``, che legge una 
determinata quantità di dati e li restituisce in forma di stringa (in modalità 
testuale) o di oggetti byte (in modalità binaria). *Size* è un parametro 
numerico opzionale. Se *size* è omesso, o è negativo, l'intero contenuto del 
file verrà letto e restituito: può essere un problema se il file occupa il 
doppio della memoria disponibile. Altrimenti, al massimo un numero *size* di 
caratteri (in modalità testuale) o di byte (in modalità binaria) verranno 
letti e restituiti. Se è stata raggiunta la fine del file, ``f.read()`` 
restituisce una stringa vuota (``''``). ::

   >>> f.read()
   'Questo è tutto il file.\n'
   >>> f.read()
   ''

``f.readline()`` legge una singola riga del file. Lascia il carattere di 
"a-capo" finale (``\n``) nella stringa restituita, omettendolo solo alla fine 
se il file non termina con una nuova riga. In questo modo il valore di ritorno 
non è ambiguo: se ``f.readline()`` restituisce una stringa vuota, vuol dire 
che è stata raggiunta la fine del file; invece, una riga vuota nel file è 
restituita come ``'\n'``, ovvero una stringa che contiene solo il carattere di 
"a-capo". ::

   >>> f.readline()
   'Questa è la prima riga del file.\n'
   >>> f.readline()
   'Seconda riga del file.\n'
   >>> f.readline()
   ''

Per leggere le righe di un file, è possibile iterare sull'oggetto-file. Questo 
metodo è efficiente per il consumo di memoria, veloce e porta a scrivere 
codice più semplice::

   >>> for line in f:
   ...     print(line, end='')
   ...
   Questa è la prima riga del file.
   Seconda riga del file.

Se volete mettere tutte le righe di un file in una lista, potete usare 
``list(f)`` o ``f.readlines()``.

``f.write(string)`` scrive il contenuto di una *stringa* in un file e 
restituisce il numero dei caratteri che sono stati scritti::

   >>> f.write('This is a test\n')
   15

Altri tipi di oggetti devono essere convertiti prima di scriverli, o in una 
stringa (in modalità testuale) o in bytes (in modalità binaria)::

   >>> value = ('the answer', 42)
   >>> s = str(value)  # converte la tupla in una stringa
   >>> f.write(s)
   18

``f.tell()`` restituisce un numero intero che rappresenta la posizione 
corrente nell'oggetto-file, come numero di byte a partire dall'inizio del 
file, se questo è aperto in modalità binaria; se è aperto in modalità 
testuale, il numero non indica tuttavia il numero di caratteri. 

Per cambiare la posizione nell'oggetto-file, usate ``f.seek(offset, whence)``. 
La nuova posizione è calcolata aggiungendo *offset* a un punto di riferimento 
indicato dall'argomento *whence*. Passando 0 a *whence*, la misura viene fatta 
dall'inizio del file; 1 indica la posizione attuale; 2 usa la fine del file 
come punto di riferimento. Se l'argomento *whence* viene omesso, il suo 
default è 0, ovvero l'inizio del file è preso come riferimento:: 

   >>> f = open('workfile', 'rb+')
   >>> f.write(b'0123456789abcdef')
   16
   >>> f.seek(5)      # vai al sesto byte del file
   5
   >>> f.read(1)
   b'5'
   >>> f.seek(-3, 2)  # vai al terzultimo byte prima della fine
   13
   >>> f.read(1)
   b'd'

In modalità testuale (per i file aperti senza una ``b`` passata all'argomento 
*mode*) è permesso di riferirsi solo all'inizio del file, con la sola 
eccezione di un ``seek(0, 2)`` che si riferisce esattamente alla fine del 
file; inoltre gli unici *offset* validi sono quelli restituiti da 
``f.tell()``, oppure 0. Tutti gli altri possibili *offset* producono risultati 
non definiti. 

Gli oggetti-file dispongono di altri metodi di uso meno frequente, come 
:meth:`~file.isatty` o :meth:`~file.truncate`; rimandiamo alla documentazione 
della libreria standard per informazioni complete su questi oggetti.

.. _tut-json:

Persistenza di dati strutturati con :mod:`json`
-----------------------------------------------

.. index:: module: json

Le stringhe si possono leggere e scrivere facilmente nei file. I numeri 
richiedono un piccolo sforzo aggiuntivo, dal momento che il metodo 
:meth:`read` restituisce solo una stringa, che quindi deve poi essere passata 
per la conversione a funzioni come :func:`int`, che riceve stringhe come 
``'123'`` e restituisce il corrispondente valore numerico 123. Tuttavia, 
quando volete "salvare" strutture-dati più complesse come liste annidate e 
dizionari, diventa complicato fare a mano il *parsing* e la serializzazione. 

Invece di costringervi a scrivere e correggere continuamente del codice per 
persistere dati complessi nei file, Python vi consente di usare un formato di 
interscambio popolare, chiamato 
`JSON (JavaScript Object Notation) <http://json.org>`_. Il modulo :mod:`json` 
della libreria standard converte gerarchie di dati Python nelle loro 
rappresentazioni in formato stringa: questo processo si chiama serializzazione 
(:dfn:`serializing`). Ricostruire i dati a partire dalla loro rappresentazione 
si chiama deserializzazione (:dfn:`deserializing`). Nell'intervallo tra i due 
processi, la stringa che rappresenta l'oggetto può essere salvata in un file o 
altro tipo di struttura, o inviata a un computer remoto tramite una 
connessione di rete. 

.. note::
   Il formato JSON è molto usato dalle applicazioni moderne per lo scambio dei 
   dati. Molti programmatori lo conoscono già, e questo lo rende una buona 
   scelta per l'interoperabilità. 

Dato un oggetto ``x``, potete ricavarne la rappresentazione JSON con una sola 
riga di codice::

   >>> import json
   >>> x = [1, 'simple', 'list']
   >>> json.dumps(x)
   '[1, "simple", "list"]'

Una variante della funzione :func:`~json.dumps`, chiamata :func:`~json.dump`, 
serializza l'oggetto e lo scrive in un :term:`file di testo<text file>`. 
Quindi, se ``f`` è un file aperto in modalità di scrittura, potete fare 
questo::

   json.dump(x, f)

Per ricostruire l'oggetto, se ``f`` è un file binario o di testo aperto 
in modalità di lettura, basta fare::

   x = json.load(f)

.. note::
   I file JSON devono avere encoding UTF-8. Usate ``encoding='utf-8'`` al 
   momento di aprire un JSON come file di testo, in lettura o in scrittura. 

Questa tecnica di serializzazione è semplice e riesce a gestire liste e 
dizionari; tuttavia, serializzare istanze di classi arbitrarie in JSON 
richiede qualche sforzo ulteriore. Si veda la documentazione del modulo 
:mod:`json` per ulteriori spiegazioni. 

.. seealso::

   il modulo :mod:`pickle`

   Al contrario di :ref:`JSON <tut-json>`, il protocollo di *pickle* permette 
   la serializzazione di oggetti Python complessi. Di conseguenza, è specifico 
   di Python e non può essere usato per comunicare con applicazioni scritte in 
   altri linguaggi. Inoltre è intrinsecamente non sicuro: deserializzare un 
   *pickle* che proviene da una fonte non affidabile può provocare 
   l'esecuzione di codice arbitrario, se i dati sono stati confezionati da un 
   attaccante abile. 
