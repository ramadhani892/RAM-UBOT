# Using Python Slim-Buster
FROM xluxz/geezproject:buster
# KIM-UBOT
# Geez-project
#yaudah iya

RUN git clone -b KIM-UBOTS https://github.com/abdurrohimbontro/KIM-UBOT /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/abdurrohimbontro/KIM-UBOT/KIM-UBOTS/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
