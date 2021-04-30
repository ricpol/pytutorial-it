.. _tut-errors:

*******************
Errori ed eccezioni
*******************

Fino ad ora non abbiamo parlato in modo specifico dei messaggi di errore ma, 
se avete provato gli esempi, sicuramente ne avrete visto qualcuno. Ci sono 
almeno due tipi di errore: gli *errori di sintassi* e le *eccezioni*. 

.. _tut-syntaxerrors:

Errori di sintassi
==================

Gli errori di sintassi, noti anche come errori di parsing, sono forse 
l'inciampo più comune quando state ancora imparando Python::

   >>> while True print('Hello world')
     File "<stdin>", line 1
       while True print('Hello world')
                      ^
   SyntaxError: invalid syntax

Il parser riporta la riga sbagliata e mostra una piccola "freccia" che indica 
il primo punto in cui l'errore è stato rilevato. L'errore è causato (o almeno 
rilevato) dall'elemento che *precede* la freccia: nell'esempio qui sopra, 
l'errore è rilevato nella funzione :func:`print`, perché mancano i "due punti" 
(``':'``) prima. Anche il nome del file e la riga sono riportati, in modo da 
sapere dove guardare, se l'input proviene da uno script. 

.. _tut-exceptions:

Eccezioni
=========

Anche quando un'istruzione o un'espressione sono corretti dal punto di vista 
sintattico, possono provocare un errore quando sono *eseguiti*. Gli errori 
rilevati durante l'esecuzione si chiamano eccezioni e non sono sempre fatali: 
imparerete presto come gestirle nel vostro programma Python. Molte eccezioni, 
comunque, non sono gestite dal programma e restituiscono messaggi di errore 
come questi::

   >>> 10 * (1/0)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   ZeroDivisionError: division by zero
   >>> 4 + spam*3
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   NameError: name 'spam' is not defined
   >>> '2' + 2
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: Can't convert 'int' object to str implicitly

L'ultima riga del messaggio d'errore ci dice che cosa è successo. Gli 
oggetti-eccezioni possono avere diversi tipi, e la prima parte del messaggio 
riporta il tipo: negli esempi qui sopra, :exc:`ZeroDivisionError`, 
:exc:`NameError` e :exc:`TypeError`. La stringa mostrata come tipo è il nome 
dell'eccezione predefinita incontrata. Questo succede per tutte le eccezioni 
predefinite, ma potrebbe essere diverso per le eccezioni definite dall'utente 
(anche se è comunque una convenzione utile). I nomi delle eccezioni standard 
sono identificatori predefiniti, ma non parole-chiave riservate. 

Il resto della riga fornisce dettagli che dipendono dal tipo dell'eccezione e 
da che cosa l'ha causata. 

Tutto ciò che precede il messaggio d'errore mostra il *contesto* in cui è 
avvenuta l'eccezione, nella forma di un *traceback* dello stack. In generale, 
il traceback elenca le righe di codice coinvolte nel problema; tuttavia non 
visualizza le righe lette dallo standard input. 

La sezione della documentazione :ref:`Eccezioni predefinite<bltin-exceptions>` 
elenca tutte le eccezioni predefinite e il loro significato.

.. _tut-handling:

Gestire le eccezioni
====================

I programmi possono gestire delle eccezioni specifiche. Nell'esempio che 
segue, chiediamo un input all'utente, fin quando non inserisce un numero 
valido; in ogni caso l'utente può interrompere il programma (con 
:kbd:`Control-C` o in qualunque modo consentito dal sistema operativo). Si 
noti che un'interruzione generata dall'utente provoca un'eccezione 
:exc:`KeyboardInterrupt`::

   >>> while True:
   ...     try:
   ...         x = int(input("Please enter a number: "))
   ...         break
   ...     except ValueError:
   ...         print("Oops!  That was no valid number.  Try again...")
   ...

L'istruzione :keyword:`try` funziona in questo modo:

* Per prima cosa, viene eseguito il blocco *try*, ovvero le istruzioni tra il 
  :keyword:`try` e lo :keyword:`except`.

* Se nessuna eccezione viene incontrata, il blocco *except* non viene eseguito 
  e l'esecuzione dell'istruzione :keyword:`try` termina così.

* Se durante l'esecuzione del blocco *try* viene incontrata un'eccezione, le 
  eventuali istruzioni rimanenti del blocco vengono saltate. Quindi, se il 
  tipo dell'eccezione coincide con quella nominata dopo la parola-chiave 
  :keyword:`except`, allora viene eseguito il blocco *except*. Quindi 
  l'esecuzione prosegue normalmente con ciò che segue l'istruzione 
  :keyword:`try`.

