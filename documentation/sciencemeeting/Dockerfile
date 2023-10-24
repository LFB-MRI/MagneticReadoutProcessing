FROM node:lts-buster
#chromium for pdf export
#RUN apt-get update  && apt-get install -y libglu1 chromium
COPY . ./base
#RUN mkdir /base
WORKDIR /base
RUN chmod +x ./run.sh
RUN ls /base && sleep 1

ENV NODE_OPTIONS=--openssl-legacy-provider

RUN npm install
RUN npm i @fusuma/task-pdf
RUN npm i mermaid
RUN npm audit fix --force || true
RUN chown -R node:node /base
USER node

ENTRYPOINT ["/base/run.sh"]
