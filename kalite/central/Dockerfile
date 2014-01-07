FROM kalite:dev

MAINTAINER Aron Fyodor Asor aron@learningequality.org

# copy the central server local_settings.py
ADD local_settings-central.py /local_settings.py

CMD python manage.py runserver 0.0.0.0:8000