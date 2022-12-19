.. _tut-structures:

**************
Strutture dati
**************

Questo capitolo descrive più in dettaglio argomenti già visti e aggiunge anche 
alcune cose nuove.

.. _tut-morelists:

Un approfondimento sulle liste
==============================

Il tipo di dato "lista" ha diverse funzionalità ulteriori. Ecco un elenco di 
tutti i metodi disponibili per gli oggetti-lista:

.. method:: list.append(x)
   :noindex:

   Aggiunge un elemento alla fine della lista. Equivale a ``a[len(a):] = [x]``.

.. method:: list.extend(iterable)
   :noindex:

   Estende una lista aggiungendovi tutti gli elementi di un oggetto iterabile. 
   Equivale a ``a[len(a):] = iterable``.

.. method:: list.insert(i, x)
   :noindex:

   Inserisce un elemento alla posizione data. Il primo parametro è l'indice 
   dell'elemento *prima del quale* sarà inserito il nostro, quindi 
   ``a.insert(0, x)`` inserisce all'inizio della lista e 
   ``a.insert(len(a), x)`` equivale a ``a.append(x)``.

.. method:: list.remove(x)
   :noindex:

   Rimuove il primo elemento della lista che ha valore *x*. Emette un 
   :exc:`ValueError` se non esiste un elemento con questo valore.

.. method:: list.pop([i])
   :noindex:

   Rimuove e *restituisce* l'elemento alla posizione specificata. Se non viene 
   specificato un indice, ``a.pop()`` rimuove e restituisce l'ultimo elemento 
   della lista. (Le parentesi quadre intorno alla *i* nell'elenco dei 
   parametri non significano che dovreste usare quelle parentesi quando 
   chiamate il metodo, ma indicano invece che il parametro è *opzionale*. 
   Vedrete molto spesso questa notazione nella documentazione della libreria 
   standard di Python.)

.. method:: list.clear()
   :noindex:

   Rimuove tutti gli elementi della lista. Equivale a ``del a[:]``.

.. method:: list.index(x[, start[, end]])
   :noindex:

   Restituisce l'indice (partendo da zero) del primo elemento con valore *x*.
   Emette un :exc:`ValueError` se non esiste un elemento con quel valore.

   I parametri opzionali *start* e *end* limitano la ricerca all'interno di 
   una determinata sotto-lista, e sono interpretati come nella notazione per 
   il sezionamento. L'indice restituito è però relativo all'intera lista, non 
   alla sequenza che inizia con *start*. 

.. method:: list.count(x)
   :noindex:

   Restituisce il numero di volte che *x* appare nella lista.

.. method:: list.sort(*, key=None, reverse=False)
   :noindex:

   Ordina sul posto gli elementi della lista. I parametri possono essere usati 
   per aggiungere criteri all'ordinamento: si veda la funzione :func:`sorted` 
   per il loro uso. 

.. method:: list.reverse()
   :noindex:

   Capovolge sul posto gli elementi della lista.

.. method:: list.copy()
   :noindex:

   Restituisce una copia per indirizzo (*shallow copy*) della lista. Equivale 
   a ``a[:]``.

Un esempio che utilizza molti metodi delle liste::

    >>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    >>> fruits.count('apple')
    2
    >>> fruits.count('tangerine')
    0
    >>> fruits.index('banana')
    3
    >>> fruits.index('banana', 4)  # Il prossimo "banana", dalla posizione 4
    6
    >>> fruits.reverse()
    >>> fruits
    ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
    >>> fruits.append('grape')
    >>> fruits
    ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
    >>> fruits.sort()
    >>> fruits
    ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
    >>> fruits.pop()
    'pear'

