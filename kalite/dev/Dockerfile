FROM learningequality/kalite:base

MAINTAINER Aron Asor aron@learningequality.org

# install setuptools, virtualenv and pip
RUN curl -O http://python-distribute.org/distribute_setup.py
RUN python distribute_setup.py
RUN rm distribute_setup.py
RUN easy_install pip
RUN pip install virtualenv

# create the virtualenv
RUN python -m virtualenv -p python2.6 /venv

# delete the builtin ka-lite, since we're gonna overlay our own
RUN rm -rf ka-lite

# activate virtualenv on startup if we're running bash (which we most likely are)
RUN sed -i '$a source /venv/bin/activate' /etc/bash.bashrc

EXPOSE 8000

# insert our local_settings.py and set the pythonpath to find it
ADD local_settings-distributed.py local_settings.py
ENV PYTHONPATH /:

VOLUME /ka-lite
WORKDIR /ka-lite/kalite
CMD bash