.. _tut-modules:

******
Moduli
******

Se chiudete l'interprete di Python e poi vi rientrate, non ritroverete le 
definizioni che avevate impostato (funzioni e variabili). Di conseguenza, se 
volete scrivere un programma più lungo, vi conviene usare un editor di testo 
per preparare le istruzioni per l'interprete, e invocarlo poi con il file 
risultante come input. In questo modo avete creato uno *script*. Quando poi il 
vostro programma diventa più lungo, potreste volerlo dividere in diversi file 
più maneggevoli. Potreste anche voler usare in diversi programmi le stesse 
funzioni utili che avete scritto, senza bisogno di copiarle tutte le volte. 

A questo scopo, in Python potete mettere le definizioni in un file e usarle 
poi in uno script o nella sessione interattiva dell'interprete. Un file di 
questo tipo è un *modulo*; le definizioni di un modulo possono essere 
*importate* in altri moduli o nel modulo *principale* (ovvero, l'insieme delle 
variabili a cui avete accesso da uno script quando è eseguito, o dalla 
modalità interattiva).

Un modulo è un file che contiene definizioni e istruzioni Python. Il nome del 
file è quello del modulo più il suffisso :file:`.py`. Dentro il modulo, il 
nome è disponibile come valore della variabile globale ``__name__`` (una 
stringa). Per esempio, usate il vostro editor preferito per creare un file dal 
nome :file:`fibo.py` nella directory corrente, che contiene questo::

   # modulo per i numeri di Finonacci

   def fib(n):    # scrive i numeri di Fibonacci fino a n
       a, b = 0, 1
       while a < n:
           print(a, end=' ')
           a, b = b, a+b
       print()

   def fib2(n):   # restituisce i numeri di Fibonacci fino a n
       result = []
       a, b = 0, 1
       while a < n:
           result.append(a)
           a, b = b, a+b
       return result

Adesso entrate nell'interprete interattivo dei comandi e importate questo 
modulo così::

   >>> import fibo

Questa istruzione non inserisce i nomi delle funzioni definite in ``fibo`` 
direttamente nel :term:`namespace` corrente (vedi :ref:`tut-scopes` 
per ulteriori dettagli); invece, vi inserisce il nome 
del modulo ``fibo``. Usando il nome del modulo potete accedere alle funzioni 
che contiene::

   >>> fibo.fib(1000)
   0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
   >>> fibo.fib2(100)
   [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
   >>> fibo.__name__
   'fibo'

Se intendete usare spesso una funzione, potete assegnarle un nome locale::

   >>> fib = fibo.fib
   >>> fib(500)
   0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

.. _tut-moremodules:

Approfondimenti sui moduli
==========================

Un modulo può contenere istruzioni eseguibili oltre a definizioni di funzioni. 
Queste istruzioni devono essere intese come un modo di inizializzare il 
modulo. Sono eseguite solo la *prima volta* che il nome del modulo è 
incontrato in una istruzione ``import``. [#]_ (Sono anche eseguite se il 
modulo è eseguito come script.) 

Ciascun modulo ha un suo namespace privato, che vale come namespace globale 
per tutte le funzioni che vi sono definite. Quindi l'autore del modulo può 
usare delle variabili globali senza preoccuparsi di conflitti accidentali con 
le variabili globali dell'utente del modulo. D'altra parte, se siete sicuri di 
quello che fate, potete accedere alle variabili globali del modulo con la 
stessa notazione che usate per riferirvi alle sue funzioni, ovvero 
``modname.itemname``.

I moduli possono importare altri moduli. È consuetudine, ma non obbligatorio, 
mettere tutte le istruzioni :keyword:`import` all'inizio del modulo (o dello 
script). I nomi dei moduli importati, se collocati al livello più alto del 
modulo (fuori da ogni classe o funzione) sono inseriti nel namespace 
globale del modulo importatore.

Esiste una variante dell'istruzione :keyword:`import` che consente di 
importare direttamente i nomi contenuti in un modulo nella tabella dei 
simboli del modulo importatore. Per esempio::

   >>> from fibo import fib, fib2
   >>> fib(500)
   0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

