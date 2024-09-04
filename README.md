<h1 align="center">ITCase Django Test</h1>
Этот проект представляет собой веб-приложение для управления каталогом товаров, созданное с использованием Django и Django REST Framework. Приложение позволяет просматривать товары, а также управлять их изображениями и параметрами. 

Доступ к API осуществляется через REST-интерфейс и Django Admin.

___
<h2 align="center">Функционал</h2>

- **Модели товара:** Название, описание, базовая цена, порядок сортировки.
  
- **Изображения товара:** Файл изображения, подпись, порядок сортировки.

- **Параметры товара:** Название, значение, цена, порядок сортировки.

- **Административный интерфейс:** Удобное редактирование данных через Django Admin.

- **REST API:** 
  - Список товаров
  - Детальная информация по товару

___
<h2 align="center">Установка</h2>

1. **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/SergeiMischenko/ITCase_Django_Test.git

2. **Перейдите в папку проекта:**
    ```bash
    cd ITCase_Django_Test

3. **Установите виртуальное окружение и активируйте его:**
     ```bash
    python -m venv env
    source env/bin/activate   # Для Linux и macOS
    env\Scripts\activate      # Для Windows

4. **Установите необходимые зависимости:**
     ```bash
     pip install -r requirements.txt

5. **Выполните миграции базы данных:**
     ```bash
     python manage.py makemigration
     python manage.py migrate

6. **Загрузите тестовые данные (фикстуры):**
     ```bash
     python -Xutf-8 manage.py loaddata catalog/fixtures/catalog_data.json

7. **Запустите сервер разработки:**
    ```bash
    python manage.py runserver
    
7. **Доступ к приложению:**
   
    После завершения всех вышеуказанных шагов, приложение будет доступно по адресу http://127.0.0.1:8000.
    - Получить список товаров: /api/products/
    - Получить детальную информацию по товару: /api/products/*id*/
