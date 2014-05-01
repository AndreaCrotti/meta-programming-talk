# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = meta

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   =  $(PAPEROPT_$(PAPER)) $(SPHINXOPTS)
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
DROP = $(HOME)/Dropbox/Public/talks

.PHONY: unit clean upload

all: test unit upload

test:
	nosetests3 code/test_meta.py

upload:
	cp -Rv $(BUILDDIR) $(DROP)/

unit:
	$(SPHINXBUILD) -b slides $(ALLSPHINXOPTS) . $(BUILDDIR)

clean:
	-rm -rf $(BUILDDIR)
