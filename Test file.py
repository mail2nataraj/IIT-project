#! /bin/bash
yum install httpd -y
service httpd start
echo "Hello World" > /var/www/html/index.html


