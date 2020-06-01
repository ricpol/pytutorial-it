.. _tut-morecontrol:

******************************************
Altri strumenti per il controllo di flusso
******************************************

Oltre a :keyword:`while` di cui abbiamo già parlato, Python utilizza le consuete istruzioni per il controllo del flusso, comuni a molti linguggi, con qualche peculiarità. 

.. _tut-if:

Istruzione :keyword:`!if`
=========================

Forse l'istruzione più famosa è la :keyword:`if`. Per esempio::

   >>> x = int(input("Please enter an integer: "))
   Please enter an integer: 42
   >>> if x < 0:
   ...     x = 0
   ...     print('Negative changed to zero')
   ... elif x == 0:
   ...     print('Zero')
   ... elif x == 1:
   ...     print('Single')
   ... else:
   ...     print('More')
   ...
   More

Possono esserci nessuna, una o più sezioni :keyword:`elif` e la sezione :keyword:`else` è opzionale. La parola riservata ':keyword:`!elif`' è una scorciatoia per "else if", e permette di evitare troppi livelli annidati. Una sequenza :keyword:`!if` ... :keyword:`!elif` ... :keyword:`!elif` ... sostituisce le istruzioni ``switch`` o
``case`` tipiche di altri linguaggi.

.. _tut-for:

Istruzione :keyword:`!for`
==========================

.. index::
   statement: for

Se siete abituati a Pascal o a C, troverete l'istruzione :keyword:`for` in Python leggermente diversa. Invece di iterare solo su una progressione aritmetica, come in Pascal, o dare la possibilità di definire sia il passo dell'iterazione sia la condizione d'arresto, come in C, il :keyword:`!for` di Python itera sugli elementi di una qualsiasi sequenza (una lista, una stringa...), nell'ordine in cui appaiono nella sequenza. Per esempio, ma senza alcun sottinteso omicida::

   >>> # Misura la lunghezza di alcune stringhe:
   ... words = ['cat', 'window', 'defenestrate']
   >>> for w in words:
   ...     print(w, len(w))
   ...
   cat 3
   window 6
   defenestrate 12

Se occorre modificare una sequenza su cui si sta iterando (per esempio per duplicare certi elementi), è consigliabile farne prima una copia. Iterare su una sequenza non produce automaticamente una copia. Un modo semplice per farlo è usare il sezionamento::

   >>> for w in words[:]:  # Itera su una copia dell'intera lista
   ...     if len(w) > 6:
   ...         words.insert(0, w)
   ...
   >>> words
   ['defenestrate', 'cat', 'window', 'defenestrate']

Se avessimo usato ``for w in words:``, questo esempio avrebbe cercato di creare una lista infinita, continuando a inserire ``defenestrate`` per sempre. 

.. _tut-range:

La funzione :func:`range`
=========================

Se dovete iterare su una sequenza di numeri, la funzione predefinita :func:`range` è molto comoda. Produce una progressione aritmetica::

    >>> for i in range(5):
    ...     print(i)
    ...
    0
    1
    2
    3
    4

Il punto di arresto indicato non fa parte della sequenza generata: ``range(10)`` produce dieci valori, che sono anche gli indici corretti per una sequenza di lunghezza 10. Potete far partire l'intervallo da un numero diverso o specificare un incremento, anche negativo. A volte l'incremento è chiamato "il passo"::

    range(5, 10)
       5, 6, 7, 8, 9

    range(0, 10, 3)
       0, 3, 6, 9

    range(-10, -100, -30)
      -10, -40, -70

Per iterare sugli indici di una sequenza, potete combinare le funzioni :func:`range` e
:func:`len` come segue::

   >>> a = ['Mary', 'had', 'a', 'little', 'lamb']
   >>> for i in range(len(a)):
   ...     print(i, a[i])
   ...
   0 Mary
   1 had
   2 a
   3 little
   4 lamb

In casi del genere, tuttavia, vi conviene usare la funzione :func:`enumerate`: si veda per questo :ref:`tut-loopidioms`.

Se cercate semplicemente di "stampare" un intervallo, succede una cosa strana::

   >>> print(range(10))
   range(0, 10)

