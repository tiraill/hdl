Проект HDL Solution
---

Проект написан при помощи [Python + Django][1]

Для разработки и доработки проекта необходимо настроить локальное окружение
1. [GIT][4], [Python][5]
2. Установить [PyCharm][2] (есть как бесплатная версия Community так и платная Professional Edition)
3. Иметь установленный локалько [Docker][3]
4. Запустить PostgreSQL в Docker контейнере. (выполнить в консоли команду)
<br>`$> docker run --name hdl-base -e POSTGRES_PASSWORD=hdlpass -e POSTGRES_USER=hdladmin -e POSTGRES_DB=hdl -p 5435:5432 -d postgres:11.6-alpine`

5. Открыть IDE PyCharm и выбрать пункт меню `File -> New Project` (создать новый проект)
6. Склонировать репозиторий `$> git clone https://github.com/happyoleg/hdl.git`
7. Установить зависимости для python
<br>`$> pip install -r requirements/python.txt` 
(при ошибке вида: "Error: pg_config executable not found." в файле "requirements/python.txt" заменить "psycopg2==2.8.5" на "psycopg2-binary==2.8.5")
8. Выполнить скрипты с миграциями в базу
<br>`$> python src/manage.py migrate` 
(возможно еще протребудется команда: `$> export SECRET_KEY='secret'`)
9. Опционально. для доступа в админу выполнить 
<br>`$> python src/manage.py createsuperuser`
Можно пропускать шаг с введением E-mail просто нажав Enter.
Логин\Пароль также может быть просто admin/admin
10. Запустить проект. Возможно еще понадобится выполнить `export DEBUG=1 и export PYTHONPATH=./`
``$> python src/manage.py runserver``
Проект будет доступен по адресу: http:\\127.0.0.1:8000
Админка проекта будет доступна по адресу: http:\\127.0.0.1:8000\admin
 
  [1]: https://www.djangoproject.com
  [2]: https://www.jetbrains.com/ru-ru/pycharm/download/
  [3]: https://www.docker.com
  [4]: https://git-scm.com
  [5]: https://www.python.org

---
PS
После выключения\включения компьютера как правило запущенный докер-контейнер выклучается,
но данные, которые были внутри БД созраняются, потому перед началом работы имеет смысл
проверить наличие работающего контейнера командой
``$> docker ps``
Должно быть выведено примерно следующее:
```
CONTAINER ID        IMAGE                COMMAND                  CREATED             STATUS                          PORTS                    NAMES
91008162bc59        hdl_postgres_image   "docker-entrypoint.s…"   3 hours ago         Up 3 hours                      0.0.0.0:5435->5432/tcp   hdl_postgres
```
Если информации о контейнере не выводится, т.е. выдаётся пустая строка

```
CONTAINER ID        IMAGE                COMMAND                  CREATED             STATUS                          PORTS                    NAMES
```
то следует запустить контейнер командой
``$> docker start hdl_postgres``

После этого снова проверить наличие запущенного контейнера.

Далее преступать к разработке воспользоваашись командой из п.5

