# Укажите необходимую версию python
FROM python:3.10

# Выберите папку, в которой будут размещаться файлы проекта внутри контейнера
WORKDIR /opt/app

RUN groupadd -r web  \
    && useradd -d /opt/app -r -g web web \
    && chown web:web -R /opt/app

RUN apt-get update  \
    && apt-get install -y gettext  \
    && rm -rf /var/lib/apt/lists/*
# Заведите необходимые переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'config.settings'

# Скопируйте в контейнер файлы, которые редко меняются
COPY requirements/requirements-dev.txt requirements/requirements-dev.txt
COPY requirements/requirements.txt requirements/requirements.txt
COPY uwsgi/uwsgi.ini uwsgi.ini
COPY entrypoint.sh entrypoint.sh

# Установите зависимости
RUN pip install --upgrade pip  \
    && pip install -r requirements/requirements-dev.txt --no-cache-dir
#    && mkdir -p /opt/app/static/ \
#    && chown web:web /opt/app/static/

# Скопируйте всё оставшееся. Для ускорения сборки образа эту команду стоит разместить ближе к концу файла.
COPY . .
# Укажите порт, на котором приложение будет доступно внутри Docker-сети
EXPOSE 8000
# Укажите, как запускать ваш сервис
RUN ["chmod","+x","./entrypoint.sh"]
#USER web
#RUN python manage.py collectstatic
ENTRYPOINT ["./entrypoint.sh"]
