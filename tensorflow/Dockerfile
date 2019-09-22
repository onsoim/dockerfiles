From tensorflow/tensorflow

LABEL maintainer="onsoim <onsoim@gmail.com>" 

RUN apt-get update && apt-get install -y vim wget unzip

RUN wget https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip && unzip student.zip -d student

WORKDIR /onsoim

# RUN pip install sklearn pandas

# docker build -t oss . && docker run --rm -it -v $(pwd):/onsoim oss bash -c "pip install sklearn pandas && python student.py"