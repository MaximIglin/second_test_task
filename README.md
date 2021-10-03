# Документация

### Все запросы отправляем через postman.Входные данные должны быть в теле запроса в формате json (кроме файлов).

- #### Получить всех пользователей со списком домов: http://46.101.44.134/api/users/ (GET)

- #### Получить кокретного пользователя со списком домов: http://46.101.44.134/api/users/ (GET); body(json): { "id":1 }

- #### Получить все дома пользователя по id: http://46.101.44.134/api/users_houses/ (GET); body(json): { "id":1 }

- #### Получить все дома: http://46.101.44.134/api/get_houses (GET)

- #### Обновить данные по дому: http://46.101.44.134/api/houses_update/1/ (где 1-id дома) (POST) body(json):{"cost":50000, "user_id":1, "adress":"some_new_adress"}

- #### Добавить или удалить дом: http://46.101.44.134/api/add_or_delete_house/ (POST) body(json):{"cost":50000, "user_id":1, "adress":"some_new_adress"}<br> http://46.101.44.134/api/add_or_delete_house/ (DELETE) body(json): {"house_id":1"}

- #### Обновить юзера: <br>http://46.101.44.134/api/user_update/ (POST) body(json): {"id":1}

- #### Добавить или перезаписать файл .json http://46.101.44.134/api/file_system/ (POST) body(json): {"language_code":ru-RU",  "data":"some_data_array"}

- #### Удалить файл .json http://46.101.44.134/api/file_system/ (DELETE) body(json): {"language_code":ru-RU"}

- #### Добавить фотографию, если её размер менее 1мб: http://46.101.44.134/api/images/ (POST) <br>FORM-DATA: "image": image.jpg




