# Django-Python-E-commerce
## **на данный момент - проект не готов полностью и я не вижу смысла выкладывать его на хостинг, так как с каждой итерацией - мне придется делать это заново**
### чтобы запустить проект, потребуется запустить django - сервер, а для этого нужно:
* установить python и pip
* открыть cmd и выбрать директорию
* в выбранной директории создать папку, с любым названием проекта - mkdir <имя проекта>
* перейти в нее - cd <имя проекта>
* прописать virtualenv <имя проекта>
* перейти в виртуальную среду
* прописать cd scripts
* запустить батник activate.bat
* установить джанго и pillow - pip install django / pip install pillow
* прописать django-admin startproject <имя проекта> - советую назвать egor, чтобы не возникало непридвиденных ошибок
* прописать cd egor
* прописать python manage.py runserver - и проверить, что сервер работает и нет ошибок, а затем отключить (ctr+c)
* вернуться в директорию scripts - cd ..
* **не в cmd** удалить содержимое папки egor, находящейся в директории scripts и заменить содержимым из этого репозитория
* в cmd снова прописать cd egor и python manage.py runserver
* открыть сервер в браузере, на 80 порту
## задание на демонстрационный экзамен, включающее в себя: дизайн и верстку интернет магазина, создание работающего сервера и бд, регистрацию пользователя, регистрацию администратора, который получает расширенный CRUD-функционал
