#!/bin/bash

if [[ "$(docker images -q mrpthesis:latest 2> /dev/null)" == "" ]]; then
  echo "mrpthesis:latest IMAGE BUILD STARTED"
  docker build -t mrpthesis:latest .
else
 echo "markdownthesisbuilder:latest IMAGE EXISTS; NO BUILD REQUIRED"
fi


docker run -i --rm -v "$(pwd)":/var/thesis mrpthesis:latest



#docker tag markdownthesisbuilder ghcr.io/rbegamer/markdownthesistemplate:latest