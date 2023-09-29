#!/bin/bash

if [[ "$(docker images -q latexmod:latest 2> /dev/null)" == "" ]]; then
  echo "latexmod:latest IMAGE BUILD STARTED"
  docker build -t latexmod:latest .
else
 echo "latexmod:latest IMAGE EXISTS; NO BUILD REQUIRED"
fi


docker run -i --rm -v "$(pwd)":/var/thesis latexmod
