FROM fnndsc/ubuntu-python3
COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt pylint==2.6.0
WORKDIR /root/
COPY flappy ./flappy
COPY .pylintrc .
ENTRYPOINT ["pylint", "flappy"]