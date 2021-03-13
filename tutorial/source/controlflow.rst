.. _tut-morecontrol:

******************************************
Altri strumenti per il controllo di flusso
******************************************

Oltre a :keyword:`while` di cui abbiamo già parlato, Python utilizza le 
consuete istruzioni per il controllo del flusso, comuni a molti linguggi, con 
qualche peculiarità. 

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

Possono esserci nessuna, una o più sezioni :keyword:`elif` e la sezione 
:keyword:`else` è opzionale. La parola riservata ':keyword:`!elif`' è una 
scorciatoia per "else if", e permette di evitare troppi livelli annidati. Una 
sequenza :keyword:`!if` ... :keyword:`!elif` ... :keyword:`!elif` ... 
sostituisce le istruzioni ``switch`` o ``case`` tipiche di altri linguaggi.

Se volete confrontare lo stesso valore con diverse costanti, o controllare 
l'esistenza di tipi o attributi specifici, allora potreste trovare utile 
l'istruzione :keyword:`!match`. Per ulteriori informazioni, si veda la sezione 
:ref:`tut-match`.

.. _tut-for:

Istruzione :keyword:`!for`
==========================

.. index::
   statement: for

Se siete abituati a Pascal o a C, troverete l'istruzione :keyword:`for` in 
Python leggermente diversa. Invece di iterare solo su una progressione 
aritmetica, come in Pascal, o dare la possibilità di definire sia il passo 
dell'iterazione sia la condizione d'arresto, come in C, il :keyword:`!for` di 
Python itera sugli elementi di una qualsiasi sequenza (una lista, una 
stringa...), nell'ordine in cui appaiono nella sequenza. Per esempio, ma senza 
alcun sottinteso omicida::

   >>> # Misura la lunghezza di alcune stringhe:
   ... words = ['cat', 'window', 'defenestrate']
   >>> for w in words:
   ...     print(w, len(w))
   ...
   cat 3
   window 6
   defenestrate 12

Il codice che *modifica* una collezione mentre itera sulla stessa può essere 
complicato da scrivere correttamente. Di solito è più semplice iterare su una 
*copia* della collezione, o crearne una nuova::

    # Una collezione di esempio
    users = {'Hans': 'active', 'Eleonore': 'inactive', 'Keitaro': 'active'}
    
    # Strategia: iterare su una copia
    for user, status in users.copy().items():
        if status == 'inactive':
            del users[user]

    # Strategia: creare una nuova collezione
    active_users = {}
    for user, status in users.items():
        if status == 'active':
            active_users[user] = status

.. _tut-range:

La funzione :func:`range`
=========================

Se dovete iterare su una sequenza di numeri, la funzione predefinita 
:func:`range` è molto comoda. Produce una progressione aritmetica::

    >>> for i in range(5):
    ...     print(i)
    ...
    0
    1
    2
    3
    4

Il punto di arresto indicato non fa parte della sequenza generata: 
``range(10)`` produce dieci valori, che sono anche gli indici corretti per una 
sequenza di lunghezza 10. Potete far partire l'intervallo da un numero diverso 
o specificare un incremento, anche negativo. A volte l'incremento è chiamato 
"il passo"::

    range(5, 10)
       5, 6, 7, 8, 9

    range(0, 10, 3)
       0, 3, 6, 9

    range(-10, -100, -30)
      -10, -40, -70

Per iterare sugli indici di una sequenza, potete combinare le funzioni 
:func:`range` e :func:`len` come segue::

   >>> a = ['Mary', 'had', 'a', 'little', 'lamb']
   >>> for i in range(len(a)):
   ...     print(i, a[i])
   ...
   0 Mary
   1 had
   2 a
   3 little
   4 lamb

In casi del genere, tuttavia, vi conviene usare la funzione :func:`enumerate`: 
si veda per questo :ref:`tut-loopidioms`.

Se cercate semplicemente di "stampare" un intervallo, succede una cosa strana::

   >>> print(range(10))
   range(0, 10)

L'oggetto restituito da :func:`range` si comporta in modo simile a una lista, 
ma in effetti non lo è. In realtà è un oggetto che restituisce l'elemento 
successivo della sequenza desiderata, quando vi iterate sopra, ma non *crea* 
davvero la lista, per risparmiare spazio. 

Chiamiamo :term:`iterabile<iterable>` un oggetto di questo tipo: ovvero, un 
oggetto adatto a essere usato da funzioni e costrutti che si aspettano 
qualcosa da cui ottenere via via elementi successivi, finché ce ne sono. 
Abbiamo visto che l'istruzione :keyword:`for` è un costrutto di questo tipo; 
invece, un esempio di funzione che accetta un iterabile come argomento è 
:func:`sum`::

    >>> sum(range(4))  # 0 + 1 + 2 + 3
    6

