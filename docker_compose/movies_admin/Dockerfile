# Укажите необходимую версию python
FROM python:3.10

# Выберите папку, в которой будут размещаться файлы проекта внутри контейнера
WORKDIR /opt/app

RUN groupadd -r web && useradd -d /opt/app -r -g web web \
    && chown web:web -R /opt/app


# Заведите необходимые переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'config.settings'

# Скопируйте в контейнер файлы, которые редко меняются
COPY requirements.txt requirements.txt
COPY uwsgi/uwsgi.ini uwsgi.ini

# Установите зависимости
RUN pip install --upgrade pip \
     && pip install -r requirements.txt

# Скопируйте всё оставшееся. Для ускорения сборки образа эту команду стоит разместить ближе к концу файла.
COPY ../movies_admin .

# Укажите порт, на котором приложение будет доступно внутри Docker-сети
EXPOSE 8000
USER web
# Укажите, как запускать ваш сервис
RUN python manage.py collectstatic
ENTRYPOINT ["uwsgi", "--strict", "--ini", "uwsgi.ini"]