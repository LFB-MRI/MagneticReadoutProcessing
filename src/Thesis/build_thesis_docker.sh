#!/bin/bash

if [[ "$(docker images -q markdownthesisbuilder:latest 2> /dev/null)" == "" ]]; then
  echo "markdownthesisbuilder:latest IMAGE BUILD STARTED"
  docker build -t markdownthesisbuilder:latest .
else
 echo "markdownthesisbuilder:latest IMAGE EXISTS; NO BUILD REQUIRED"
fi


docker run -i --rm -v "$(pwd)":/var/thesis markdownthesisbuilder



#docker tag markdownthesisbuilder ghcr.io/rbegamer/markdownthesistemplate:latest