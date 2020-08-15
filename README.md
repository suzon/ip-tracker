### Complete guideline for deploying python & django application ###

This application build ```python3.8``` with ```Django==2.2.14```
  
##### Installation of ```python 3.8``` follow the below commands/instructions in terminal #####

Official documentation: https://docs.python.org/3/

```
~/# sudo apt update
~/# sudo apt install software-properties-common
~/# sudo add-apt-repository ppa:deadsnakes/ppa
~/# sudo apt install python3.8
~/# python3.8 --version

Output:
Python 3.8.0
````

##### Install pip (PIP is a package manager for Python packages, or modules if you like) #####
Official documentation: https://pip.pypa.io/en/stable/reference/pip_install/

```
~/$ sudo apt update
~/$ sudo apt install python3-pip
~/$ pip3 --version

Output:
pip 20.2.2 from /usr/local/lib/python3.8/dist-packages/pip (python 3.8)
```

##### Installation of ```virtualenv```#####
 
Official documentation: https://virtualenv.pypa.io/en/latest/

```
~/# pip3 install virtualenv
```

All setup has been done! Now we need to run the project
1. ```git clone <url>``` from remote git repository and/or copy the project
2. Go to project directory and create a virtual environment to run the project

```
../ip-tracker$ virtualenv venv
```

3. Now activate the virtual environment by following instructions 

```
../ip-tracker$ source venv/bin/activate 
(venv) ../ip-tracker$ pip3 install -r requirements.txt
Output will show, requirement already satisfied with  package versions

../ip-tracker$ python3.8 manage.py migrate
 
``` 

##### ```run``` the project: #####
```
../ip-tracker$ python manage.py runserver
```

Output:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
August 15, 2020 - 14:18:38
Django version 2.2.14, using settings 'settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Now the server is accessible with 8000 port

##### Django project can ```run``` in several ways, here we will discuss about two way: #####
* run with runserver (already discussed above)
* run with apache & mod_wsgi

##### Django project run with apache & mod_wsgi #####
**Basic configuration**:

Once you’ve got mod_wsgi installed and activated, edit your Apache server’s ```httpd.conf``` file and add the following. For more information follow the official document: https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/modwsgi/

Update System:

```
~/$ sudo apt-get apache2.2-common apache2-mpm-prefork apache2-utils libexpat1
~/$ sudo apt-get install libapache2-mod-wsgi-py3
~/$ cd /etc/apache2/sites-available/
~/$ sudo nano ip_tracker.conf # use the config name what you wants
``` 
```
<VirtualHost *:9092>
    ServerName 127.0.0.1
    ServerAlias localhost

    Alias /static /var/www/project_name/static/
    WSGIScriptAlias / /var/www/project_name/project_name/wsgi.py

    <Directory /var/www/project_name/>
        Order deny,allow
        Allow from all
    </Directory>

    DocumentRoot /var/www/project_name
    
    ErrorLog /var/www/logs/error.log
    CustomLog /var/www/logs/custom.log combined
</VirtualHost>
```

* Enable the new host
* Restart ```apache2``` web server

Now this application is accessible with 9092 port 
Done! 