"""
Base config for all individual Sphinx docs in the array API repo.

The array-api repo contains an individual Sphinx doc for each spec version, all
of which exist in ../spec/. This file is star-imported in the conf.py files of
these docs, allowing us to standardize configuration accross API versions.

Every conf.py file which star-imports this should define

* `release`, the str YYYY.MM release. Use "DRAFT" for the draft.
* `sys.modules['array_api']`, the stubs module to use for autodoc.
"""
import re

import sphinx_material

# -- Project information -----------------------------------------------------

project = 'Python array API standard'
copyright = '2020, Consortium for Python Data API Standards'
author = 'Consortium for Python Data API Standards'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx_markdown_tables',
    'sphinx_copybutton',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
]

autosummary_generate = True
autodoc_typehints = 'signature'
add_module_names = False
napoleon_custom_sections = [('Returns', 'params_style')]
default_role = 'code'

# nitpicky = True makes Sphinx warn whenever a cross-reference target can't be
# found.
nitpicky = True
# autodoc wants to make cross-references for every type hint. But a lot of
# them don't actually refer to anything that we have a document for.
nitpick_ignore = [
    ('py:class', 'collections.abc.Sequence'),
    ('py:class', "Optional[Union[int, float, Literal[inf, - inf, 'fro', 'nuc']]]"),
    ('py:class', "Union[int, float, Literal[inf, - inf]]"),
    ('py:obj', "typing.Optional[typing.Union[int, float, typing.Literal[inf, - inf, 'fro', 'nuc']]]"),
    ('py:obj', "typing.Union[int, float, typing.Literal[inf, - inf]]"),
    ('py:class', 'enum.Enum'),
    ('py:class', 'ellipsis'),
]
nitpick_ignore_regex = [
    ('py:class', '.*array'),
    ('py:class', '.*device'),
    ('py:class', '.*dtype'),
    ('py:class', '.*NestedSequence'),
    ('py:class', '.*SupportsBufferProtocol'),
    ('py:class', '.*PyCapsule'),
    ('py:class', '.*finfo_object'),
    ('py:class', '.*iinfo_object'),
]
# In array_object.py we have to use aliased names for some types because they
# would otherwise refer back to method objects of array
autodoc_type_aliases = {
    'array': 'array',
    'Device': 'device',
    'Dtype': 'dtype',
}

# Make autosummary show the signatures of functions in the tables using actual
# Python syntax. There's currently no supported way to do this, so we have to
# just patch out the function that processes the signatures. See
# https://github.com/sphinx-doc/sphinx/issues/10053.
import sphinx.ext.autosummary as autosummary_mod
if hasattr(autosummary_mod, '_module'):
    # It's a sphinx deprecated module wrapper object
    autosummary_mod = autosummary_mod._module
autosummary_mod.mangle_signature = lambda sig, max_chars=30: sig

# Add any paths that contain templates here, relative to this directory.
templates_path = ['../_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# MyST options
myst_heading_anchors = 3
myst_enable_extensions = ["colon_fence"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
extensions.append("sphinx_material")
html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()
html_theme = 'sphinx_material'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../_static']


# -- Material theme options (see theme.conf for more information) ------------
html_show_sourcelink = False
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

html_theme_options = {

    # Set the name of the project to appear in the navigation.
    'nav_title': f'Python array API standard',

    # Set you GA account ID to enable tracking
    #'google_analytics_account': 'UA-XXXXX',

    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    #'base_url': 'https://project.github.io/project',

    # Set the color and the accent color (see
    # https://material.io/design/color/the-color-system.html)
    'color_primary': 'indigo',
    'color_accent': 'green',

    # Set the repo location to get a badge with stats
    #'repo_url': 'https://github.com/project/project/',
    #'repo_name': 'Project',

    "html_minify": False,
    "html_prettify": False,
    "css_minify": True,
    "logo_icon": "&#xe869",
    "repo_type": "github",
    "touch_icon": "images/apple-icon-152x152.png",
    "theme_color": "#2196f3",
    "master_doc": False,

    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 2,
    # If False, expand all TOC entries
    'globaltoc_collapse': True,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': True,

    "nav_links": [
        {"href": "index", "internal": True, "title": "Array API standard"},
        {
            "href": "https://data-apis.org",
            "internal": False,
            "title": "Consortium for Python Data API Standards",
        },
    ],
    "heroes": {
        "index": "A common API for array and tensor Python libraries",
        #"customization": "Configuration options to personalize your site.",
    },

    "version_dropdown": True,
    "version_json": "../versions.json",
    "table_classes": ["plain"],
}


todo_include_todos = True
#html_favicon = "images/favicon.ico"

html_use_index = True
html_domain_indices = True

extlinks = {
    "duref": (
        "http://docutils.sourceforge.net/docs/ref/rst/" "restructuredtext.html#%s",
        "",
    ),
    "durole": ("http://docutils.sourceforge.net/docs/ref/rst/" "roles.html#%s", ""),
    "dudir": ("http://docutils.sourceforge.net/docs/ref/rst/" "directives.html#%s", ""),
    "pypa": ("https://packaging.python.org/%s", ""),
}

# -- Prettify type hints -----------------------------------------------------
r_type_prefix = re.compile(r"array_api(?:_stubs\._[a-z0-9_]+)?\._types\.")

def process_signature(app, what, name, obj, options, signature, return_annotation):
    if signature:
<<<<<<<< HEAD:spec/2021.12/conf.py
        signature = signature.replace("signatures._types.", "")
    if return_annotation:
        return_annotation = return_annotation.replace("signatures._types.", "")
========
        signature = re.sub(r_type_prefix, "", signature)
    if return_annotation:
        return_annotation = re.sub(r_type_prefix, "", return_annotation)
>>>>>>>> bbd0384 (Squashed old all-versions work):src/_array_api_conf.py
    return signature, return_annotation

def setup(app):
    app.connect("autodoc-process-signature", process_signature)
