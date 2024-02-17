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
rm -Rf tmp


if [[ ! -v BUILD_FAST ]]; then

rm -f ./thesis_document_tmp.md
rm -f ./thesis_document_tmp.md.*

rm -Rf generated_images
mkdir -p generated_images
# REMOVE GENERATED TEX
rm -f ./thesis_declaration.tex
rm -f ./thesis_document.tex
rm -f ./thesis_document_tmp.tex
rm -f ./thesis_abstract.tex
rm -f ./thesis_attachments.tex
fi
# REMOVE GENERATED PDF
rm -f ./thesis.pdf


echo "-- STARTING BUILDING THESIS DOCUMENT --"
pandoc --version

# CONVERT CSV TABLES to MARKDOWN
if [[ ! -v BUILD_FAST ]]; then
cp ./thesis_document.md ./thesis_document_tmp.md 
FILES="./tables/*.csv"
for f in $FILES
do
    FN="${f##*/}"
    FNWOE="${FN%%.*}"
    echo "Processing table $FN file..."
    cat "$f"
    # CREATE TABLE MARKDOWN FILE
    rm -f "$f.md"
    touch "$f.md"
    replace="_"
    replacewith=" "
    TABLENAME="${FNWOE//${replace}/${replacewith}}"
    echo "tablename: $TABLENAME"
    ## INSERT TABLE HEADER AND REF
    echo ": $TABLENAME \label{$FN}" >> "$f.md"
    echo "" >> "$f.md"
    ## INSERT TABLE
    csv2md "$f" >> "$f.md"
    cat "$f.md"


    # REPLACE CONTENT WITH SED
    #cat "$f.md" | sed -e 's/[@table:'$FN']/g/' ./thesis_document_tmp.md 
    str="%%$FN%%"
    echo "$str"
    sed -e "/$str/ {" -e "r $f.md" -e 'd' -e '}' -i ./thesis_document_tmp.md 
done
fi




if [[ ! -v BUILD_FAST ]]; then
# ADD IMAGES
imagefiles="./images/*.png"
for f in $imagefiles
do  
    FN="${f##*/}"
    FNWOE="${FN%%.*}"
    echo "Processing image $FN file..."

    # ADD A SMALL BORDER AROUNF THE IMAGE
    DIR="$(dirname "${f}")" 
    filenameimageboarder="./generated_images/border_$FN"
    cp "$f" "$filenameimageboarder"
    # ADD IMAGE BORDERS
    convert -bordercolor transparent -border 10 "$f" "$filenameimageboarder"


    
    # CREATE TABLE MARKDOWN FILE
    rm -f "$f.md"
    touch "$f.md"
    replace="_"
    replacewith=" "
    IMAGENAME="${FNWOE//${replace}/${replacewith}}"
    echo "image: $IMAGENAME"
    ## INSERT TABLE HEADER AND REF
    echo "![$IMAGENAME \label{$FN}]($filenameimageboarder)" >> "$f.md"
    #echo ": $IMAGENAME \label{$FN}" >> "$f.md"
    echo "" >> "$f.md"
    ## INSERT TABLE
    cat "$f.md"


    # REPLACE CONTENT WITH SED
    #cat "$f.md" | sed -e 's/[@table:'$FN']/g/' ./thesis_document_tmp.md 
    str="%%$FN%%"
    echo "$str"
    sed -e "/$str/ {" -e "r $f.md" -e 'd' -e '}' -i ./thesis_document_tmp.md 
done
fi

if [[ ! -v BUILD_FAST ]]; then
# CONVERT LISTINGS
python3 convert_listings_head.py ./thesis_document_tmp.md 


pandoc ./thesis_document_tmp.md.listings -o ./thesis_document.tex --from markdown --biblatex --template ./pandoc_template.tex --listings --top-level-division=chapter --lua-filter ./pandoc_filters/pandoc-gls.lua #x -M codeBlockCaptions=true
# NOW THE HACKY PART WE WANT TO USE THE STANDART cite command instead the from pandoc used cite to we use sed to hard replace the stuff
# sed -i 's/\\autocite{/\\cite{/g' ./thesis_document.tex

# python3 ./fix-table-color-bleed.py ./thesis_document.tex > ./thesis_document.tex
pandoc ./thesis_declaration.md -o ./thesis_declaration.tex --from markdown --top-level-division=chapter --listings
pandoc ./thesis_abstract.md -o ./thesis_abstract.tex --from markdown --top-level-division=chapter --listings
pandoc ./thesis_attachments.md -o ./thesis_attachments.tex --from markdown --top-level-division=chapter --listings

sed -i 's/\\autocite{/\\customcite{/g' ./thesis_document.tex

echo "------------- PANDOC GENERATION FINISHED -----------"
fi


python3 ./generate_citealias.py ./thesis_document.tex  ./thesis_references_alias.tex
#sed -i 's/\\autocite{/\\cite{/g' ./thesis_document.tex



# BUILD THESIS FIRST TIME GENERATE .AUX and .TOC FILE
pdflatex ./thesis.tex ./thesis.pdf
# GENERATE BIBTEX INDEX
makeglossaries thesis # ACRONYM
bibtex thesis # REFERENCES
pdflatex ./thesis.tex ./thesis.pdf
# BUILD FINAL DOCUMENT
pdflatex ./thesis.tex ./thesis.pdf

echo "------------- PDF EXPORT FINISHED -----------"



# EXPORT AS HTML

#pandoc -s thesis.tex -o thesis.md
#pandoc thesis.tex -f latex -t html -s -o thesis.html --bibliography thesis_references.bib

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
rm -Rf tmp



# COPY INTO BUILD FOLDER
rm -f ./build_out/*.*
cp thesis.pdf ./build_out/
cp -Rf ./deploly_server ./build_out

DIR="/tmp/thesis_build"
if [ -d "$DIR" ]; then
  echo "copy build into ${DIR}"
  cp -Rf ./build_out/ $DIR
fi
# TODO IF ENV IS sET
# START HTTP SERVER

exit 0
