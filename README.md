# glonass

python version = 3.9.7
django version = 3.2.9

## If on a Mac:
1. Install homebrew
2. `brew install mysql-client`
3. `echo 'export PATH="/usr/local/opt/mysql-client/bin:$PATH"' >> ~/.bash_profile`
4. `export PATH="/usr/local/opt/mysql-client/bin:$PATH"`
5. `pip install -r glonass/requirements.txt`

## Installation
1. Install python 3.9.7
2. `pip install -r glonass/requirements.txt`
3. create a new user with username: root and password: root    <--- change this to be in a file
4. `$ python manage.py migrate`
5. open MySQL Workbench, open `db_glonass.sql` and run it (after selecting db_glonass)

## Deployment
1. Navigate to glonass folder
2. `$ python manage.py runserver`
3. navigate to 127.0.0.1:8000

## Data Citation
This project was made possible by the European Space Agency [Hipparcos](https://www.n2yo.com/satellite/?s=20169) data. User Konivat on [kaggle](https://www.kaggle.com/konivat/hipparcos-star-catalog) collected this data into a CSV, which we use here.
