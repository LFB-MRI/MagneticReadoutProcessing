FROM ubuntu:22.04

LABEL org.opencontainers.image.source=https://github.com/RBEGamer/MarkdownThesisTemplate



ARG DEBIAN_FRONTEND=noninteractive

RUN apt update
RUN apt install -y texlive-full texmaker pandoc sed nano

RUN apt install -y imagemagick

RUN apt install -y build-essential
RUN apt install -y haskell-platform
#RUN apt install -y cabal-install
RUN apt install -y python3 python3-pip
RUN pip3 install setuptools

#RUN apt install locales
#RUN locale-gen en_US.utf8


RUN export PATH="$HOME/.cabal/bin:$PATH"
#RUN cabal install cabal-install
#RUN cabal update

#RUN cabal install alex happy
#RUN cabal install --ghc-options="+RTS -M7G" -j1 --force-reinstalls pandoc
#RUN cabal install --ghc-options="+RTS -M7G" -j1 --force-reinstalls --dependencies-only pandoc-csv2table
WORKDIR /tmp
COPY csv2md .
RUN python3 ./setup.py install
RUN csv2md -h

WORKDIR /var/thesis
COPY . .
CMD ["/var/thesis/build_thesis.sh"]
