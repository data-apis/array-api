# You can set these variables from the command line.
SPHINXOPTS    ?= -W --keep-going
SOURCEDIR     = spec
BUILDDIR      = _site

.PHONY: default clean build

default: clean build

clean:
	-rm -rf $(BUILDDIR)
	-find . -type d -name generated -exec rm -rf {} +

build:
	-mkdir -p $(BUILDDIR)
	-cp "$(SOURCEDIR)/_ghpages/_gitignore.txt" "$(BUILDDIR)/.gitignore"
	-cp "$(SOURCEDIR)/_ghpages/versions.json" "$(BUILDDIR)/versions.json"
	-cp "$(SOURCEDIR)/_ghpages/index.html" "$(BUILDDIR)/index.html"
	-touch "$(BUILDDIR)/.nojekyll"
	-sphinx-build "$(SOURCEDIR)/2021.12" "$(BUILDDIR)/2021.12" $(SPHINXOPTS)
	-cp -r "$(BUILDDIR)/2021.12" "$(BUILDDIR)/latest"
	-sphinx-build "$(SOURCEDIR)/draft" "$(BUILDDIR)/draft" $(SPHINXOPTS)
