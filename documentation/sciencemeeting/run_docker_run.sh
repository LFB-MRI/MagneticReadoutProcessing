#!/bin/bash

if [[ "$(docker images -q mrpsciencemeeting:latest 2> /dev/null)" == "" ]]; then
  echo "mrpsciencemeeting:latest IMAGE BUILD STARTED"
  docker build -t mrpsciencemeeting:latest .
else
 echo "mrpsciencemeeting:latest IMAGE EXISTS; NO BUILD REQUIRED"
fi


docker run -i --rm -p 8080:8080  \
    -v "$(pwd)/:/base/" \
    mrpsciencemeeting:latest
   # -v "$(pwd)/images:/base/images" \
   # -v "$(pwd)/fusumarc.yml:/base/.fusumarc.yml" \
   # -v "$(pwd)/package.json:/base/package.json" \
    
