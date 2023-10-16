.. _tut-fp-issues:

***********************************************
Aritmetica in virgola mobile: problemi e limiti
***********************************************

.. sectionauthor:: Tim Peters <tim_one@users.sourceforge.net>

I computer rappresentano i numeri in virgola mobile come frazioni binarie. Per 
esempio, la frazione decimale [#]_ ``0.125`` vale 1/10 + 2/100 + 5/1000, 
e allo stesso modo la frazione binaria ``0.001`` vale 0/2 + 0/4 + 1/8.  
Queste due frazioni hanno lo stesso valore: l'unica 
differenza è che una è espressa come frazione in base 10, l'altra come 
frazione in base 2.

Purtroppo molte frazioni decimali non possono essere rappresentate in modo 
esatto come frazioni binarie. Una conseguenza di ciò è che, in generale, i 
numeri con la virgola decimali che inserite possono essere rappresentati nel 
computer solo in modo approssimato come numeri binari con la virgola. 

Il problema è più facile da capire in base 10. Si consideri la frazione 1/3. 
Si può approssimare in base 10::

   0.3

o meglio, ::

   0.33

o meglio, ::

   0.333

e così via. Non importa quante cifre decimali si vogliono scrivere, il 
risultato non sarà mai esattamente 1/3, ma un'approssimazione sempre migliore 
di 1/3.

Allo stesso modo, non importa quante cifre si scrivono, ma il valore decimale 
0.1 non può essere rappresentato esattamente in base 2. Il valore 1/10 in base 
2 è la frazione periodica ::

   0.0001100110011001100110011001100110011001100110011...

Se arrestiamo lo sviluppo a un numero qualsiasi di cifre, otteniamo 
un'approssimazione. Sui computer moderni i numeri con la virgola sono 
rappresentati con una frazione binaria dove il numeratore usa i primi 53 bit, 
partendo dal bit più significativo, e il denominatore è una potenza di 2. Nel 
caso di 1/10, la frazione binaria è ``3602879701896397 / 2 ** 55``: vicina, ma 
non esattamente uguale al vero valore di 1/10. 

Molti utenti non si accorgono di questa approssimazione perché le cifre 
visualizzate non sono abbastanza. Python scrive un'approssimazione decimale 
del vero valore che internamente è rappresentato come un'approssimazione 
binaria. Sulla maggior parte dei computer, se Python dovesse scrivere il 
valore decimale esatto dell'approssimazione binaria interna di 0.1, dovrebbe 
farci vedere ::

   >>> 0.1
   0.1000000000000000055511151231257827021181583404541015625

Sono molte più cifre di quelle di cui la gente ha bisogno. Python preferisce 
mantenere un numero gestibile di cifre decimali, visualizzando un valore 
approssimato::

   >>> 1 / 10
   0.1

Bisogna però ricordare che, anche se il risultato visualizzato assomiglia al 
valore esatto di 1/10, il valore *memorizzato* è quello della frazione binaria 
più prossima. 

Un aspetto interessante è che ci sono molti numeri decimali che condividono la 
rappresentazione della stessa frazione binaria più prossima. Per esempio, i 
numeri ``0.1`` e ``0.10000000000000001`` e 
``0.1000000000000000055511151231257827021181583404541015625`` sono tutti 
approssimati da ``3602879701896397 / 2 ** 55``. Dal momento che tutti questi 
valori decimali condividono la stessa approssimazione, ciascuno di essi 
potrebbe essere visualizzato preservando l'invariante ``eval(repr(x)) == x``.

Molti anni fa, il prompt di Python e la funzione predefinita :func:`repr` 
sceglievano tra le possibili rappresentazioni quella con 17 cifre 
significative, ``0.10000000000000001``. A partire da Python 3.1, sulla maggior 
parte delle piattaforme Python è in grado di scegliere quella più breve e 
visualizza semplicemente ``0.1``.

Si noti che questo comportamento è dovuto alla natura intrinseca 
dell'aritmetica binaria in virgola mobile: non è un baco di Python e non è 
neppure un baco nel vostro codice. Avreste lo stesso risultato con tutti i 
linguaggi che si appoggiano all'aritmetica in virgola mobile del vostro 
hardware (anche se un linguaggio potrebbe non *visualizzare* la differenza di 
default, oppure non in tutte le modalità di output). 

Per ottenere un output più semplice, potete usare la formattazione delle 
stringhe per limitare il numero delle cifre significative::

   >>> format(math.pi, '.12g')  # produce 12 cifre significative
   '3.14159265359'

   >>> format(math.pi, '.2f')   # produce 2 cifre significative dopo la virgola
   '3.14'

   >>> repr(math.pi)
   '3.141592653589793'

È importante capire che, in un certo senso, si tratta di un'illusione: state 
semplicemente arrotondando la *visualizzazione* del vero valore conservato dal 
computer. 

Un'illusione può portare a un'altra illusione. Per esempio, siccome 0.1 non è 
esattamente 1/10, sommare tre volte 0.1 potrebbe non dare 0.3::

   >>> .1 + .1 + .1 == .3
   False

Inoltre, siccome 0.1 non può avvicinarsi ulteriormente al valore esatto di 
1/10 e 0.3 non può avvicinarsi di più a 3/10, arrotondare preventivamente con 
la funzione :func:`round` non è una soluzione::

   >>> round(.1, 1) + round(.1, 1) + round(.1, 1) == round(.3, 1)
   False

Anche se i numeri non possono avvicinarsi di più al loro valore reale, la 
funzione :func:`round` può essere utile comunque per arrotondare *dopo*, in 
modo da rendere confrontabili i risultati approssimati::

    >>> round(.1 + .1 + .1, 10) == round(.3, 10)
    True

L'aritmetica binaria in virgola mobile presenta molte sorprese come questa. 
Spieghiamo nel dettaglio il problema di "0.1" nella sezione successiva. Si 
veda 
`Examples of FLoating Point Problems <https://jvns.ca/blog/2023/01/13/examples-of-floating-point-problems/>`_ 
per una introduzione piacevole alla virgola mobile binaria e ai problemi che 
si possono trovare in pratica. Si veda inoltre 
`The Perils of Floating Point <https://www.lahey.com/float.htm>`_ per un 
elenco più completo di altri inciampi frequenti. 

Come si usa concludere, "non ci sono risposte facili". Tuttavia non bisogna 
neppure avere troppa paura della virgola! Gli errori nelle operazioni decimali 
in Python sono ereditati dall'architettura in virgola mobile sottostante, e 
sulle macchine moderne questi sono dell'ordine di una parte su 2\*\*53 per 
ciascuna operazione. È più che adeguato nella maggior parte dei casi, ma 
dovete tener presente che non si tratta di aritmetica decimale e che ciascuna 
nuova operazione può accumulare un nuovo errore di arrotondamento. 

Anche se esistono dei casi estremi, nella vita di tutti i giorni l'aritmetica 
in virgola mobile si comporta come ci si aspetta, se si arrotonda 
semplicemente il risultato finale al numero di decimali che si desidera. Di 
solito basta la funzione :func:`str`; per un controllo più fine si può usare 
il metodo :meth:`str.format` e la sua 
:ref:`sintassi di formattazione<formatstrings>`.

Per gli scenari dove è richiesta una rappresentazione decimale esatta, potete 
usare il modulo :mod:`decimal`, che implementa l'aritmetica decimale adatta 
per la contabilità e i programmi che fanno calcoli di alta precisione. 

Una forma alternativa di aritmetica esatta è quella del modulo 
:mod:`fractions`, che implementa l'aritmetica dei numeri razionali (così che 
numeri come 1/3 possano essere espressi in modo esatto).

