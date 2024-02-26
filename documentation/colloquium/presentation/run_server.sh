#!/bin/bash
cd "$(dirname "$0")"

docker build -t mrppresentation:latest .

#docker run --rm -it -p 8800:8800 -v $(pwd):/presentation mrppresentation:latest /bin/bash -c 'cd /presentation && quarto preview index.qmd --to coeos-revealjs --no-browser --port 8800 --host 0.0.0.0'
docker run --rm -it -p 8800:8800 mrppresentation:latest /bin/bash -c 'cd /presentation && quarto preview index.qmd --to coeos-revealjs --no-browser --port 8800 --host 0.0.0.0'
