.. _tut-using:

**************************
Usare l'interprete Python.
**************************

.. _tut-invoking:

Invocare l'interprete
=====================

L'interprete Python di solito è installato in :file:`/usr/local/bin/python3.9` sui computer dove è disponibile. Aggiungere :file:`/usr/local/bin` alla *path* della shell Unix vi permette di invocarlo con il comando [#]_

.. code-block:: text

   python3.9

Dal momento che la scelta della directory dell'interprete è un'opzione di installazione, sono possibili altre configurazioni. Chiedete a un esperto di Python o all'amministratore del sistema. Per esempio, un'alternativa popolare è :file:`/usr/local/python`.

Su Windows, se avete installato Python dal :ref:`Microsoft Store<windows-store>`, sarà disponibili il comando :file:`python3.9`. Se avete installato il *launcher* :ref:`py.exe <launcher>` potete usare il comando :file:`py`. Il paragrafo :ref:`Excursus: Impostare le variabili d'ambiente<setting-envvars>` descrive altri modi per avviare Python. 

Inserire il carattere terminatore del file (:kbd:`Control-D` in Unix, :kbd:`Control-Z` in Windows) nel *prompt* principale costringe l'interprete a uscire con *exit status* ``0``. Se non funziona, potete uscire dall'interprete con questo comando: ``quit()``.

Sui sistemi che supportano la libreria `GNU Readline <https://tiswww.case.edu/php/chet/readline/rltop.html>`_, l'interprete consente di fare *editing* interattivo, auto-completamento e storico degli inserimenti. Il modo più rapido per controllare se l'editing della riga di comando è supportato, è inserire :kbd:`Control-P` appena il prompt primario di Python è disponibile. Se sentite un beep, l'editing è supportato; l'Appendice :ref:`tut-interacting` presenta un'introduzione a questi comandi. Se invece non succede nulla, o se risponde semplicemente ``^P``, l'editing non è disponibile: potete solo usare il *backspace* per cancellare i caratteri. 

L'interprete funziona più o meno come la shell di Unix: quando è invocato con lo *standard input* collegato al terminale, legge ed esegue interattivamente i comandi; quando è invocato con il nome di un file come parametro, o con lo standard input collegato a un file, legge ed esegue il file come *script*.  

Un altro modo di avviare l'interprete è ``python -c command [arg] ...``, che esegue l'istruzione (o le istruzioni) in *command*, analogamente all'opzione :option:`-c` della shell. Siccome le istruzioni Python di solito comprendono spazi o altri caratteri speciali della shell, è consigliabile racchiudere *command* tra apici singoli. 

Alcuni moduli Python possono essere eseguiti come script. Si possono invocare con ``python -m module [arg] ...``, che esegue il file *module* come se ne aveste scritto il nome per intero nella riga di comando. 

Quando si esegue uno script, talvolta è utile poter entrare in modalità interattiva al termine dell'esecuzione del file. Per fare questo, passate l'opzione :option:`-i` prima del nome dello script. 

Tutte le opzioni della riga di comando sono descritte nel capitolo :ref:`Riga di comando e ambiente<using-on-general>` della documentazione. 

.. _tut-argpassing:

Passare dei parametri
---------------------

Quando specificati, il nome dello script ed eventuali successivi parametri sono convertiti in una lista di stringhe e assegnate alla variabile ``argv`` del modulo ``sys``. Potete accedere a questa lista eseguendo ``import sys``. La lista contiene sempre almeno un elemento; se non passate nessuno script né altri parametri, ``sys.argv[0]`` è una stringa vuota. Quando invece di uno script passate ``'-'``, per indicare lo standard input, allora ``sys.argv[0]`` è impostato a ``'-'``. Quando usate :option:`-c` *command*, allora ``sys.argv[0]`` è ``'-c'``. Quando usate :option:`-m` *module*, ``sys.argv[0]`` è il nome completo del modulo eseguito. Le opzioni eventualmente passate dopo :option:`-c` *command* oppure :option:`-m` *module* non sono processate dall'interprete Python ma sono comunque disponibili in ``sys.argv`` e possono quindi essere gestite dal modulo o dal comando. 

.. _tut-interactive:

Modalità interattiva
--------------------

Quando i comandi sono letti da un terminale, l'interprete è in *modalità interattiva*. In questa condizione, l'interprete resta in attesa del comando successivo presentando il *prompt primario*, di solito tre segni "maggiore-di" (``>>>``). Per le linee di continuazione viene usato il *prompt secondario*, in genere tre punti (``...``). L'interprete stampa un messaggio di benvenuto che riporta il numero di versione e l'indicazione del copyright, prima di presentare il prompt:

.. code-block:: shell-session

   $ python3.9
   Python 3.9 (default, June 4 2019, 09:25:04)
   [GCC 4.8.2] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>>

.. XXX update for new releases

Le linee di continuazione sono necessarie per i costrutti multi-linea. Per esempio, osservate questa istruzione :keyword:`if`::

   >>> the_world_is_flat = True
   >>> if the_world_is_flat:
   ...     print("Be careful not to fall off!")
   ...
   Be careful not to fall off!

Per ulteriori informazioni sulla modalità interattiva, si veda :ref:`tut-interac`.

.. _tut-interp:

L'interprete e il suo ambiente
==============================

.. _tut-source-encoding:

*Encoding* del codice
---------------------

I file di codice Python sono processati con l'encoding UTF-8 di default. In questo encoding, i caratteri della gran parte dei linguaggi umani possono essere usati contemporaneamente nelle stringhe di testo, negli identificatori e nei commenti. Tuttavia la libreria standard usa esclusivamente caratteri ASCII per gli identificatori, una convenzione che il codice interessato alla compatibilità dovrebbe rispettare. Per visualizzare correttamente i caratteri, il vostro editor deve saper riconoscere l'encoding UTF-8 e deve usare un font che supporta tutti i caratteri usati nel file. 

Per dichiarare un encoding diverso da quello di default, occorre aggiungere una riga speciale di commento esattamente *all'inizio* del file. La sintassi è questa::

   # -*- coding: encoding -*-

dove *encoding* è uno dei vari :mod:`codecs` supportati da Python.

Per esempio, per dichiarare che occorre usare l'encoding Windows-1252 per leggere il file, la prima riga del codice dovrebbe essere::

   # -*- coding: cp1252 -*-

L'eccezione alla regola è quando lo script inizia invece con una :ref:`shebang UNIX<tut-scripts>`. In questo caso, la dichiarazione di encoding deve essere la seconda riga del file. Per esempio::

   #!/usr/bin/env python3
   # -*- coding: cp1252 -*-

.. only:: html

   .. rubric:: Note

.. [#] In ambiente Unix, l'eseguibile dell'interprete Python 3.x *non* è installato col nome ``python``, così da non entrare in conflitto con l'eseguibile di Python 2.x, anch'esso contemporaneamente presente. 
