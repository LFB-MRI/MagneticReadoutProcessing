#!/bin/bash
IMAGE=mrpthesis:latest
if [[ "$(docker images -q $IMAGE 2> /dev/null)" == "" ]]; then
  echo "mrpthesis:latest IMAGE BUILD STARTED"
  docker build -t $IMAGE .
else
 echo "IMAGE EXISTS; NO BUILD REQUIRED"
fi


docker run -i --rm -v "$(pwd)":/var/thesis $IMAGE



#docker tag markdownthesisbuilder ghcr.io/rbegamer/markdownthesistemplate:latest