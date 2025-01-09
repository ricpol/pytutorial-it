# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Il tutorial di Python'
copyright = '2025, Riccardo Polignieri'
author = 'Riccardo Polignieri'

# we don't need version number - we just track Python releases
release = ''

master_doc = 'index'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.intersphinx']

intersphinx_mapping = {'python': ('https://docs.python.org/3.11', None)}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'it'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Latex options ------------------------

latex_engine = 'xelatex'

preamble_contents = r'''
\addto\captionsitalian{\renewcommand{\literalblockcontinuedname}{...segue}}
\addto\captionsitalian{\renewcommand{\literalblockcontinuesname}{continua...}}
'''

latex_elements = {
    'papersize': 'a4paper',
    'preamble': preamble_contents,
    'classoptions': ',oneside',
}

latex_documents = [
    (master_doc, 'pytutorial-it.tex', 'Il tutorial di Python',
     'traduzione a cura di Riccardo Polignieri', 'manual', False),
]

latex_toplevel_sectioning = 'chapter'
latex_domain_indices = False
