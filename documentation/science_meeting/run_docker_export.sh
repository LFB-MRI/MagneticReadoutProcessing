#!/bin/bash

if [[ "$(docker images -q rbegamer/fusuma:latest 2> /dev/null)" == "" ]]; then
  echo "rbegamer/fusuma:latest IMAGE BUILD STARTED"
  docker build -t rbegamer/fusuma:latest .
else
 echo "rbegamer/fusuma:latest IMAGE EXISTS; NO BUILD REQUIRED"
fi


docker run -i --rm -p 8080:8080  \
    -v "$(pwd)/:/base/" \
    -e FUSUM_EXPORT_ONLY='1' \
    rbegamer/fusuma:latest
   # -v "$(pwd)/images:/base/images" \
   # -v "$(pwd)/fusumarc.yml:/base/.fusumarc.yml" \
   # -v "$(pwd)/package.json:/base/package.json" \
    
