# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath('../../MRP'))
sys.path.insert(0, os.path.abspath('../../MRPcli'))
sys.path.insert(0, os.path.abspath('../../tests'))
sys.path.insert(0, os.path.abspath('../../MRPudpp'))
sys.path.insert(0, os.path.abspath('../../../MagneticReadoutProcessing'))
#sys.path.insert(0, os.path.abspath('../../test'))
autodoc_mock_imports = ["numpy",
                        "configparser",
                        "google",
                        "matplotlib",
                        "math",
                        "vg",
                        "support",
                        "test_support",
                        "libregrtest",
                        "regrtest",
                        "ann_module3",
                        "ann_module2",
                        "ann_module",
                        "test",
                        "vector",
                        "testsupport"]


autodoc_default_options = {
    "private-members": False,
    "inherited-members": True,
}
# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "MagneticReadoutProcessing"
copyright = "2023, Marcel Ochsendorf"
author = "Marcel Ochsendorf"
master_doc = "index"
language = "en"

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- General configuration ---------------------------------------------------
# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
#    "myst_parser"
]
autosummary_generate = True  # Turn on sphinx.ext.autosummary

intersphinx_mapping = {
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["templates"]

# -- Options for EPUB output
epub_show_urls = "footnote"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["static"]
