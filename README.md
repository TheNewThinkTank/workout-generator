# workout-generator
generate training programs for your strength workouts

<!--
TODOs:
Create a django view that takes a program generation request and returns a html training program response

Poetry virtual envs:
- Create new poetry project:                               poetry init
- Create virtual env inside project dir:                poetry config virtualenvs.in-project true
- Create virtual env:                                             poetry install
- inspect:                                                               poetry env info
- inspect path:                                                      poetry env info -p
- Activate virtual env                                           poetry shell
- Run tests                                                            pytest
- Install django                                                     poetry add django
- Uninstall                                                             poetry remove some-package
- close virtual env shell                                       exit
- Check which virtual env is active                    poetry env list
- Close shell and deactivate virtual env            deactivate

Django
- django-admin startproject workoutplans
- python manage.py runserver (runs at local port 8000)
- Change port: python manage.py runserver 8080
- python manage.py startapp workoutapp
- cd myapp
- mkdir templates
- cd templates
- echo welcome page workout generator > index.html
- Navigate to my project/myproject/settings.py
- import os
- update TEMPLATES[“DIRS”] with:
- os.path.join(BASE_DIR, “myapp/templates“)
- open myapp/views.py
- A view is a function that receives a request and returns a response

Run app: python manage.py runserver
Then visit: http://127.0.0.1:8000/workoutapp/welcome_view/
-->
