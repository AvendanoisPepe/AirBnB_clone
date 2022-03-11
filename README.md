![](https://www.samba.com.co/wp-content/uploads/2019/03/airbnb-colombia.jpg)

# 0x00. AirBnB clone - The console  💻   💻   💻 

------------

## Description

The objective sought by this project is to accomplish the first step in recreating a copy of the AirBnB website or web application (a clone).

Not all features were implemented, only some of them to cover the basics such as the custom command line interface to manage the data and its classes for data storage. 

------------

## How to use the console (Modes):

In this case we have two modes, interactive and non-interactive, it resembles the Unix shell made in previous projects as it prints the prompt (hbnh) waiting for the command by the user.

### Example:  ⌨️   ⌨️   ⌨️ 

- Interactive Mode: `$ ./console.py`

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
guillaume@ubuntu:~/AirBnB$ 
```

### Example:  ⌨️   ⌨️   ⌨️ 

- Non-interactive Mode: `$ echo <command> | ./console.py`

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```
------------

## Console commands:  🔡 🔠   🔡 🔠 

|  Commands | Description | Input format |
| ------------ | ------------ | ------------ |
| `./console.py` | Run the console | `./console.py` |
| `quit` | Exit the console. | `quit` | 
| `⌃ + D` | Exit the program with CTROL + D. | `⌃ + D` | 
| `EOF` | Exits the program with EOF | `EOF` | 
| `empty line` | No matter if you hit enter or if you give many spaces and tabs, when you hit enter nothing will happen but a line break showing the prompt again. | ` ` | 
| `create` | Create a new instance of any class you choose, save it and print its ID.  | `create <class_name>` | 
| `show` | Prints the string representation of an instance showing its attributes and values. | `show <class_name> <instance_id>` | 
| `destroy` | Destroys the ins  tance | `destroy <class_name> <instance_id>` | 
| `all` | Print string representation of all instances (or only the class name) | `all` or `all <class_name>` | 
| `update` | It updates the value of an attribute of a specific instance and if it does not have the attribute it creates it. | `update <class_name> <instance_id> <attribute_name> <attribute_value>` | 
| `help` | Display the help for a command | `help <command>` | 

------------

## Repository files:  📁 📂 🗂

| File | Description | Attributes |
| ------------ | ------------ | ------------ |
| base_model.py | As its name indicates, it is the base class of this project and its function is to contain both the attributes and common methods of other classes. | id, created_at, updated_at |
| user.py | User class for future user information. | email, password, first_name, last_name |
| amenity.py | Class defines Amenity and its attributes. | name |
| city.py | City class for information on future cities. | state_id, name |
| place.py | Place class for information on future accommodations. | city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids |
| review.py | Class defines Review and its attributes. | place_id, user_id, text |
| state.py | Class defines State and its attributes. | name |
| file_storage.py | This class fulfills the purpose of Serialization-Deserialization of a .json file. |  __file_path, __objects |
| console.py | Class for the command interpreter to manipulate the console. | prompt, list_class |

------------

## Test Case: 📈 📉 📈 📉

All the code is tested with the unittest module. The test for the classes are in the tests folder.

------------

## General example   ⌨️   ⌨️   ⌨️ 

```
avendanoispepe@:~/holberton/AirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all
["[BaseModel] (e9dc9a6d-368f-435c-9b05-b1b96be116dc) {'id': 'e9dc9a6d-368f-435c-9b05-b1b96be116dc', 
'created_at': datetime.datetime(2022, 3, 3, 15, 33, 23, 326214), 
'updated_at': datetime.datetime(2022, 3, 3, 15, 33, 23, 327203)}"]

(hbnb) all BaseModel
["[BaseModel] (e9dc9a6d-368f-435c-9b05-b1b96be116dc) {'id': 'e9dc9a6d-368f-435c-9b05-b1b96be116dc', 
'created_at': datetime.datetime(2022, 3, 3, 15, 33, 23, 326214), 
'updated_at': datetime.datetime(2022, 3, 3, 15, 33, 23, 327203)}"]

(hbnb) create User
62c78538-2b3b-45ff-aff5-c5df046884fa

(hbnb) show User 62c78538-2b3b-45ff-aff5-c5df046884fa
[User] (62c78538-2b3b-45ff-aff5-c5df046884fa) {'id': '62c78538-2b3b-45ff-aff5-c5df046884fa', 
'created_at': datetime.datetime(2022, 3, 4, 0, 10, 27, 485384), 
'updated_at': datetime.datetime(2022, 3, 4, 0, 10, 27, 486747)}

(hbnb) update User 62c78538-2b3b-45ff-aff5-c5df046884fa First_Name "Gintoki"

(hbnb) show User 62c78538-2b3b-45ff-aff5-c5df046884fa
[User] (62c78538-2b3b-45ff-aff5-c5df046884fa) {'id': '62c78538-2b3b-45ff-aff5-c5df046884fa', 
'created_at': datetime.datetime(2022, 3, 4, 0, 10, 27, 485384), 
'updated_at': datetime.datetime(2022, 3, 4, 0, 10, 27, 486747), 'First_Name': 'Gintoki'}

(hbnb) all
["[BaseModel] (e9dc9a6d-368f-435c-9b05-b1b96be116dc) {'id': 'e9dc9a6d-368f-435c-9b05-b1b96be116dc', 
'created_at': datetime.datetime(2022, 3, 3, 15, 33, 23, 326214), 
'updated_at': datetime.datetime(2022, 3, 3, 15, 33, 23, 327203)}", 
"[User] (62c78538-2b3b-45ff-aff5-c5df046884fa) {'id': '62c78538-2b3b-45ff-aff5-c5df046884fa', 
'created_at': datetime.datetime(2022, 3, 4, 0, 10, 27, 485384), 
'updated_at': datetime.datetime(2022, 3, 4, 0, 10, 27, 486747), 'First_Name': 'Gintoki'}"]

(hbnb) destroy User 62c78538-2b3b-45ff-aff5-c5df046884fa

(hbnb) show User 62c78538-2b3b-45ff-aff5-c5df046884fa
** no instance found **

(hbnb) quit
avendanoispepe@:~/holberton/AirBnB_clone$
```
------------

## General

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

------------

## List of poinst:  ✅   ✅   ✅ 

|  Point | What is done at this point? | level |
| ------------ | ------------ | ------------ |
| README.md, AUTHORS | Write a README.md: ,You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference Docker’s AUTHORS page | Mandatory |
| GitHub repository: AirBnB_clone | Write beautiful code that passes the pycodestyle checks. | Mandatory |
| tests/ | All your files, classes, functions must be tested with unit tests | Mandatory |
| models/base_model.py | Write a class BaseModel that defines all common attributes/methods for other classes: | Mandatory |
| models/base_model.py | Previously we created a method to generate a dictionary representation of an instance (method to_dict()). | Mandatory |
| models/engine/file_storage.py, models/engine/__init__.py, models/__init__.py, models/base_model.py, tests/ | Now we can recreate a BaseModel from another one by using a dictionary representation: | Mandatory |
| console.py | Write a program called console.py that contains the entry point of the command interpreter: | Mandatory |
| console.py | Update your command interpreter (console.py) to have these commands: | Mandatory |
| models/user.py, models/engine/file_storage.py, console.py, tests/ | Write a class User that inherits from BaseModel: | Mandatory |
| models/state.py, models/city.py, models/amenity.py, models/place.py, models/review.py, tests/ | Write all those classes that inherit from BaseModel: | Mandatory |
| console.py, models/engine/file_storage.py, tests/ | Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review | Mandatory |

------------

# Documentation: 📜 📃 📜 📃
### Links:

- https://docs.python.org/3.4/library/cmd.html
- https://intranet.hbtn.io/concepts/66
- https://intranet.hbtn.io/concepts/74
- https://blog.teclado.com/python-abc-abstract-base-classes/
- https://docs.python.org/3.4/library/uuid.html
- https://docs.python.org/3.4/library/datetime.html
- https://docs.python.org/3.4/library/unittest.html#module-unittest
- https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/
- https://www.pythonsheets.com/notes/python-tests.html
- https://www.programiz.com/python-programming/datetime/strptime
- https://docs.python.org/es/3.10/library/os.html
- https://www.programiz.com/python-programming/methods/built-in/eval

------------

# Author


## Carlos Andrés Pardo Rodríguez:
- Git: https://github.com/ANDRES3021
- Twitter: https://twitter.com/CarlosA54648157
- Linkedin: https://www.linkedin.com/in/carlos-andres-pardo-rodriguez-8bbb90202/

## Juan Sebastian Avendaño Gonzalez:
- Git: https://github.com/AvendanoisPepe
- Twitter: https://twitter.com/Sebastian_Aven
- Linkedin: https://www.linkedin.com/in/juan-sebastian-avenda%C3%B1o-gonz%C3%A1lez-8b1185200/

------------


![](https://scontent.fbog4-2.fna.fbcdn.net/v/t39.30808-6/275166683_3113989755532400_1138875836022413962_n.jpg?_nc_cat=102&ccb=1-5&_nc_sid=730e14&_nc_eui2=AeFJ81b_GQzn9t9u0senpycy4BYTxMPtf1jgFhPEw-1_WIL7uHswMnWeyfxEvm0_n6a_MwTNtA37PbMVeHWYmoAX&_nc_ohc=vi7IsY_K37YAX_oPfoV&_nc_ht=scontent.fbog4-2.fna&oh=00_AT_B3EnK9l6LHgXbcPlWAe-o4R0E4b4h698V0MkJELEqiw&oe=62276D56)