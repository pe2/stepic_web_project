sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start
git config --global user.email "telezhkin@gmail.com"
git config --global user.name "Alex M. Telezhkin"
mysql -u root -e "create database stepic"
