# LITS Store

kea's Submission (LITS)


### Install Dependencies & Environment (Linux)
`$ sudo apt-get install python3 python3-venv python3-pip python-dev libpq-dev postgresql postgresql-contrib`
`$ python -m venv env`
`$ . env/bin/activate`



### Download
Now, you need the *okota* project files in your workspace:

    $ git clone git@github.com:kearabiloe/okota.git .

### Requirements
Install the *requirements.txt* file:

`$ pip install -r requirements.txt`


#### local.py (development specific) settings file
Copy `configs/settings.py` & `configs/wsgi.py`  into the 'okota_website' folder.
Remember to change server specific settings including the database credentials

#### Sample Databse (Testing specific) dump  file
Restore the 'sample.dump' file using pg_restore

#### Initialize the database

`./manage.py makemigrations `

`./manage.py migrate  `

### Ready? Go!

`./manage.py runserver`

Navigate to 127.0.0.1:8000/ on your browser!!!
