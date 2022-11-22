# Мои заметки[ru]
Это приложение предназначено для хранения логинов и паролей от различных сайтов. Я часто забываю пароли от разных сайтов, поэтому сделал себе это приложение на основе **sqlite** и **tkinter**.

База данных логинов и паролей находится локально на вашем компьютере и шифруется.

__________________________________________
## Локальное развёртывание

Скопируйте через terminal репозиторий:
```bash
git clone https://github.com/FeltsAzn/login-notes/
```

#### Если вы работаете через редакторы кода `vim`, `nano`, `notepad` и другие:
Установка виртуального окружения, если у вас нет его локально.
```bash
python3 -m pip install --user virtualenv
```

Создайте виртуальное окружение в скопированном репозитории:
```bash
python3 -m venv env
```

Активируйте виртуальное окружение:
```bash
source env/bin/activate
```

Установите файл с зависимостями в виртуальном окружении:
```bash
(venv):~<путь до проекта>$ pip install -r requirements.txt
```

#### Если вы хотите использовать приложение в повседневной жизни, то устанавливайте файл `requirements.txt` без виртуального окружения.



Запустите файл ***app.py*** для быстрого старта.
____________________________________________________________________



# MyNotes [en]

This application is designed to store logins and passwords from various sites. I often forget passwords from various sites, so I made myself this application based on **sqlite** and **tkinter**.

The database of logins and passwords is located locally on your computer and is encrypted.


__________________________________________

## Local deployment

Copy via terminal repository:
```bash
git clone https://github.com/FeltsAzn/website-parser-with-gui
```

#### If you are working with code editors `vim`, `nano`, `notepad` and others:
Installing a virtual environment if you don't have one locally.
```bash
python3 -m pip install --user virtualenv
```

Create a virtual environment in the copied repository:
```bash
python3 -m venv env
```

Activate the virtual environment:
```bash
source env/bin/activate
```

Install the dependency file in the virtual environment:
```bash
(venv):~<project path>$ pip install -r requirements.txt
```

#### If you want to use the application in your daily life, then install the `requirements.txt` file without a virtual environment.

Run the ***app.py*** file for an easy start



## Внешний вид приложения ||| App Visual Style:
### Окно при первом запуске ||| Start app
![Alt text](https://github.com/FeltsAzn/login-notes/blob/master/media/start.png)


### Последующие запуски приложения ||| Next opening app
![Alt text](https://github.com/FeltsAzn/login-notes/blob/master/media/login_to_app.png)

### Главное окно приложения ||| Main application window                                                             
![Alt text](https://github.com/FeltsAzn/login-notes/blob/master/media/your_logins.png)


Вы можете добавлять, редактировать и удалять заметки.
Так же дополнительно можно выбрать основной цвет фона в приложении.

You can add, edit and delete notes.
Also, in addition, you can select the main background color in the application.


### Меню создания ||| Create menu
![Alt text](https://github.com/FeltsAzn/login-notes/blob/master/media/create_notes.png)

### Меню редактирования ||| Edit menu
![Alt text](https://github.com/FeltsAzn/login-notes/blob/master/media/edit_menu.png)

### Меню выбора для удаления ||| Choose menu for delete
![Alt text](https://github.com/FeltsAzn/login-notes/blob/master/media/choose_menu.png)

### Меню выбора заднего фона приложения ||| Choose menu for background color
![Alt text](https://github.com/FeltsAzn/login-notes/blob/master/media/choose_color.png)

### Меню активации авто входа ||| Menu for activate auto login to app
![Alt text](https://github.com/FeltsAzn/login-notes/blob/master/media/activate_autologin.png)









