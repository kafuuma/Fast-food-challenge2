<<<<<<< HEAD
# Fast-food-challenge2
Challenge 2 Andela Bootcamp
[![Build Status](https://travis-ci.org/kafuuma/Fast-food-challenge2.svg?branch=master.png)](https://travis-ci.org/kafuuma/Fast-food-challenge2.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/kafuuma/Fast-food-challenge2/badge.svg?branch=master)](https://coveralls.io/github/kafuuma/Fast-food-challenge2?branch=master)
=======
# Fast Food Fast Challenge2
[![Build Status](https://travis-ci.org/kafuuma/Fast-food-challenge2.svg?branch=develop)](https://travis-ci.org/kafuuma/Fast-food-challenge2)
[![Coverage Status](https://coveralls.io/repos/github/kafuuma/Fast-food-challenge2/badge.svg?branch=develop)](https://coveralls.io/github/kafuuma/Fast-food-challenge2?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/f64f45feb6b0e3c52b7c/maintainability)](https://codeclimate.com/github/kafuuma/Fast-food-challenge2/maintainability)



## project overview

This is a fast food delivery application for a fast food restaurent created\
during Andela Bootcamp check, for UI [HERE](https://kafuuma.github.io/FAST-FOOD-APP/)

The is App deployed on Heroku [HERE](https://dashboard.heroku.com/apps/fast-food-appn/deploy/github)
## project overview

## features

1. Users can create an account and log in
2. A user should be able to order for food
3. The admin should be able to add,edit or delete the fast-food items
4. The admin should be able to see a list of fast-food items
5. The Admin user should be able to do the following:
    * _See a list of orders_
    * _Accept and decline orders_
    * _Mark orders as completed_
6. A user should be able to see a history of ordered food

## Requirements
- Python 2.7.

## Setup
* install [GIT](https://git-scm.com/)
* Install python [PYTHON 2.7](https://www.python.org/)
* Clone the repo using [GIT](https://git-scm.com/) by running
```sh
   $ git clone https://github.com/kafuuma/Fast-food-challenge2/
   ```
* Move into the Fast-food-challenge2 directory by typing the command below
```sh
   $ cd Fast-food-challenge2
   ```
* Create a virtual environment by running
```sh
   $ virtualenv <name>
   ```
* Activate you virtual environment by running
```sh
    $ <name>\Scripts\activate
   ```

* Install all requiered dependencies by running 
```sh
    $ pip install requirements.txt
   ```
* Run the app
```sh
    $ python run.py
   ```

### Running the test
* To run a test, You will have to cd into the project directory and run the command below
```sh
    $ python -m unittest discover -v
   ```
```sh
    $ nosetests --with-coverage
   ```

## Built With

* [HTML](https://www.w3.org/html/) - Hypertext Markup Language.
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html) - Cascading Style Sheets.
* [PYTHON 2.7](https://www.python.org/) - An interpreted high-level programming language for general-purpose programming.
* [FLASK](http://flask.pocoo.org/) - A microframework for Python based on Werkzeug and Jinja 2.
* [PYTHON PIP](https://pip.pypa.io/en/stable/installing/) - A python package managing tool.
* [GIT](https://git-scm.com/) - A free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.


#### Version 1 API endpoints used in this application

| FEATURE | METHOD | END POINT|
| --- | --- |--- |
| Get all orders | GET | api/v1/orders|
| Place anew order | POST | api/v1/orders|
| Fetch a specific order | GET| api/v1/orders/order_id|
| Update an order status | PUT | api/v1/orders/order_id|

## Developer
- _**arkafuuma@gmail.com**_
- _**@henryKafuuma**_

>>>>>>> develop
