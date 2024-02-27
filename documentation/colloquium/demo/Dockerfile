FROM python:3.11

ENV TZ=Europe \
    DEBIAN_FRONTEND=noninteractive

# Update and install necessary packages
RUN apt-get update && apt-get install -y --no-install-recommends python3-serial curl wget python3-pip
RUN pip install MagneticReadoutProcessing
WORKDIR /demo
COPY . .
RUN MRPCli --help
