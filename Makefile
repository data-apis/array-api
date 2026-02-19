# You can set these variables from the command line.
SPHINXOPTS    ?= -W --keep-going
SOURCEDIR     = spec
BUILDDIR      = _site

.PHONY: default clean draft spec

default: clean spec

clean:
	rm -rf $(BUILDDIR)
	find . -type d -name generated -exec rm -rf {} +

draft:
	mkdir -p $(BUILDDIR)
	sphinx-build "$(SOURCEDIR)/draft" "$(BUILDDIR)/draft" $(SPHINXOPTS)

spec:
	mkdir -p $(BUILDDIR)
	cp "$(SOURCEDIR)/_ghpages/_gitignore.txt" "$(BUILDDIR)/.gitignore"
	cp "$(SOURCEDIR)/_ghpages/versions.json" "$(BUILDDIR)/versions.json"
	cp "$(SOURCEDIR)/_ghpages/index.html" "$(BUILDDIR)/index.html"
	touch "$(BUILDDIR)/.nojekyll"
	sphinx-build "$(SOURCEDIR)/2021.12" "$(BUILDDIR)/2021.12" $(SPHINXOPTS)
	sphinx-build "$(SOURCEDIR)/2022.12" "$(BUILDDIR)/2022.12" $(SPHINXOPTS)
	sphinx-build "$(SOURCEDIR)/2023.12" "$(BUILDDIR)/2023.12" $(SPHINXOPTS)
	sphinx-build "$(SOURCEDIR)/2024.12" "$(BUILDDIR)/2024.12" $(SPHINXOPTS)
	sphinx-build "$(SOURCEDIR)/2025.12" "$(BUILDDIR)/2025.12" $(SPHINXOPTS)
	cp -r "$(BUILDDIR)/2025.12" "$(BUILDDIR)/latest"
	sphinx-build "$(SOURCEDIR)/draft" "$(BUILDDIR)/draft" $(SPHINXOPTS)