Vedremo più in là altri esempi di funzioni che restituiscono degli iterabili, 
o che accettano iterabili come argomento. Infine, se siete curiosi di sapere 
come si può ottenere una lista da un :func:`range`, ecco la risposta::

   >>> list(range(4))
   [0, 1, 2, 3]

Nel capitolo :ref:`tut-structures` approfondiremo ancora la funzione 
:func:`list`.

.. _tut-break:

Le istruzioni :keyword:`!break` e :keyword:`!continue`, e la clausola :keyword:`!else` nei cicli
================================================================================================

L'istruzione :keyword:`break` come in C, "salta fuori" dal ciclo 
:keyword:`for` o :keyword:`while` più interno in cui è inserita.

Le istruzioni di iterazione possono avere una clausola :keyword:`!else`: 
questa viene eseguita quando il ciclo termina perché l'iterabile si è esaurito 
(in un :keyword:`for`), o perché la condizione è divenuta "falsa" (in un 
:keyword:`while`); non viene però eseguita quando il ciclo termina a causa di 
una istruzione :keyword:`break`. Per esempio, il ciclo seguente ricerca i 
numeri primi::

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

(Sì, questo codice è giusto. Fate attenzione: la clausola ``else`` appartiene 
al ciclo :keyword:`for`, *non* all'istruzione :keyword:`if`.)

Quando viene usata in un ciclo, la clausola ``else`` è più simile alla 
``else`` di un'istruzione :keyword:`try`, piuttosto che a quella di un 
:keyword:`if`. La ``else`` di un'istruzione :keyword:`try` viene eseguita 
quando non sono rilevate eccezioni, e allo stesso modo la ``else`` di un ciclo 
viene eseguita quando non ci sono ``break``. Approfondiremo l'istruzione 
:keyword:`!try` e le eccezioni nel capitolo :ref:`tut-handling`.

L'istruzione :keyword:`continue`, anch'essa un prestito dal C, prosegue con la 
successiva iterazione del ciclo::

    >>> for num in range(2, 10):
    ...     if num % 2 == 0:
    ...         print("Trovato un numero pari", num)
    ...         continue
    ...     print("Trovato un numero dispari", num)
    Trovato un numero pari 2
    Trovato un numero dispari 3
    Trovato un numero pari 4
    Trovato un numero dispari 5
    Trovato un numero pari 6
    Trovato un numero dispari 7
    Trovato un numero pari 8
    Trovato un numero dispari 9

.. _tut-pass:

L'istruzione :keyword:`!pass`
=============================

L'istruzione :keyword:`pass` non fa nulla. Può essere usata quando 
sintatticamente è richiesta un'istruzione, ma il programma in sé non ha 
bisogno di fare nulla. Per esempio::

   >>> while True:
   ...     pass  # Blocca in attesa dell'interruzione da tastiera (Ctrl+C)
   ...

Si usa di solito per creare una classe elementare::

   >>> class MyEmptyClass:
   ...     pass
   ...

Un altro modo di usare :keyword:`pass` è come segnaposto per una funzione o 
una condizione, quando state scrivendo codice nuovo e volete ragionare in 
termini più astratti. Il :keyword:`!pass` verrà ignorato silenziosamente::

   >>> def initlog(*args):
   ...     pass   # Ricordati di implementare questa funzione!
   ...

.. _tut-match:

L'istruzione :keyword:`!match`.
===============================

Un'istruzione match riceve un'espressione e ne compara il valore con diversi 
pattern in successione, espressi con uno o più blocchi "case". A prima vista 
è simile all'istruzione "switch" in C, Java o JavaScript (e molti altri 
linguaggi), ma può anche estrarre e assegnare a variabili i componenti dei 
valori confrontati (come elementi di sequenze, o attributi di oggetti). 

Nella sua forma più semplice, confronta un valore dato con uno o più valori 
(*literal*)::

    def http_error(status):
        match status:
            case 400:
                return "Richiesta non valida"
            case 404:
                return "Non trovato"
            case 418:
                return "Sono una teiera"
            case _:
                return "Qualcosa non va con Internet"

Si noti che nell'ultimo blocco il "nome variabile" ``_`` funziona da jolly e 
intercetta sempre tutto. Se nessun confronto riesce, nessun ramo viene 
eseguito.

Potete combinare diversi valori in un singolo pattern usando ``|`` ("or")::

    case 401 | 403 | 404:
        return "Non permesso"

I pattern possono assomigliare a spacchettamenti di sequenze e possono essere 
usati per assegnare a variabili::

    # point è una tupla (x, y)
    match point:
        case (0, 0):
            print("Origine")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Non è un punto")

