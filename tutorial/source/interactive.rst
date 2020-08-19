.. _tut-interacting:

*****************************************************
Editing e history substitution nell'input interattivo
*****************************************************

Alcune versioni dell'interprete Python supportano l'editing dell'input 
corrente e la *history substitution*, in modo analogo alle shell Korn e GNU 
Bash. Questa possibilità è implementata con la libreria `GNU Readline`_, che 
supporta diversi stili di editing e che ha una sua documentazione, che 
pertanto non ripetiamo in questa sede. 

.. _tut-keybindings:

Tab completion e history editing
================================

Il completamento delle variabili e dei nomi dei moduli è 
:ref:`abilitato automaticamente<rlcompleter-config>` all'avvio 
dell'interprete, così che il tasto :kbd:`Tab` invoca la funzione di 
*completion* cercando tra i nomi delle istruzioni, le variabili locali e i 
nomi dei moduli disponibili. Le espressioni con il punto, come ``string.a``, 
sono valutate fino al punto finale; quindi vengono suggeriti completamenti 
tratti dagli attributi dell'oggetto risultante. Si noti che così facendo è 
possibile che sia eseguito del codice dell'applicazione, se l'espressione 
comprende un oggetto con un metodo :meth:`__getattr__` definito. La 
configurazione di default salva inoltre la storia dei comandi in un file 
:file:`.python_history` nella vostra directory home. La storia sarà nuovamente 
disponibile nella prossima sessione dell'interprete. 

.. _tut-commentary:

Alternative all'interprete interattivo
======================================

Queste funzionalità costituiscono un grande passo avanti rispetto alle prime 
versioni dell'interprete. Tuttavia, alcune cose restano irrisolte: sarebbe 
utile presentare un rientro adeguato per le linee di continuazione, dal 
momento che l'interprete riconosce se il prossimo *token* richiede un rientro. 
Il meccanismo di completamento potrebbe utilizzare la tabella dei simboli 
dell'interprete. Sarebbe anche utile avere un comando per controllare o 
suggerire il bilanciamento delle parentesi, degli apici etc. 

Un'alternativa potenziata per l'interprete interattivo, disponibile da 
parecchi anni, è IPython_ che supporta la *tab completion*, l'esplorazione 
degli oggetti e la gestione avanzata della storia dei comandi. Può anche 
essere personalizzato in molti aspetti e incorporato in altre applicazioni. Un 
ambiente di sviluppo simile è bpython_.

.. _GNU Readline: https://tiswww.case.edu/php/chet/readline/rltop.html
.. _IPython: https://ipython.org/
.. _bpython: https://www.bpython-interpreter.org/
