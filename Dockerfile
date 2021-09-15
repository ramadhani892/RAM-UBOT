# Using Python Slim-Buster
FROM xluxz/geezproject:buster
# JOO-UBOT

RUN git clone -b JOO-UBOT https://github.com/H3llnn/JOO-UBOT /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/H3llnn/JOO-UBOT/JOO-UBOT/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
