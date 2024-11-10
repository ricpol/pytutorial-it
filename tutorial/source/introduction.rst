.. _tut-informal:

**********************************
Un'introduzione informale a Python
**********************************

Negli esempi che seguono, l'input e l'output si distinguono dalla presenza o 
assenza del *prompt* (:term:`>>>` e :term:`...`). Per riprodurre gli esempi, 
quando appare il prompt dovete inserire tutto ciò che segue nella riga; le 
righe che non hanno il prompt sono l'output dell'interprete. Si noti che 
quando una riga riporta solo il prompt secondario senza nient'altro, significa 
che dovete inserire una riga vuota: questo serve a terminare un'istruzione 
multi-linea. 

.. only:: html

  Potete alternare la visualizzazione del prompt e dell'output cliccando il 
  pulsante ``>>>`` nell'angolo in alto a destra di una casella di codice. Se 
  nascondete il prompt e l'output, potete facilmente copincollare le righe 
  di input nel vostro interprete. (N.d.T.: Questo funziona *solo* nella 
  versione originale inglese del Tutorial.)

.. index:: single: # (hash); comment

Molti esempi nella documentazione, anche quelli da inserire nell'interprete 
interattivo, includono dei commenti. I commenti in Python iniziano con il 
"cancelletto" ``#`` e comprendono tutto il resto della riga. Un commento può 
partire all'inizio della riga o dopo uno spazio, ma non può essere inserito 
all'interno di una stringa: un cancelletto dentro una stringa è solo un 
cancelletto. Siccome i commenti servono a spiegare il codice, ma non sono 
processati da Python, non dovete copiarli quando provate gli esempi. 

Ecco alcuni esempi::

   # questo è il primo commento
   spam = 1  # e questo è il secondo
             # ... ed ecco il terzo!
   text = "# Questo non è un commento perché è dentro una stringa."

.. _tut-calculator:

Usare Python come una calcolatrice
==================================

Proviamo qualche semplice istruzione Python. Avviate l'interprete e aspettate 
il prompt primario ``>>>`` (non dovrebbe volerci molto). 

.. _tut-numbers:

Numeri
------

L'interprete funziona come una semplice calcolatrice: potete inserire 
un'espressione e lui restituirà il suo valore. La sintassi delle espressioni 
è banale: gli operatori ``+``, ``-``, ``*`` e ``/`` funzionano come per 
l'aritmetica; le parentesi (``()``) si possono 
usare per i raggruppamenti. Per esempio::

   >>> 2 + 2
   4
   >>> 50 - 5*6
   20
   >>> (50 - 5*6) / 4
   5.0
   >>> 8 / 5  # dividere produce sempre un numero con la virgola
   1.6

I numeri interi (per es. ``2``, ``4``, ``20``) hanno il tipo :class:`int`, 
quelli frazionari (es. ``5.0``, ``1.6``) hanno il tipo :class:`float`. Vedremo 
altri tipi numerici più avanti in questo tutorial. 

La divisione (``/``) restituisce sempre un numero *float*. Per 
:term:`arrotondare<floor division>` e ottenere un intero,
potete usare l'operatore ``//``. Per ottenere il resto usate 
``%``::

   >>> 17 / 3  # la divisione normale restituisce un float
   5.666666666666667
   >>>
   >>> 17 // 3  # l'arrotondamento scarta la parte frazionaria
   5
   >>> 17 % 3  # l'operatore % restituisce il resto della divisione
   2
   >>> 5 * 3 + 2  # quoziente arrotondato * divisore + resto
   17

Con Python è possibile usare l'operatore ``**`` per calcolare le potenze [#]_::

   >>> 5 ** 2  # 5 al quadrato
   25
   >>> 2 ** 7  # 2 alla settima
   128

Il segno di "uguale" (``=``) viene usato per assegnare un valore a una 
variabile. Nessun risultato viene mostrato prima del successivo prompt 
interattivo::

   >>> width = 20
   >>> height = 5 * 9
   >>> width * height
   900

Cercare di usare una variabile non "definita" (che non ha un valore 
assegnato), produce un errore::

   >>> n  # cerco di accedere a una variabile non definita
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   NameError: name 'n' is not defined

I numeri "con la virgola" (float) sono pienamente supportati; le operazioni 
che coinvolgono operandi di tipo misto convertono automaticamente gli interi 
in float::

   >>> 4 * 3.75 - 1
   14.0

In modalità interattiva, l'ultima espressione restituita è assegnata alla 
variabile ``_``. Ciò vuol dire che, quando usate Python come una calcolatrice, 
è più semplice riportare i risultati, per esempio::

   >>> tax = 12.5 / 100
   >>> price = 100.50
   >>> price * tax
   12.5625
   >>> price + _
   113.0625
   >>> round(_, 2)
   113.06