* Se viene incontrata un'eccezione che non corrisponde a quella prevista nel 
  blocco *except*, allora l'eccezione è passata ad eventuali altre istruzioni 
  :keyword:`try` annidate di livello superiore; se nessun gestore viene 
  trovato, l'eccezione è *non gestita*: a questo punto l'esecuzione del 
  programma si arresta con il messaggio di errore visto sopra. 

L'istruzione :keyword:`try` può avere più di una clausola *except*, per 
specificare gestori per diverse eccezioni: non più di un gestore per volta può 
essere eseguito. Il gestore affronta solo l'eccezione che si è verificata 
nella clausola *try* corrispondente, non quelle che eventualmente si 
verificano in altri gestori della stessa istruzione :keyword:`!try`. Una 
clausola *except* può gestire più eccezioni, specificandole come una tupla 
(con parentesi obbligatorie), per esempio::

   ... except (RuntimeError, TypeError, NameError):
   ...     pass

Un'eccezione specificata in una clausola :keyword:`except` è compatibile con 
l'eccezione che si verifica se sono istanze della stessa classe, o se 
quest'ultima è una sotto-classe della prima (ma non il contrario: se 
l'eccezione specificata è una sotto-classe di quella che si verifica, non sono 
compatibili). Per esempio, il codice che segue produrrà nell'ordine B, C, D:: 

   class B(Exception):
       pass

   class C(B):
       pass

   class D(C):
       pass

   for cls in [B, C, D]:
       try:
           raise cls()
       except D:
           print("D")
       except C:
           print("C")
       except B:
           print("B")

Si noti che, mettendo le clausole *except* in ordine inverso (con ``except B`` 
al primo posto), l'output prodotto sarebbe B, B, B: viene eseguita la prima 
clausola *except* in grado di gestire l'eccezione. 

È possibile omettere il nome dell'eccezione nell'ultima clausola *except*, in 
modo che serva come risorsa estrema. Questa strategia va però usata con 
cautela, dal momento che è facile mascherare in questo modo un errore di 
programmazione. È anche possibile scrivere un messaggio di errore e quindi 
ri-emettere l'eccezione, in modo che il codice chiamante possa eventualmente 
gestirla::

   import sys

   try:
       f = open('myfile.txt')
       s = f.readline()
       i = int(s.strip())
   except OSError as err:
       print("OS error: {0}".format(err))
   except ValueError:
       print("Could not convert data to an integer.")
   except:
       print("Unexpected error:", sys.exc_info()[0])
       raise

L'istruzione :keyword:`try` ... :keyword:`except` prevede una clausola 
opzionale *else* che, se presente, deve venire dopo tutte le clausole 
*except*. Vi si può inserire del codice che deve essere eseguito solo se la 
clausola *try* non emette alcuna eccezione. Per esempio:: 

   for arg in sys.argv[1:]:
       try:
           f = open(arg, 'r')
       except OSError:
           print('cannot open', arg)
       else:
           print(arg, 'has', len(f.readlines()), 'lines')
           f.close()

Usare :keyword:`!else` è preferibile a inserire del codice in più nel 
:keyword:`try`, perché in questo modo si evita di intercettare accidentalmente 
delle eccezioni emesse dal codice che non si intendeva proteggere nella 
clausola *try*. 

Quando si verifica un'eccezione, questa può avere un valore associato, detto 
anche *argomento* dell'eccezione. La presenza e il tipo di questo argomento 
dipende dall'eccezione. 

La clausola *except* può specificare una variabile dopo il nome dell'eccezione. 
La variabile è legata all'istanza dell'eccezione, e i suoi argomenti sono 
conservati in ``instance.args``. Per comodità, l'istanza dell'eccezione 
definisce un metodo :meth:`__str__` tale per cui gli argomenti possono essere 
scritti direttamente, senza doversi riferire a ``.args``. È possibile anche 
istanziare l'eccezione prima di emetterla, in modo da aggiungere gli attributi 
desiderati::

   >>> try:
   ...     raise Exception('spam', 'eggs')
   ... except Exception as inst:
   ...     print(type(inst))    # l'istanza dell'eccezione
   ...     print(inst.args)     # gli argomenti conservati in .args
   ...     print(inst)          # __str__ scrive direttamente gli argomenti
   ...                          # ma può essere sovrascritto nelle sottoclassi
   ...     x, y = inst.args     # spacchettiamo gli argomenti
   ...     print('x =', x)
   ...     print('y =', y)
   ...
   <class 'Exception'>
   ('spam', 'eggs')
   ('spam', 'eggs')
   x = spam
   y = eggs

Se un'eccezione ha degli argomenti, questi sono scritti nell'ultima parte 
("detail") del messaggio di errore causato dall'eccezione non gestita. 

