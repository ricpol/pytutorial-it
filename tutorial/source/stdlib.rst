.. _tut-brieftour:

***************************************
Una breve visita alla libreria standard
***************************************

.. _tut-os-interface:

Interfacce al sistema operativo
===============================

Il modulo :mod:`os` contiene moltissime funzioni per interagire con il sistema 
operativo::

   >>> import os
   >>> os.getcwd()      # restituisce la directory corrente
   'C:\\Python39'
   >>> os.chdir('/server/accesslogs')   # cambia la directory corrente
   >>> os.system('mkdir today')   # esegue "mkdir" nella shell di sistema
   0

È importante usare ``import os`` e non ``from os import *``, in modo che la 
funzione :func:`os.open` non mascheri la funzione predefinita :func:`open` che 
lavora in modo molto differente.

.. index:: builtin: help

È conveniente ricorrere alle funzioni predefinite :func:`dir` e :func:`help` 
per ricevere aiuto interattivo quando si lavora con moduli di grandi 
dimensioni come :mod:`os`::

   >>> import os
   >>> dir(os)
   <restituisce una lista di tutte le funzioni del modulo>
   >>> help(os)
   <restituisce una documentazione completa costruita in base alle docstring>

Per il lavoro di tutti i giorni con file e directory, :mod:`shutil` fornisce 
un'interfaccia di livello più alto, che è più semplice da usare::

   >>> import shutil
   >>> shutil.copyfile('data.db', 'archive.db')
   'archive.db'
   >>> shutil.move('/build/executables', 'installdir')
   'installdir'

.. _tut-file-wildcards:

Caratteri jolly per i file
==========================

Il modulo :mod:`glob` comprende una funzione per cercare file con i caratteri 
jolly::

   >>> import glob
   >>> glob.glob('*.py')
   ['primes.py', 'random.py', 'quote.py']

.. _tut-command-line-arguments:

Argomenti della riga di comando
===============================

Molti script di hanno bisogno di processare gli argomenti della riga di 
comando. Questi argomenti vengono conservati nell'attributo *argv* del modulo 
:mod:`sys`, sotto forma di una lista. Per esempio, l'output che segue risulta 
dall'aver invocato ``python demo.py one two three`` al prompt della shell::

   >>> import sys
   >>> print(sys.argv)
   ['demo.py', 'one', 'two', 'three']

Il modulo :mod:`argparse` mette a disposizione un meccanismo più sofisticato 
per gestire gli argomenti della riga di comando. Lo script che segue estrae 
uno o più nomi di file e un numero opzionale di righe da visualizzare::

    import argparse

    parser = argparse.ArgumentParser(prog = 'top',
        description = 'Show top lines from each file')
    parser.add_argument('filenames', nargs='+')
    parser.add_argument('-l', '--lines', type=int, default=10)
    args = parser.parse_args()
    print(args)

Quando viene invocato con ``python top.py --lines=5 alpha.txt beta.txt``, lo 
script imposta ``args.lines`` a ``5`` e ``args.filenames`` a 
``['alpha.txt', 'beta.txt']``.

.. _tut-stderr:

Re-dirigere lo standard error e terminare il programma
======================================================

Il modulo :mod:`sys` ha degli attributi per *stdin*, *stdout* e *stderr*. 
Quest'ultimo è utile per emettere avvisi e messaggi d'errore e renderli 
visibili anche quando lo standard output è stato re-diretto::

   >>> sys.stderr.write('Warning, log file not found starting a new one\n')
   Warning, log file not found starting a new one

Il modo più diretto per terminare un programma è usare ``sys.exit()``.

.. _tut-string-pattern-matching:

Ricerca di pattern nelle stringhe
=================================

Il modulo :mod:`re` fornisce strumenti per il trattamento delle stringhe con 
le *regular expression*. Per ricerche e manipolazioni sofisticate, le regular 
expression costituiscono una soluzione compatta ed efficiente::

   >>> import re
   >>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
   ['foot', 'fell', 'fastest']
   >>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
   'cat in the hat'