Avrete notato che i metodi come ``insert``, ``remove`` o ``sort``, che 
modificano soltanto la lista, non hanno valore di ritorno -- ovvero, 
restituiscono il ``None`` di default. [#]_  Questo è un principio di design 
che vale per tutte le strutture-dati mutabili in Python.

Un'altra cosa da osservare è che non tutti i dati possono essere ordinati o 
confrontati. Per esempio, ``[None, 'hello', 10]`` non può essere ordinato 
perché gli interi non possono essere confrontati con le stringhe e *None* non 
si può confrontare con altri tipi di dato. Inoltre, ci sono alcuni tipi che 
non hanno un ordinamento predefinito: per esempio, ``3+4j < 5+7j`` non è una 
comparazione valida.

.. _tut-lists-as-stacks:

Usare le liste come pile
------------------------

.. sectionauthor:: Ka-Ping Yee <ping@lfw.org>

È molto facile, grazie ai metodi che abbiamo visto, usare le liste come una 
pila (*stack*) ovvero come strutture in cui l'ultimo elemento aggiunto è il 
primo restituito (*last-in, first-out*). Per aggiungere un elemento in cima 
allo stack, usate :meth:`append`. Per estrarre un elemento dalla cima dello 
stack, usate :meth:`pop` senza un indice esplicito. Per esempio::

   >>> stack = [3, 4, 5]
   >>> stack.append(6)
   >>> stack.append(7)
   >>> stack
   [3, 4, 5, 6, 7]
   >>> stack.pop()
   7
   >>> stack
   [3, 4, 5, 6]
   >>> stack.pop()
   6
   >>> stack.pop()
   5
   >>> stack
   [3, 4]

.. _tut-lists-as-queues:

Usare le liste come code
------------------------

.. sectionauthor:: Ka-Ping Yee <ping@lfw.org>

È anche possibile usare le liste come code (*queue*), dove il primo elemento 
aggiunto è il primo restituito (*first-in, first-out*). Tuttavia le liste non 
sono strutture efficienti per questo scopo. Gli ``append`` e i ``pop`` alla 
fine della lista sono veloci, ma gli ``insert`` e i ``pop`` *all'inizio* sono 
lenti (perché tutti gli altri elementi devono slittare di una posizione). 

Per implementare una coda, usate invece :class:`collections.deque`, che è 
pensata appositamente per avere ``append`` e ``pop`` veloci da entrambi i 
lati. Per esempio::

   >>> from collections import deque
   >>> queue = deque(["Eric", "John", "Michael"])
   >>> queue.append("Terry")           # Terry arriva
   >>> queue.append("Graham")          # Graham arriva
   >>> queue.popleft()                 # Il primo ad arrivare parte
   'Eric'
   >>> queue.popleft()                 # Adesso parte il secondo arrivato
   'John'
   >>> queue                           # Il resto, in ordine di arrivo
   deque(['Michael', 'Terry', 'Graham'])

.. _tut-listcomps:

List comprehension
------------------

Una *list comprehension* è un modo conciso di creare una lista. Accade di 
frequente di dover creare una lista dove ciascun elemento è il risultato di 
un'operazione condotta sugli elementi di un'altra lista o iterabile; oppure, 
di dover estrarre gli elementi che soddisfano una certa condizione. 

Per esempio, vogliamo creare una lista di numeri quadrati, come questa::

   >>> squares = []
   >>> for x in range(10):
   ...     squares.append(x**2)
   ...
   >>> squares
   [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

Si noti che in questo modo creiamo e sovrascriviamo più volte una variabile 
``x`` che resta in vita anche dopo che il ciclo è terminato. Possiamo 
eliminare questo *side effect* creando la lista in questo modo::

   squares = list(map(lambda x: x**2, range(10)))

o, in modo equivalente::

   squares = [x**2 for x in range(10)]

che è più sintetico e leggibile.

Una *list comprehension* è racchiusa tra parentesi quadre; contiene 
un'espressione, seguita da una clausola :keyword:`!for`, seguita da zero o più 
clausole :keyword:`!for` o :keyword:`!if`. Il risultato è una nuova lista 
costruita valutando l'espressione nel contesto delle clausole :keyword:`!for` 
e :keyword:`!if` che la seguono. Per esempio, questa *list comprehension* 
produce una combinazione degli elementi di due liste, se non sono uguali::

   >>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
   [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

è equivalente a::

   >>> combs = []
   >>> for x in [1,2,3]:
   ...     for y in [3,1,4]:
   ...         if x != y:
   ...             combs.append((x, y))
   ...
   >>> combs
   [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

Si noti che l'ordine del :keyword:`for` e dello :keyword:`if` è lo stesso in 
entrambe le soluzioni. 

Se l'espressione è una tupla (come ``(x, y)`` nell'esempio precedente) deve 
essere messa tra parentesi. ::

   >>> vec = [-4, -2, 0, 2, 4]
   >>> # crea una nuova lista con i valori raddoppiati
   >>> [x*2 for x in vec]
   [-8, -4, 0, 4, 8]
   >>> # fitra la lista togliendo i valori negativi
   >>> [x for x in vec if x >= 0]
   [0, 2, 4]
   >>> # applica una funzione a tutti gli elementi
   >>> [abs(x) for x in vec]
   [4, 2, 0, 2, 4]
   >>> # chiama un metodo su ciascun elemento
   >>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
   >>> [weapon.strip() for weapon in freshfruit]
   ['banana', 'loganberry', 'passion fruit']
   >>> # crea una lista di tiple del tipo (number, square)
   >>> [(x, x**2) for x in range(6)]
   [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
   >>> # le tuple devono essere tra parentesi, o viene emesso un errore
   >>> [x, x**2 for x in range(6)]
     File "<stdin>", line 1, in <module>
       [x, x**2 for x in range(6)]
        ^^^^^^^
   SyntaxError: did you forget parentheses around the comprehension target? 
   >>> # "appiattisce" una lista con due 'for'
   >>> vec = [[1,2,3], [4,5,6], [7,8,9]]
   >>> [num for elem in vec for num in elem]
   [1, 2, 3, 4, 5, 6, 7, 8, 9]

Le *list comprehension* possono contenere espressioni complesse e funzioni 
dentro funzioni::

   >>> from math import pi
   >>> [str(round(pi, i)) for i in range(1, 6)]
   ['3.1', '3.14', '3.142', '3.1416', '3.14159']

List comprehension annidate
---------------------------

L'espressione iniziale di una *list comprehension* può essere qualsiasi cosa, 
anche un'altra *list comprehension*. 

Per esempio, questa è una matrice 3x4, implementata come una lista di tre 
liste di lunghezza 4::

   >>> matrix = [
   ...     [1, 2, 3, 4],
   ...     [5, 6, 7, 8],
   ...     [9, 10, 11, 12],
   ... ]

La seguente *list comprehension* annidata traspone righe e colonne::

   >>> [[row[i] for row in matrix] for i in range(4)]
   [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

Come abbiamo visto nel paragrafo precedente, la *list comprehension* interna 
è valutata nel contesto del :keyword:`for` che la segue; il nostro esempio 
equivale quindi a::

   >>> transposed = []
   >>> for i in range(4):
   ...     transposed.append([row[i] for row in matrix])
   ...
   >>> transposed
   [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

che a sua volta è la stessa cosa di::

   >>> transposed = []
   >>> for i in range(4):
   ...     # le 3 righe seguenti equivalgono alla list comp. annidata
   ...     transposed_row = []
   ...     for row in matrix:
   ...         transposed_row.append(row[i])
   ...     transposed.append(transposed_row)
   ...
   >>> transposed
   [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

Nella pratica di tutti i giorni, è preferibile usare le funzioni predefinite 
alle istruzioni di controllo di flusso troppo complicate. La funzione 
:func:`zip` è molto adatta al nostro specifico scenario::

   >>> list(zip(*matrix))
   [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

Si veda :ref:`tut-unpacking-arguments` per l'uso dell'asterisco in questa 
chiamata di funzione.

.. _tut-del:

L'istruzione :keyword:`!del`
============================

L'istruzione :keyword:`del` consente di rimuovere un elemento da una lista, 
data la sua posizione anziché il valore. È differente dal metodo :meth:`pop`, 
che restituisce il valore dell'elemento rimosso. L'istruzione :keyword:`del` 
può anche essere usata per rimuovere una sezione della lista, o svuotare 
l'intera lista (come abbiamo già fatto assegnando una lista vuota alla 
sezione). Per esempio::

   >>> a = [-1, 1, 66.25, 333, 333, 1234.5]
   >>> del a[0]
   >>> a
   [1, 66.25, 333, 333, 1234.5]
   >>> del a[2:4]
   >>> a
   [1, 66.25, 1234.5]
   >>> del a[:]
   >>> a
   []

:keyword:`del` può anche eliminare una variabile::

   >>> del a

Adesso riferirsi ad ``a`` produce un errore, almeno finché non le viene 
assegnato un nuovo valore. Vedremo in seguito altri possibili usi di 
:keyword:`del`.

.. _tut-tuples:

Tuple e sequenze
================

Abbiamo visto che le liste e le stringhe hanno molte proprietà in comune, come 
le operazioni di indicizzazione e sezionamento. In effetti sono due esempi del 
tipo di dato *sequenza* (si veda :ref:`Sequenze - liste, tuple, 
range<typesseq>`). Dal momento che Python è un linguaggio in evoluzione, altri 
tipi di sequenza potrebbero essere aggiunti in futuro. Un altro tipo di 
sequenza predefinita è la *tupla*. 

Una tupla è una serie di valori separati da virgola, per esempio::

   >>> t = 12345, 54321, 'hello!'
   >>> t[0]
   12345
   >>> t
   (12345, 54321, 'hello!')
   >>> # Le tuple possono essere annidate:
   ... u = t, (1, 2, 3, 4, 5)
   >>> u
   ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
   >>> # Le tuple sono immutabili:
   ... t[0] = 88888
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'tuple' object does not support item assignment
   >>> # ma possono contenere oggetti mutabili:
   ... v = ([1, 2, 3], [3, 2, 1])
   >>> v
   ([1, 2, 3], [3, 2, 1])

Come si può vedere, le tuple in output sono sempre scritte con le parentesi, 
in modo che le tuple annidate siano leggibili facilmente. Possono essere 
scritte in input con o senza parentesi, anche se molto spesso le parentesi 
sono comunque necessarie (se la tupla fa parte di un'espressione più grande). 
Non è possibile assegnare a un elemento della tupla: tuttavia è possibile 
creare tuple che contengono oggetti mutabili, come una lista. 

Anche se le tuple possono sembrare simili alle liste, sono usate in contesti 
diversi e per scopi diversi. Le tuple sono :term:`immutabili<immutable>` e di 
solito ospitano una collezione di elementi eterogenei, a cui si può accedere 
tramite "spacchettamento" (vedi oltre) o indici, o anche attributi, nel caso 
di una :func:`namedtuples <collections.namedtuple>`. Le liste sono 
:term:`mutabili<mutable>` e di solito ospitano elementi omogenei, a cui si 
accede iterando sulla lista. 

Le tuple che hanno zero o un elemento pongono un problema di costruzione: la 
sintassi prevede due piccole stranezze per risolvere questi casi. Le tuple 
vuote si creano con una coppia di parentesi, senza nulla dentro. Le tuple con 
un solo elemento hanno una virgola finale (non è sufficiente mettere il valore 
tra parentesi per creare una tupla). Non è bello da vedere, ma funziona. Per 
esempio::

   >>> empty = ()
   >>> singleton = 'hello',    # <-- notare la virgola finale
   >>> len(empty)
   0
   >>> len(singleton)
   1
   >>> singleton
   ('hello',)

L'assegnazione ``t = 12345, 54321, 'hello!'`` è un esempio di 
*impacchettamento* di tupla: i valori``12345``, ``54321`` e ``'hello!'`` sono 
impacchettati insieme nella tupla. L'inverso è anche possibile::

   >>> x, y, z = t

Questo si chiama, prevedibilmente, *spacchettamento* di sequenza, e funziona 
con tutti i tipi di sequenza, a destra del segno di uguaglianza. Lo 
spacchettamento richiede che il numero delle variabili sul lato sinistro sia 
uguale al numero di elementi della sequenza sul lato destro. Si noti che 
l'assegnamento multiplo è in realtà una combinazione delle due operazioni di 
impacchettamento e spacchettamento. 

.. _tut-sets:

Set
===

Python ha un tipo di dato per i *set*. Un set è una collezione non ordinata 
senza elementi duplicati. Tra gli utilizzi più frequenti vi sono i test di 
appartenenza e l'eliminazione dei duplicati. I set supportano anche le 
operazioni matematiche di unione, intersezione, differenza e differenza 
simmetrica. 

Per creare un set si può usare la funzione :func:`set` o le parentesi graffe. 
Si noti che per creare un set vuoto occorre usare ``set()``, non ``{}``: 
questo infatti crea un *dizionario* vuoto, come vedremo nella prossima sezione. 

Ecco una breve dimostrazione::

   >>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
   >>> print(basket)                      # i duplicati sono stati rimossi
   {'orange', 'banana', 'pear', 'apple'}
   >>> 'orange' in basket                 # test di appartenza veloce
   True
   >>> 'crabgrass' in basket
   False

   >>> # Dimostra le operazioni sui set con i caratteri di due parole
   ...
   >>> a = set('abracadabra')
   >>> b = set('alacazam')
   >>> a                                  # caratteri unici in a
   {'a', 'r', 'b', 'c', 'd'}
   >>> a - b                              # in a ma non in b
   {'r', 'd', 'b'}
   >>> a | b                              # in a o b o entrambi
   {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
   >>> a & b                              # sia in a sia in b
   {'a', 'c'}
   >>> a ^ b                              # in a o b, ma non in entrambi
   {'r', 'd', 'b', 'm', 'z', 'l'}

Analogamente alle :ref:`list comprehensions <tut-listcomps>`, esistono le 
*set comprehensions*::

   >>> a = {x for x in 'abracadabra' if x not in 'abc'}
   >>> a
   {'r', 'd'}

.. _tut-dictionaries:

Dizionari
=========

Un altro utile tipo predefinito in Python è il *dizionario* (si veda 
:ref:`Tipi di mapping - dizionari<typesmapping>`). I dizionari sono anche 
chiamati "array associativi" o "memorie associative" in altri linguaggi. A 
differenza delle sequenze che sono indicizzate con intervalli numerici, i 
dizionari sono indicizzati con *chiavi*; le chiavi possono essere di qualsiasi 
tipo immutabile: stringhe e numeri sono sempre adatti come chiavi. Le tuple 
possono essere usate come chiavi, se contengono solo stringhe, numeri o altre 
tuple; se una tupla contiene qualsiasi altro oggetto mutabile, direttamente o 
indirettamente, allora non può fungere da chiave per un dizionario. Non potete 
usare le liste come chiavi, dal momento che queste possono essere modificate 
sul posto con l'assegnamento a un indice, il sezionamento o metodi come 
:meth:`append` e :meth:`extend`.

Conviene pensare a un dizionario come a una collezione di coppie 
*chiave: valore*, con il requisito che le chiavi devono essere univoche 
all'interno del dizionario. Una coppia di parentesi graffe crea un dizionario 
vuoto: ``{}``. Per inizializzare il dizionario è possibile inserire nelle 
parentesi delle coppie *chiave: valore*; questo è anche il modo in cui i 
dizionari sono scritti in output. 

Le operazioni principali con i dizionari sono: conservare un valore 
accoppiandolo a una chiave; ed estrarre il valore data la chiave. È inoltre 
possibile cancellare una coppia *chiave: valore* con ``del``. Se si accoppia 
un valore a una chiave già in uso, il vecchio valore viene sovrascritto. 
Estrarre un valore con una chiave inesistente produce un errore. 

Usare ``list(d)`` su un dizionario restituisce una lista di tutte le chiavi 
usate nel dizionario, in ordine di inserimento (se le preferite ordinate, 
potete invece usare ``sorted(d)``). Per sapere se una chiave è presente in un 
dizionario, usate la parola-chiave :keyword:`in`.

Ecco un esempio di utilizzo di un dizionario::

   >>> tel = {'jack': 4098, 'sape': 4139}
   >>> tel['guido'] = 4127
   >>> tel
   {'jack': 4098, 'sape': 4139, 'guido': 4127}
   >>> tel['jack']
   4098
   >>> del tel['sape']
   >>> tel['irv'] = 4127
   >>> tel
   {'jack': 4098, 'guido': 4127, 'irv': 4127}
   >>> list(tel)
   ['jack', 'guido', 'irv']
   >>> sorted(tel)
   ['guido', 'irv', 'jack']
   >>> 'guido' in tel
   True
   >>> 'jack' not in tel
   False

La funzione :func:`dict` costruisce un dizionario da una sequenza di coppie 
*chiave, valore*::

   >>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
   {'sape': 4139, 'guido': 4127, 'jack': 4098}

Inoltre, è possibile usare le *dict comprehension* per creare dizionari da 
espressioni arbitrarie che restituiscono coppie *chiave: valore*::

   >>> {x: x**2 for x in (2, 4, 6)}
   {2: 4, 4: 16, 6: 36}

Quando le chiavi sono delle stringhe, è più semplice passare a :func:`dict` 
degli argomenti keyword::

   >>> dict(sape=4139, guido=4127, jack=4098)
   {'sape': 4139, 'guido': 4127, 'jack': 4098}

.. _tut-loopidioms:

Tecniche di iterazione
======================

Quando occorre iterare su un dizionario, le chiavi e i valori corrispondenti 
si possono estrarre contemporaneamente con il metodo :meth:`items`::

   >>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
   >>> for k, v in knights.items():
   ...     print(k, v)
   ...
   gallahad the pure
   robin the brave

Quando si itera su una sequenza, l'indice e il valore corrispondente si 
possono estrarre contemporaneamente con la funzione :func:`enumerate`::

   >>> for i, v in enumerate(['tic', 'tac', 'toe']):
   ...     print(i, v)
   ...
   0 tic
   1 tac
   2 toe

Per iterare su due o più sequenze contemporaneamente, queste possono essere 
accoppiate con la funzione :func:`zip`::

   >>> questions = ['name', 'quest', 'favorite color']
   >>> answers = ['lancelot', 'the holy grail', 'blue']
   >>> for q, a in zip(questions, answers):
   ...     print('What is your {0}?  It is {1}.'.format(q, a))
   ...
   What is your name?  It is lancelot.
   What is your quest?  It is the holy grail.
   What is your favorite color?  It is blue.

Per iterare su una sequenza in ordine inverso, si scrive l'iterazione in 
avanti e su questa si chiama poi la funzione :func:`reversed`::

   >>> for i in reversed(range(1, 10, 2)):
   ...     print(i)
   ...
   9
   7
   5
   3
   1

Per iterare su una sequenza in modo ordinato, usate la funzione :func:`sorted` 
che restituisce una nuova lista ordinata, lasciando inalterato l'originale::

   >>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
   >>> for i in sorted(basket):
   ...     print(i)
   ...
   apple
   apple
   banana
   orange
   orange
   pear

Usate la funzione :func:`set` su una sequenza per eliminare i duplicati. 
Combinare :func:`sorted` con :func:`set` è un modo idiomatico per iterare 
sugli elementi unici di una sequenza in ordine alfabetico::

   >>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
   >>> for f in sorted(set(basket)):
   ...     print(f)
   ...
   apple
   banana
   orange
   pear

Talvolta si cerca di modificare la lista mentre ci si sta iterando sopra; è 
spesso più semplice creare invece una nuova lista::

   >>> import math
   >>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
   >>> filtered_data = []
   >>> for value in raw_data:
   ...     if not math.isnan(value):
   ...         filtered_data.append(value)
   ...
   >>> filtered_data
   [56.2, 51.7, 55.3, 52.5, 47.8]

.. _tut-conditions:

Un approfondimento sulle condizioni
===================================

Le condizioni usate nelle istruzioni ``while`` e ``if`` possono contenere 
qualsiasi operatore, non solo di confronto. 

Gli operatori di confronto ``in`` e ``not in`` sono dei test di appartenenza 
che controllano se un valore esiste o meno in un contenitore. Gli operatori 
``is`` e ``is not`` ci dicono se due oggetti sono effettivamente lo stesso 
oggetto. Tutti gli operatori di confronto hanno la stessa priorità, che è 
più bassa di quella di tutti gli altri operatori numerici. 

I confronti possono essere collegati. Per esempio, ``a < b == c`` testa se 
``a`` è minore di ``b`` e inoltre se ``b`` è uguale a ``c``.

I confronti possono essere combinati usando gli operatori booleani ``and`` e 
``or``; il risultato di un confronto, o di qualsiasi altra espressione 
booleana, si può negare con ``not``. Questi operatori hanno una priorità più 
bassa degli operatori di confronto; tra di loro, ``not`` ha la priorità più 
alta e ``or`` la più bassa, così che ``A and not B or C`` equivale a 
``(A and (not B)) or C``. Come sempre, si possono usare le parentesi per 
esprimere la priorità desiderata. 

Gli operatori booleani ``and`` e ``or`` sono detti "operatori corto-circuito": 
i loro argomenti sono valutati da sinistra a destra, ma la valutazione si 
ferma non appena l'esito è chiaro. Per esempio, se ``A`` e ``C`` sono "veri" 
ma ``B`` è "falso", allora ``A and B and C`` si ferma prima di valutare 
l'espressione ``C``. Quando vengono usati per restituire un valore, e non come 
booleani, gli operatori corto-circuito restituiscono l'ultimo argomento 
valutato. 

È possibile assegnare a una variabile il risultato di un confronto o di 
un'altra espressione booleana. Per esempio, ::

   >>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
   >>> non_null = string1 or string2 or string3
   >>> non_null
   'Trondheim'

Si noti che in Python, a differenza di C, un assegnamento dentro 
un'espressione può essere fatto solo esplicitamente con il 
:ref:`walrus operator <why-can-t-i-use-an-assignment-in-an-expression>` 
``:=``. Questo evita una serie di problemi comuni che si incontrano 
programmando in C: scrivere per sbaglio ``=`` in un'espressione, quando si 
intende ``==``. 

.. _tut-comparing:

Confronto di sequenze e altri tipi
==================================

In genere è possibile confrontare un oggetto-sequenza con una sequenza dello 
stesso tipo. Il confronto è fatto in ordine *lessicografico*: prima sono 
confrontati i primi due elementi tra loro; se sono diversi questo determina 
l'esito del confronto; se sono uguali, si confrontano i secondi elementi e 
così via, fino a quando una delle due sequenze termina. Se due elementi da 
confrontare sono essi stessi delle sequenze, viene effettuato un confronto 
lessicografico tra questi, ricorsivamente. Se tutti gli elementi sono uguali 
fra loro, le sequenze sono considerate uguali. Se una sequenza è una 
sotto-sequenza iniziale di un'altra, è la sequenza più breve a risultare la 
minore nel confronto. L'ordine lessicografico per le stringhe usa i 
*code point* Unicode per confrontare i singoli caratteri. Ecco alcuni esempi 
di confronto tra sequenze dello stesso tipo::

   (1, 2, 3)              < (1, 2, 4)
   [1, 2, 3]              < [1, 2, 4]
   'ABC' < 'C' < 'Pascal' < 'Python'
   (1, 2, 3, 4)           < (1, 2, 4)
   (1, 2)                 < (1, 2, -1)
   (1, 2, 3)             == (1.0, 2.0, 3.0)
   (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)

Si noti che confrontare oggetti di tipo diverso con ``<`` o ``>`` è possibile, 
purché gli oggetti abbiano un metodo di confronto adeguato. Per esempio, i 
diversi tipi numerici sono confrontati in base al loro valore, quindi 0 è 
uguale a 0.0 e così via. In assenza di un metodo di confronto, l'interprete 
non fornisce un ordinamento arbitrario, ma emette invece un'eccezione 
:exc:`TypeError`.

.. only:: html

   .. rubric:: Note

.. [#] Altri linguaggi preferiscono restituire l'oggetto mutato, cosa che 
   consente il concatenamento dei metodi, per esempio 
   ``d->insert("a")->remove("b")->sort();``.