Un gestore può intercettare non solo le eccezioni che accadono direttamente 
nel blocco *try*, ma anche quelle emesse da funzioni chiamate (anche 
indirettamente) dal codice del *try*. Per esempio::

   >>> def this_fails():
   ...     x = 1/0
   ...
   >>> try:
   ...     this_fails()
   ... except ZeroDivisionError as err:
   ...     print('Handling run-time error:', err)
   ...
   Handling run-time error: division by zero

.. _tut-raising:

Emettere eccezioni
==================

L'istruzione :keyword:`raise` permette di forzare l'emissione di una specifica 
eccezione. Per esempio::

   >>> raise NameError('HiThere')
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   NameError: HiThere

L'unico argomento di :keyword:`raise` è il nome dell'eccezione da emettere. 
Questa deve essere o un'istanza o una classe-eccezione (ovvero, una classe che 
deriva da :class:`Exception`). Se viene passata una classe, questa sarà 
implicitamente istanziata chiamando il costruttore senza argomenti::

   raise ValueError  # scorciatoia per 'raise ValueError()'

Se avete bisogno di rilevare soltanto un'eccezione, ma non intendete davvero 
gestirla, potete usare una forma più semplice di :keyword:`raise` che permette 
di rilanciare l'eccezione::

   >>> try:
   ...     raise NameError('HiThere')
   ... except NameError:
   ...     print('An exception flew by!')
   ...     raise
   ...
   An exception flew by!
   Traceback (most recent call last):
     File "<stdin>", line 2, in <module>
   NameError: HiThere

.. _tut-exception-chaining:

Concatenamento di eccezioni
===========================

L'istruzione :keyword:`raise` accetta un'opzione :keyword:`from<raise>` 
che consente di concatenare due eccezioni. Per esempio::

    # exc deve essere l'istanza di una eccezione, o None
    raise RuntimeError from exc

Questo è utile per trasformare un'eccezione in un'altra. Per esempio::

    >>> def func():
    ...    raise IOError
    ...
    >>> try:
    ...     func()
    ... except IOError as exc:
    ...     raise RuntimeError('Failed to open database') from exc
    ...
    Traceback (most recent call last):
      File "<stdin>", line 2, in <module>
      File "<stdin>", line 2, in func
    OSError
    <BLANKLINE>
    The above exception was the direct cause of the following exception:
    <BLANKLINE>
    Traceback (most recent call last):
      File "<stdin>", line 4, in <module>
    RuntimeError: Failed to open database

Il concatenamento delle eccezioni avviene automaticamente quando 
un'eccezione viene emessa da dentro una clausola :keyword:`except` oppure 
:keyword:`finally`. L'idioma ``from None`` disabilita il 
concatenamento::

    >>> try:
    ...     open('database.sqlite')
    ... except IOError:
    ...     raise RuntimeError from None
    ...
    Traceback (most recent call last):
      File "<stdin>", line 4, in <module>
    RuntimeError

Per ulteriori informazioni sul meccanismo del concatenamento, si veda 
la sezione sulle :ref:`Eccezioni predefinite <bltin-exceptions>`.

.. _tut-userexceptions:

Eccezioni personalizzate
========================

Un programma può creare le sue eccezioni interne, scrivendo una nuova 
classe-eccezione (si veda la sezione :ref:`tut-classes` per ulteriori 
informazioni sulle classi in Python). Le eccezioni dovrebbero tipicamente 
derivare dalla classe :exc:`Exception`, direttamente o indirettamente.

Le classi delle eccezioni possono fare tutto ciò che farebbe una classe 
normale, ma di solito si preferisce mantenerle semplici, spesso fornendole 
solo di qualche attributo che aiuta a capire il problema quando viene 
intercettato dai gestori dell'eccezione. Quando si scrive un modulo che può 
incontrare diversi casi di errore, una pratica comune è scrivere una 
classe-madre per le eccezioni di quel modulo, e delle sotto-classi che 
descrivono eccezioni specifiche per le diverse condizioni di errore::

   class Error(Exception):
       """Classe-madre per le eccezioni di questo modulo."""
       pass

   class InputError(Error):
       """Eccezione emessa in caso di errore nell'input.

       Attributi:
           expression -- espressione di input che ha generato l'errore
           message -- spiegazione dell'errore
       """

       def __init__(self, expression, message):
           self.expression = expression
           self.message = message

   class TransitionError(Error):
       """Emessa quando un'operazione provoca una transizione di stato
       non permessa.

       Attributi:
           previous -- stato iniziale della transizione
           next -- stato finale che si cercava di ottenere
           message -- motivo per cui la transizione non è ammessa
       """

       def __init__(self, previous, next, message):
           self.previous = previous
           self.next = next
           self.message = message

In genere si fa in modo che le eccezioni personalizzate abbiano nomi che 
finiscono in "Error", analogamente ai nomi delle eccezioni standard.

