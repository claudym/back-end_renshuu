<CH.1>[flask basics]
GET & POST Requests
===================
> GET  google.com/index.html: "requesting 'index.html' resource from google.com"
> POST "send server some data, expects response"


<CH.2>[simple api]
"Restful API Resource Method Chart"
RESOURCE      METHOD      PATH      USED_FOR                PARAM           ERROR_CODE
   +          post        /add      adding 2 numbers        x:int, y: int   200 ok
                                                                            301 misssing argument
                                                                            302 not integer
   -          post        /subtract subtracting 2 numbers   x:int, y: int   200 ok
                                                                            301 misssing argument
                                                                            302 not integer                                                                      
   /          post        /divide   x/y                     x:int, y: int   200 ok
                                                                            301 misssing argument
                                                                            302 not integer
                                                                            303 y is 0
   *          post        /multiply x*y                     x:int, y: int   200 ok
                                                                            301 misssing argument
                                                                            302 not integer
                                                                           

<CH.3>[docker]
'Docker is a tool that allows developers, sys-admins etc. to easily deploy their applications in a sandbox (called containers) '
'to run on the host operating system i.e. Linux. The key benefit of Docker is that it allows users to package an application '
'with all of its dependencies into a standardized unit for software development.' 

'Unlike virtual machines, containers do not have high overhead and hence enable more efficient usage of the underlying system and resources.'
install docker:
-https://developer.fedoraproject.org/tools/docker/docker-installation.html
-https://docs.docker.com/engine/install/fedora/

install docker compose:
-https://docs.docker.com/compose/cli-command/
-https://docs.docker.com/engine/install/linux-postinstall/

docker hub:
-https://hub.docker.com/

git branch coloring:
-https://thucnc.medium.com/how-to-show-current-git-branch-with-colors-in-bash-prompt-380d05a24745


<CH.4>[mongoDB]
'MongoDB is a cross-platform, document oriented database that provides high performance, high availability, and easy scalability.'
document: 'is a set of key-value pairs. Dynamic schema'
collection: 'a group of MongoDB documents. Do not enforce schema'

doc example:
{
   _id: <ObjectId1>,
   username: "123xyz",
   contact: {
               phone: "123-456",
               email: "xyz@ex.com"
            }
   access:  {
               level: 5,
               group: "dev"
            }
}

install:
https://developer.fedoraproject.org/tech/database/mongodb/about.html
https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-20-04

[Mongodb]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/8/mongodb-org/4.4/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-4.4.asc

cheat sheet: https://www.mongodb.com/developer/quickstart/cheat-sheet/

create: 'use DB'
insert: 'db.COLLECTION_NAME.insert({"namae": "suga"})'
delete: 'db.dropDatabase()'
create collection: 'db.createCollection(name, options)'
delete collection: 'db.COLLECTION_NAME.drop()'

<CH.5>[db API]
'Expose mongoDB operations as service restful API':

#store username and hashed_pw into database
users.insert_one({
"username": username,
"password": hashed_pw,
"sentence": "test sentence",
"tokens": 5
})
#store the sentence return 200 ok
users.update_one({
"username": username
}, {
"$set": {
   "sentence": sentence,
   "tokens": num_tokens-1
   }
})

#get sentence
sentence= users.find({
   "username": username      
   })[0]["sentence"]

<extra_1>[flask_gunicorn_nginx_docker]
'tree':
├── flask_app 
│   ├── app.py          
│   ├── wsgi.py
│   ├── requirements.txt
│   └── Dockerfile
├── nginx
│   ├── nginx.conf          
│   ├── project.conf
│   └── Dockerfile
├── docker-compose.yml
└── run_docker.sh

'/flask_app/app.py':
from flask import Flask

server = Flask(__name__)

@server.route('/')
def hello_world():
    return 'Ohayou seikai! Greetings!'

'/flask_app/wsgi.py':
from app import server

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=5000)

'/flask_app/requirements.txt':
flask
gunicorn

'/flask_app/Dockerfile':
FROM python:3.10.1

WORKDIR /usr/src/flask_app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

'/nginx/nginx.conf':
# Define the user that will own and run the Nginx server
user  nginx;
# Define the number of worker processes; recommended value is the number of
# cores that are being used by your server
worker_processes  2;
# Define the location on the file system of the error log, plus the minimum
# severity to log messages for
error_log  /var/log/nginx/error.log warn;
# Define the file that will store the process ID of the main NGINX process
pid        /var/run/nginx.pid;

# events block defines the parameters that affect connection processing.
events {
    # Define the maximum number of simultaneous connections that can be opened by a worker proce$
    worker_connections  1024;
}

