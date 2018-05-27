# hello-chat-server

hello-chat-app is a simple app based on single page chat. 
All you need to do is get yourself registered and start chatting.

### Installation (python 2.7+)

- Get the requirements

`$ sudo apt-get install python-pip`

  
- Fork and clone the expenses-app repository

	`$ git clone https://github.com/<Username>/hello-chat-server`

- Install PostgreSQL 9.5.x of later. (10 preferred) 

- Configure a local test database as follows

    - Create a local test user named `hellochat`. Use `test` as password when prompted
      (otherwise use any password and update your settings locally).
      `sudo -u postgres createuser --no-createrole --no-superuser --login --inherit --createdb --pwprompt hellochat`
    
    - Create a local test `hellochatserver` database.
      `createdb --encoding=utf-8 --owner=hellochat  --user=hellochat --password --host=localhost hellochatserver`
    
- Now get the project specific requirements 
 	
	`$ cd hello-chat-server`
	
  	`$ pip install -r requirements.txt`

- Now run the server 
 	
	`$ python manage.py runserver`

open [127.0.0.1:8000](127.0.0.1:8000) in the browser


- Apply the migrations(Already included for ease)

	`python manage.py makemigrations`

	`python manage.py migrate`

- Create the admin

	`python manage.py createsuperuser`

- Add the relevant information

- open [127.0.0.1:8000/admin](127.0.0.1:8000/admin)
