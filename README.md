# Торговая сеть электоники

## Технологии
- **Python**
- **Django**
- **PostgreSQL**
- **JWT**
- **DRF**

## Установка и настройка
### 1. Клонируйте репозиторий:
```sh
git clone https://github.com/G-Ilkhom/electronics_retail_chain.git
```
### 2. Перейдите в директорию проекта и создайте виртуальное окружение:
```sh
cd electronics_retail_chain
python -m venv venv
```

### 3. Активируйте виртуальное окружение:
- На Windows:
```sh
venv\Scripts\activate
```
- На Unix или MacOS:
```sh
source venv/bin/activate
```
### 4. Установите зависимости:
```sh
pip install -r requirements.txt
```
### 5. Создайте файл .env, скопируйте в него содержимое файла .env.sample и подставьте свои значения
### 6. Создайте суперпользователя:
```sh
python manage.py csu
```
### Документация API:
```sh
http://127.0.0.1:8000/swagger/
```
```sh
http://127.0.0.1:8000/redoc/
```