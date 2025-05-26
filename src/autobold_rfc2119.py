from sphinx.application import Sphinx
import re

rfc_2119_words = [
    'must',
    'must not',
    'required',
    'shall',
    'shall not',
    'should',
    'should not',
    'recommended',
    'not recommended',
    'may',
    'optional',
]

def bold_terms(source):
    return re.sub(rf'\b({"|".join(rfc_2119_words)})\b(?!\[)', r'**\1**', source, flags=re.IGNORECASE)

def bold_terms_source_read(app, docname, source):
    source[0] = bold_terms(source[0])

def bold_terms_autodoc(app, what, name, obj, options, lines):
    for i in range(len(lines)):
        lines[i] = bold_terms(lines[i])

def setup(app: Sphinx):
    app.connect('source-read', bold_terms_source_read)
    app.connect('autodoc-process-docstring', bold_terms_autodoc)
