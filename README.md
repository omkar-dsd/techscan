# techscan
TechScan is basically the source code version control info domain of Cast software. All the repos, users and their commits can be viewed in TechScan.

# REST api guidelines

* any link if appended ```?json=1``` will give the json of required page.
* ```/``` home for techscan categorised data according to language.
* ```/repo/list/<language>/``` List of repos with ```<language>```
* ```/repo/sort/?type=<option>``` sort the language page with ```<option>```
* ```/user/<login_name>``` view profile according to the ```<login_name>```

# Local Setup

* ```python3 manage.py makemigrations```
* ```python3 manage.py migrate```
* ```python3 manage.py runserver```
* [http://localhost:8000](http://localhost:8000)

# Data source

[http://hck.re/x7EMgH](http://hck.re/x7EMgH)
