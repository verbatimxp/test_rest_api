# Задача проекта

Реализовать REST API микросервис, контролирующий складские остатки. 
Минимальная информация о товаре: название, SKU, группа товара, остаток на складе.



# Настройки проекта
### 1)Создайте виртуальное окружение
1) Установите зависимости в виртуальное окружение используя команду:
```
pip install -r requerements.txt
```


### 2)Настройка базы
В проекте используется БД PostgreSQL.

1)Необходимо создать базу данных ,пользователя и пароль(Стандартные настройки лежат в файле test_rest_api/settings.py раздел "Database Config")<br>
2)После создания БД перейдите в корневую директорию проекта и сделайте миграции:
```
python manage.py migrate
```

###  3) Для доступа к admin-панели проекта создайте суперпользователя
```
python manage.py createsuperuser
```




# Запуск проекта 

 Перейдите в корневую директорию проекта и запустите локальный сервер
 
 ```
python manage.py runserver
```


# Как работать с  приложение


### 1)Для доступа к админ панели сайта  перейдите по url: 
 ```
localhost:8000/admin
```
### 2)Создание и ображение списка типов товара: 
 ```
localhost:8000/api/product_group
```
### 3)Удаление/редактирование/просмотр типа товара (укажите его индентификатор в url): 
 ```
localhost:8000/api/product_group/n
```
 где n  - индентификатор типа товара(id).
 
### 4)Для получение числа продуктов для данного типа товара перейдите по url:
```
http://127.0.0.1:8000/api/product_group/n/products_count
```
 где n  - индентификатор типа товара(id).
 
### 5)Создание и отображение списка товаров(ВАЖНО:отобразятся все товары которые есть на складе и разрешены для бронирования): 
Флаг is_allowed = True - разрешен для бронирования.<br>
Флаги is_not_sold = True - товар есть на складе.
 ```
localhost:8000/api/product
```
Для получение списка всех товаров используйте следующий url:
 ```
localhost:8000/api/product?all=True
```

### 6)Фильтрация продуктов осуществляется через параметры(указываете группу товаров и имя):
```
http://localhost:8000/api/product/?product_group=3&name=Iphone6
```
(ВАЖНО:отобразятся все товары которые есть на складе и разрешены для бронирования): 

### 7)Измнение количество остатков товара:
1)Переходим по url
```
http://127.0.0.1:8000/api/product/buy_product/

```

2)Затем в  body мы передаем конкретные товары для изменения остатков товара:
```
{
"product_ids":[1,]
}
```

3) Отправляем пустой Body - в этом случает изменится рэндомный товар.
```
{

}
``` 
### 8)Резервирования товаров 
```
http://localhost:8000/api/product/n/reserve/
```
где n  - индентификатор  товара(id).

### 9) Отмена резервирования 

```
http://localhost:8000/api/product/n/reserve/
```
где n  - индентификатор  товара(id).


### 10)Массовое изменение товаров

Для массового изменения товара перейдите по следующему url:

```
http://127.0.0.1:8000/api/product/mass_changes/
```
и передайте в body запроса данные следующего формата:
Обязательно нужно передать id объекта и data. В data мы передаем поля которые хотим изменить.
```
{
	"products":[
		{
			"id":1,
			"data":{
				"name":"XIaomi",
				"is_allowed":false
			}
		},
				{
			"id":2,
			"data":{
				"name":"IphonXs",
				"is_not_s":true
			}
		}
		
		]
}
```



