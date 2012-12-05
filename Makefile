.PHONY: doc
doc:
	a2x -f xhtml README.asciidoc

.PHONY: clean
clean:
	rm -rf *.css
	rm -rf *.html
	rm -rf __pycache__ */__pycache__
	rm -rf *.py[co] */*.py[co]