Studiate questo esempio con attenzione! Il primo pattern ha due valori 
(*literal*) e può essere considerato un'estensione del pattern con i valori 
mostrato prima. Ma i successivi due pattern uniscono un valore a una variabile, 
e la variabile *referenzia* un valore preso dal soggetto iniziale (``point``). 
Il quarto pattern intercetta due variabili, cosa che lo rende concettualmente 
simile all'assegnamento con spacchettamento ``(x, y) = point``.

Se usate le classi per strutturare i dati, potete usare il nome della classe 
seguito da una lista di argomenti che ricorda quella di un costruttore, ma 
con la capacità di catturare gli attributi e assegnarli a variabili::

    class Point:
        x: int
        y: int

    def where_is(point):
        match point:
            case Point(x=0, y=0):
                print("Origine")
            case Point(x=0, y=y):
                print(f"Y={y}")
            case Point(x=x, y=0):
                print(f"X={x}")
            case Point():
                print("Altrove da qualche parte")
            case _:
                print("Non è un punto")

Potete usare i parametri posizionali con alcune classi predefinite che offrono 
un ordinamento degli attributi (per esempio le *dataclass*). Potete inoltre 
definire una posizione specifica per gli attributi in un pattern, impostando 
l'attributo speciale ``__match_args__`` della vostra classe. Se lo impostate a 
``('x', 'y')``, allora tutti questi pattern sono equivalenti (e collegano 
l'attributo ``y`` alla variabile ``var``)::

    Point(1, var)
    Point(1, y=var)
    Point(x=1, y=var)
    Point(y=var, x=1)

Un buon modo di leggere i pattern è considerarli come una forma estesa di ciò 
che si può mettere nella parte sinistra di un assegnamento, così da capire 
quali variabili verranno assegnate a quali valori. Solo i nomi "sciolti" (come 
il ``var`` qui sopra) possono essere assegnati in una istruzione *match*. 
I nomi con il punto (come ``foo.bar``), gli attributi (come gli ``x=`` e 
``y=`` qui sopra) o i nomi delle classi (riconoscibili dalle parentesi "(...)" 
accanto al nome, come nei ``Point(...)`` qui sopra) non sono mai assegnati. 

I pattern possono essere arbitrariamente annidati. Per esempio, se abbiamo una 
breve lista di punti, potremmo confrontarla con dei pattern in questo modo::

    match points:
        case []:
            print("Nessun punto")
        case [Point(0, 0)]:
            print("L'origine")
        case [Point(x, y)]:
            print(f"Un punto singolo {x}, {y}")
        case [Point(0, y1), Point(0, y2)]:
            print(f"Due sull'asse Y in {y1}, {y2}")
        case _:
            print("Qualcos'altro")

Possiamo aggiungere una clausola ``if`` al pattern, detta "sentinella". Se la 
sentinella è *False*, allora ``match`` passa a provare il blocco ``case`` 
successivo. Si noti che la cattura dei valori avviene prima di valutare la 
sentinella::

    match point:
        case Point(x, y) if x == y:
            print(f"Y=X in {x}")
        case Point(x, y):
            print(f"Non sulla diagonale")

Ecco alcune altre caratteristiche importanti dell'istruzione ``match``:

- Come per gli assegnamenti con spacchettamento, i pattern con le tuple hanno 
  lo stesso significato di quelli con le liste, e anzi catturano sequenze 
  arbitrarie. Un'eccezione importante è che non catturano gli iteratori o 
  le stringhe. 

- I pattern con le sequenze supportano lo spacchettamento "esteso": 
  ``[x, y, *rest]`` e ``(x, y, *rest)`` funzionano in modo simile agli 
  assegnamenti con spacchettamento. Il nome dopo il ``*`` può anche essere 
  ``_``, così che ``(x, y, *_)`` intercetta una sequenza di almeno due 
  elementi, senza collegare i restanti a una variabile. 

- I pattern con *mapping*: ``{"bandwidth": b, "latency": l}`` intercetta i 
  valori di ``bandwidth`` e ``latency`` da un dizionario. A differenza dei 
  pattern con le sequenze, qui i valori restanti sono ignorati. Gli 
  spacchettamenti come ``**rest`` sono supportati, ma ``**_`` sarebbe 
  ridondante e quindi non è permesso. 

- I sotto-pattern si possono intercettare con la parola riservata ``as``::

    case (Point(x1, y1), Point(x2, y2) as p2): ...

  questo intercetta il secondo elemento dell'input come ``p2`` (fintanto che 
  l'input è una sequenza di due punti). 

- La maggior parte dei valori (*literal*) viene confrontata per uguaglianza, 
  ma i *singleton* ``True``, ``False`` e ``None`` sono confrontati per 
  identità. 

- I pattern possono usare costanti con un nome. Queste però devono essere 
  indicate con la sintassi col punto, per evitare che siano interpretate come 
  variabili intercettate::

      from enum import Enum
      class Color(Enum):
          RED = 0
          GREEN = 1
          BLUE = 2

      match color:
          case Color.RED:
              print("Vedo rosso!")
          case Color.GREEN:
              print("L'erba è verde")
          case Color.BLUE:
              print("Mi sento giù :(")

Per una spiegazione più dettagliata con esempi ulteriori, si veda la :pep:`636` 
che è scritta in forma di tutorial. 

.. _tut-functions:

Definire le funzioni
====================

Possiamo creare una funzione che scrive i numeri di Fibonacci fino a un limite 
determinato::

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

La parola chiave :keyword:`def` introduce la *definizione* di una funzione. 
Deve essere seguita dal nome della funzione e da una lista di parametri 
*formali* tra parentesi. Le istruzioni che compongono il corpo della funzione 
iniziano nella riga successiva, e devono essere rientrate. 

Opzionalmente, la prima istruzione della funzione può essere una stringa non 
assegnata: questa è la :dfn:`docstring`, ovvero la stringa di documentazione 
della funzione. Potete trovare altre informazioni nella sezione 
:ref:`tut-docstrings`. Esistono strumenti che usano le docstring per generare 
automaticamente la documentazione online o stampata, o per consentire 
all'utente di accedervi interattivamente. Includere la documentazione nel 
vostro codice è una buona pratica e dovrebbe diventare un'abitudine.

*L'esecuzione* di una funzione produce una nuova tabella dei simboli usati per 
le variabili locali alla funzione. Più precisamente, tutti gli *assegnamenti* 
fatti all'interno della funzione conservano il valore in una tabella dei 
simboli locale; invece, i *riferimenti* alle variabili per prima cosa cercano 
il nome nella tabella locale, quindi nella tabella locale delle eventuali 
funzioni "superiori" in cui la nostra può essere inclusa, quindi nella tabella 
dei simboli globali, infine nella tabella dei nomi predefiniti. Di conseguenza 
è possibile *riferirsi* a una variabile globale o di una funzione superiore, 
ma non è possibile *assegnarle* un valore (a meno di non ricorrere 
all'istruzione :keyword:`global` per le variabili globali, o a 
:keyword:`nonlocal` per quelle delle funzioni superiori).

I parametri *reali* (gli argomenti [#]_) di una funzione sono introdotti nella 
tabella dei simboli locali nel momento in cui la funzione è chiamata. Quindi, 
gli argomenti sono "passati per valore" (dove però il "valore" è sempre un 
*riferimento* all'oggetto, non il valore dell'oggetto). [#]_ Quando una 
funzione chiama un'altra funzione, o sé stessa ricorsivamente, una nuova tabella 
di simboli è creata per quella chiamata. 

La *definizione* della funzione associa il nome della funzione con 
l'oggetto-funzione nella tabella dei simboli corrente. L'interprete riconosce 
l'oggetto a cui punta il nome come un oggetto-funzione definito dall'utente. 
Anche altri nomi possono puntare al medesimo oggetto-funzione e possono essere 
usati per accedere alla funzione::

   >>> fib
   <function fib at 10042ed0>
   >>> f = fib
   >>> f(100)
   0 1 1 2 3 5 8 13 21 34 55 89

Se avete esperienza con altri linguaggi, potreste obiettare che ``fib`` non è 
una funzione ma una procedura, dal momento che non restituisce un valore. 
Tuttavia in Python anche le funzioni senza un'istruzione :keyword:`return` 
esplicita *restituiscono* in effetti un valore, per quanto piuttosto 
insignificante. Questo valore si chiama ``None`` (è un nome predefinito). 
L'interprete di solito evita di emettere direttamente ``None`` in output, 
quando è l'unica cosa che dovrebbe scrivere. Se volete davvero vedere il 
``None``, potete usare la funzione :func:`print`::

   >>> fib(0)
   >>> print(fib(0))
   None

Non è difficile scrivere una funzione che *restituisce* una lista di numeri di 
Fibonacci, invece di scriverla::

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

* L'istruzione :keyword:`return` esce dall'esecuzione della funzione 
  restituendo un valore. Se :keyword:`!return` non seguito da alcuna 
  espressione, allora restituisce ``None``. Anche uscire dalla funzione senza 
  un :keyword:`!return` restituisce ``None``.

* L'istruzione ``result.append(a)`` chiama un *metodo* dell'oggetto-lista 
  ``result``. Un metodo è una funzione che "appartiene" all'oggetto e si può 
  chiamare con la sintassi ``obj.methodname`` dove ``obj`` è l'oggetto (che 
  potrebbe essere il risultato di un'espressione) e ``methodname`` è il nome 
  del metodo che è stato definito nel tipo dell'oggetto. Tipi diversi 
  definiscono metodi diversi. Metodi di tipi diversi possono avere lo stesso 
  nome, senza che ciò produca ambiguità. Potete definire i vostri tipi e i 
  vostri metodi, usando le *classi*: vedi :ref:`tut-classes`. Il metodo 
  :meth:`append` mostrato nell'esempio è definito per gli oggetti-lista: 
  aggiunge un nuovo elemento in coda alla lista. In questo esempio è 
  equivalente a ``result = result + [a]``, ma più efficiente. 

.. _tut-defining:

Altre cose sulla definizione delle funzioni
===========================================

È possibile definire le funzioni con un numero variabile di parametri. Ci sono 
tre modi per fare questo, che si possono combinare tra loro. 

.. _tut-defaultargs:

Parametri con valori di default
-------------------------------

Il modo più utile è specificare un valore di default per uno o più parametri. 
In questo modo è possibile chiamare la funzione con meno argomenti di quelli 
che la definizione prescriverebbe. Per esempio::

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

Questo esempio introduce anche la parola-chiave :keyword:`in`, che testa se 
na sequenza contiene un certo valore oppure no.

I valori di default sono valutati al momento della definizione della funzione, 
nella tabella dei simboli che ospita la definizione. Quindi questo ::

   i = 5

   def f(arg=i):
       print(arg)

   i = 6
   f()

restituirà ``5``.

**Attenzione:**  I valori di default sono valutati una volta sola. Questo fa 
differenza quando il default è un oggetto *mutabile* come una lista, un 
dizionario o un'istanza di molte altre classi. Per esempio, questa funzione 
accumula gli argomenti che le vengono passati in chiamate successive::

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

Se non volete che i valori di default siano condivisi tra chiamate successive, 
potete scrivere la funzione in questo modo::

   def f(a, L=None):
       if L is None:
           L = []
       L.append(a)
       return L

.. _tut-keywordargs:

Parametri *keyword*
-------------------

Le funzioni possono essere chiamate anche passando 
:term:`argomenti keyword <keyword argument>` nella forma ``kwarg=value``. Per 
esempio, questa funzione ::

   def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
       print("-- This parrot wouldn't", action, end=' ')
       print("if you put", voltage, "volts through it.")
       print("-- Lovely plumage, the", type)
       print("-- It's", state, "!")

prevede un parametro obbligatorio (``voltage``) e tre opzionali (``state``, 
``action`` e ``type``). Questa funzione può essere chiamata in molti modi 
diversi::

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

Nella chiamata di funzione, gli argomenti keyword devono seguire quelli 
posizionali. Ciascun argomento keyword passato deve corrispondere a uno 
accettato dalla funzione (``actor`` non è un argomento valido per la funzione 
``parrot``), anche se l'ordine non è importante. Questo vale anche per gli 
argomenti non opzionali (``parrot(voltage=1000)`` è una chiamata valida). 
Nessun argomento può ricevere un valore più di una volta. Ecco un esempio che 
non funziona perché viola questa restrizione::

   >>> def function(a):
   ...     pass
   ...
   >>> function(0, a=0)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: function() got multiple values for keyword argument 'a'

Quando compare un parametro finale nella forma ``**name``, questo può ricevere 
un dizionario (vedi :ref:`Tipi di mapping - dizionari<typesmapping>`) che 
contiene tutti gli argomenti keyword che non corrispondono a un parametro 
formale. Questo può essere unito a un parametro nella forma ``*name`` (che 
descriviamo nella prossima sezione), che riceve una :ref:`tupla <tut-tuples>` 
con tutti gli argomenti posizionali che eccedono quelli indicati nella lista 
dei parametri. ``*name`` deve essere elencato prima di ``**name``. Per 
esempio, se definiamo una funzione in questo modo::

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

Si noti che l'ordine in cui sono scritti gli argomenti corrisponde sempre a 
quello in cui li abbiamo inseriti nella chiamata di funzione. 

Parametri speciali
------------------

Gli argomenti possono essere passati a una funzione Python per *posizione*, 
oppure esplicitamente in modo *keyword*. Per ragioni di leggibilità e 
performance, è una buona idea regolamentare i modi in cui si possono passare 
gli argomenti, così che basti solo un'occhiata alla definizione della funzione 
per capire se i vari elementi sono passati per posizione, per *keyword* o in 
entrambi i modi. 

Una definizione di funzione potrebbe essere così:

.. code-block:: none

   def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
         -----------    ----------     ----------
           |             |                  |
           |        posizionali o keyword   |
           |                                - solo keyword
            -- solo posizionali

dove ``/`` e ``*`` sono opzionali. Se vengono usati, questi simboli 
distinguono il tipo di parametro a seconda di come l'argomento può essere 
passato alla funzione: solo posizionale, posizione o keyword, solo keyword. 
Gli argomenti keyword sono detti anche "passati per nome". 

-------------------------------
Parametri posizionali o keyword
-------------------------------

Se ``/`` e ``*`` non compaiono nella definizione della funzione, allora gli 
argomenti possono essere passati per posizione o per nome (keyword).

--------------------------
Parametri solo posizionali
--------------------------

Volendo specificare più in dettaglio, è possibile marcare certi parametri come 
*solo posizionali*. Per i parametri solo posizionali, l'ordine in cui sono 
elencati deve essere rispettato e non possono essere passati per nome. I 
parametri solo posizionali sono messi prima del segno ``/``, che è usato per 
separarli logicamente dagli altri parametri. Se non c'è il segno ``/`` nella 
definizione della funzione, allora non ci sono parametri solo posizionali. 

I parametri che vengono dopo il ``/`` possono essere *posizionali o keyword*, 
oppure *solo keyword*. 

----------------------
Parametri solo keyword
----------------------

Per marcare i parametri come "solo keyword", indicando quindi che gli 
argomenti corrispondenti possono essere passati solo per nome, mettete un 
segno ``*`` nella lista dei parametri, subito prima del primo parametro "solo 
keyword".

------
Esempi
------

Si considerino queste definizioni di funzione, facendo attenzione ai segni 
``/`` e ``*``::

   >>> def standard_arg(arg):
   ...     print(arg)
   ...
   >>> def pos_only_arg(arg, /):
   ...     print(arg)
   ...
   >>> def kwd_only_arg(*, arg):
   ...     print(arg)
   ...
   >>> def combined_example(pos_only, /, standard, *, kwd_only):
   ...     print(pos_only, standard, kwd_only)

La prima, ``standard_arg``, ha la forma più comune e non pone alcuna 
restrizione al modo di chiamare la funzione. Gli argomenti possono essere 
passati indifferentemente per posizione o per nome::

   >>> standard_arg(2)
   2

   >>> standard_arg(arg=2)
   2

La seconda funzione, ``pos_only_arg``, può solo passare gli argomenti per 
posizione, come prescrive il segno ``/`` nella sua definizione::

   >>> pos_only_arg(1)
   1

   >>> pos_only_arg(arg=1)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: pos_only_arg() got an unexpected keyword argument 'arg'

La terza, ``kwd_only_args``, permette solo di passare gli argomenti per nome, 
avendo il segno ``*`` nella definizione::

   >>> kwd_only_arg(3)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given

   >>> kwd_only_arg(arg=3)
   3

L'ultima utilizza tutte e tre le convenzioni per la chiamata, nella stessa 
definizione::

   >>> combined_example(1, 2, 3)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: combined_example() takes 2 positional arguments but 3 were given

   >>> combined_example(1, 2, kwd_only=3)
   1 2 3

   >>> combined_example(1, standard=2, kwd_only=3)
   1 2 3

   >>> combined_example(pos_only=1, standard=2, kwd_only=3)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: combined_example() got an unexpected keyword argument 'pos_only'

Infine, si consideri questa definizione di funzione, che presenta un 
potenziale conflitto tra il parametro posizionale ``name`` e un ``**kwds`` che 
potrebbe a sua volta contenere ``name`` tra le sue chiavi::

    def foo(name, **kwds):
        return 'name' in kwds

Non c'è modo di chiamare la funzione e farle restituire ``True``: infatti la 
chiave ``'name'`` sarà sempre collegata al primo argomento, mai a ``**kwds``. 
Per esempio::

    >>> foo(1, **{'name': 2})
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: foo() got multiple values for argument 'name'

Tuttavia, se usiamo il segno ``/`` per specificare i parametri solo 
posizionali, allora diventa possibile usare ``name`` come parametro 
posizionale e allo stesso tempo mettere ``'name'`` tra gli argomenti keyword::

    def foo(name, /, **kwds):
        return 'name' in kwds
    >>> foo(1, **{'name': 2})
    True

In altre parole, i nomi dei parametri posizionali possono essere usati in 
``**kwds`` senza pericolo di ambiguità.

-------------
Ricapitolando
-------------

Scegliere che tipo di parametri impiegare nella definizione di una funzione 
dipende dalla necessità::

   def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):

Qualche indicazione:

* Usate i parametri solo posizionali se volete che il nome dei parametri non 
  sia disponibile per l'utente. Questo è utile quando i nomi non hanno un 
  significato particolare, o se volete che l'ordine dei parametri sia 
  obbligato, o se avete bisogno anche di qualche parametro keyword oltre a 
  quelli posizionali. 
* Usate i parametri solo keyword quando i nomi hanno un significato e la 
  definizione della funzione è più chiara esplicitando i nomi, o se volete 
  impedire che l'utente possa affidarsi all'ordine degli argomenti passati. 
* Dal punto di vista dell'interfaccia, usate i parametri solo posizionali per 
  prevenire che un cambiamento futuro nel nome del parametro modifichi la API 
  della funzione. 

.. _tut-arbitraryargs:

Liste di parametri arbitrari
----------------------------

.. index::
   single: * (asterisk); in function calls

Infine, il metodo usato meno frequentemente consiste nello specificare che una 
funzione può essere chiamata passando un numero arbitrario di argomenti. 
Questi valori verranno conservati in una :ref:`tupla<tut-tuples>`. Prima dei 
parametri variabili, è possibile inserire degli altri parametri normali. ::

   def write_multiple_items(file, separator, *args):
       file.write(separator.join(args))

Di solito questi parametri "variadici" vengono per ultimi nella lista della 
definizione, perché catturano tutti i restanti argomenti che vengono passati 
alla funzione. Tutti i parametri formali che vengono dopo ``*args`` non 
possono che essere "solo keyword", ovvero argomenti che possono essere passati 
solo per nome. ::

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

Il caso opposto si verifica quando i valori da passare sono già contenuti in 
una lista o in una tupla, e devono essere "spacchettati" perché la chiamata di 
funzione richiede argomenti posizionali separati. Per esempio, la funzione 
predefinita :func:`range` prevede un parametro *start* e uno *stop*. Se non 
sono disponibili separatamente, potete scrivere la chiamata di funzione con 
l'operatore ``*``, che spacchetta gli argomenti di una lista o una tupla::

   >>> list(range(3, 6))   # chiamata normale con argomenti separati
   [3, 4, 5]
   >>> args = [3, 6]
   >>> list(range(*args))  # chiamata con argomenti spacchettati da una lista
   [3, 4, 5]

.. index::
   single: **; in function calls

Analogamente, i dizionari possono essere spacchettati con l'operatore ``**`` 
per passare argomenti keyword::

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

È possibile creare delle piccole funzioni anonime con la parola-chiave 
:keyword:`lambda`. Questa funzione restituisce la somma dei suoi due 
argomenti: ``lambda a, b: a+b``. Le funzioni lambda possono essere usate 
dovunque si può usare una normale funzione. Dal punto di vista sintattico, 
sono limitate a una singola espressione. Dal punto di vista semantico, sono 
solo una scorciatoia al posto di una normale definizione di funzione. Come le 
funzioni interne ad altre funzioni, anche le lambda possono accedere a 
variabili definite nella funzione soprastante::

   >>> def make_incrementor(n):
   ...     return lambda x: x + n
   ...
   >>> f = make_incrementor(42)
   >>> f(0)
   42
   >>> f(1)
   43

Questo esempio utilizza una lambda per restituire una funzione. Un altro 
possibile utilizzo è quando si vuole passare una piccola funzione come 
argomento di un'altra funzione::

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

Ci sono alcune convenzioni sul contenuto e la formattazione di una stringa di 
documentazione. 

La prima riga dovrebbe essere un sintetico riepilogo dello scopo dell'oggetto 
documentato. Per brevità, non dovrebbe dichiarare esplicitamente il nome 
dell'oggetto o il suo tipo, dal momento che queste informazioni si possono 
ottenere in altro modo (a meno che il nome non sia un verbo che descrive 
l'azione della funzione - *questo naturalmente è più facile in Inglese, ndT*). 
La riga dovrebbe iniziare con la lettera maiuscola e finire con un punto. 

Se la stringa ha più di una riga, la seconda dovrebbe essere vuota, in modo da 
separare visivamente il sommario dal resto della documentazione. Le righe 
successive dovrebbero contenere uno o più paragrafi che descrivono come si 
deve usare l'oggetto, i suoi *side-effect*, etc. 

Il parser di Python non elimina lo spazio dei rientri da una stringa 
multi-riga: di conseguenza i *tool* che processano la documentazione dovranno 
compiere questa operazione, se lo desiderano. Per questo occorre utilizzare 
una convenzione: la prima riga non vuota *dopo* la riga iniziale determina lo 
spazio di rientro per tutto il resto della stringa. (Non possiamo usare la 
prima riga, perché di solito inizia con gli apici e quindi la stringa in sé 
non ha nessun rientro apparente.) Lo spazio "equivalente" a questo rientro 
deve essere quindi eliminato da tutte le righe della stringa. Non dovrebbero 
esserci righe con un rientro minore di questo, ma se ci sono allora tutto lo 
spazio iniziale dovrebbe essere tolto. Lo spazio "equivalente" dovrebbe essere 
calcolato dopo la conversione delle eventuali tabulazioni in spazi (di solito 
otto). 

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

Le :ref:`annotazioni<function>` sono del tutto facoltative: si tratta di 
metadati informativi sui tipi utilizzati dalle funzioni (si vedano la 
:pep:`3107` e la :pep:`484` per ulteriori informazioni). 

Le :term:`annotazioni <function annotation>` sono conservate nell'attributo 
:attr:`__annotations__` della funzione, che è un dizionario, e non hanno 
effetto su nessun'altra parte della funzione. Le annotazioni dei parametri si 
indicano con un "due punti" dopo il nome del parametro, seguito da 
un'espressione che restituisce il valore dell'annotazione. Le annotazioni per 
i valori di ritorno si indicano con un ``->`` seguito da un'espressione, 
collocati tra la fine della lista dei parametri e il "due punti" che termina 
l'istruzione :keyword:`def`. Nell'esempio che segue sono annotati un parametro 
posizionale, un parametro keyword e il valore di ritorno::

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

Prima di iniziare a scrivere codice Python più lungo e complesso, è arrivato 
il momento di affrontare il tema dello "stile" del codice. Molti linguaggi 
possono essere scritti (o più precisamente, *formattati*) usando stili 
diversi; alcuni più leggibili di altri. È sempre una buona idea facilitare la 
lettura del vostro codice per gli altri, e per questo adottare uno stile 
chiaro aiuta moltissimo. 

Nel mondo Python, la :pep:`8` si è affermata come la guida di stile usata in 
molti progetti: promuove uno stile molto leggibile e scorrevole all'occhio. 
Tutti i programmatori Python dovrebbero leggerla prima o poi; sintetizziamo 
qui i punti più importanti per voi:  

* I rientri si fanno con 4 spazi, non con le tabulazioni. 

   4 spazi sono un buon compromesso tra rientri più stretti (che permettono 
   più livelli di annidamento) e più larghi (che sono più facili da leggere). 
   Le tabulazioni fanno solo confusione ed è meglio non usarle. 
   
* Le righe non devono superare i 79 caratteri.

   Questo è per aiutare gli utenti con schermi piccoli e rende possibile 
   affiancare due file di codice su quelli più grandi. 

* Lasciate una riga vuota per separare le funzioni e le classi, e anche i 
  blocchi di codice più grandi all'interno delle funzioni. 

* Quando possibile, mettete i commenti su una riga separata.

* Usate le docstring. 

* Mettete uno spazio prima e dopo gli operatori e dopo la virgola, ma non 
  accanto alle parentesi: ``a = f(1, 2) + g(3, 4)``.

* Adottate dei nomi consistenti per le vostre classi e le funzioni; la 
  convenzione è usare ``UpperCamelCase`` per le classi e 
  ``lowercase_with_underscores`` per le funzioni e i metodi. Il nome del primo 
  parametro di un metodo è sempre ``self`` (si veda :ref:`tut-firstclasses` 
  per ulteriori informazioni su classi e metodi).

* Non usate encoding esotici se il vostro codice deve essere usato in un 
  contesto internazionale. UTF-8 (il default per Python), o anche il semplice 
  ASCII, sono preferibili in ogni caso. 

* Analogamente, non usate caratteri non-ASCII per gli identificatori se vi è 
  anche la più remota possibilità che delle persone di nazionalità diversa 
  leggeranno e lavoreranno sul codice. 

.. only:: html

   .. rubric:: Note

.. [#] ndT: in questa traduzione italiana cerchiamo di mantenere una coerente, 
   se pure acrobatica, distinzione tra *parametri* (quelli formali, che 
   appaiono nella *definizione* della funzione) e *argomenti* (i parametri 
   reali, che appaiono nella *chiamata* della funzione). Il testo originale è 
   talvolta meno preciso. 

.. [#] In effetti, una descrizione più accurata sarebbe *passati per 
   riferimento all'oggetto*, dal momento che, se viene passato un oggetto 
   mutabile, il codice chiamante vedrà tutte le modifiche fatte dal codice 
   chiamato (come l'inserimento di elementi in una lista).