In questo modo però il nome del modulo, i cui nomi interni sono importati, non 
è importato esso stesso (quindi, in questo esempio, ``fibo`` non è definito).

C'è poi una variante che consente di importare *tutti* i nomi definiti in un 
modulo::

   >>> from fibo import *
   >>> fib(500)
   0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

In questo modo vengono importati tutti i nomi del modulo, eccetto quelli che 
iniziano con un *underscore* (``_``). In genere i programmatori Python non 
usano questa tecnica, dal momento che introduce un numero sconosciuto di nomi 
nell'interprete, eventualmente sovrascrivendo nomi che erano già stati 
definiti. 

Si noti che in generale importare ``*`` da un modulo o da un package è 
considerato cattiva pratica, perché spesso rende il codice più difficile da 
leggere. Tuttavia va bene usare questa tecnica nelle sessioni interattive, per 
risparmiare battute nei nomi da inserire. 

Se il nome del modulo è seguito dalla parola-chiave :keyword:`!as`, allora il 
nome che segue :keyword:`!as` è collegato direttamente al modulo importato.

::

   >>> import fibo as fib
   >>> fib.fib(500)
   0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

Questo modo di importare il modulo è del tutto equivalente a ``import fibo``, 
con l'unica differenza che adesso il modulo sarà disponibile con il nome 
``fib``.

Si può anche usare in combinazione con la parola-chiave :keyword:`from`, con 
effetti analoghi::

   >>> from fibo import fib as fibonacci
   >>> fibonacci(500)
   0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

.. note::

   Per ragioni di efficienza, ogni modulo è importato solo una volta nella 
   sessione dell'interprete. Di conseguenza, se nel frattempo modificate il 
   vostro modulo, dovete riavviare l'interprete. In alternativa, se si tratta 
   di un modulo che state testando interattivamente, potete usare la funzione 
   :func:`importlib.reload`, ovvero scrivere 
   ``import importlib; importlib.reload(modulename)``.

.. _tut-modulesasscripts:

Eseguire moduli come script
---------------------------

Quando eseguite un modulo Python con ::

   python fibo.py <arguments>

il codice del modulo verrà eseguito, proprio come se lo aveste importato, ma 
la variabile ``__name__`` sarà impostata a ``"__main__"``. Ciò vuol dire che, 
se inserite alla fine del modulo questa clausola::

   if __name__ == "__main__":
       import sys
       fib(int(sys.argv[1]))

potete rendere questo file utilizzabile sia come script sia come modulo 
importabile, perché il codice incluso nella clausola, che parsa la riga di 
comando, verrà eseguito solo quando il modulo è eseguito come il file "main": 

.. code-block:: shell-session

   $ python fibo.py 50
   0 1 1 2 3 5 8 13 21 34

Se il modulo è importato, il codice non verrà eseguito::

   >>> import fibo
   >>>

Questa tecnica è usata spesso, sia per fornire una comoda interfaccia utente 
per un modulo, sia per eseguire dei test (facendo in modo che, quando si 
esegue il modulo come script, si esegua una suite di test).

.. _tut-searchpath:

Il percorso di ricerca dei moduli
---------------------------------

.. index:: triple: module; search; path

Quando importiamo un modulo di nome :mod:`!spam`, l'interprete per prima cosa 
cerca tra i moduli predefiniti se ne esiste uno con quel nome. Questi sono 
elencati in :data:`sys.builtin_module_names`. Se non lo 
trova, cerca un file :file:`spam.py` in una lista di directory contenuta nella 
variabile :data:`sys.path`. Questa, a sua volta, viene inizializzata con le 
seguenti *path*:

* La directory che contiene lo script importatore (o la directory corrente se 
  questo non è specificato).
* La variabile d'ambiente :envvar:`PYTHONPATH` (se impostata, contiene una 
  lista di directory, con la stessa sintassi della variabile :envvar:`PATH`).
* Un default che dipende dall'installazione di Python (che per convenzione 
  include una directory ``site-packages`` gestita dal modulo :mod:`site`). 

Altri dettagli si trovano nella documentazione: :ref:`sys-path-init`.

