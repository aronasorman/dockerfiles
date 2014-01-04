FROM ubuntu

MAINTAINER Aron Asor aron@learningequality.org

# some stuff for adding new apt repositories
RUN apt-get install -y software-properties-common python-software-properties

# repository for old python versions
RUN add-apt-repository ppa:fkrull/deadsnakes
RUN apt-get update

# get python2.6, the oldest supported version of KA Lite. And oh Git and curl as well.
RUN apt-get install -y python2.6 git curl

# clone KA Lite
RUN git clone https://github.com/learningequality/ka-lite.git

# add initial_data.json with default admin user
RUN  curl -o ka-lite/kalite/initial_data.json https://gist.github.com/aronasorman/8246715/raw/cbd2a0353b2d47364b5c938b368f69a8a2876641/initial_data.json

# local_settings.py for local development
ADD files/local_settings-distributed.py /ka-lite/kalite/local_settings.py