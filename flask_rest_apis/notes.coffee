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


<DEPLOYMENT>['Sever Deployment']
#Deploy to a server, virtual server, AWS `EC2`, Digital Ocean `droplet`
#Instructions for REHL, Rocky, CentOS, fedora (SEL distros)

1>'Connect to the server using SSH:'
  #You will be asked for the root password (or ssh key if setup previously)
  ssh root@<server_ip>
  #update os
  dnf upgrade --refresh
  #install vim
  dnf install vim
  
2>'Create another user':
  useradd <new_user>
  #add password
  passwd <password>
  #provide the user with sudo privileges
  visudo
  #add a new line under the root user:
  root ALL=(ALL) ALL
  <new_user> ALL=(ALL) ALL  
  #manage ssh
  vim /etc/ssh/sshd_config
  #change to `no` to disable root login
  PermitRootLogin no
  #make sure this is `yes` for password authentication
  PasswordAuthentication yes
  #go to the bottom and add:
  AllowUsers <new_user>
  #reload sshd service
  systemctl reload sshd
  #switch to <new_user>
  su <new_user>

3>'Configure Postgres (if using it)':
  #List the PostgreSQL modules:
  sudo dnf module list postgresql
  #Enable the latest version of PostgreSQL module i.e. version 13:
  sudo dnf module enable postgresql:13
  #After the version 13 module has been enabled, install the postgresql-server:
  sudo dnf install postgresql-server
  #Initialize a database storage area on disk
  sudo postgresql-setup --initdb
  #Start the PostgreSQL service:
  sudo systemctl start postgresql
  #Enable the PostgreSQL service:
  sudo systemctl enable postgresql
  #Verify status
  sudo systemctl status postgresql
  #change postgres user password
  sudo passwd postgres
  #create postgres user
  sudo -iu postgress
  createuser <new_user>
  #create db for user:
  createdb <new_user>
  #switch to <new_user>
  su <new_user>
  #configure postgres security options:
  sudo vim /var/lib/pgsql/data/pg_hba.conf
  #To enable password authentication, change line:
  local   all             all             peer
  local   all             127.0.0.1/32    ident
  local   all             ::1/128         ident
  #to:
  local   all             all             md5 
  local   all             127.0.0.1/32    md5
  local   all             ::1/128         md5
  #add above:
  local   all             postgres        peer
  #restart postgresql
  sudo systemctl restart postgresql

4>'Getting project code from GitHub':
  #create directory for repo data
  mkdir /home/<new_user>/Devs/
  cd /home/<new_user>/Devs/
  #install git
  sudo dnf install git
  #clone appropriate git repository
  git clone <git_repo_location>
  #tools to set up our app:
  sudo dnf install python39 python39-pip python39-devel libpq-devel
  #upgrade pip
  pip3 install --upgrade pip
  #install virtualenv
  pip3 install virtualenv
  #create virtual environment
  virtualenv venv
  #activate venv
  source venv/bin/activate
  #upgrade pip
  pip install --upgrade pip
  #install python requirements:
  pip install -r requirements.txt
  #deactivate venv
  deactivate

5>'Install firewalld':
  sudo dnf install firewalld
  #enable service 
  sudo systemctl enable firewalld
  #start service
  sudo systemctl start firewalld
  #check if firewall is running
  sudo firewall-cmd --state

