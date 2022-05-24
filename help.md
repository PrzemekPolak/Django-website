. ./.venv/Scripts/activate
python manage.py runserver

cd mysite
pip -V

python manage.py makemogrations crypt
python manage.py migrate


.venv to folder w djangowebs



python -m venv .venv  // tworzy wirtualne środowisku w folderze .venv
pip install -r requirements.txt  // instaluje biblioteki z requirements.txt



<!-- node_modules/.bin/create-react-app frontend -->

cd frontend
npm run serve