.. note::
   Nei file system che supportano i symlink, la directory che contiene lo 
   script importatore è calcolata dopo aver seguito i symlink. In altre 
   parole, la directory che contiene il symlink *non* è aggiunta al percorso 
   di ricerca dei moduli.

Dopo che è stata inizializzata, è possibile modificare :data:`sys.path` 
dall'interno di un programma Python. La directory che contiene lo script in 
esecuzione è collocata all'inizio del lista dei percorsi da cercare, davanti 
alla directory della libreria standard. Ciò vuol dire che i moduli locali, se 
hanno lo stesso nome, verranno importati al posto di quelli della libreria 
standard. In genere questo è un errore, a meno che non sia fatto 
intenzionalmente. Si veda la sezione :ref:`tut-standardmodules` per maggiori 
informazioni.

.. %
    Do we need stuff on zip files etc. ? DUBOIS

.. _tut-pycache:

File "compilati"
----------------

Per velocizzare il caricamento dei moduli, Python conserva nella directory di 
cache ``__pycache__`` una versione compilata di ciascun modulo, con il nome 
:file:`module.{version}.pyc`, dove *version* specifica il formato del file 
compilato: di solito è il numero di versione di Python. Per esempio, in 
CPyhton 3.3 la versione compilata del modulo ``spam.py`` si chiamerebbe 
``__pycache__/spam.cpython-33.pyc``. Questa convenzione permette la 
coesistenza di moduli compilati da diverse versioni di Python. 

Python confronta la data di ultima modifica del modulo con la sua versione 
compilata, e ricompila all'occorrenza. Questo processo è completamente 
automatico. Inoltre, i moduli compilati sono indipendenti dalla piattaforma, 
così che lo stesso modulo possa essere condiviso su sistemi diversi, con 
diverse architetture. 

Python non controlla la cache in due circostanze. In primo luogo, quando un 
modulo è caricato direttamente dalla riga di comando, Python ricompila sempre 
il modulo senza conservarlo nella cache. In secondo luogo, non controlla la 
cache se non c'è anche il modulo originale. Per ottenere una distribuzione 
senza sorgenti (solo compilata), oltre a togliere il modulo originale, il 
modulo compilato deve essere collocato nella directory dei file originali. 

Alcuni consigli per gli esperti:

* Potete usare le opzioni :option:`-O` o :option:`-OO` della riga di comando 
  Python per ridurre le dimensioni del modulo compilato. La ``-O`` rimuove le 
  istruzioni *assert*, mentre ``-OO`` rimuove sia gli *assert* sia le 
  docstring. Dal momento che alcuni programmi potrebbero averne bisogno, usate 
  queste opzioni solo se sapete che cosa state facendo. I moduli "ottimizzati" 
  hanno un contrassegno ``opt-`` e di solito sono più piccoli. Future versioni 
  di Python potrebbero cambiare gli effetti dell'ottimizzazione. 

* Un programma non è più veloce se usa i file ``.pyc`` invece dei normali 
  ``.py``. L'unica differenza è la velocità di *caricamento* del modulo. 

* Il modulo :mod:`compileall` della libreria standard può compilare tutti i 
  moduli di una directory.

* Si veda la :pep:`3147` per ulteriori dettagli su questi procedimenti, 
  incluso un diagramma di flusso dei vari passaggi. 

.. _tut-standardmodules:

Moduli della libreria standard
==============================

.. index:: pair: module; sys

Python è distribuito con una libreria standard di moduli, documentata in un 
una sezione separata, la Guida di Riferimento della Libreria Standard. Alcuni 
moduli sono pre-caricati nell'interprete: questi forniscono delle operazioni 
che non fanno parte del linguaggio, ma sono comunque predefinite, sia per 
ragioni di efficienza, sia per dare accesso alle primitive del sistema 
operativo sottostante. La composizione di questi moduli dipende dalla 
configurazione, che a sua volta dipende dalla piattaforma. Per esempio, 
:mod:`winreg` è solo disponibile su Windows. Un modulo meritevole di 
attenzione particolare è :mod:`sys`, sempre disponibile. Le variabili 
``sys.ps1`` e ``sys.ps2`` definiscono le stringhe usate per il prompt primario 
e secondario::

   >>> import sys
   >>> sys.ps1
   '>>> '
   >>> sys.ps2
   '... '
   >>> sys.ps1 = 'C> '
   C> print('Yuck!')
   Yuck!
   C>

