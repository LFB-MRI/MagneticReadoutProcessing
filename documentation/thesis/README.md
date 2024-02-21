# Markdown Thesis Template
The master thesis behind MagnetCharacterization project


# TODO

formeln mittels 
```formular {caption='abc'}
``

bilder generierieren neu als order:
LABEL_FOLDER:
=> caption.txt
=> image.png


`\noteworthy{\text{CoG} = \frac{\sum{D_{istance} \times W_{eight}}}{\sum{W_{eight}}}}{Center of Gravity}`

## Build thesis document as PDF

* install docker

```bash
$ cd src && bash build_thesis_docker.sh
# result is: thesis.tex and thesis.pdf
``````

## Edit document

* `thesis_abstract.md` -  Abtract 
* `thesis_declaration.md` - Legal notices
*  `thesis_document.md` - MAIN DOCUMENT

*  `thesis_references.bib` -  Book references
*  `thesis_acronyms.tex` -  Word acronyms
*  `thesis_titleinformation.tex` - Coverpage information

## IMAGES
See `MAKRDOWN_SNIPPETS.md`
Place all images in `images` folder with name as caption, use underscore as blankspace

## TABLES
See `MAKRDOWN_SNIPPETS.md`
Place all .csv tables in `tables` folder with name as caption, use underscore as blankspace


## CODE
See `MAKRDOWN_SNIPPETS.md`