6>'Try app before creating daemon service':
  #add port 5000 temporarily for testing:
  sudo firewall-cmd --zone=public --add-port=5000/tcp
  #verify firewall settings
  sudo firewall-cmd --list-all
  #check that host="0.0.0.0" when app is run in python file
    app.run(host="0.0.0.0")  #default port is 5000
  #activate virtual environment
  source venv/bin/activate
  #run app using python (#1)
  python wsgi.py
  #go and check if app is running at:
  http://<server_ip>:5000 #test with postman if necessary
  #deactivate venv
  deactivate
  #enable postgres
  #check postgres server status if active
  sudo systemctl status postgresql  
  #log into postgres
  sudo -iu postgres
  #run psql client
  psql
  #add new_password to db <new_user>
  ALTER USER <new_user> PASSWORD '<new-password>';
  #exit psql
  \q + enter
  #go back to new_user shell: new_user@server
  exit
  #activate venv
  source venv/bin/activate  
  #open python interpreter and type:
    from sqlalchemy import create_engine
    eng= create_engine("postgresql://<new_user>:<new_password>@localhost:5432/<new_user>")
    #if error check postgresql status/current authorization
  #export postgres ENVIRONMENT VARIABLE
  export DATABASE_URL=postgresql://<new_user>:<new_password>@localhost:5432/<new_user>
  #run app using python (#2)
  python wsgi.py
  #go and check if app is running at:
  http://<server_ip>:5000 #test with postman if necessary  

  #test using uwsgi (it needs a C compiler)
  #check for `Development Tools` module
  sudo dnf group list
  #install module
  sudo dnf groupinstall "Development Tools"
  #install Perl Compatible Regular Expressions && pcre-devel
  sudo dnf install pcre pcre-devel
  #activate virtual environment
  source venv/bin/activate
  #install uwsgi inside venv
  pip install uwsgi
  #check wsgi.py is like this:
    app.run()   #no host or port
  #run using uwsgi (#1)
  uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
  #verify it is working, close app and disable port 5000 by reloading the firewall
  sudo firewall-cmd --reload
  #deactivate venv
  deactivate

7>'Set up nginx':
  #List the nginx modules:
  sudo dnf module list nginx
  #Enable the latest version of nginx module i.e. version 1.20:
  sudo dnf module enable nginx:1.20
  #install nginx
  sudo dnf install nginx
  #enable nginx
  sudo systemctl enable nginx
  #start nginx
  sudo systemctl start nginx
  #check nginx status
  sudo systemctl status nginx
  #allow http and https service
  sudo firewall-cmd --add-service=http --zone=public --permanent
  sudo firewall-cmd --add-service=https --zone=public --permanent
  #add nginx to <new_user> group
  sudo usermod -a -G <new_user> nginx
  #add execute permission to group in the <new_user> homefolder
  chmod 710 /home/<new_user>
  #create config file
  sudo vim /etc/nginx/conf.d/myproject.conf 
  'myproject.conf':
    server {
      listen 80;
      server_name _;

      location / {
          include uwsgi_params;
          uwsgi_pass unix:/home/<new_user>/Devs/<git_repo_location>/sockets/myproject.sock;
      }
    }
  #in the app folder (/home/<new_user>/Devs/<git_repo_location>)
  vim uwsgi.ini
  'uwsgi.ini':
    [uwsgi]
    module = wsgi:app
    master = true
    processes = 2

    socket = sockets/myproject.sock
    chmod-socket = 660
    vacuum = true

    die-on-term = true
    logto = log/%n.log
  #create sockets directory:
  mkdir sockets
  #create directory for log files
  mkdir log
  #activate venv
  source venv/bin/activate
  #run using uwsgi (#2)
  uwsgi --ini uwsgi.ini
  #this will produce a 502 bad gateway error on the browser
  #SELinux is preventing access
  sudo journalctl -t setroubleshoot -r
  #You will see what SELinux is preventing and a series of steps to 'audit' (add exceptions to) them
  sudo ausearch -c 'nginx' --raw | audit2allow -M my-nginx_1
  sudo semodule -i my-nginx_1.pp
  #another useful command to check nginx errors is:
  sudo tail /var/log/nginx/error.log
  #check general log messages
  sudo tail /var/log/messages

  #run using uwsgi (#3) test emperor with log
  uwsgi --master --emperor uwsgi.ini --logto /home/<new_user>/Devs/<git_repo_location>/log/emperor.log
  #verify everything is being accessed and logged.
  #stop uwsgi and deactivate venv
  deactivate

