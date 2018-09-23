main:
	rm main.gl*
	pdflatex main.tex
	makeglossaries main
	pdflatex main.tex