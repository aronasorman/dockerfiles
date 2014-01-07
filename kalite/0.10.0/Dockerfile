
FROM kalite:base

MAINTAINER Aron Asor aron@learningequality.org

# this commit is for 0.10.0
RUN cd ka-lite; git checkout d3751

# expose port 8000 if we ever desire to connect to it
expose 8000

# initialize the db
RUN python2.6 ka-lite/kalite/manage.py syncdb --migrate --noinput --traceback

# default directory is ka-lite/kalite, default command is runserver
WORKDIR ka-lite/kalite
CMD python2.6 manage.py runserver 0.0.0.0:8000