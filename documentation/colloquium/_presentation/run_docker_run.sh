#!/bin/bash
cd "$(dirname "$0")"

if [[ "$(docker images -q mrpcolloquium:latest 2> /dev/null)" == "" ]]; then
  echo "mrpcolloquium:latest IMAGE BUILD STARTED"
  docker build -t mrpcolloquium:latest .
else
 echo "mrpcolloquium:latest IMAGE EXISTS; NO BUILD REQUIRED"
fi


docker run -i --rm -p 8081:8080  \
    -v "$(pwd)/:/base/" \
    mrpcolloquium:latest
   # -v "$(pwd)/images:/base/images" \
   # -v "$(pwd)/fusumarc.yml:/base/.fusumarc.yml" \
   # -v "$(pwd)/package.json:/base/package.json" \