# http block defines the parameters for how NGINX should handle HTTP web traffic
http {
    # Include the file defining the list of file types that are supported by NGINX
    include       /etc/nginx/mime.types;
    # Define the default file type that is returned to the user
    default_type  text/html;
    # Define the format of log messages.
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
                          # Define the location of the log of access attempts to NGINX
    access_log  /var/log/nginx/access.log  main;
    # Define the parameters to optimize the delivery of static content
    sendfile        on;
    tcp_nopush     on;
    tcp_nodelay    on;
    # Define the timeout value for keep-alive connections with the client
    keepalive_timeout  65;
    # Define the usage of the gzip compression algorithm to reduce the amount of data to transmit
    #gzip  on;
    # Include additional parameters for virtual host(s)/server(s)
    include /etc/nginx/conf.d/*.conf;
}

'/nginx/project.conf':
server {

    listen 80;
    server_name docker_flask_gunicorn_nginx;

    location / {
        proxy_pass http://flask_app:5000;

        # Do not change this
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static {
        rewrite ^/static(.*) /$1 break;
        root /static;
    }
}

'/nginx/Dockerfile':
FROM nginx:1.21.4

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx
RUN rm /etc/nginx/conf.d/default.conf
COPY project.conf /etc/nginx/conf.d/

'/docker-compopse.yml':
version: "3"

services:
  flask_app:
    container_name: flask_app
    restart: always
    build: ./flask_app
    ports:
      - "5000:5000"
    command: gunicorn -w 1 -b 0.0.0.0:5000 wsgi:server

  nginx:
    container_name: nginx
    restart: always
    build: ./nginx
    ports:
      - "80:80"
    depends_on:
      - flask_app

'/run_docker.sh':
echo killing old docker processes
docker-compose rm -fs

echo building docker containers
docker-compose up --build -d

'After the files are in place run':
bash run_docker.sh


<extra_2>[flask_gunicorn_nginx_docker with ssl]
"How to obtain an SSL certificate, using Let's Encrypt, for a multi-container Docker web application"
sudo dnf install certbot python3-certbot-nginx nginx
sudo certbot --nginx -d your_domain -d www.your_domain
#the certificate will be saved in /etc/letsencrypt/live

#check for the process id next to LISTEN
sudo netstat -ntulp | grep 443
#kill process
sudo kill process_pid

'/nginx/nginx.conf':
# Define the user that will own and run the Nginx server
user  nginx;
# Define the number of worker processes; recommended value is the number of
# cores that are being used by your server
worker_processes  2;
# Define the location on the file system of the error log, plus the minimum
# severity to log messages for
error_log  /var/log/nginx/error.log warn;
# Define the file that will store the process ID of the main NGINX process
pid        /var/run/nginx.pid;

# events block defines the parameters that affect connection processing.
events {
    # Define the maximum number of simultaneous connections that can be opened by a worker proce$
    worker_connections  1024;
}

# http block defines the parameters for how NGINX should handle HTTP web traffic
http {
    # Include the file defining the list of file types that are supported by NGINX
    include       /etc/nginx/mime.types;
    # Define the default file type that is returned to the user
    default_type  text/html;
    # Define the format of log messages.
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
                          # Define the location of the log of access attempts to NGINX
    access_log  /var/log/nginx/access.log  main;
    # Define the parameters to optimize the delivery of static content
    sendfile        on;
    tcp_nopush     on;
    tcp_nodelay    on;
    # Define the timeout value for keep-alive connections with the client
    keepalive_timeout  65;
    # Define the usage of the gzip compression algorithm to reduce the amount of data to transmit
    #gzip  on;
    # Include additional parameters for virtual host(s)/server(s)
    include /etc/nginx/conf.d/*.conf;
}

'/nginx/project.conf':
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    location / {
        return 301 https://$host$request_uri;
    }
}

#works and serves in https
server { 
  listen 443 ssl http2;
  listen [::]:443 ssl http2;
  # server_name flask_nginx_ssl;
  server_name renshuu.tk;

  location / {
    proxy_pass http://flask_app:8000;

    #dont change
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  }

  ssl_certificate /etc/letsencrypt/live/renshuu.tk/fullchain.pem;
  ssl_certificate_key /etc/letsencrypt/live/renshuu.tk/privkey.pem;
  include /etc/letsencrypt/options-ssl-nginx.conf;
  ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;
}

'/nginx/Dockerfile':
FROM nginx:1.21.4

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx
RUN rm /etc/nginx/conf.d/default.conf
COPY project.conf /etc/nginx/conf.d/

'/docker-compopse.yml':
version: "3"

services:
  flask_app:
    container_name: flask_app
    restart: always
    build: ./flask_app
    ports:
      - "8000:8000"
    command: gunicorn -w 4 -b 0.0.0.0:8000 wsgi:server

  nginx:
    container_name: nginx
    restart: always
    build: ./nginx
    volumes:
      - /etc/letsencrypt/:/etc/letsencrypt/
    ports:
      - "80:80"
      - "443:443"
    depends_on:
      - flask_app

'/run_docker.sh':
echo killing old docker processes
docker compose rm -fs

echo building docker containers
docker compose up --build -d
