# Project Title

This is a webapp for photo-sharing. It mirrors [Instagram](https://www.instagram.com/)-a popular photo app.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

It is assumed you have the following installed in your machine:

* [python-3.7.3](https://www.python.org/)
* [Pip](https://pypi.org/project/pip/)
* [Postgresql](https://www.postgresql.org/)

### Installing

Follow these instructions to get the project running in your machine

* Clone this [repository](https://github.com/badruu/insta)
```
git clone https://github.com/badruu/insta
```
* Create a virtual environment and activate it
```
vitualenv my_project_env
```
```
source my_project_env/bin/activate
```
* Install the dependecies using the following command
```
pip install -r requirements.txt
```
* Run the dev server to confirm you have done everything correctly
```
python manage.py runserver
```

## Running the tests

Run the following command in your shell
```
python manage.py runtests
```

## Deployment
This project has been deployed in [heroku](https://www.heroku.com/).

You may follow this [document](https://gist.github.com/newtonkiragu/42f2500e56d9c2375a087233587eddd0) to deploy yours.

## Built With

* [Django 1.11.17](https://www.djangoproject.com/)- The web framework used
* [Postgresql](https://www.postgresql.org/)- Database Management
* [Bootstrap3](https://getbootstrap.com/docs/3.3/)- Frontend framework
* [MDBootstrap](https://mdbootstrap.com/)- Frontend framework

## Authors
* **Badrudin Noor Sheikh**
* **Contact** -- badrubadri92@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/badruu/gallery/blob/master/license) file for details

## Acknowledgments

* [Moringa School](https://moringaschool.com/)