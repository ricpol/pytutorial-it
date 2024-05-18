.. _tut-appendix:

*********
Appendice
*********

.. _tut-interac:

Modalità interattiva
====================

Esistono due versioni della :term:`REPL` interattiva. L'interprete di base, 
tradizionale, è supportato su tutte le piattaforme ma ha minime capacità di 
controllo della riga di comando. 

Sui sistemi Unix-like (es. Linux o macOS) che supportano :mod:`curses` e 
:mod:`readline`, di default è usata una nuova shell interattiva. Questa 
supporta i colori, l'editing multi-riga, la storia dei comandi e la modalità 
"incolla". Per disabilitare i colori, si veda :ref:`using-on-controlling-color` 
per i dettagli. I tasti-funzione forniscono alcune funzionalità aggiuntive: 
:kbd:`F1` attiva l'aiuto interattivo di :mod:`pydoc`. :kbd:`F2` permette di 
scorrere la storia dei comandi senza l'output e i prompt :term:`>>>` e 
:term:`...`. :kbd:`F3` attiva la modalità "incolla", che facilita il copincolla 
di grandi blocchi di testo; premere di nuovo :kbd:`F3` per tornare al normale 
prompt. 

Per uscire dalla nuova shell, si inserisca :kbd:`exit` o :kbd:`quit`. Non è 
necessario aggiungere le parentesi di chiamata. 

Se non si desidera la nuova shell interattiva, si può disabilitare con la 
variabile d'ambiente :envvar:`PYTHON_BASIC_REPL`. 

.. _tut-error:

Gestione degli errori
---------------------

Quando si verifica un errore, l'interprete emette un messaggio di errore e uno 
*stack trace*. In modalità interattiva, ritorna quindi al prompt primario; se 
l'input arriva da un file, esce con *exit status* non-zero dopo aver 
visualizzato lo *stack trace*. (Le eccezioni gestite da una clausola 
:keyword:`except` all'interno di un'istruzione :keyword:`try` non sono 
"errori" in questo contesto.) Alcuni errori sono irrimediabilmente fatali e 
comportano l'uscita con *exit-status* non-zero: per esempio inconsistenze 
interne, o alcune situazioni di esaurimento della memoria disponibile. Tutti i 
messaggi di errore sono scritti nello *standard error*; l'output normale delle 
istruzioni eseguite è scritto nello *standard output*. 

Inserire il carattere di interruzione (di solito :kbd:`Control-C` o 
:kbd:`Delete`) al prompt primario o secondario cancella l'input e ritorna al 
prompt primario. [#]_ Inserire un'interruzione mentre un'istruzione è in 
esecuzione emette l'eccezione :exc:`KeyboardInterrupt`, che può essere gestita 
da un'istruzione :keyword:`try`.

.. _tut-scripts:

Script Python eseguibili
------------------------

Sui sistemi Unix/BSD, gli script Python possono essere resi direttamente 
eseguibili, come gli script della shell, con la riga ::

   #!/usr/bin/env python3

all'inizio dello script (si assume che l'interprete sia nella :envvar:`PATH` 
di sistema dell'utente) e dando al file modalità eseguibile. I caratteri 
``#!`` devono essere esattamente all'inizio del file. Su alcune piattaforme, 
questa prima riga deve terminare con un "a-capo" in stile Unix (``'\n'``) e 
non Windows (``'\r\n'``). Si noti che il cancelletto ``'#'`` viene usato in 
Python per iniziare un commento.

Si può dare al file dello script modalità eseguibile con il comando 
:program:`chmod`.

.. code-block:: shell-session

   $ chmod +x myscript.py

Su Windows non esiste la nozione di "modalità eseguibile". L'installazione di 
Python associa automaticamente le estensioni dei file ``.py`` con 
``python.exe``, in modo che fare doppio clic sul file lo esegue come script. 
L'estensione può anche essere ``.pyw``: in questo caso la finestra della 
console che appare normalmente non viene mostrata. 

.. _tut-startup:

Il file di avvio interattivo
----------------------------

Quando usate Python interattivamente, può far comodo che alcuni comandi 
standard siano eseguiti automaticamente ogni volta che l'interprete viene 
avviato. Questo si può fare creando una variabile d'ambiente 
:envvar:`PYTHONSTARTUP` che contiene il nome di un file con i vostri comandi 
di avvio. È simile a un file :file:`.profile` per le shell di Unix. 

Questo file viene preso in considerazione solo per le sessioni interattive, 
non quando Python legge l'input da uno script, e non quando :file:`/dev/tty` 
è indicato esplicitamente come sorgente per le istruzioni (altrimenti il 
terminale si comporta come una normale sessione interattiva). Il file è 
eseguito nello stesso *namespace* dei comandi interattivi, quindi gli oggetti 
che definisce possono essere importati come nomi non qualificati nella 
sessione dell'interprete. In questo file potete anche cambiare i prompt 
``sys.ps1`` e ``sys.ps2``.

Se volete leggere un file di avvio aggiuntivo nella directory corrente, potete 
farlo nel file di avvio principale con del codice come 
``if os.path.isfile('.pythonrc.py'): exec(open('.pythonrc.py').read())``. 
Se volete usare il file di avvio in uno script, dovete farlo in modo esplicito 
nello script::

   import os
   filename = os.environ.get('PYTHONSTARTUP')
   if filename and os.path.isfile(filename):
       with open(filename) as fobj:
           startup_file = fobj.read()
       exec(startup_file)

.. _tut-customize:

Personalizzare l'installazione
------------------------------

Python mette a disposizione due strumenti che vi consentono di 
personalizzarlo: i moduli :index:`sitecustomize` e :index:`usercustomize`. Per 
vederli in azione, dovete per prima cosa ricavare la collocazione della vostra 
directory *site-packages*. Avviate Python ed eseguite questo codice::

   >>> import site
   >>> site.getusersitepackages()
   '/home/user/.local/lib/python3.x/site-packages'

Adesso potete creare un file :file:`usercustomize.py` in questa directory e 
collocarvi qualsiasi istruzione. Questo avrà effetto su qualsiasi invocazione 
di Python, a meno che non venga passata l'opzione :option:`-s` per 
disabilitarne l'importazione automatica. 

Il modulo :index:`sitecustomize` funziona allo stesso modo, ma viene creato di 
solito da un amministratore del computer nella directory *site-packages* 
globale, ed è importato *prima* di :index:`usercustomize`. Si veda la 
documentazione del modulo :mod:`site` per ulteriori informazioni. 

.. only:: html

   .. rubric:: Note

.. [#] Un problema della libreria GNU Readline potrebbe impedirlo.
