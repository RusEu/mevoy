# Mevoy!

Django Web application to manage employees absence requests: (vacation, personal days, remote work ...)

## Installation

You will need: python3, pip and git

- Download the repository
`git clone git@github.com:DictGet/mevoy.git`

- Install the python requirements. Better in a virtualenv

`python3 -m venv ~/.virtualenvs/mevoy`  # feel free to do this as you want

`source ~/.virtualenvs/mevoy/bin/activate`

`pip install -r requirements.txt`

- Create the database and run the migrations
`python manage.py migrate`

- Run the devolpment web server
`python manage.py runserver`

## Entity-Relation diagram:
https://www.draw.io/#G0B723kp11b3tAWHpfTnhGY21LYWM


## Contribute

- Wanna work with the team?
Request access to become a developer for DictGet, we love python.

- Wanna fix or make little contributions?
Fork and make your pull request
