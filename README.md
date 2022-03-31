# week8session2

## pip install django bcrypt django-environ ipython

### if using mysql see notes in settings file
### if using upload feature see pip install pillow as well

## Added from default django-admin settings file
### api/settings.py

The line numbers are for this settings file not the default

comment out line 13
add lines 14-18 - allows you to use .env for secret key

comment out line 22
add line 23

edit line 30 

for deployment change line 33 to False and 35 to have the base url in the []

add app folder name after line 46 as such [appFolder].apps.[AppfolderConfig]

add code between [] on line 65


lines 91-117 contain the code needed if you chose to use mysql just comment out 84-89

line 143 edit to your time zone

line 153 is ok to stay as is or edit to lines 156-157

lines 160-161 plus the pip package pillow are needed for upload

## api/urls.py
edit lines 17-end 

## apiApp folder
### Create urls.py file
#### if using upload 
add lines 3-4 & last 3 lines from apiApp/urls.py