Tuttavia, per ricerche e sostituzioni semplici, è preferibile usare i metodi 
delle stringhe, che sono più semplici da leggere e correggere::

   >>> 'tea for too'.replace('too', 'two')
   'tea for two'

.. _tut-mathematics:

Matematica
==========

Il modulo :mod:`math` dà accesso alla sottostante libreria C, che raccoglie 
funzioni per il calcolo in virgola mobile::

   >>> import math
   >>> math.cos(math.pi / 4)
   0.70710678118654757
   >>> math.log(1024, 2)
   10.0

Il modulo :mod:`random` consente di effettuare selezioni casuali::

   >>> import random
   >>> random.choice(['apple', 'pear', 'banana'])
   'apple'
   >>> random.sample(range(100), 10)   # campionamento senza rimpiazzamento
   [30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
   >>> random.random()    # un float casuale
   0.17970987693706186
   >>> random.randrange(6)    # in intero casuale compreso in range(6)
   4

Il modulo :mod:`statistics` produce misure statistiche di base (media, 
mediana, varianza etc.) su dati numerici::

    >>> import statistics
    >>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
    >>> statistics.mean(data)
    1.6071428571428572
    >>> statistics.median(data)
    1.25
    >>> statistics.variance(data)
    1.3720238095238095

Il progetto `SciPy <https://scipy.org>`_ offre molti altri moduli per il 
calcolo numerico. 

.. _tut-internet-access:

Accesso a internet
==================

Esistono diversi moduli per accedere a internet e gestire i protocolli 
internet. Due dei più semplici sono :mod:`urllib.request` per raccogliere dati 
da una URL e :mod:`smtplib` per spedire email::

   >>> from urllib.request import urlopen
   >>> with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
   ...     for line in response:
   ...         line = line.decode()             # Converte i bytes a str
   ...         if line.startswith('datetime'):
   ...             print(line.rstrip())         # Rimuove l'a-capo finale
   ...
   datetime: 2022-01-01T01:36:47.689215+00:00

   >>> import smtplib
   >>> server = smtplib.SMTP('localhost')
   >>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
   ... """To: jcaesar@example.org
   ... From: soothsayer@example.org
   ...
   ... Beware the Ides of March.
   ... """)
   >>> server.quit()

(Si noti che l'ultimo esempio richiede che un server mail sia funzionante su 
localhost.)

.. _tut-dates-and-times:

Date e orari
============

Il modulo :mod:`datetime` contiene delle classi per manipolazioni semplici e 
complesse di date e orari. Anche se i calcoli con le date sono supportati, il 
modulo si concentra soprattutto sull'estrazione dei componenti per scopi di 
manipolazione e formattazione. Sono anche previsti oggetti sensibili alle 
*timezone*. ::

   >>> # dates are easily constructed and formatted
   >>> from datetime import date
   >>> now = date.today()
   >>> now
   datetime.date(2003, 12, 2)
   >>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
   '12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

   >>> # le date supportano l'aritmetica del calendario
   >>> birthday = date(1964, 7, 31)
   >>> age = now - birthday
   >>> age.days
   14368

.. _tut-data-compression:

Compressione dei dati
=====================

I moduli :mod:`zlib`, :mod:`gzip`, :mod:`bz2`, :mod:`lzma`, :mod:`zipfile` e
:mod:`tarfile` offrono il supporto per i comuni formati di archiviazione e 
compressione dei dati. ::

   >>> import zlib
   >>> s = b'witch which has which witches wrist watch'
   >>> len(s)
   41
   >>> t = zlib.compress(s)
   >>> len(t)
   37
   >>> zlib.decompress(t)
   b'witch which has which witches wrist watch'
   >>> zlib.crc32(s)
   226805979

.. _tut-performance-measurement:

Misurazione di performance
==========================

Alcuni utenti di Python sono molto interessati a conoscere la differenza tra 
vari approcci allo stesso problema, in termini di performance. Python mette a 
disposizione uno strumento di misura che risponde immediatamente a queste 
domande. 

