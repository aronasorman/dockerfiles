FROM ubuntu

MAINTAINER Aron Asor aron@learningequality.org

# some stuff for adding new apt repositories
RUN apt-get install -y software-properties-common python-software-properties

# repository for old python versions
RUN add-apt-repository ppa:fkrull/deadsnakes
RUN apt-get update

# get python2.6, the oldest supported version of KA Lite. And oh Git as well.
RUN apt-get install -y python2.6 git

# clone KA Lite
RUN git clone https://github.com/learningequality/ka-lite.git
