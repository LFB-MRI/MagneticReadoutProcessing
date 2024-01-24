#!/bin/bash

if [[ "$(docker images -q mrpcolloquium:latest 2> /dev/null)" == "" ]]; then
  echo "mrpcolloquium:latest IMAGE BUILD STARTED"
  docker build -t mrpcolloquium:latest .
else
 echo "rbegamer/fusuma:latest IMAGE EXISTS; NO BUILD REQUIRED"
fi


docker run -i --rm -p 8080:8080  \
    -v "$(pwd)/:/base/" \
    -e FUSUM_EXPORT_ONLY='1' \
    mrpcolloquium:latest
   # -v "$(pwd)/images:/base/images" \
   # -v "$(pwd)/fusumarc.yml:/base/.fusumarc.yml" \
   # -v "$(pwd)/package.json:/base/package.json" \
    