Per esempio, si può provare a usare lo spacchettamento di tupla, invece del 
tradizionale approccio di scambiare le variabili. Il modulo :mod:`timeit` ci 
fa rapidamente vedere che in effetti esiste un leggero vantaggio di 
performance::

   >>> from timeit import Timer
   >>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
   0.57535828626024577
   >>> Timer('a,b = b,a', 'a=1; b=2').timeit()
   0.54962537085770791

Mentre :mod:`timeit` ha un livello di granularità più fine, i moduli 
:mod:`profile` e :mod:`pstats` forniscono strumenti per identificare, 
all'interno di sezioni di codice più ampie, le parti che provocano 
rallentamenti. 

.. _tut-quality-control:

Controllo di qualità
====================

Una strada per scrivere codice di alta qualità è quella di scrivere dei test 
per ciascuna funzione, man mano che viene sviluppata, e di eseguire i test con 
una certa frequenza durante il processo di sviluppo. 

Il modulo :mod:`doctest` è uno strumento per scansionare un modulo e validare 
i test che sono contenuti nelle sue docstring. Creare un test è questione di 
un semplice copia-e-incolla, nella docstring, dell'invocazione e del risultato 
atteso. In questo modo si migliora la documentazione, fornendo un esempio di 
utilizzo per l'utente, e si permette a *doctest* di garantire che il codice 
resti fedele a quanto documentato::

   def average(values):
       """Restituisce la media aritmetica di una lista di numeri.

       >>> print(average([20, 30, 70]))
       40.0
       """
       return sum(values) / len(values)

   import doctest
   doctest.testmod()   # valida automaticamente i test inclusi

Il modulo :mod:`unittest` non è di immediato utilizzo come :mod:`doctest`, ma 
permette di mantenere una raccolta più completa di test in file separati::

   import unittest

   class TestStatisticalFunctions(unittest.TestCase):

       def test_average(self):
           self.assertEqual(average([20, 30, 70]), 40.0)
           self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
           with self.assertRaises(ZeroDivisionError):
               average([])
           with self.assertRaises(TypeError):
               average(20, 30, 70)

   unittest.main()  # invocare dalla riga di comando esegue tutti i test

.. _tut-batteries-included:

Le batterie sono incluse
========================

La filosofia di Python è che "le batterie sono incluse". Ne è prova 
l'inclusione nella libreria standard di grandi package che forniscono 
strumenti più sofisticati e robusti. Per esempio:

* Con i moduli :mod:`xmlrpc.client` e :mod:`xmlrpc.server`, realizzare 
  invocazioni di procedure remote diventa quasi banale. Nonostante il nome, 
  non è necessario conoscere o manipolare XML per usarli. 

* Il package :mod:`email` è una libreria per manipolare i messaggi email, che 
  include MIME e altri documenti basati sulla :rfc:`2822`. A differenza di 
  :mod:`smtplib` e :mod:`poplib`, che ricevono e spediscono messaggi, questo 
  package fornisce un set di strumenti completo per costruire e decodificare 
  strutture complesse, allegati inclusi, e per implementare gli encoding di 
  internet e i protocolli degli *header*. 

* Il package :mod:`json` supporta il *parsing* di questo popolare formato 
  d'interscambio. Il modulo :mod:`csv` fornisce strumenti per la lettura e 
  scrittura di file in formato CSV, molto diffuso per i database e i fogli di 
  calcolo. La gestione di XML è garantita dai package 
  :mod:`xml.etree.ElementTree`, :mod:`xml.dom` e :mod:`xml.sax`. 
  Complessivamente, questi moduli e package semplificano molto lo scambio di 
  informazioni tra le applicazioni Python e il mondo esterno. 

* Il modulo :mod:`sqlite3` permette l'accesso ai database SQLite, mettendo a 
  disposizione uno strumento di persistenza accessibile con una sintassi SQL 
  leggermente modificata. 

* L'internazionalizzazione è garantita da un gran numero di moduli come 
  :mod:`gettext`, :mod:`locale` e il package :mod:`codecs`.
