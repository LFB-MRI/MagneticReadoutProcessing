#!/bin/bash
cd .
# REMOVE TEMP FILES
rm -f *.acn
rm -f *.acr
rm -f *.alg
rm -f *.ist
rm -f *.glg
rm -f *.glo
rm -f *.gls
rm -f *.aux
rm -f *.lof
rm -f *.lot
rm -f *.aux
rm -f *.out
rm -f *.toc
rm -f *.log
rm -f *.synctex.gz
rm -f *.bbl
rm -f *.blg
rm -f *.fls
rm -f *.fdb_latexmk
rm -f *.run.xml


# REMOVE GENERATED PDF
rm -f ./main.pdf


echo "-- STARTING BUILDING DOCUMENT --"
pandoc --version




# BUILD THESIS FIRST TIME GENERATE .AUX and .TOC FILE
pdflatex ./main.tex ./main.pdf
# GENERATE BIBTEX INDEX
makeglossaries main # ACRONYM
bibtex main # REFERENCES
pdflatex ./main.tex ./main.pdf
# BUILD FINAL DOCUMENT
pdflatex ./main.tex ./main.pdf


cp ./main.pdf ./paperwssarbeiten.pdf
echo "------------- PDF EXPORT FINISHED -----------"


# REMOVE TEMP FILES
rm -f *.acn
rm -f *.acr
rm -f *.alg
rm -f *.ist
rm -f *.glg
rm -f *.glo
rm -f *.gls
rm -f *.aux
rm -f *.lof
rm -f *.lot
rm -f *.aux
rm -f *.out
rm -f *.toc
rm -f *.log
rm -f *.synctex.gz
rm -f *.bbl
rm -f *.blg
rm -f *.fls
rm -f *.fdb_latexmk
rm -f *.run.xml


exit 0
