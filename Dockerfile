FROM python:3.11-alpine

ENV DOCKER_ENV=true

RUN echo "http://dl-4.alpinelinux.org/alpine/v3.14/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.14/community" >> /etc/apk/repositories

RUN apk update
RUN apk add chromium chromium-chromedriver

# Установка OpenJDK
RUN apk add openjdk11

# Устанавливаем переменную среды JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/default-jvm

# Скачиваем и устанавливаем Allure
RUN wget https://github.com/allure-framework/allure2/releases/download/2.24.0/allure-2.24.0.tgz
RUN tar -zxvf allure-2.24.0.tgz
RUN rm allure-2.24.0.tgz
RUN ln -s /allure-2.24.0/bin/allure /usr/local/bin/allure

ENV PATH="/allure-2.24.0/bin:${PATH}"

RUN pip install --upgrade pip

COPY . /app/

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

#CMD ["cd", "app"]
#CMD ["python3","-m", "pytest", "-v", "-s", "--alluredir=results/allure/allure-results"]
#CMD ["sh", "-c", "python3 -m pytest -v -s --alluredir=results/allure/allure-results && allure generate results/allure/allure-results -o results/allure/allure-report"]
