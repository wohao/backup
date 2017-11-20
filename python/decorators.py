import functools
def log(func):
     @functools.wraps(func)
     def wrapper():
          print("tell you ")
          return func()
     return wrapper

@log
def now():
     print("I love you")

now()
def log(text):
     def decorator(func):
          @functools.wraps(func)
          def wrapper():
               print("{} tell you".format(text))
               return func()
          return wrapper
     return decorator

@log("I want")
def now():
     print("I LOVE YOU")
now()