Queste variabili sono disponibili solo se l'interprete è in modalità 
interattiva. 

La variabile ``sys.path`` è una lista di stringhe che determina il percorso di 
ricerca dei moduli da importare. È inizializzata con delle path contenute 
nella variabile d'ambiente :envvar:`PYTHONPATH`, oppure da default predefiniti 
se questa non è impostata. Potete modificare ``sys.path`` con le normali 
tecniche di manipolazione delle liste::

   >>> import sys
   >>> sys.path.append('/ufs/guido/lib/python')

.. _tut-dir:

La funzione :func:`dir`
=======================

La funzione predefinita :func:`dir` ci dice quali nomi sono definiti in un 
modulo. Restituisce una lista ordinata di stringhe::

   >>> import fibo, sys
   >>> dir(fibo)
   ['__name__', 'fib', 'fib2']
   >>> dir(sys)  # doctest: +NORMALIZE_WHITESPACE
   ['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
    '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
    '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
    '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
    '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
    'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
    'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
    'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
    'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
    'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
    'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
    'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
    'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
    'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
    'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
    'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
    'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
    'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
    'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
    'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
    'warnoptions']

Senza argomenti, :func:`dir` elenca i nomi disponibili attualmente::

   >>> a = [1, 2, 3, 4, 5]
   >>> import fibo
   >>> fib = fibo.fib
   >>> dir()
   ['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']

Si noti che nell'elenco compaiono tutti i tipi di nomi: variabili, moduli, 
funzioni e così via. 

.. index:: pair: module; builtins

:func:`dir` non elenca però i nomi delle funzioni e delle variabili 
predefinite. Se volete un lista di questi, sono definiti nel modulo 
:mod:`builtins`::

   >>> import builtins
   >>> dir(builtins)  # doctest: +NORMALIZE_WHITESPACE
   ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
    'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
    'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
    'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
    'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
    'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
    'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
    'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
    'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
    'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
    'NotImplementedError', 'OSError', 'OverflowError',
    'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
    'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
    'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
    'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
    'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
    'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
    'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
    '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
    'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
    'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
    'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
    'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
    'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
    'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
    'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
    'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
    'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
    'zip']

.. _tut-packages:

Package
=======

I package sono un modo di strutturare il *namespace* di un modulo Python 
usando la "notazione col punto". Per esempio, il nome :mod:`!A.B` indica un 
sotto-modulo ``B`` all'interno di un package ``A``. Proprio come i moduli 
permettono a diversi autori di non doversi preoccupare dei nomi *di variabile* 
usati in altri moduli, così i package permettono agli autori di package con 
molti moduli, come NumPy o Pillow, di non doversi preoccupare dei nomi 
*dei moduli* usati da altri. 

Immaginate di voler costruire una collezione di moduli (un package) per la 
gestione di suoni e file sonori. Ci sono diversi formati di file sonori (di 
solito sono riconoscibili dalle estensioni, per esempio :file:`.wav`, 
:file:`.aiff`, :file:`.au`): quindi avrete bisogno di creare e mantenere una 
raccolta crescente di moduli per la conversione tra i vari formati. Ci sono 
poi molte diverse operazioni che si possono fare sui suoni (mixare, aggiungere 
eco, equalizzare, creare un effetto stereo artificiale): quindi dovrete 
scrivere una serie interminabile di moduli che implementano queste operazioni. 
Ecco una possibile struttura per il vostro package (espressa in forma di 
gerarchia del file system):

.. code-block:: text

   sound/                          package top-level
         __init__.py               inizializzazione del package
         formats/                  sotto-package per le conversioni
                 __init__.py
                 wavread.py
                 wavwrite.py
                 aiffread.py
                 aiffwrite.py
                 auread.py
                 auwrite.py
                 ...
         effects/                  sotto-package per gli effetti
                 __init__.py
                 echo.py
                 surround.py
                 reverse.py
                 ...
         filters/                  sotto-package per i filtri
                 __init__.py
                 equalizer.py
                 vocoder.py
                 karaoke.py
                 ...