Se fate un uso massiccio di operazioni in virgola mobile potreste voler 
considerare il pacchetto NumPy e i molti altri package di 
interesse matematico e statistico compresi nel progetto 
`SciPy <https://scipy.org>`_.

Python fornisce degli strumenti utili per le rare occasioni in cui davvero 
volete conoscere il valore esatto di un *float*. Il metodo 
:meth:`float.as_integer_ratio` esprime il valore del numero sotto forma di 
frazione::

   >>> x = 3.14159
   >>> x.as_integer_ratio()
   (3537115888337719, 1125899906842624)

Siccome il rapporto è un valore esatto, può essere usato per ricreare il 
valore originario senza perdita di precisione::

    >>> x == 3537115888337719 / 1125899906842624
    True

Il metodo :meth:`float.hex` esprime il numero in notazione esadecimale (base 
16), restituendo il valore esatto conservato nel computer::

   >>> x.hex()
   '0x1.921f9f01b866ep+1'

Anche questa rappresentazione esadecimale è precisa e può essere usata per 
ricostruire il numero originale::

    >>> x == float.fromhex('0x1.921f9f01b866ep+1')
    True

Dal momento che questa rappresentazione è esatta, può essere usata per 
trasportare il valore in modo affidabile tra diverse versioni di Python (su 
diverse piattaforme) e per scambiare dati con altri linguaggi che supportano 
lo stesso formato (come Java e C99).

