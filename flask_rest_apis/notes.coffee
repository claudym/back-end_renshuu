<DEPLOYMENT>['HEROKU']
#Heroku is a cloud platform for deploying and running modern apps.

'runtime.txt':
python-3.8.12

'requirements.txt':
Flask
Flask-RESTful
Flask-JWT
Flask-SQLAlchemy
uwsgi
psycopg2

'uwsgi.ini':
[uwsgi]
http-socket = :$(PORT)
master = true
die-on-term = true
module = run:app
memory-report = true

'Procfile':
web: uwsgi uwsgi.ini

>Create Heroku Dyno
>Create Heroku app
>Deploy app
