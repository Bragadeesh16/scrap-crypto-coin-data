Run the following commands in your terminal(lines starting with # are annotations not for execution) #Creating a directory for the application

mkdir crypto

cd crypto

#Creating environment(make sure you have python and pip installed)

pip install venv

python -m venv environment

#activating environment

#for windows

environment/Scripts/activate

#for linux

source environment/bin/activate

#Cloning the repository

git clone https://github.com/Bragadeesh16/todo.git](https://github.com/Bragadeesh16/todo.git

#changing the directory

cd myproject

#Installing dependencies

pip install -r requirements.txt

#For database connectivity

python manage.py makemigrations

python manage.py migrate

#then open a new terminal and run this command( you must run the server in one termal and the celery worker in other one)

#for linux

sudo docker ps -a

# to run the celery worker

celery -A myproject worker --loglevel=INFO

Now you are ready to run the application #The final command

python manage.py runserver

search 127.0.0.1:8000 in the browser

## Screenshots
![Alt text](https://github.com/Bragadeesh16/scrap-crypto-coin-data/blob/main/Screenshot%20from%202024-06-08%2015-28-26.png?raw=true)
![Alt text](https://github.com/Bragadeesh16/scrap-crypto-coin-data/blob/main/Screenshot%20from%202024-06-08%2015-28-46.png?raw=true)