8>'Enable HTTPS':
  #get(freenom.com) or purchase domain (namecheap.com)
  #associate domain with server ip address
  #get certificate and key for domain
  #add epel repository
  sudo dnf install epel-release
  #install certbot and dependencies
  sudo dnf install certbot python3-certbot-nginx
  #check certbot version and see if installed
  certbot --version
  #modify myproject.conf
  sudo vim /etc/nginx/conf.d/myproject.conf
  '/etc/nginx/conf.d/myproject.conf':
    server {
      listen 80 default_server;
      listen [::]:80 default_server;

      location / {
        return 301 https://$host$request_uri;
      }
    }

    server {
      listen 443 ssl http2;
      listen [::]:443 ssl http2;
      server_name <website_name.domain>;

      location / {
        include uwsgi_params;
        uwsgi_pass unix:/home/kura/Devs/renshuu_rest-api-on-server/sockets/myproject.sock;
      }
      ssl_certificate /etc/letsencrypt/live/shuuresting.tk/fullchain.pem;
      ssl_certificate_key /etc/letsencrypt/live/shuuresting.tk/privkey.pem;
    }
  #activate venv
  source venv/bin/activate
  #run using uwsgi (#4)
  uwsgi --master --emperor uwsgi.ini --logto /home/<new_user>/devs/<git_repo_location>/log/emperor.log
  #create certificate
  sudo certbot --nginx -d <website_name.domain> -d www.<website_name.domain>
  #certbot will install the certificate and modify myproject.conf
  #check everything is running smoothly in https
  'modified myproject.conf':
    server {
      listen 80 default_server;
      listen [::]:80 default_server;

      location / {
        return 301 https://$host$request_uri;
      }
    }
    server {
      listen 443 ssl http2;
      listen [::]:443 ssl http2;
      server_name <website_name.domain>;

      location / {
        include uwsgi_params;
        uwsgi_pass unix:/home/<new_user>/devs/<git_repo_location>/sockets/myproject.sock;
      }
      ssl_certificate /etc/letsencrypt/live/<website_name.domain>/fullchain.pem; # managed by Certbot
      ssl_certificate_key /etc/letsencrypt/live/<website_name.domain>/privkey.pem; # managed by Certbot
    }
    server {
      location / {
        return 301 https://$host$request_uri;
      }

      server_name www.<website_name.domain>; # managed by Certbot

      listen [::]:443 ssl ipv6only=on; # managed by Certbot
      listen 443 ssl; # managed by Certbot
      ssl_certificate /etc/letsencrypt/live/<website_name.domain>/fullchain.pem; # managed by Certbot
      ssl_certificate_key /etc/letsencrypt/live/<website_name.domain>/privkey.pem; # managed by Certbot
      include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
      ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
    }
    server {
      if ($host = www.<website_name.domain>) {
        return 301 https://$host$request_uri;
      } # managed by Certbot

      listen 80 ;
      listen [::]:80 ;
        server_name www.<website_name.domain>;
        return 404; # managed by Certbot
    }
    #deactivate venv
    deactivate

9>'Create uwsgi service':
  #define uwsgi service in the system:
  sudo vim /etc/systemd/system/myproject_uwsgi.service
  'myproject_uwsgi.service':
    [Unit]
    Description=uWSGI items rest
    After=network.target

    [Service]
    User=kura
    Group=kura
    WorkingDirectory=/home/<new_user>/Devs/<git_repo_location>
    Environment=DATABASE_URL="postgresql://<new_user>:<new_password>@localhost:5432/<new_user>"
    ExecStart=/home/<new_user>/Devs/<git_repo_location>/venv/bin/uwsgi --master --emperor uwsgi.ini --logto /home/<new_user>/Devs/<git_repo_location>/log/emperor.log
    Restart=always
    KillSignal=SIGQUIT
    Type=notify
    NotifyAccess=all

    [Install]
    WantedBy=multi-user.target
  #save changes
  #Loop 3 times
    #run service:
    sudo systemctl start myproject_uwsgi
    #this will fail and process will exit with error code
    #SELinux is preventing access [file access]
    sudo journalctl -t setroubleshoot -r
    #You will see what SELinux is preventing and a series of steps to 'audit' (add exceptions to) them
    sudo ausearch -c '(uwsgi)' --raw | audit2allow -M my-uwsgi_1 #then this can be my-uwsgi_2 and so on
    sudo semodule -i my-uwsgi_1.pp
  #Loop 3 times (or until project starts)
    sudo systemctl start myproject_uwsgi
    #if error:
    sudo ausearch -c 'uwsgi' --raw | audit2allow -M my-uwsgi_4
    sudo semodule -i my-uwsgi_4.pp
  #now try acces <website_name.domain> in the browser
  #you will see a 502 bad gateway error
  #SELinux is preventing access [socket accesses]
  #Loop until 502 error is gone (4 times)
    sudo ausearch -c 'uwsgi' --raw | audit2allow -M my-uwsgi_7
    sudo semodule -i my-uwsgi_7.pp
  #verify app is correctly deployed and working
  #enable myproject_uwsgi service (the process will load everytime when booting)
  sudo systemctl enable myproject_uwsgi