Quando importate il package, Python cerca nei percorsi della ``sys.path`` la 
directory del package.

I file :file:`__init__.py` sono necessari perché Python consideri 
effettivamente come un package la directory che contiene i moduli (a meno che
non siano dei :term:`namespace package`, una possibilità più avanzata). Questo è 
per evitare che directory con un nome comune, per esempio ``string``, possano 
nascondere inavvertitamente dei nomi di moduli che vengono dopo nell'ordine 
dei percorsi di ricerca. Nel caso più semplice, :file:`__init__.py` può essere 
lasciato vuoto, ma è anche possibile fargli eseguire del codice di 
inizializzazione o impostare la variabile ``__all__``, come vedremo tra poco. 

Gli utenti del package possono importare dei singoli moduli al suo interno, 
per esempio::

   import sound.effects.echo

Questo carica il modulo :mod:`!sound.effects.echo`. Occorre riferirsi a questo 
con il nome completo. ::

   sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

Un modo alternativo per importare il modulo è questo::

   from sound.effects import echo

Anche in questo modo carichiamo il modulo :mod:`!echo`, ma lo rendiamo 
disponibile senza il prefisso del nome del package. Può essere quindi usato 
così::

   echo.echofilter(input, output, delay=0.7, atten=4)

Un altro modo ancora è importare direttamente la funzione o la variabile 
richiesta::

   from sound.effects.echo import echofilter

Ancora una volta, questo carica il modulo :mod:`!echo`, rendendo però 
direttamente disponibile la sua funzione :func:`!echofilter`::

   echofilter(input, output, delay=0.7, atten=4)

Notate che quando si usa la modalità ``from package import item``, allora 
*item* può essere sia il nome di un modulo (o sotto-package) del package, sia 
qualche altro nome definito nel package, come una funzione, una classe o una 
variabile. L'istruzione ``import`` per prima cosa controlla se *item* è 
definito nel package; se no, assume che si tratti di un modulo e cerca di 
caricarlo. Se l'operazione fallisce, viene emessa un'eccezione 
:exc:`ImportError`.

Al contrario, quando usate la sintassi ``import item.subitem.subsubitem``, 
ogni elemento eccetto l'ultimo *deve* essere un package; l'ultimo può essere 
un package o un modulo, ma *non* può essere una classe o una funzione o una 
variabile definita nell'elemento precedente. 

.. _tut-pkg-import-star:

Importare \* da un package
--------------------------

.. index:: single: __all__

Che cosa succede quando scriviamo ``from sound.effects import *``? Idealmente, 
ci si potrebbe aspettare che questa istruzione provochi una scansione nel file 
system, trovi i moduli presenti nel package e li importi tutti in un colpo 
solo. Questo però potrebbe richiedere molto tempo e importare un sotto-modulo 
potrebbe causare *side-effect* indesiderati, che dovrebbero verificarsi solo 
quando il modulo è importato direttamente. 

L'unica soluzione è che l'autore del package fornisca un indice esplicito del 
suo contenuto. L'istruzione :keyword:`import` segue questa convenzione: se il 
modulo :file:`__init__.py` di un package definisce una lista col nome 
``__all__``, allora considera questa come l'indice dei moduli che dovrebbero 
essere importati da un ``from package import *``. È compito dell'autore 
aggiornare la lista quando rilascia una nuova versione del package. Un autore 
potrebbe anche non fornire la lista, se decide che non può essere utile 
importare "\*" dal suo package. Per esempio, il file 
:file:`sound/effects/__init__.py` potrebbe contenere questo codice::

   __all__ = ["echo", "surround", "reverse"]

In questo modo, ``from sound.effects import *`` importerebbe i tre moduli 
indicati del package :mod:`!sound.effects`.

