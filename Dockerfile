FROM ramadhani892/ramubot:slim-buster
# Rama ganteng, Yang hapus credit, Lo babi heheh
# ======================
#    RAM-UBOT DOCKER
#   FROM DOCKERHUB.COM
# ======================

RUN git clone -b RAM-UBOT https://github.com/amibotdisini/RAM-UBOT/root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/amibotdisini/RAM-UBOT/RAM-UBOT/requirements.txt

CMD ["python3","-m","userbot"]
