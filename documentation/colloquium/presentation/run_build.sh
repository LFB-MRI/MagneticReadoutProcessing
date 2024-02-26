#!/bin/bash
cd "$(dirname "$0")"

docker build -t mrppresentation:latest .

#docker run --rm -it -v $(pwd):/presentation mrppresentation:latest /bin/bash -c 'cd /presentation && quarto render'
docker run --rm -it mrppresentation:latest /bin/bash -c 'cd /presentation && quarto render'
docker run --rm -it mrppresentation:latest /bin/bash -c 'cd /presentation && quarto render --to pdf --toc'

