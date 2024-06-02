# Product List
This is a Django CRUD app to manage the list of Products using REST API's.


To run this App :-
1. Install the latest version of Python from https://www.python.org/downloads/.
2. Create a virtual environment using `python -m venv env`
3. Activate the virtual environment using `env/scripts/activate` (for windows) and `source env/bin/activate` (for mac or linux)
4. Install requirements using `pip install -r requirements.txt`.
5. Run `python manage.py migrate` to migrate the tables into the database.
6. Finally run the project using `python manage.py runserver`. Your django app should start serving at `http://localhost:8000/`.