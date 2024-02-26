#! /bin/bash
export NODE_OPTIONS=--openssl-legacy-provider

env


if [[ -z "${FUSUM_EXPORT_ONLY}" ]]; then
    npx fusuma start
else
    # BUILD HTML
    npx fusuma build
    mv dist dist_html
    #  BUILD PDF
    npx fusuma pdf
    mv dist dist_pdf
fi




#npm build
#npm install fusuma
#fusuma start
