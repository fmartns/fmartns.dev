sudo apt-get update && sudo apt-get dist-upgrade
sudo apt install python3.8-venv
mkdir www
cd www
python3 -m venv venv
source venv/bin/activate
pip install django
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential 
cd ..
sudo rm -r www
git clone https://github.com/fmartns/fmartns.dev
cd fmartns.dev/
sudo rm -r env
python3 -m venv venv
source venv/bin/activate
pip install django
pip install pillow
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential 
pip install mysqlclient
python manage.py runserver
python manage.py makemigrations, migrate, collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py runserversudo ufw allow 8000
sudo ufw allow 8000
python manage.py runserver 0.0.0.0:8000 --inscure
python manage.py runserver 0.0.0.0:8000 --insecure
cd fmartns/
ls
sudo nano settings.py 
cd ..
python manage.py runserver 0.0.0.0:8000 --insecure
sudo apt install nginx
sudo nano /etc/nginx/sites-available/default
pwd
sudo nano /etc/nginx/sites-available/default
sudo nginx -t
sudo systemctl restart nginx
sudo ufw allow 80
python manage.py runserver 0.0.0.0:8000 --insecure
sudo pip install gunicorn
pip install gunicorn
sudo nano /etc/systemd/system/gunicorn.service
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl restart nginx
gunicorn --workers 3 --bind unix:/home/ubuntu/fmartns.dev/fmartns.sock fmartns.wsgi:application
nohup python manage.py runserver 0.0.0.0:80 &
s
nohup python manage.py runserver 0.0.0.0:8000 --insecure
sudo ufw allow fmartns.dev
sudo ufw allow fmartns.dev:80
nohup python manage.py runserver 0.0.0.0:8000 --insecure
sudo systemctl status nginx
nohup python manage.py runserver 0.0.0.0:8000 --insecure
python manage.py migrate
python manage.py createsuperuser
nohup python manage.py runserver 0.0.0.0:8000 --insecure
cd fmartns.dev
cd fmartns
sudo nano settings.py 
cd ..
nohup python manage.py runserver 0.0.0.0:8000 --insecure
sudo certbot certonly --nginx -d fmartns.dev
sudo apt-get update
sudo apt-get install certbot python3-certbot-nginx
sudo certbot-auto certonly --nginx -d fmartns.dev
sudo apt-get install certbot python3-certbot-nginx
sudo certbot-auto certonly --nginx -d fmartns.dev
wget https://dl.eff.org/certbot-auto
sudo snap install --classic certbot
sudo certbot-auto certonly --nginx -d fmartns.dev
chmod +x certbot-auto
sudo chmod +x certbot-auto
certbot --version
chmod +x certbot-auto
ls
sudo find / -name certbot-auto
certbot
sudo certbot certonly --nginx -d fmartns.dev
ls
cd ..
ls
cd ..
ls
cd etc
cd letsencrypt/
cd live/
ls
sudo cd live
cd live
sudo cd live
sudo -u
sudo -i
sudo nano /etc/nginx/sites-available/default
sudo systemctl reload nginx
sudo nano /etc/nginx/sites-available/default
sudo systemctl reload nginx
systemctl status nginx.service
sudo systemctl restart nginx
systemctl status nginx.service
sudo nano /etc/nginx/sites-available/default
systemctl status nginx.service
sudo systemctl restart nginx
systemctl status nginx.service
cd ..
ls
cd apt
ls
cd ..
cd opt
ls
cd ..
ls
cd ubuntu
cd ..
ls
cd etc
cd ubuntu-advantage/
cd ..
cd ubuntu
cd ..
cd opt
cd ubuntu
cd ..
cd home
cd ubuntu/
cd fmartns.dev/
cd fmartns
sudo nano 
sudo nano settings.py
python manage.py runserver --cert /etc/letsencrypt/live/fmartns.dev/fullchain.pem --key /etc/letsencrypt/live/fmartns.dev/privkey.pem
python3 manage.py runserver --cert /etc/letsencrypt/live/fmartns.dev/fullchain.pem --key /etc/letsencrypt/live/fmartns.dev/privkey.pem
cd ..
python3 manage.py runserver --cert /etc/letsencrypt/live/fmartns.dev/fullchain.pem --key /etc/letsencrypt/live/fmartns.dev/privkey.pem
python manage.py runserver --cert /etc/letsencrypt/live/fmartns.dev/fullchain.pem --key /etc/letsencrypt/live/fmartns.dev/privkey.pem
python manage.py runserver
source env\Scripts\activate
cd env
ls
cd venv
ls
cd ..
source venv\bin\activate
source venv/bin/activate
python manage.py runserver --cert /etc/letsencrypt/live/fmartns.dev/fullchain.pem --key /etc/letsencrypt/live/fmartns.dev/privkey.pem
python manage.py runsslserver --certificate /etc/letsencrypt/live/fmartns.dev/fullchain.pem --key /etc/letsencrypt/live/fmartns.dev/privkey.pem
python manage.py 
nohup python manage.py runserver 0.0.0.0:8000 --insecure
clear
nohup python manage.py runserver 0.0.0.0:8000 --insecure
pkill -f 'nohup'
nohup python manage.py runserver 0.0.0.0:8000 --insecure
pkill -f 'nohup'
ps aux | grep 'nohup'
pkill 8168
ps aux | grep 'nohup'
pkill 25190
ps aux | grep 'nohup'
pkill 25193
ps aux | grep 'nohup'
nohup python manage.py runserver 0.0.0.0:8000 --insecure
cd fmartns.dev/
nohup python manage.py runserver 0.0.0.0:8000 --insecure
source venv/bin/activate
nohup python manage.py runserver 0.0.0.0:8000 --insecure
pkill -f 'nohup'
nohup python manage.py runserver 0.0.0.0:8000 --insecure
cd fmartns
sudo nano settings.py
nohup python manage.py runserver 0.0.0.0:8000 --insecure
cd fmartns.dev/
ls
cd fmartns/
sudo nano settings.py
pkill -f 'nohup'
nohup python manage.py runserver 0.0.0.0:8000 --insecure
source venv/bin/activate
cd ..
source venv/bin/activate
pkill -f 'nohup'
nohup python manage.py runserver 0.0.0.0:8000 --insecure
sudo nano /etc/nginx/sites-available/default
sudo nano /etc/nginx/sites-available/defaultsudo service nginx restart
sudo service nginx restart
sudo systemctl restart nginx
sudo service nginx status
sudo nano /etc/nginx/sites-available/defaultsudo service nginx restart
sudo nano /etc/nginx/sites-available/default
sudo systemctl restart nginx
sudo service nginx status
cd fmartns
sudo nano settings.py
cd ..
pkill -f 'nohup'
nohup python manage.py runserver 0.0.0.0:8000 --insecure
ps aux | grep nohup
ps aux
kill 22668
nohup python manage.py runserver 0.0.0.0:8000 --insecure
kill 22668
ps aux
cd fmartns
sudo nano settings.py
nohup python manage.py runserver 0.0.0.0:8000 --insecure
ps aux
cd ..
nohup python manage.py runserver 0.0.0.0:8000 --insecure
cd fmartns
sudo nano settings.py
cd ..
nohup python manage.py runserver 0.0.0.0:8000 --insecure
python manage.py runserver
python manage.py runserver 3.82.145.23:8000
sudo nano /etc/nginx/sites-available/default
python manage.py runserver 0.0.0.0:8000
cd fmartns/
sudo nano settings.py
python manage.py runserver 0.0.0.0:8000
cd ..
python manage.py runserver 0.0.0.0:8000
cd fmartns/
sudo nano settings.py
cd ..
python manage.py runserver 0.0.0.0:8000
cd fmartns/
sudo nano settings.py
python manage.py runserver 0.0.0.0:8000
cd ..
python manage.py runserver 0.0.0.0:8000
cd fmartns/
sudo nano settings.py
python manage.py runserver 0.0.0.0:8000
cd ..
python manage.py runserver 0.0.0.0:8000
sudo nano /etc/nginx/sites-available/default
python manage.py runserver 0.0.0.0:8000
cd fmartns/
sudo nano settings.py
cd ..
sudo nano settings.py
python manage.py runserver 0.0.0.0:8000
cd ..
cd fmartns.dev/
cd fmartns/
sudo nano settings.py
cd ..
python manage.py runserver 0.0.0.0:800
cd fmartns/
sudo nano settings.py
cd ..
python manage.py runserver 0.0.0.0:800
sudo python manage.py runserver 0.0.0.0:800
python manage.py runserver 0.0.0.0:8000
cd fmartns/
sudo nano settings.py
cd ..
python manage.py runserver 0.0.0.0:8000
sudo nano /etc/nginx/sites-available/default
sudo fmartns/
cd fmartns/
sudo nano settings.py
git add settings.py
git commit -m "Update Settings.py"
git push
cd ..
sudo nano .env
python manage.py runserver 0.0.0.0:8000
rm -r .env
cd fmartns/
sudo nano settings.py
git add settings.py
git commit 'Settings Update'
git commit -m  'Settings Update'
python manage.py runserver 0.0.0.0:8000
cd ..
python manage.py runserver 0.0.0.0:8000
cd fmartns/
sudo nano settings.py
cd ..
python manage.py runserver 0.0.0.0:8000
cd fmartns
sudo nano settings.py
cd ..
python manage.py runserver 0.0.0.0:8000
cd fmartns
sudo nano settings.py
cd ..
python manage.py runserver 0.0.0.0:8000
sudo nano /etc/nginx/sites-available/default
python manage.py runserver 0.0.0.0:8000
sudo nano /etc/nginx/sites-available/default
python manage.py runserver 0.0.0.0:8000
sudo nano /etc/nginx/sites-available/default
cd fmartns
sudo nano settings.py
cd ..
python manage.py runserver 0.0.0.0:8000
sudo nano /etc/nginx/sites-available/default
python manage.py runserver 0.0.0.0:8000
sudo nano settings.py
cd fmartns
sudo nano settings.py
cd ..
python manage.py runserver 0.0.0.0:8000
cd fmartns/
git add settings.py
git commit -m 'Update settings.py'
git push
sudo nano /etc/nginx/sites-available/default
python manage.py runserver 0.0.0.0:8000
CD ..
python manage.py runserver 0.0.0.0:8000
cd ..
python manage.py runserver 0.0.0.0:8000
cd fmartns.dev
nohup python manage.py runserver 0.0.0.0:8000 --insecure
source venv/bin/activate
nohup python manage.py runserver 0.0.0.0:8000 --insecure
ps aux
pkill 28367
source venv/bin/activate
cd fmartns.dev/
source venv/bin/activate
pkill 28367
ps aus
ps aux
kill 28367
ps aux
sudo nano /etc/nginx/sites-available/default
python manage.py runserver
python manage.py runserver --insecure
python manage.py runserver 0.0.0.0:8000
python manage.py runserver 3.82.145.23:8000
python manage.py runserver 0.0.0.0:8000
cd fmartns/
sudo nano settings.py
git pull
sudo nano settings.py
cd ..
python manage.py runserver
python manage.py runserver 0.0.0.0:8000
cd fmartns/
sudo nano settings.py
cd ..
python manage.py runserver 0.0.0.0:8000
python manage.py runserver 3.82.145.23:8000
sudo nano /etc/nginx/sites-available/default
python manage.py runserver 0.0.0.0:8000
python manage.py runserver
python manage.py runserver 0.0.0.0:8000
cd fmartns
sudo nano settings.py
cd ..
python manage.py runserver 0.0.0.0:8000
sudo nano /etc/nginx/sites-available/default
sudo systemctl restart nginx
sudo systemctl status nginx
python manage.py runserver 0.0.0.0:8000
cd fmartns
sudo nano settings.py
cd ..
python manage.py runserver 0.0.0.0:8000
sudo systemctl status nginx
sudo nano /etc/nginx/sites-available/default
sudo systemctl restart nginx
sudo systemctl status nginx
python manage.py runserver 0.0.0.0:8000
sudo nano /etc/nginx/sites-available/default
sudo systemctl restart nginx
sudo systemctl status nginx
sudo systemctl stop  nginx
sudo systemctl stop nginx
sudo systemctl status nginx
sudo systemctl start nginx
sudo systemctl status nginx
sudo nano /etc/nginx/sites-available/default
sudo systemctl restart nginx
sudo systemctl stop nginx
sudo systemctl start nginx
sudo systemctl status nginx
sudo systemctl start nginx
sudo nano /etc/nginx/sites-available/default
sudo systemctl start nginx
sudo systemctl status nginx
sudo nano /etc/nginx/sites-available/default
cd fmartns
sudo nano settings.py
sudo systemctl start nginx
python manage.py runserver 0.0.0.0:8000
cd ..
python manage.py runserver 0.0.0.0:8000
cd fmartns
sudo nano settings.py
cd ..
python manage.py runserver 0.0.0.0:8000
cd fmartns
sudo nano settings.py
cd ..
python manage.py runserver 0.0.0.0:8000
cd fmartns
sudo nano settings.py
cd ..
python manage.py runserver 0.0.0.0:8000
python manage.py runserver 0.0.0.0:8000 --insecure
cd fmartns
sudo nano settings.py
cd ..
python manage.py runserver 0.0.0.0:8000 --insecure
cd fmartns
sudo nano settings.py
cd ..
python manage.py runserver 0.0.0.0:8000 --insecure
cd fmartns
sudo nano settings.py
cd ..
python manage.py runserver 0.0.0.0:8000 --insecure
cd fmartns
sudo nano settings.py
cd .
cd ..
python manage.py runserver 0.0.0.0:8000 --insecure
git add .
git commit -m 'Update settings.py'
git push
nohup python manage.py runserver 0.0.0.0:8000 --insecure
git pull
cd fmartns.dev/
git pull
cd fmartns.dev/
ls
git add db.sqlite3 
git commit -m 'Update db'
git push
git pull
cd fmartns.dev/
git pull
git 
git checkou
git checkout
git pull
git update-index --skip-worktree nohup.out
ls
git update-index --skip-worktree db.sqlite3
git update-index --skip-worktree venv/
git pull
git update-index --skip-worktree nohup.out
git pull
git update-index --skip-worktree nohup.out
git pull
git chechkou -- nohup.out
git chechkout -- nohup.out
git chechkout nohup.out
git checkout nohup.out
git checkout -- nohup.out
ls
git checkout nohup.out
git pull
git add nohup.out 
git commit -m 'Update nohup.out'
git pull
git commit -m 'Update nohup.out'
git pull origin
git checkout -- nohup.out
rm nohup.out
git pull
ls
source venv/bin/activate
cd venv/
ls
cd ..
rm -r venv
.
ls
python -m venv venv
python3 -m venv venv
source venv/bin/activate
pip install django
pip install pillow
nohup python manage.py runserver 0.0.0.0:8000 --insecure
python manage.py createsuperuser
python manage.py migrate
python manage.py createsuperuser
nohup python manage.py runserver 0.0.0.0:8000 --insecure
pip install gettext 
cd fmartns.dev/
source venv/bin/activate
pip install gettext 
pip install gettext
ls
cd locale/
ls
sudo apt-get install gettext
cd ..
cd fmartns/
sudo nano settings.py
ps au
kill 33784
nohup python manage.py runserver 0.0.0.0:8000 --insecure
ps aux
nohup python manage.py runserver 0.0.0.0:8000 --insecure
cd fmartns.dev/
source venv/bin/activate
nohup python manage.py runserver 0.0.0.0:8000 --insecure
cd fmartns/
sudo nano settings.py
nohup python manage.py runserver 0.0.0.0:8000 --insecure
cd ..
nohup python manage.py runserver 0.0.0.0:8000 --insecure
python manage.py compilemessages
nohup python manage.py runserver 0.0.0.0:8000 --insecure
cd fmartns/
sudo nano settings.py
export EMAIL_HOST='smtp.zoho.com'
export EMAIL_PORT=465
export EMAIL_HOST_USER='hello@fmartns.dev'
export EMAIL_HOST_PASSWORD='M@rina13'
nohup python manage.py runserver 0.0.0.0:8000 --insecure
cd ...
cd ..
nohup python manage.py runserver 0.0.0.0:8000 --insecure
px aus
px aux
psa ux
ps aux
nohup python manage.py runserver 0.0.0.0:8000 --insecure
cd fmartns
cd fmartns.dev/
python manage.py runserver 0.0.0.0:8000
soure venv/bin/activate
source venv/bin/activate
python manage.py runserver 0.0.0.0:8000
cd fmartns
sudo nano settings.py
cd ..
python manage.py runserver 0.0.0.0:8000
nohup python manage.py runserver 0.0.0.0:8000 --insecure
git pull
nohup python manage.py runserver 0.0.0.0:8000 --insecure
cd fmartns
sudo nano settings.py
ls
sudo nano urls.py 
cd ..
nohup python manage.py runserver 0.0.0.0:8000 --insecure
cd fmartns
sudo nano urls.py 
cd ..
nohup python manage.py runserver 0.0.0.0:8000 --insecure
git pull
nohup python manage.py runserver 0.0.0.0:8000 --insecure
cd fmartns/
sudo nano settings.py
cd ..
nohup python manage.py runserver 0.0.0.0:8000 --insecure
processing locale pt-br
cd fmartns/
sudo nano settings.py
cd ..
nohup python manage.py runserver 0.0.0.0:8000 --insecure
cd fmartns.dev/
sudo apt-get install language-pack-pt
cd fmartns/
sudo nano settings.py