L'oggetto restituito da :func:`range` si comporta in modo simile a una lista, ma in effetti non lo è. In realtà è un oggetto che restituisce l'elemento successivo della sequenza desiderata, quando vi iterate sopra, ma non *crea* davvero la lista, per risparmiare spazio. 

Chiamiamo :term:`iterabile<iterable>` un oggetto di questo tipo: ovvero, un oggetto adatto a essere usato da funzioni e costrutti che si aspettano qualcosa da cui ottenere via via elementi successivi, finché ce ne sono. Abbiamo visto che l'istruzione :keyword:`for` è un *iteratore* di questo tipo; un altro è la funzione :func:`list`, che crea liste a partire da *iterabili*::

   >>> list(range(5))
   [0, 1, 2, 3, 4]

Vedremo più in là altri esempi di funzioni che restituiscono degli iterabili, o che accettano iterabili come argomento.

.. _tut-break:

Le istruzioni :keyword:`!break` e :keyword:`!continue`, e la clausola :keyword:`!else` nei cicli
================================================================================================

L'istruzione :keyword:`break` come in C, "salta fuori" dal ciclo :keyword:`for` o :keyword:`while` più interno in cui è inserita.

Le istruzioni di iterazione possono avere una clausola :keyword:`!else`: questa viene eseguita quando il ciclo termina perché la lista si è esaurita (in un :keyword:`for`), o perché la condizione è divenuta "falsa" (in un :keyword:`while`); non viene però eseguita quando il ciclo termina a causa di una istruzione :keyword:`break`. Per esempio, il ciclo seguente ricerca i numeri primi::

   >>> for n in range(2, 10):
   ...     for x in range(2, n):
   ...         if n % x == 0:
   ...             print(n, 'è uguale a', x, '*', n//x)
   ...             break
   ...     else:
   ...         # il ciclo è finito senza trovare un fattore primo
   ...         print(n, 'è un numero primo')
   ...
   2 è un numero primo
   3 è un numero primo
   4 è uguale a 2 * 2
   5 è un numero primo
   6 è uguale a 2 * 3
   7 è un numero primo
   8 è uguale a 2 * 4
   9 è uguale a 3 * 3

(Sì, questo codice è giusto. Fate attenzione: la clausola ``else`` appartiene al ciclo :keyword:`for`, *non* all'istruzione :keyword:`if`.)

Quando viene usata in un ciclo, la clausola ``else`` è più simile alla ``else`` di un'istruzione :keyword:`try`, piuttosto che a quella di un :keyword:`if`. La ``else`` di un'istruzione :keyword:`try` viene eseguita quando non sono rilevate eccezioni, e allo stesso modo la ``else`` di un ciclo viene eseguita quando non ci sono ``break``. Approfondiremo l'istruzione :keyword:`!try` e le eccezioni nel capitolo :ref:`tut-handling`.

L'istruzione :keyword:`continue`, anch'essa un prestito dal C, prosegue con la successiva iterazione del ciclo::

    >>> for num in range(2, 10):
    ...     if num % 2 == 0:
    ...         print("Trovato un numero pari", num)
    ...         continue
    ...     print("Trovato un numero", num)
    Trovato un numero pari 2
    Trovato un numero 3
    Trovato un numero pari 4
    Trovato un numero 5
    Trovato un numero pari 6
    Trovato un numero 7
    Trovato un numero pari 8
    Trovato un numero 9

.. _tut-pass:

L'istruzione :keyword:`!pass`
=============================

L'istruzione :keyword:`pass` non fa nulla. Può essere usata quando sintatticamente è richiesta un'istruzione, ma il programma in sé non ha bisogno di fare nulla. Per esempio::

   >>> while True:
   ...     pass  # Blocca in attesa dell'interruzione da tastiera (Ctrl+C)
   ...

Si usa di solito per creare una classe elementare::

   >>> class MyEmptyClass:
   ...     pass
   ...

Un altro modo di usare :keyword:`pass` è come segnaposto per una funzione o una condizione, quando state scrivendo codice nuovo e volete ragionare in termini più astratti. Il :keyword:`!pass` verrà ignorato silenziosamente::

   >>> def initlog(*args):
   ...     pass   # Ricordati di implementare questa funzione!
   ...

.. _tut-functions:

Definire le funzioni
====================

Possiamo creare una funzione che scrive i numeri di Fibonacci fino a un limite determinato::

   >>> def fib(n):    # scrive la serie di Fibonacci fino a n
   ...     """Scrive la serie di Fibonacci fino a n."""
   ...     a, b = 0, 1
   ...     while a < n:
   ...         print(a, end=' ')
   ...         a, b = b, a+b
   ...     print()
   ...
   >>> # Adesso chiamate la funzione appena definita:
   ... fib(2000)
   0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

.. index::
   single: documentation strings
   single: docstrings
   single: strings, documentation

La parola chiave :keyword:`def` introduce la *definizione* di una funzione. Deve essere seguita dal nome della funzione e da una lista di parametri *formali* tra parentesi. Le istruzioni che compongono il corpo della funzione iniziano nella riga successiva, e devono essere rientrate. 

Opzionalmente, la prima istruzione della funzione può essere una stringa non assegnata: questa è la :dfn:`docstring`, ovvero la stringa di documentazione della funzione. Potete trovare altre informazioni nella sezione :ref:`tut-docstrings`. Esistono strumenti che usano le docstring per generare automaticamente la documentazione online o stampata, o per consentire all'utente di accedervi interattivamente. Includere la documentazione nel vostro codice è una buona pratica e dovrebbe diventare un'abitudine.

*L'esecuzione* di una funzione produce una nuova tabella dei simboli usati per le variabili locali alla funzione. Più precisamente, tutti gli *assegnamenti* fatti all'interno della funzione conservano il valore in una tabella dei simboli locale; invece, i *riferimenti* alle variabili per prima cosa cercano il nome nella tabella locale, quindi nella tabella locale delle eventuali funzioni "superiori" in cui la nostra può essere inclusa, quindi nella tabella dei simboli globali, infine nella tabella dei nomi predefiniti. Di conseguenza è possibile *riferirsi* a una variabile globale o di una funzione superiore, ma non è possibile *assegnarle* un valore (a meno di non ricorrere all'istruzione :keyword:`global` per le variabili globali, o a :keyword:`nonlocal` per quelle delle funzioni superiori).

I parametri *reali* (gli argomenti [#]_) di una funzione sono introdotti nella tabella dei simboli locali nel momento in cui la funzione è chiamata. Quindi, gli argomenti sono "passati per valore" (dove però il "valore" è sempre un *riferimento* all'oggetto, non il valore dell'oggetto). [#]_ Quando una funzione chiama un'altra funzione, una nuova tabella di simboli è creata per quella chiamata. 

La *definizione* della funzione inserisce il nome della funzione nella tabella dei simboli corrente. Il valore assegnato al nome della funzione ha un tipo riconosciuto dall'interprete come un oggetto-funzione definita dall'utente. Questo valore può essere assegnato a un altro nome, che a questo punto può essere utilizzato come la funzione stessa. Questo meccanismo consente di rinominare le cose::

   >>> fib
   <function fib at 10042ed0>
   >>> f = fib
   >>> f(100)
   0 1 1 2 3 5 8 13 21 34 55 89

Se avete esperienza con altri linguaggi, potreste obiettare che ``fib`` non è una funzione ma una procedura, dal momento che non restituisce un valore. Tuttavia in Python anche le funzioni senza un'istruzione :keyword:`return` esplicita *restituiscono* in effetti un valore, per quanto piuttosto insignificante. Questo valore si chiama ``None`` (è un nome predefinito). L'interprete di solito evita di emettere direttamente ``None`` in output, quando è l'unica cosa che dovrebbe scrivere. Se volete davvero vedere il ``None``, potete usare la funzione :func:`print`::

   >>> fib(0)
   >>> print(fib(0))
   None

Non è difficile scrivere una funzione che *restituisce* una lista di numeri di Fibonacci, invece di scriverla::

   >>> def fib2(n):  # restituisce i numeri di Fibonacci fino a n
   ...     """Restituisce una lista con i numeri Fibonacci fino a n."""
   ...     result = []
   ...     a, b = 0, 1
   ...     while a < n:
   ...         result.append(a)    # vedi sotto
   ...         a, b = b, a+b
   ...     return result
   ...
   >>> f100 = fib2(100)    # chiama la funzione
   >>> f100                # scrive il risultato
   [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

Questo esempio, come di consueto, introduce alcuni concetti nuovi:

* L'istruzione :keyword:`return` esce dall'esecuzione della funzione restituendo un valore. Se :keyword:`!return` non seguito da alcuna espressione, allora restituisce ``None``. Anche uscire dalla funzione senza un :keyword:`!return` restituisce ``None``.

* L'istruzione ``result.append(a)`` chiama un *metodo* dell'oggetto-lista ``result``. Un metodo è una funzione che "appartiene" all'oggetto e si può chiamare con la sintassi ``obj.methodname`` dove ``obj`` è l'oggetto (che potrebbe essere il risultato di un'espressione) e ``methodname`` è il nome del metodo che è stato definito nel tipo dell'oggetto. Tipi diversi definiscono metodi diversi. Metodi di tipi diversi possono avere lo stesso nome, senza che ciò produca ambiguità. Potete definire i vostri tipi e i vostri metodi, usando le *classi*: vedi :ref:`tut-classes`. Il metodo :meth:`append` mostrato nell'esempio è definito per gli oggetti-lista: aggiunge un nuovo elemento in coda alla lista. In questo esempio è equivalente a ``result = result + [a]``, ma più efficiente. 

.. _tut-defining:

Altre cose sulla definizione delle funzioni
===========================================

È possibile definire le funzioni con un numero variabile di parametri. Ci sono tre modi per fare questo, che si possono combinare tra loro. 

.. _tut-defaultargs:

Parametri con valori di default
-------------------------------

Il modo più utile è specificare un valore di default per uno o più parametri. In questo modo è possibile chiamare la funzione con meno argomenti di quelli che la definizione prescriverebbe. Per esempio::

   def ask_ok(prompt, retries=4, reminder='Please try again!'):
       while True:
           ok = input(prompt)
           if ok in ('y', 'ye', 'yes'):
               return True
           if ok in ('n', 'no', 'nop', 'nope'):
               return False
           retries = retries - 1
           if retries < 0:
               raise ValueError('invalid user response')
           print(reminder)

Questa funzione può essere chiamata in diversi modi:

* passando solo l'argomento necessario:
  ``ask_ok('Do you really want to quit?')``
* passando anche uno degli argomenti opzionali:
  ``ask_ok('OK to overwrite the file?', 2)``
* o passando tutti gli argomenti:
  ``ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')``

Questo esempio introduce anche la parola-chiave :keyword:`in`, che testa se una sequenza contiene un certo valore oppure no.

I valori di default sono valutati al momento della definizione della funzione, nella tabella dei simboli che ospita la definizione. Quindi questo ::

   i = 5

   def f(arg=i):
       print(arg)

   i = 6
   f()

restituirà ``5``.

**Attenzione:**  I valori di default sono valutati una volta sola. Questo fa differenza quando il default è un oggetto *mutabile* come una lista, un dizionario o un'istanza di molte altre classi. Per esempio, questa funzione accumula gli argomenti che le vengono passati in chiamate successive::

   def f(a, L=[]):
       L.append(a)
       return L

   print(f(1))
   print(f(2))
   print(f(3))

Questo produrrà ::

   [1]
   [1, 2]
   [1, 2, 3]

Se non volete che i valori di default siano condivisi tra chiamate successive, potete scrivere la funzione in questo modo::

   def f(a, L=None):
       if L is None:
           L = []
       L.append(a)
       return L

.. _tut-keywordargs:

Parametri *keyword*
-------------------

Le funzioni possono essere chiamate anche passando :term:`argomenti keyword <keyword argument>` nella forma ``kwarg=value``. Per esempio, questa funzione ::

   def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
       print("-- This parrot wouldn't", action, end=' ')
       print("if you put", voltage, "volts through it.")
       print("-- Lovely plumage, the", type)
       print("-- It's", state, "!")

prevede un parametro obbligatorio (``voltage``) e tre opzionali (``state``, ``action`` e ``type``). Questa funzione può essere chiamata in molti modi diversi::

   parrot(1000)                                          # 1 arg. posizionale
   parrot(voltage=1000)                                  # 1 arg. keyword
   parrot(voltage=1000000, action='VOOOOOM')             # 2 arg. keyword
   parrot(action='VOOOOOM', voltage=1000000)             # 2 arg. keyword
   parrot('a million', 'bereft of life', 'jump')         # 3 arg. posizionali
   parrot('a thousand', state='pushing up the daisies')  # 1 posizionale, 1 keyword

Ma tutte queste chiamate invece non sono valide::

   parrot()                     # manca un argomento richiesto
   parrot(voltage=5.0, 'dead')  # argomento non-keyword dopo un keyword
   parrot(110, voltage=220)     # doppio valore per lo stesso argomento
   parrot(actor='John Cleese')  # argomento keyword sconosciuto

Nella chiamata di funzione, gli argomenti keyword devono seguire quelli posizionali. Ciascun argomento keyword passato deve corrispondere a uno accettato dalla funzione (``actor`` non è un argomento valido per la funzione ``parrot``), anche se l'ordine non è importante. Questo vale anche per gli argomenti non opzionali (``parrot(voltage=1000)`` è una chiamata valida). Nessun argomento può ricevere un valore più di una volta. Ecco un esempio che non funziona perché viola questa restrizione::

   >>> def function(a):
   ...     pass
   ...
   >>> function(0, a=0)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: function() got multiple values for keyword argument 'a'

Quando compare un parametro finale nella forma ``**name``, questo può ricevere un dizionario (vedi :ref:`Tipi di mapping - dizionari<typesmapping>`) che contiene tutti gli argomenti keyword che non corrispondono a un parametro formale. Questo può essere unito a un parametro nella forma ``*name`` (che descriviamo nella prossima sezione), che riceve una :ref:`tupla <tut-tuples>` con tutti gli argomenti posizionali che eccedono quelli indicati nella lista dei parametri. ``*name`` deve essere elencato prima di ``**name``. Per esempio, se definiamo una funzione in questo modo::

   def cheeseshop(kind, *arguments, **keywords):
       print("-- Do you have any", kind, "?")
       print("-- I'm sorry, we're all out of", kind)
       for arg in arguments:
           print(arg)
       print("-" * 40)
       for kw in keywords:
           print(kw, ":", keywords[kw])

Potrebbe essere chiamata così::

   cheeseshop("Limburger", "It's very runny, sir.",
              "It's really very, VERY runny, sir.",
              shopkeeper="Michael Palin",
              client="John Cleese",
              sketch="Cheese Shop Sketch")

e naturalmente restituirebbe questo:

.. code-block:: none

   -- Do you have any Limburger ?
   -- I'm sorry, we're all out of Limburger
   It's very runny, sir.
   It's really very, VERY runny, sir.
   ----------------------------------------
   shopkeeper : Michael Palin
   client : John Cleese
   sketch : Cheese Shop Sketch

Si noti che l'ordine in cui sono scritti gli argomenti corrisponde sempre a quello in cui li abbiamo inseriti nella chiamata di funzione. 

.. _tut-arbitraryargs:

Liste di parametri arbitrari
----------------------------

.. index::
   single: * (asterisk); in function calls

Infine, il metodo usato meno frequentemente consiste nello specificare che una funzione può essere chiamata passando un numero arbitrario di argomenti. Questi valori verranno conservati in una :ref:`tupla<tut-tuples>`. Prima dei parametri variabili, è possibile inserire degli altri parametri normali. ::

   def write_multiple_items(file, separator, *args):
       file.write(separator.join(args))

Di solito questi parametri "variadici" vengono per ultimi nella lista della definizione, perché catturano tutti i restanti argomenti che vengono passati alla funzione. Tutti i parametri formali che vengono dopo ``*args`` non possono che essere "solo keyword", ovvero argomenti che possono essere passati solo per nome. ::

   >>> def concat(*args, sep="/"):
   ...     return sep.join(args)
   ...
   >>> concat("earth", "mars", "venus")
   'earth/mars/venus'
   >>> concat("earth", "mars", "venus", sep=".")
   'earth.mars.venus'

.. _tut-unpacking-arguments:

Spacchettare le liste di argomenti
----------------------------------

Il caso opposto si verifica quando i valori da passare sono già contenuti in una lista o in una tupla, e devono essere "spacchettati" perché la chiamata di funzione richiede argomenti posizionali separati. Per esempio, la funzione predefinita :func:`range` prevede un parametro *start* e uno *stop*. Se non sono disponibili separatamente, potete scrivere la chiamata di funzione con l'operatore ``*``, che spacchetta gli argomenti di una lista o una tupla::

   >>> list(range(3, 6))   # chiamata normale con argomenti separati
   [3, 4, 5]
   >>> args = [3, 6]
   >>> list(range(*args))  # chiamata con argomenti spacchettati da una lista
   [3, 4, 5]

.. index::
   single: **; in function calls

Analogamente, i dizionari possono essere spacchettati con l'operatore ``**`` per passare argomenti keyword::

   >>> def parrot(voltage, state='a stiff', action='voom'):
   ...     print("-- This parrot wouldn't", action, end=' ')
   ...     print("if you put", voltage, "volts through it.", end=' ')
   ...     print("E's", state, "!")
   ...
   >>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
   >>> parrot(**d)
   -- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !

.. _tut-lambda:

Funzioni lambda
---------------

È possibile creare delle piccole funzioni anonime con la parola-chiave :keyword:`lambda`. Questa funzione restituisce la somma dei suoi due argomenti: ``lambda a, b: a+b``. Le funzioni lambda possono essere usate dovunque si può usare una normale funzione. Dal punto di vista sintattico, sono limitate a una singola espressione. Dal punto di vista semantico, sono solo una scorciatoia al posto di una normale definizione di funzione. Come le funzioni interne ad altre funzioni, anche le lambda possono accedere a variabili definite nella funzione soprastante::

   >>> def make_incrementor(n):
   ...     return lambda x: x + n
   ...
   >>> f = make_incrementor(42)
   >>> f(0)
   42
   >>> f(1)
   43

Questo esempio utilizza una lambda per restituire una funzione. Un altro possibile utilizzo è quando si vuole passare una piccola funzione come argomento di un'altra funzione::

   >>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
   >>> pairs.sort(key=lambda pair: pair[1])
   >>> pairs
   [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

.. _tut-docstrings:

Stringhe di documentazione
--------------------------

.. index::
   single: docstrings
   single: documentation strings
   single: strings, documentation

Ci sono alcune convenzioni sul contenuto e la formattazione di una stringa di documentazione. 

La prima riga dovrebbe essere un sintetico riepilogo dello scopo dell'oggetto documentato. Per brevità, non dovrebbe dichiarare esplicitamente il nome dell'oggetto o il suo tipo, dal momento che queste informazioni si possono ottenere in altro modo (a meno che il nome non sia un verbo che descrive l'azione della funzione - *questo naturalmente è più facile in Inglese, ndT*). La riga dovrebbe iniziare con la lettera maiuscola e finire con un punto. 

Se la stringa ha più di una riga, la seconda dovrebbe essere vuota, in modo da separare visivamente il sommario dal resto della documentazione. Le righe successive dovrebbero contenere uno o più paragrafi che descrivono come si deve usare l'oggetto, i suoi *side-effect*, etc. 

Il parser di Python non elimina lo spazio dei rientri da una stringa multi-riga: di conseguenza i *tool* che processano la documentazione dovranno compiere questa operazione, se lo desiderano. Per questo occorre utilizzare una convenzione: la prima riga non vuota *dopo* la riga iniziale determina la spazio di rientro per tutto il resto della stringa. (Non possiamo usare la prima riga, perché di solito inizia con gli apici e quindi la stringa in sé non ha nessun rientro apparente.) Lo spazio "equivalente" a questo rientro deve essere quindi eliminato da tutte le righe della stringa. Non dovrebbero esserci righe con un rientro minore di questo, ma se ci sono allora tutto lo spazio iniziale dovrebbe essere tolto. Lo spazio "equivalente" dovrebbe essere calcolato dopo la conversione delle eventuali tabulazioni in spazi (di solito otto). 

Ecco un esempio di docstring multi-riga::

   >>> def my_function():
   ...     """Non fa nulla, ma lo documenta.
   ...
   ...     Davvero, non fa proprio nulla.
   ...     """
   ...     pass
   ...
   >>> print(my_function.__doc__)
   Non fa nulla, ma lo documenta.

       Davvero, non fa proprio nulla.

.. _tut-annotations:

Annotazione di funzioni
-----------------------

.. sectionauthor:: Zachary Ware <zachary.ware@gmail.com>
.. index::
   pair: function; annotations
   single: ->; function annotations
   single: : (colon); function annotations

Le :ref:`annotazioni<function>` sono del tutto facoltative: si tratta di metadati informativi sui tipi utilizzati dalle funzioni (si vedano la :pep:`3107` e la :pep:`484` per ulteriori informazioni). 

Le :term:`annotazioni <function annotation>` sono conservate nell'attributo :attr:`__annotations__` della funzione, che è un dizionario, e non hanno effetto su nessun'altra parte della funzione. Le annotazioni dei parametri si indicano con un "due punti" dopo il nome del parametro, seguito da un'espressione che restituisce il valore dell'annotazione. Le annotazioni per i valori di ritorno si indicano con un ``->`` seguito da un'espressione, collocati tra la fine della lista dei parametri e il "due punti" che termina l'istruzione :keyword:`def`. Nell'esempio che segue sono annotati un parametro posizionale, un parametro keyword e il valore di ritorno::

   >>> def f(ham: str, eggs: str = 'eggs') -> str:
   ...     print("Annotations:", f.__annotations__)
   ...     print("Arguments:", ham, eggs)
   ...     return ham + ' and ' + eggs
   ...
   >>> f('spam')
   Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
   Arguments: spam eggs
   'spam and eggs'

.. _tut-codingstyle:

Intermezzo: stile per il codice
===============================

.. sectionauthor:: Georg Brandl <georg@python.org>
.. index:: pair: coding; style

Prima di iniziare a scrivere codice Python più lungo e complesso, è arrivato il momento di affrontare il tema dello "stile" del codice. Molti linguaggi possono essere scritti (o più precisamente, *formattati*) usando stili diversi; alcuni più leggibili di altri. È sempre una buona idea facilitare la lettura del vostro codice per gli altri, e per questo adottare uno stile chiaro aiuta moltissimo. 

Nel mondo Python, la :pep:`8` si è affermata come la guida di stile usata in molti progetti: promuove uno stile molto leggibile e scorrevole all'occhio. Tutti i programmatori Python dovrebbero leggerla prima o poi; sintetizziamo qui i punti più importanti per voi:  

* I rientri si fanno con 4 spazi, non con le tabulazioni. 

   4 spazi sono un buon compromesso tra rientri più stretti (che permettono più livelli di annidamento) e più larghi (che sono più facili da leggere). Le tabulazioni fanno solo confusione ed è meglio non usarle. 
   
* Le righe non devono superare i 79 caratteri.

   Questo è per aiutare gli utenti con schermi piccoli e rende possibile affiancare due file di codice su quelli più grandi. 

* Lasciate una riga vuota per separare le funzioni e le classi, e anche i blocchi di codice più grandi all'interno delle funzioni. 

* Quando possibile, mettete i commenti su una riga separata.

* Usate le docstring. 

* Mettete uno spazio prima e dopo gli operatori e dopo la virgola, ma non accanto alle parentesi: ``a = f(1, 2) + g(3, 4)``.

* Adottate dei nomi consistenti per le vostre classi e le funzioni; la convenzione è usare ``UpperCamelCase`` per le classi e ``lowercase_with_underscores`` per le funzioni e i metodi. Il nome del primo parametro di un metodo è sempre ``self`` (si veda :ref:`tut-firstclasses` per ulteriori informazioni su classi e metodi).

* Non usate encoding esotici se il vostro codice deve essere usato in un contesto internazionale. UTF-8 (il default per Python), o anche il semplice ASCII, sono preferibili in ogni caso. 

* Analogamente, non usate caratteri non-ASCII per gli identificatori se vi è anche la più remota possibilità che delle persone di nazionalità diversa leggeranno e lavoreranno sul codice. 

.. only:: html

   .. rubric:: Note

.. [#] ndT: in questa traduzione italiana cerchiamo di mantenere una coerente, se pure acrobatica, distinzione tra *parametri* (quelli formali, che appaiono nella *definizione* della funzione) e *argomenti* (i parametri reali, che appaiono nella *chiamata* della funzione). Il testo originale è talvolta meno preciso. 

.. [#] In effetti, una descrizione più accurata sarebbe *passati per riferimento all'oggetto*, dal momento che, se viene passato un oggetto mutabile, il codice chiamante vedrà tutte le modifiche fatte dal codice chiamato (come l'inserimento di elementi in una lista).
