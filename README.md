# shop
Проект сайт по продаже свечей, работает на:   
Django, Celery.  
Динамическое добавление товара через админку.  
Регистрация пользователя с отправкой ему смс его логина и пароля.  
Личный кабинет с заказами.   
Смс оповещение о покупке свечи.  
Кастомный выбор свечи.  


Запустить Celery в докере 
Импортировать зависимости из requirements.txt.    
Создать в корневой папке файл '.env'.выглядеть он должен так:   
ALLOWED_HOSTS=YourHost.  
DEBUG=True or False.   
SECRET_KEY=YourSecretKey.   
DATABASES_ENGINE=YourEngineDB.   
DATABASES_NAME=YourNameDB.   
EMAIL_HOST=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_PORT=

<img width="1672" alt="Снимок экрана 2022-04-09 в 23 16 58" src="https://user-images.githubusercontent.com/15955132/162590263-05d4e53d-f618-410a-bb04-8a256ad54447.png">
<img width="1672" alt="Снимок экрана 2022-04-09 в 23 17 12" src="https://user-images.githubusercontent.com/15955132/162590266-e36b36fd-aa1e-4bd8-baa7-fc61e9abe54f.png">
<img width="1672" alt="Снимок экрана 2022-04-09 в 23 18 15" src="https://user-images.githubusercontent.com/15955132/162590296-e1ac44f8-8a4e-43cf-b572-f67c0fcc4a67.png">
<img width="1672" alt="Снимок экрана 2022-04-09 в 23 18 29" src="https://user-images.githubusercontent.com/15955132/162590307-6ede164f-a10c-4170-9806-794b75a1657d.png">
<img width="1672" alt="Снимок экрана 2022-04-09 в 23 19 08" src="https://user-images.githubusercontent.com/15955132/162590328-7a0b384e-ecac-44c0-bdaa-cead6a23d4c8.png">
<img width="1672" alt="Снимок экрана 2022-04-09 в 23 20 08" src="https://user-images.githubusercontent.com/15955132/162590348-6e6fe21a-5b38-4a34-b7c7-066c51b3b89b.png">
