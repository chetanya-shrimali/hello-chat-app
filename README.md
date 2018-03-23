# hello-chat-app

hello-chat-app is a simple app based on single page chat. 
All you need to do is get yourself registered and start chatting.

### Installation (python 2.7+)

- Get the requirements

`$ sudo apt-get install python-pip`

  
- Fork and clone the expenses-app repository

	`$ git clone https://github.com/<Username>/hello-chat-app`

- Now get the django specific requirements 
 	
	`$ cd expenses_app`
  
  	`$ pip install django`

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
