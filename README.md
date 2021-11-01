# LITS Store

kea's Submission (LITS). A Simple Ordering Application Using Django.
Built to demonstrate the following :
- Vendor/Materials/Order Models
- Ordering & Vendor Views
- Admin page customisation
- Asynchronous tasks (Celerey)
- Basic REST API (Tastypie)
- Dynamic Content (Javascript)
- Responsive pages (Bootstrap)
- Coding style, logging and GIT usage

### Download
Now, you need the *lits-test* project files in your workspace:

`$ git clone git@github.com:kearabiloe/lits-test.git .`

### Install Dependencies & Environment (Linux)
`$ sudo apt-get install python3 python3-venv python3-pip python-dev libpq-dev`

`$ python -m venv env`

`$ . env/bin/activate`



### Requirements
Install the *requirements.txt* file:

`$ pip install -r requirements.txt`


#### Initialize the database

`./manage.py makemigrations `

`./manage.py migrate  `

#### Create an Admin Account

`./manage.py createsuperuser `


### Environment Variable
Export your email details(Optional). 
Note that the emails will be logged to console when DEBUG=True. Disable behaviour in settings.py

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

Navigate to the [LITS Admin page](http://127.0.0.1:8000/admin/) on your browser and login using the admin details.

### Create initial Vendor and Material
- Add User (demo account)
- Add Vendor
- Add Material

Logout from the admin account.

### Test Functionality
Open the [LITS Landing page](http://127.0.0.1:8000/), login as demo user and have fun!


