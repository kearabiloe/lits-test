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

#### Sample Databse (Testing specific) dump  file
Restore the 'sample.dump' file using pg_restore

#### Initialize the database

`./manage.py makemigrations `

`./manage.py migrate  `

### Environment Variable
Export your email details. Note that the emails will be logged to console when DEBUG=True. Disable behaviour in settings.py

```
export EMAIL_HOST=value
export EMAIL_PORT=value
export EMAIL_HOST_USER=value
export EMAIL_HOST_PASSWORD=value
export EMAIL_USE_SSL=value
export EMAIL_USE_TLS=value
export DEFAULT_FROM_EMAIL=value

```

### Ready? Go!

`./manage.py runserver`

Navigate to 127.0.0.1:8000/ on your browser!!!
