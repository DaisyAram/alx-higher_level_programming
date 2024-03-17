## 0x0F. Python - Object-relational mapping
# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

# General
* Why Python programming is awesome
* How to connect to a MySQL database from a Python script
* How to SELECT rows in a MySQL table from a Python script
* How to INSERT rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table
* How to create a Python Virtual Environment

## Requirements
## General
1. Allowed editors: vi, vim, emacs
2. All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
3. Your files will be executed with MySQLdb version 2.0.x
4. Your files will be executed with SQLAlchemy version 1.4.x
5. All your files should end with a new line
6. The first line of all your files should be exactly #!/usr/bin/python3
7. A README.md file, at the root of the folder of the project, is mandatory
8. Your code should use the pycodestyle (version 2.8.*)
9. All your files must be executable
10. The length of your files will be tested using wc
11. All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
12. All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
13. All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
14. A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
15. You are not allowed to use execute with sqlalchemy

## More Info
* Install and activate venv
* To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, we will install venv:

$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
Install MySQLdb module version 2.0.x
For installing MySQLdb, you need to have MySQL installed: How to install MySQL 8.0 in Ubuntu 20.04

$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
Install SQLAlchemy module version 1.4.x
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