source venv/bin/activate
cd ..
source venv/bin/activate
python manage.py compilemessages
sudo nano /etc/nginx/sites-available/default
sudo systemctl restart nginx
sudo systemctl status nginx
cd locale/
ls
mv pt_br pt_BR
ls
python manage.py compilemessages
cd .
cd ..
python manage.py compilemessages
ls

ls
cd ..
cd fmartns
sudo nano settings.py
cd ..
nohup python manage.py runserver 0.0.0.0:8000 --insecure
cd fmartns/
sudo s
sudo nano settings.py
nohup python manage.py runserver 0.0.0.0:8000 --insecure
cd ..
nohup python manage.py runserver 0.0.0.0:8000 --insecure
cd locale/
mv pt_BR/ pt-BR
CD ..
cd ..
python manage.py compilemessages
cd ..
cd fmartns.dev/
cd locale/
ls
mv pt-BR/ pt_BR/
cd ..
cd locale/
cd pt_BR/
ls
cd ..
sudo nano locale/
ls
cd locale/
ls
cd pt_BR/
ls
cd l
cd LC_MESSAGES/
ls
sudo nano django.
sudo nano django.mo
ls
processing locale pt-br
cd fmartns.dev/
git pull
cd fmartns.dev/
git pull
cd fmartns.dev/
cd 
cd fmartns
cd fmartns.dev/
cd fmartns/
sudo nano settings.py
cd ..
nohup python manage.py runserver 0.0.0.0:8000 --insecure
source venv/bin/activate
nohup python manage.py runserver 0.0.0.0:8000 --insecure
c dfm
cd fmartns/
sudo nano settings.py
cd ..
sudo nano settings.py
nohup python manage.py runserver 0.0.0.0:8000 --insecure
cd fmartns/
sudo nano settings.py
cd ..
cd fmartns.dev/
nohup python manage.py runserver 0.0.0.0:8000 --insecure
cd fmartns/
sudo nano settings.py
cd ..
nohup python manage.py runserver 0.0.0.0:8000 --insecure
cd fmartns.dev/
cd fmartns/
sudo nano settings.py
git pull
git checkout -- settings.py
cd ..
git pull
cd fmartns/
git checkout -- urls.py
cd ..
git pull
python manage.py compilemessages
source venv/bin/activate
git pull
python manage.py compilemessages
cd fmartns.dev/
cd locale/
ls
rm
rm -r pt_BR
mv pt_br/ mv_BR
ls
mv mv_BR/
mv mv_BR/ pt_BR
ls
cd fmartns.dev/
git pull
cd fmartns/
sudo nano settings.py
cd ..
sudo nano settings.py
cd fmartns/
sudo nano settings.py
cd ..
ls
cd locale/
LS
ls
cd fmartns
cd fmartns.dev/
cd fmartns/
sudo nano settings.py
cd ..
cd fmartns.dev/
git pull
clean
clear
cd fmartns.dev/
git pull
ls
sudo nano /etc/nginx/sites-available/default
ps aux
lear
git pull
cd fmartns.dev/
git pull
cd fmartns.dev/
git pull
cd fmartns.dev/
git pull
cd fmartns.dev/
git pull
cd fmartns.dev/
git pull
cd fmartns.dev/
git pull
cd fmartns.dev/
git pull
cd locale/
ls
cd pt_BR/
ls
cd l
cd LC_MESSAGES/
ls
sudo nano django.po
ls
sudo apt update
sudo apt install default-jdk
java -Xmx1024M -Xms1024M -jar spigot-1.20.4.jar nogui
sudo apt update
sudo apt install default-jdk
java -Xmx1024M -Xms1024M -jar spigot-1.20.4.jar nogui
java -jamvm|-cacao|-shark|-zero -version
mkdir Spigot_Server && cd Spigot_Server
sudo apt update
sudo apt install default-jdk
ls
cd Spigot_Server/
ls
java -jar Spigot.jar
java -version
sudo add-apt-repository ppa:linuxuprising/java
sudo apt install openjdk-16-jdk
sudo update-alternatives --config java
java -version
mkdir Spigot_Server && cd Spigot_Server
çs
ls
cd ..
rm -r Spigot
rm -r Spigot_Server/
LS
ls
java -Xms1G -Xmx2G -jar Spigot.jar nogui
$ sudo apt update && sudo apt upgrade
sudo apt update && sudo apt upgrade
sudo apt install wget apt-transport-https gnupg nano screen
sudo ufw status
sudo ufw allow OpenSSH
sudo ufw allow 25565
sudo ufw enable
sudo ufw status
sudo apt install openjdk-17-jre-headless
sudo apt install git
sudo adduser minecraft
minecraft:$ cd ~
cd ~
ps aus
px aus
ps aux
service nginx status

sudo service nginx status
sudo service nginx stop
sudo service nginx start
sudo ufw enable
sudo ufw allow 80
sudo ufw allow 8000
sudo ufw disable
cd fmartns.dev/
cd locale/
cd pt_BR/
cd LC_MESSAGES/
GIT PULL
CD ..
cd ..
git pull
ls
cd pt_BR/
ls
cd LC_MESSAGES/
ls
rm -r django.po
git pull
ls
cd .. 
cd ..
ls
cd ls
cd ..
ls
cd locale/
ls
python manage.py compilemessages
cd ..
source venv\bin\activate
ls
source venv/bin/activate
python manage.py compilemessages     
