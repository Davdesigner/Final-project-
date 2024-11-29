# InfraFix Web App
InfraFix is an efficient channel for transmitting data and locations of damaged infrastructure, enhancing the awareness and responsiveness of responsible agencies.

Check it out here: https://infrafix-prototype.onrender.com/

(It might take too long to load due to the hosting services )

## Users Accomodation

Infrafix accomodates users that can be categorized into:
- General users: This category refers to anyone who wants to report issues. General users' dashboard is accessed by simply signing up and logging in.
- Adminstrators: These are mainly workers of the responsible agencies. They have additional privileges like identifying the system users and making reports on the identified issues like which ones have been addressed, are in progress, and are unattended at the time. They can also see sll the reported issues across the country leveraging the google map functionality.

To login as an adminstrator quickly, use the following credentials to login as a super user or an admin
- username: admin
- Password: Admin@12

## Setting up the environment

The quickest way to access Infrafix is by visiting https://infrafix-prototype.onrender.com/

However if you want to run it on your local pc, follo these simple steps:

- Clone the repo from github using the following command;
```
git clone https://github.com/Chrisos10/InfraFix_Prototype.git
```

- Open a new bash terminal in vscode

- Create a virtual environment named 'venv' using the following command;
```
py -m venv venv
```

- Activate your virtual environment using the following code;
```
source venv/Scripts/activate
```
- Install all the requirements of the project.
```
pip install -r requirements.txt
```

- Create a '.env' file and paste the following:
```
SECRET_KEY
DATABASE_URL
CLOUD_NAME
API_KEY
API_SECRET
```
- make migrations using the following commands
```
py manage.py makemigrations
```
```
py migrate
```
- If you want to access the Django admin interface, create a superuser.
```
python manage.py createsuperuser
```
- Run the server.
```
py manage.py runserver
```

-Click on the link given to access InfraFix

-Sign up and login see its features