Molti moduli della libreria standard definiscono eccezioni proprie, per 
segnalare errori che possono verificarsi nelle funzioni che contengono. Per 
altre informazioni sulle classi, si veda la sezione :ref:`tut-classes`.

.. _tut-cleanup:

Definire azioni di chiusura
===========================

L'istruzione :keyword:`try` prevede un'altra clausola opzionale che permette 
di definire azioni di chiusura e pulizia che devono essere eseguite in 
qualsiasi circostanza. Per esempio::

   >>> try:
   ...     raise KeyboardInterrupt
   ... finally:
   ...     print('Goodbye, world!')
   ...
   Goodbye, world!
   Traceback (most recent call last):
     File "<stdin>", line 2, in <module>
   KeyboardInterrupt

Se è presente una clausola :keyword:`finally`, questa verrà eseguita come 
ultima cosa, prima che il keyword:`try` sia completato. Il blocco 
:keyword:`finally` viene eseguito in ogni caso, indipendentemente dal fatto 
che il codice nel :keyword:`!try` emetta un'eccezione o no. Approfondiamo nel 
dettaglio alcuni casi complessi:

* Se si incontra un'eccezione durante l'esecuzione del blocco :keyword:`!try`, 
  l'eccezione potrebbe essere gestita da un blocco :keyword:`except`. Se 
  l'eccezione non è gestita, allora viene rilanciata dopo l'esecuzione del 
  blocco :keyword:`!finally`.

* L'eccezione potrebbe accadere durante l'esecuzione di una clausola 
  :keyword:`!except` o :keyword:`!else`. Anche in questo caso l'eccezione è 
  rilanciata dopo l'esecuzione del blocco :keyword:`!finally`. 

* Se il codice del blocco :keyword:`!try` raggiunge un'istruzione 
  :keyword:`break` :keyword:`continue` o :keyword:`return`, allora la clausola 
  :keyword:`!finally` sarà eseguita immediatamente prima di queste istruzioni. 
  
* Se entrambi i blocchi :keyword:`!try` e :keyword:`!finally` comprendono 
  un'istruzione :keyword:`!return`, allora il valore restituito sarà quello 
  del :keyword:`!finally`, non quello del :keyword:`!try`. 

Per esempio::

   >>> def bool_return():
   ...     try:
   ...         return True
   ...     finally:
   ...         return False
   ...
   >>> bool_return()
   False

Un esempio più complesso::

   >>> def divide(x, y):
   ...     try:
   ...         result = x / y
   ...     except ZeroDivisionError:
   ...         print("divisione per zero!")
   ...     else:
   ...         print("il risultato è", result)
   ...     finally:
   ...         print("eseguo la clausola finally")
   ...
   >>> divide(2, 1)
   il risultato è 2.0
   eseguo la clausola finally
   >>> divide(2, 0)
   divisione per zero!
   eseguo la clausola finally
   >>> divide("2", "1")
   eseguo la clausola finally
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "<stdin>", line 3, in divide
   TypeError: unsupported operand type(s) for /: 'str' and 'str'

Come si può vedere, il blocco :keyword:`finally` è eseguito in ogni caso. Il 
:exc:`TypeError` emesso quando si cerca di dividere due stringhe non è gestito 
dalla clausola :keyword:`except` e quindi viene rilanciato, una volta che il 
:keyword:`!finally` è stato eseguito. 

In uno scenario concreto, la clausola :keyword:`finally` è utile per 
rilasciare le risorse esterne (come una connessione a un file o a un 
database), indipendentemente dal fatto che l'utilizzo sia andato a buon fine. 

.. _tut-cleanup-with:

Azioni di chiusura predefinite
==============================

Alcuni oggetti definiscono delle operazioni di chiusura e pulizia, quando non 
sono più necessari, indipendentemente dal fatto che l'utilizzo dell'oggetto 
sia andato a buon fine oppure no. Si consideri il seguente esempio, che cerca 
di aprire un file e scriverne il contenuto sullo schermo::

   for line in open("myfile.txt"):
       print(line, end="")

Il problema qui è che lasciamo il file aperto per un tempo indeterminato, dopo 
che questa parte del codice è stata eseguita. Questo non è grave per un 
semplice script, ma diventa un problema per le applicazioni più grandi. 
L'istruzione :keyword:`with` consente di usare oggetti come i file in modo 
tale da assicurarsi sempre le opportune operazioni di chiusura e pulizia. ::

   with open("myfile.txt") as f:
       for line in f:
           print(line, end="")

Dopo che l'istruzione è stata eseguita, il file *f* viene sempre chiuso, anche 
nel caso in cui, processandolo, si dovesse incontrare una condizione di 
errore. Se un oggetto definisce, come i file, delle operazioni di chiusura 
predefinite, questo viene indicato nella sua documentazione. 