Attenzione però che i sotto-moduli potrebbero finire "coperti" da nomi 
definiti localmente. Per esempio, se aggiungete una funzione ``reverse`` al 
file :file:`sound/effects/__init__.py`, allora ``from sound.effects import *`` 
finirebbe per importare solo i due sotto-moduli ``echo`` e ``surround`` ma 
**non** anche il modulo ``reverse``, perché sarebbe nascosto dalla funzione 
``reverse`` definita localmente::

    __all__ = [
        "echo",      # si riferisce al file 'echo.py' 
        "surround",  # si riferisce al file 'surround.py' 
        "reverse",   # !!! si riferisce alla funzione 'reverse' adesso !!! 
    ] 

    def reverse(msg: str):  # <-- questo nome copre il modulo 'reverse.py' 
        return msg[::-1]    #     se fate un 'from sound.effects import *' 

Se ``__all__`` non è definito, allora l'istruzione 
``from sound.effects import *`` *non* importa comunque tutti i moduli del 
package :mod:`!sound.effects` nel *namespace* corrente. Si limita a garantire 
che il package :mod:`!sound.effects` sia stato effettivamente importato 
eventualmente eseguendo il codice trovato nel file :file:`__init__.py`) e 
quindi importa tutti i nomi definiti nel package: questo comprende tutti i 
nomi definiti (e i moduli esplicitamente importati) nel :file:`__init__.py`. 
Include anche tutti i moduli del package che sono stati esplicitamente 
importati in precedenza. Si consideri questo codice::

   import sound.effects.echo
   import sound.effects.surround
   from sound.effects import *

In questo esempio, i moduli :mod:`!echo` e :mod:`!surround` sono importati nel 
*namespace* corrente perché sono definiti nel package :mod:`!sound.effects` al 
momento di eseguire l'istruzione ``from...import`` (funziona allo stesso modo 
quando la variabile ``__all__`` è definita).

Anche se alcuni moduli sono progettati per esportare solo alcuni nomi, secondo 
certi criteri, quando importate con ``import *``, questa è comunque 
considerata una cattiva pratica nel codice "di produzione". 

Ricordate che non c'è niente di male a importare ``from package import
specific_submodule``. In effetti questo è il modo raccomandato, a meno che il 
modulo importatore non stia anche importando un altro modulo con lo stesso 
nome da un altro package. 

.. _intra-package-references:

Riferimenti intra-package
-------------------------

Quando i package contengono a loro volta dei sub-package (come nel caso del 
nostro esempio :mod:`!sound`), potete usare gli import *assoluti* per riferirvi 
a moduli di package "cugini". Per esempio, se il modulo 
:mod:`!sound.filters.vocoder` ha bisogno di usare il modulo :mod:`!echo` nel 
package :mod:`!sound.effects`, può importarlo con 
``from sound.effects import echo``.

Potete anche usare gli import *relativi*, negli import del tipo 
``from module import name``. Gli import relativi usano una notazione con punti 
iniziali per indicare il package corrente e genitore interessati dall'import. 
Dal modulo :mod:`!surround`, per esempio, potreste importare::

   from . import echo
   from .. import formats
   from ..filters import equalizer

Si noti che gli import relativi si basano sul nome del modulo importatore. 
Siccome il nome del modulo principale è sempre ``"__main__"``, i moduli intesi 
per essere usati come script (come il modulo principale di un'applicazione 
Python) devono sempre usare gli import assoluti. 

Package in directory multiple
-----------------------------

I package hanno un attributo speciale :attr:`~module.__path__`. Questa variabile  
è una sequenza di stringhe che contiene il nome della directory dove risiede il  
file :file:`__init__.py` del package, prima che il codice di questo sia eseguito.  
Potete modificare il contenuto della variabile: così facendo modificate i 
percorsi di ricerca dei moduli e dei sub-package del package, per tutte le 
successive importazioni. 

Anche se è una funzionalità raramente necessaria, può essere usata per 
estendere l'insieme dei moduli disponibili in un package. 

.. only:: html

   .. rubric:: Note

.. [#] In effetti anche le definizioni di funzione sono delle "istruzioni" che 
   vengono eseguite; l'esecuzione della definizione di una funzione a livello 
   del modulo aggiunge il nome della funzione al namespace globale. 