Questa variabile dovrebbe essere considerata di sola lettura. Non cercate di 
assegnare esplicitamente un valore a ``_``: avreste creato una variabile 
locale con lo stesso nome, che maschera la quella predefinita, con il suo 
comportamento speciale. 

Oltre a :class:`int` e :class:`float`, Python supporta altri tipi numerici, 
come :class:`~decimal.Decimal` e :class:`~fractions.Fraction`. Python ha anche 
il supporto per i :ref:`numeri complessi <typesnumeric>` e usa il suffisso 
``j`` o ``J`` per la parte immaginaria (e.g. ``3+5j``).

.. _tut-strings:

Testo
-----

Oltre ai numeri, Python può manipolare il testo (rappresentato dal tipo 
:class:`str`, le cosiddette "stringhe"). Ciò include caratteri "``!``", 
parole "``coniglio``", nomi "``Parigi``", frasi "``Ti copro io.``", 
e così via "``Yay! :)``". Potete delimitarle con apici singoli (``'...'``) 
o doppi (``"..."``): funzionano allo stesso modo [#]_.

   >>> 'spam eggs'  # apici singoli 
   'spam eggs' 
   >>> "Il coniglio di Parigi, ti copre lui :)! Yay!" # apici doppi 
   'Il coniglio di Parigi, ti copre lui :)! Yay!' 
   >>> '1975'  # i numeri tra apici sono comunque stringhe 
   '1975'

Per virgolettare le virgolette, dovete fare "l'escaping" facendola precedere da 
``\``. Oppure, usate l'altro tipo di apice::

   >>> 'doesn\'t'  # usate \' per inserire un apice singolo nella stringa...
   "doesn't"
   >>> "doesn't"  # ...o usate apici doppi per delimitarla
   "doesn't"
   >>> '"Yes," they said.'
   '"Yes," they said.'
   >>> "\"Yes,\" they said."
   '"Yes," they said.'
   >>> '"Isn\'t," they said.'
   '"Isn\'t," they said.'

Nella shell di Python, la definizione di una stringa e il suo output possono 
sembrare differenti. La funzione :func:`print` produce un output più leggibile 
perché omette gli apici iniziali e finali, e "stampa" anche i caratteri speciali:: 

   >>> s = 'First line.\nSecond line.'  # \n significa "a-capo" 
   >>> s  # senza print(), i caratteri speciali sono inclusi nell'output 
   'First line.\nSecond line.' 
   >>> print(s)  # con print(), i caratteri speciali sono interpretati, 
   ...           # quindi \n produce una nuova riga 
   First line. 
   Second line. 

Se non volete che il carattere dopo un *backslash* ``\`` sia interpretato come 
un carattere speciale, potete usare le *raw strings* con il prefisso ``r`` 
prima dell'apice iniziale::

   >>> print('C:\some\name')  # qui \n vuol dire "a-capo"!
   C:\some
   ame
   >>> print(r'C:\some\name')  # si noti la r iniziale
   C:\some\name

Le *raw string* hanno una sottigliezza: non possono terminare con un numero 
dispari di *backslash* ``\``: si veda :ref:`la FAQ<faq-programming-raw-string-backslash>` 
per ulteriori informazioni e soluzioni. 

Le stringhe possono occupare più di una riga. Un modo per ottenere questo è 
usare gli apici tripli: ``"""..."""`` o ``'''...'''``. Gli "a-capo" sono 
inclusi automaticamente nelle stringhe, ma è possibile evitarlo aggiungendo un 
*backslash* ``\`` alla fine della riga. In questo esempio si noti che lo "a-capo" iniziale 
non è incluso::

   >>> print("""\
   ... Usage: thingy [OPTIONS]
   ...      -h                        Display this usage message
   ...      -H hostname               Hostname to connect to
   ... """)
   Usage: thingy [OPTIONS]
        -h                        Display this usage message
        -H hostname               Hostname to connect to
   >>> 

Potete concatenare ("incollare insieme") le stringhe con l'operatore ``+`` e 
ripeterle con il ``*``::

   >>> # 3 volte 'un', seguito da 'ium'
   >>> 3 * 'un' + 'ium'
   'unununium'

Due o più stringhe (racchiuse tra apici) una accanto all'altra sono 
automaticamente concatenate. ::

   >>> 'Py' 'thon'
   'Python'

Questo torna utile quando volete spezzare una stringa lunga::

   >>> text = ('Mettete diverse stringhe tra parentesi '
   ...         'per unirle insieme.')
   >>> text
   'Mettete diverse stringhe tra parentesi per unirle insieme.'

Questo però funziona solo con le stringhe "pure", non con le variabili o le 
espressioni::

   >>> prefix = 'Py'
   >>> prefix 'thon'  # non potete concatenare una variabile e una stringa
     File "<stdin>", line 1
       prefix 'thon'
              ^^^^^^
   SyntaxError: invalid syntax
   >>> ('un' * 3) 'ium'
     File "<stdin>", line 1
       ('un' * 3) 'ium'
                  ^^^^^
   SyntaxError: invalid syntax

Per concatenare le variabili, o una variabile con una stringa, usate 
l'operatore ``+``::

   >>> prefix + 'thon'
   'Python'

Le stringhe possono essere *indicizzate* (indirizzate): il primo carattere ha 
indice 0. Non esiste un tipo di dato separato per rappresentare un carattere; 
un carattere è semplicemente una stringa di lunghezza uno::

   >>> word = 'Python'
   >>> word[0]  # il carattere in posizione 0
   'P'
   >>> word[5]  # il carattere in posizione 5
   'n'

Gli indici possono anche essere negativi, contando a partire da destra::

   >>> word[-1]  # l'ultimo carattere
   'n'
   >>> word[-2]  # il penultimo carattere
   'o'
   >>> word[-6]
   'P'

Si noti che, siccome -0 è lo stesso di 0, gli indici negativi partono da -1. 

Oltre agli indici, è anche consentito *sezionare* (*slicing*). Se gli indici 
restituiscono un singolo carattere, le sezioni vi permettono di estrarre 
sotto-stringhe::

   >>> word[0:2]  # i caratteri dalla posizione 0 inclusa a 2 esclusa
   'Py'
   >>> word[2:5]  # i caratteri dalla posizione 2 inclusa a 5 esclusa
   'tho'

Gli indici delle sezioni hanno dei pratici valori di default: se si omette il 
primo indice, vuol dire "0"; se si omette il secondo, vuol dire "la lunghezza 
della stringa". ::

   >>> word[:2]   # i caratteri dall'inizio alla posizione 2 esclusa
   'Py'
   >>> word[4:]   # i caratteri dalla posizione 4 inclusa alla fine
   'on'
   >>> word[-2:]  # i caratteri dalla penultima posizione inclusa alla fine
   'on'

Si noti che l'inizio è sempre incluso, la fine è esclusa. Questo fa sì che 
``s[:i] + s[i:]`` sia sempre uguale a ``s``::

   >>> word[:2] + word[2:]
   'Python'
   >>> word[:4] + word[4:]
   'Python'

Un trucco per ricordare come funzionano le sezioni è pensare che gli indici 
puntino tra un carattere e l'altro, con lo spazio a sinistra del primo 
carattere che vale 0. Allora, lo spazio a destra dell'ultimo carattere di una 
stringa di lunghezza *n* avrà indice *n*. Per esempio::

    +---+---+---+---+---+---+
    | P | y | t | h | o | n |
    +---+---+---+---+---+---+
    0   1   2   3   4   5   6
   -6  -5  -4  -3  -2  -1

I numeri della prima riga sono le posizioni degli indici 0...6 della stringa; 
la seconda riga riporta i corrispondenti indici negativi. La sezione da *i* a 
*j* è composta da tutti i caratteri che stanno tra gli spazi numerati da *i* a 
*j*. 

Per gli indici non-negativi, la lunghezza di una sezione è la differenza tra 
gli indici, se entrambi non escono dai limiti della stringa. Per esempio, la 
lunghezza di ``word[1:3]`` è 2.

Se usate un indice troppo grande, otterrete un errore::

   >>> word[42]  # la stringa ha solo 6 caratteri
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   IndexError: string index out of range

Tuttavia, gli indici che escono dai limiti sono comunque consentiti, quando li 
usiamo per estrarre una sezione::

   >>> word[4:42]
   'on'
   >>> word[42:]
   ''

Le stringhe in Python non possono essere modificate: sono 
:term:`immutabili<immutable>`. Di conseguenza, assegnare alla posizione di un 
indice produce un errore::

   >>> word[0] = 'J'
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'str' object does not support item assignment
   >>> word[2:] = 'py'
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'str' object does not support item assignment

Se vi serve una nuova stringa, dovete crearla::

   >>> 'J' + word[1:]
   'Jython'
   >>> word[:2] + 'py'
   'Pypy'

La funzione predefinita :func:`len` restituisce la lunghezza di una stringa::

   >>> s = 'supercalifragilisticexpialidocious'
   >>> len(s)
   34

.. seealso::

   :ref:`Sequenze di testo - str<textseq>`
      Le stringhe sono esempi del tipo di dati *sequenza*, e supportano le 
      comuni operazioni possibili con le sequenze.

   :ref:`Metodi per le stringhe<string-methods>`
      Le stringhe hanno un gran numero di metodi per manipolazioni di base e 
      ricerca.

   :ref:`Stringhe formattate<f-strings>`
      Le stringhe possono includere delle espressioni al loro interno. 

   :ref:`Sintassi di format<formatstrings>`
      Informazioni sulla formattazione delle stringhe con :meth:`str.format`.

   :ref:`Formattazione in stile printf<old-string-formatting>`
      Il vecchio modo di formattare, con l'operatore ``%`` a destra della 
      stringa. 

.. _tut-lists:

Liste
-----

Python ha alcuni tipi di dati *composti*, che servono a raggruppare insieme 
altri dati. Il più versatile di questo è la *lista*, che si può scrivere come 
un elenco di valori (elementi) separati da virgola e racchiusi tra parentesi 
quadre. Le liste possono contenere valori di tipo diverso, anche se di solito 
tutti gli elementi hanno lo stesso tipo. ::

   >>> squares = [1, 4, 9, 16, 25]
   >>> squares
   [1, 4, 9, 16, 25]

Come le stringhe e tutti gli altri tipi di :term:`sequenza<sequence>`, le 
liste possono essere indicizzate e sezionate::

   >>> squares[0]  # l'indice restituisce l'elemento
   1
   >>> squares[-1]
   25
   >>> squares[-3:]  # la sezione restituisce una nuova lista
   [9, 16, 25]

Le liste supportano anche operazioni come il concatenamento::

   >>> squares + [36, 49, 64, 81, 100]
   [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

A differenza delle stringhe che sono :term:`immutabili<immutable>` le liste 
sono un tipo :term:`mutabile<mutable>`, per cui è possibile cambiare il loro 
contenuto::

    >>> cubes = [1, 8, 27, 65, 125]  # c'è qualcosa di sbagliato
    >>> 4 ** 3  # 4 al cubo fa 64, non 65!
    64
    >>> cubes[3] = 64  # rimpiazza il valore sbagliato
    >>> cubes
    [1, 8, 27, 64, 125]

Potete anche aggiungere nuovi elementi alla fine della lista, con il metodo 
:meth:`!list.append` (parleremo meglio dei metodi più tardi)::

   >>> cubes.append(216)  # aggiunge il cubo di 6
   >>> cubes.append(7 ** 3)  # e il cubo di 7
   >>> cubes
   [1, 8, 27, 64, 125, 216, 343]

Un semplice assegnamento, in Python, non copia mai i dati. Quando assegnate 
una lista a una variabile, la variabile si riferisce alla lista *esistente*. 
Ogni cambiamento apportato alla lista attraverso una variabile sarà visto 
anche attraverso tutte le altre variabili che si riferiscono a questa. ::

   >>> rgb = ["Red", "Green", "Blue"]
   >>> rgba = rgb
   >>> id(rgb) == id(rgba) # si riferiscono allo stesso oggetto
   True
   >>> rgba.append("Alph")
   >>> rgb
   ["Red", "Green", "Blue", "Alph"]

Tutte le operazioni di sezionamento restituiscono una nuova lista che contiene 
gli elementi richiesti. Ciò vuol dire che il sezionamento che segue restituisce 
una :ref:`shallow copy <shallow_vs_deep_copy>` della lista::

   >>> correct_rgba = rgba[:]
   >>> correct_rgba[-1] = "Alpha"
   >>> correct_rgba
   ["Red", "Green", "Blue", "Alpha"]
   >>> rgba
   ["Red", "Green", "Blue", "Alph"]

È possibile inoltre assegnare a una sezione, cosa che può anche cambiare la 
dimensione della lista o svuotarla del tutto::

   >>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
   >>> letters
   ['a', 'b', 'c', 'd', 'e', 'f', 'g']
   >>> # rimpiazza alcuni valori
   >>> letters[2:5] = ['C', 'D', 'E']
   >>> letters
   ['a', 'b', 'C', 'D', 'E', 'f', 'g']
   >>> # adesso li rimuove
   >>> letters[2:5] = []
   >>> letters
   ['a', 'b', 'f', 'g']
   >>> # svuota la lista rimpiazzando tutti gli elementi con una lista vuota
   >>> letters[:] = []
   >>> letters
   []

La funzione predefinita :func:`len` si applica anche alle liste::

   >>> letters = ['a', 'b', 'c', 'd']
   >>> len(letters)
   4

È possibile *annidare* le liste, ovvero creare liste dentro altre liste. Per 
esempio::

   >>> a = ['a', 'b', 'c']
   >>> n = [1, 2, 3]
   >>> x = [a, n]
   >>> x
   [['a', 'b', 'c'], [1, 2, 3]]
   >>> x[0]
   ['a', 'b', 'c']
   >>> x[0][1]
   'b'

.. _tut-firststeps:

I primi passi verso la programmazione
=====================================

Certamente possiamo usare Python per compiti più complessi che sommare due più 
due. Per esempio, possiamo scrivere i primi numeri della 
`serie di Fibonacci <https://en.wikipedia.org/wiki/Fibonacci_sequence>`_ in 
questo modo::

   >>> # serie di Fibonacci:
   >>> # la somma di due elementi è l'elemento seguente
   >>> a, b = 0, 1
   >>> while a < 10:
   ...     print(a)
   ...     a, b = b, a+b
   ...
   0
   1
   1
   2
   3
   5
   8

Questo esempio introduce diversi aspetti nuovi.

* La prima riga contiene un *assegnamento multiplo*: le variabili ``a`` e ``b`` 
  ottengono simultaneamente i valori 0 e 1. Nell'ultima riga il trucco si 
  ripete, mostrando così che le espressioni nella parte destra sono tutte 
  valutate *prima* che l'assegnamento abbia luogo. Le espressioni della parte 
  destra sono valutate nell'ordine, da sinistra a destra. 

* Un ciclo :keyword:`while` viene eseguito fin quando la condizione (in questo 
  caso, ``a < 10``) resta verificata. In Python, come in C, tutti gli interi 
  tranne lo zero sono "veri". Lo zero è "falso". La condizione può anche 
  riguardare una stringa o una lista, o in effetti qualsiasi sequenza. Tutto 
  ciò che ha lunghezza non-nulla è "vero"; le sequenza vuote sono "false". Il 
  test usato in questo esempio è una semplice comparazione. Gli operatori 
  standard per la comparazione sono gli stessi di C: ``<`` (minore di), ``>`` 
  (maggiore di), ``==`` (uguale a), ``<=`` (minore o uguale a), ``>=`` 
  (maggiore o uguale a) e ``!=`` (diverso da).

* Il *corpo* del ciclo è *rientrato*: il rientro è il modo di Python per 
  raggruppare le istruzioni. In modalità interattiva, dovete inserire una 
  tabulazione o degli spazi per ciascuna riga rientrata. In realtà, 
  preparerete le istruzioni più complicate in un editor da programmatore: 
  tutti gli editor validi hanno la funzione di rientro automatico. Quando 
  inserite un'istruzione composta in modalità interattiva, dovete concluderla 
  con una riga bianca per indicare che è terminata, dal momento che il parser 
  non può indovinare quando avete inserito l'ultima riga. Si noti che ciascuna 
  riga all'interno di un blocco deve essere rientrata della stessa misura. 

* La funzione :func:`print` scrive il valore del parametro o dei parametri che 
  le passate. È diverso da scrivere semplicemente l'espressione da calcolare 
  (come avete fatto prima nell'esempio della calcolatrice), in quanto 
  :func:`print` può gestire più parametri, numeri con la virgola e stringhe. 
  Le stringhe sono stampate senza apici; tra ciascun parametro viene inserito 
  uno spazio, per permettervi di formattare l'output in modo elegante, così::

     >>> i = 256*256
     >>> print('Il valore di i è', i)
     Il valore di i è 65536

  Potete usare il parametro *keyword* "end" per evitare l'inserimento di una 
  riga vuota dopo ciascun output, o per terminare l'output con una stringa 
  diversa::

     >>> a, b = 0, 1
     >>> while a < 1000:
     ...     print(a, end=',')
     ...     a, b = b, a+b
     ...
     0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,

.. only:: html

   .. rubric:: Note

.. [#] Dal momento che ``**`` ha una priorità più alta di ``-``, ``-3**2`` 
   sarà interpretato come ``-(3**2)`` ovvero ``-9``.  Per evitare questo e 
   ottenere invece ``9``, potete usare ``(-3)**2``.

.. [#] A differenza di altri linguaggi, i caratteri speciali come ``\n`` hanno 
   lo stesso significato con apici singoli (``'...'``) o doppi (``"..."``). 
   L'unica differenza tra i due è che all'interno di apici singoli non c'è 
   bisogno di fare *escaping* di ``"`` (ma occorre farlo per ``\'``) e 
   viceversa.