Un altro strumento utile è la funzione :func:`math.fsum`, che aiuta ad 
alleviare il problema della perdita di precisione durante la somma. Questa 
funzione tiene traccia dei "decimali perduti" man mano che i valori sono 
aggiunti al totale. Questo può fare la differenza nella precisione 
complessiva, evitando che gli errori si accumulino al punto di influenzare il 
risultato finale::

   >>> sum([0.1] * 10) == 1.0
   False
   >>> math.fsum([0.1] * 10) == 1.0
   True

.. _tut-fp-error:

Errore di rappresentazione
==========================

Questa sezione spiega in dettaglio l'esempio di "0.1" visto sopra e mostra 
come eseguire un'analisi di casi del genere. Si assume che il lettore abbia 
una conoscenza di base della rappresentazione binaria in virgola mobile. 

Con "errore di rappresentazione" si intende il fatto che alcune frazioni 
decimali (la maggior parte, in effetti) non possono essere rappresentate in 
modo esatto come frazioni binarie (in base 2). Questo è il motivo di fondo per 
cui Python (o Perl, C, C++, Java, Fortran e molti altri) talvolta non 
visualizzano esattamente il numero decimale che uno si aspetta. 

Perché succede? 1/10 non può essere rappresentato come una frazione binaria. 
Quasi tutti i computer da almeno il 2000 usano l'aritmetica in virgola 
mobile IEEE-754 e in quasi tutte le piattaforme un *float* di Python è 
implementato come un numero "in doppia precisione" IEEE-754. Questi numeri 
hanno una precisione di 53 bit, quindi il computer in ingresso cerca di 
convertire 0.1 alla frazione più vicina che riesce a ottenere nella forma 
*J*/2**\ *N* dove *J* è un intero che contiene esattamente 53 bit. Quindi, 
scrivendo ::

   1 / 10 ~= J / (2**N)

come ::

   J ~= 2**N / 10

e ricordando che *J* ha esattamente 53 bit (ovvero è ``>= 2**52`` ma 
``< 2**53``), il miglior valore per *N* è 56::

    >>> 2**52 <=  2**56 // 10  < 2**53
    True

Ovvero, 56 è l'unico valore di *N* che permette a *J* di avere esattamente 53 
bit. Il miglior valore di *J* è di conseguenza il quoziente arrotondato::

   >>> q, r = divmod(2**56, 10)
   >>> r
   6

Dal momento che il resto è maggiore della metà di 10, la migliore 
approssimazione si ottiene arrotondando verso l'alto::

   >>> q+1
   7205759403792794

Quindi la migliore approssimazione possibile di 1/10 come numero in doppia 
precisione IEEE-754 è::

   7205759403792794 / 2 ** 56

Dividere numeratore e denominatore per due riduce la frazione a::

   3602879701896397 / 2 ** 55

Si noti che, avendo arrotondato verso l'alto, questo numero è leggermente più 
grande di 1/10; se avessimo arrotondato verso il basso, sarebbe più piccolo. 
Comunque in nessun caso potrebbe essere *esattamente* 1/10.

Il computer quindi non "vede" mai 1/10: vede piuttosto la frazione esatta che 
abbiamo ricavato qui sopra, ovvero la migliore approssimazione IEEE-754 che 
può ottenere::

   >>> 0.1 * 2 ** 55
   3602879701896397.0

Se moltiplichiamo la frazione per 10\*\*55, possiamo vedere il valore che si 
sviluppa per 55 cifre decimali::

   >>> 3602879701896397 * 10 ** 55 // 2 ** 55
   1000000000000000055511151231257827021181583404541015625

Questo vuol dire che il numero esatto conservato internamente è uguale al 
valore decimale 0.1000000000000000055511151231257827021181583404541015625. 
Invece di visualizzare il valore decimale per intero, molti linguaggi (incluse 
le vecchie versioni di Python) lo arrotondano a 17 cifre significative::

   >>> format(0.1, '.17f')
   '0.10000000000000001'

I moduli :mod:`fractions` e :mod:`decimal` facilitano questi calcoli::

   >>> from decimal import Decimal
   >>> from fractions import Fraction

   >>> Fraction.from_float(0.1)
   Fraction(3602879701896397, 36028797018963968)

   >>> (0.1).as_integer_ratio()
   (3602879701896397, 36028797018963968)

   >>> Decimal.from_float(0.1)
   Decimal('0.1000000000000000055511151231257827021181583404541015625')

   >>> format(Decimal.from_float(0.1), '.17')
   '0.10000000000000001'

.. only:: html

   .. rubric:: Note

.. [#] ndT: i numeri "con la virgola" in Inglese (e in Python, e in qualsiasi 
   linguaggio di programmazione) si scrivono naturalmente "con il punto". 
   *Virgola mobile* in Inglese è *floating point*. 
