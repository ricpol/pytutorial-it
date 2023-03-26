.. _tut-venv:

*****************************
Virtual environment e package
*****************************

Introduzione
============

I programmi Python usano spesso moduli e package che non sono compresi nella 
libreria standard. Inoltre le applicazioni talvolta hanno bisogno di una 
specifica versione di una libreria, perché è necessario che un certo baco sia 
stato risolto, oppure perché fanno uso di una vecchia versione 
dell'interfaccia della libreria. 

Ciò vuol dire che non è possibile che una singola installazione di Python 
possa venire incontro alle esigenze di ogni possibile applicazione. Se il 
programma A richiede la versione 1.0 di un certo modulo, ma il programma B ha 
bisogno della 2.0, queste necessità sono in conflitto e installare una delle 
due versioni non permetterà all'altro programma di funzionare correttamente.

La soluzione è creare un :term:`virtual environment`, ovvero una directory 
auto-sufficiente che contiene una installazione di Python, per una particolare 
versione di Python, oltre a un certo numero di pacchetti aggiuntivi.

Programmi diversi possono usare virtual environment diversi. Per risolvere il 
problema di richieste in conflitto dell'esempio precedente, il programma A può 
avere il suo environment con la versione 1.0 installate, mentre il programma B 
avrà un altro virtual environment con la versione 2.0. Se in seguito B 
richiede un aggiornamento della libreria alla versione 3.0, ciò non avrà 
conseguenze sull'environment di A. 

Creare un virtual environment
=============================

:mod:`venv` è il modulo usato per creare e gestire virtual environment. 
:mod:`venv` installa in genere la versione più recente di Python che avete 
disponibile. Se avete installato più versioni di Python nel vostro sistema, 
potete selezionarne una in particolare invocando ``python3`` o qualsiasi 
versione desiderate.

Per creare un virtual environment, decidete in quale directory volete 
collocarlo e avviate il modulo :mod:`venv` come uno script, passando il 
percorso della directory scelta::

   python -m venv tutorial-env

Questo crea la directory ``tutorial-env`` se non esiste; inoltre crea al suo 
interno le directory che contengono una copia dell'interprete Python 
e diversi file di corredo.

Un luogo comune per conservare i virtual environment è ``.venv``: questo nome 
mantiene la directory nascosta nella shell in modo che non sia d'impiccio, e 
al contempo dice chiaramente a che cosa serve la directory. Inoltre evita 
conflitti con i file ``.env`` di definizione delle variabili d'ambiente, che 
qualche tool supporta. 

Creato il virtual environment, non resta che attivarlo. 

Su Windows invocate::

  tutorial-env\Scripts\activate.bat

Su Unix o MacOS::

  source tutorial-env/bin/activate

(Lo script è scritto per la bash shell. Se usate :program:`csh` o 
:program:`fish`, usate invece gli script alternativi ``activate.csh`` o 
``activate.fish``.)

Attivare il virtual environment cambia il prompt della shell per mostrare il 
nome dell'environment in uso; modifica inoltre l'ambiente di lavoro in modo 
che invocare ``python`` restituisca quella particolare versione e 
installazione dell'interprete. Per esempio:

.. code-block:: bash

  $ source ~/envs/tutorial-env/bin/activate
  (tutorial-env) $ python
  Python 3.5.1 (default, May  6 2016, 10:59:36)
    ...
  >>> import sys
  >>> sys.path
  ['', '/usr/local/lib/python35.zip', ...,
  '~/envs/tutorial-env/lib/python3.5/site-packages']
  >>>


Gestire i pacchetti con Pip
===========================

Potete installare, aggiornare, rimuovere package usando un programma chiamato 
:program:`pip`.  Per default ``pip`` installerà pacchetti pubblicati sul 
`Python Package Index <https://pypi.org>`_. Potete cercare nel PyPI con il 
vostro browser.

``pip`` offre un numero di comandi interni: "install", "uninstall", 
"freeze", etc.  (Si veda la guida a 
:ref:`Installare moduli Python<installing-index>` per la documentazione 
completa di ``pip``.)

Per installare l'ultima versione disponibile di un package, basta specificare 
il suo nome:

.. code-block:: bash

  (tutorial-env) $ python -m pip install novas
  Collecting novas
    Downloading novas-3.1.1.3.tar.gz (136kB)
  Installing collected packages: novas
    Running setup.py install for novas
  Successfully installed novas-3.1.1.3

Potete anche installare una versione specifica, indicando il nome seguito da 
``==`` e il numero di versione:

.. code-block:: bash

  (tutorial-env) $ python -m pip install requests==2.6.0
  Collecting requests==2.6.0
    Using cached requests-2.6.0-py2.py3-none-any.whl
  Installing collected packages: requests
  Successfully installed requests-2.6.0

Se eseguite due volte questo comando, ``pip`` vi informerà che la versione 
richiesta è già presente e non farà nient'altro. Potete indicare un altro 
numero di versione per ottenere quella, oppure eseguire 
``pip install --upgrade`` per aggiornare il pacchetto all'ultima versione:

.. code-block:: bash

  (tutorial-env) $ python -m pip install --upgrade requests
  Collecting requests
  Installing collected packages: requests
    Found existing installation: requests 2.6.0
      Uninstalling requests-2.6.0:
        Successfully uninstalled requests-2.6.0
  Successfully installed requests-2.7.0

``pip uninstall``, seguito dal nome di uno o più pacchetti, li rimuoverà dal 
virtual environment. 

``pip show`` visualizza informazioni su un particolare pacchetto:

.. code-block:: bash

  (tutorial-env) $ pip show requests
  ---
  Metadata-Version: 2.0
  Name: requests
  Version: 2.7.0
  Summary: Python HTTP for Humans.
  Home-page: http://python-requests.org
  Author: Kenneth Reitz
  Author-email: me@kennethreitz.com
  License: Apache 2.0
  Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
  Requires:

``pip list`` elenca tutti i pacchetti installati in un virtual environment:

.. code-block:: bash

  (tutorial-env) $ pip list
  novas (3.1.1.3)
  numpy (1.9.2)
  pip (7.0.3)
  requests (2.7.0)
  setuptools (16.0)

``pip freeze`` produce una lista simile di pacchetti installati, ma usa un 
formato che può essere letto da ``pip install``. Una convenzione molto usata è 
di collocare questa lista in un file ``requirements.txt``:

.. code-block:: bash

  (tutorial-env) $ pip freeze > requirements.txt
  (tutorial-env) $ cat requirements.txt
  novas==3.1.1.3
  numpy==1.9.2
  requests==2.7.0

Il file ``requirements.txt`` può essere incluso nel controllo di versione e 
distribuito come parte dell'applicazione. Gli utenti possono poi usarlo per 
installare tutti i pacchetti necessari con ``install -r``:

.. code-block:: bash

  (tutorial-env) $ python -m pip install -r requirements.txt
  Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
    ...
  Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
    ...
  Collecting requests==2.7.0 (from -r requirements.txt (line 3))
    ...
  Installing collected packages: novas, numpy, requests
    Running setup.py install for novas
  Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0

``pip`` ha molte altre opzioni. Consultate la guida a :ref:`Installare moduli 
Python<installing-index>` per la documentazione completa di ``pip``.  Se avete 
scritto un package Python e volete pubblicarlo sul Python Package Index, 
leggete la guida a :ref:`Distribuire moduli Python<distributing-index>`.
