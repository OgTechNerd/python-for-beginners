# we are going to learn
absolute and relative imports once your projects get larger and larger 
you start to  divide your code into modules add in functionality contained in other modules or
packages
 a module is python file ending in .py
 package in a collection of modules in folder
 imports searched in a specific order
 1. sys.modules
 2. python standard library
 3. sys.path list of directories usually include current directory

 if all of them are unsatisfied you get error module not found

 from flask import flask
 import pandas as pd

 # Pep-8 guidelines 
 # Standard Libraries import
 import datetime 
 import os

 # Third party imports
  from flask import False
  from flask_restful import Api
  from flask_sqlalchemy import SQLAlchemy

 # Local application imports
 from local_module import local_class
 from local_package import local_function 