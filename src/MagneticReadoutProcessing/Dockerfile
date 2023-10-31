FROM python:3
LABEL authors="marcelochsendorf"

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# RUN TESTS BEFORE
RUN python ./tests/all_tests.py

RUN python ./MRPcli.py --install-completion bash
#
ENTRYPOINT [ "python", "./cli.py"]
#CMD [ "python", "./MRPcli.py" , "--help"]
