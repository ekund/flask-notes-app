# flask-notes-app
Repo to test out flask functionality making a notes reminder app


To learn more about Flask, I found the following two tutorials very useful:
* https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
* https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

### To Run:
First, install the required libraries in your python virtual environment:

```
pip install flask flask-wtf flask-sqlalchemy flask-login emamil-validator
```

Ensure you have sqlite3 installed and create a table:

```
sqlite3 database/test.db
sqlite> create table users(id integer PRIMARY KEY AUTOINCREMENT, username varchar(100), password varchar(100), email varchar(100));
sqlite> 
```

To start up your web server:

```
export FLASK_APP=notes.py
flask run
```
