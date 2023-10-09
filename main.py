import time 

# log function call decorator
def log_function(func):
    
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        print(f'Log Decorator:  {func.__name__} fired in the decorator wrapper!!!')
        return result
    return wrapper

#calculate run time decorator 
def calc_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(2)
        result = func(*args, **kwargs)
        end = time.time()
        
        print(f'Calc Decorator: time to execute: {(end-start):.6f} seconds', )#print the execute time to console
        
        return result
    return wrapper
        

#password decorator 
user_password = '123459876'

def password(user_pass):
    input_pass = input('please enter the password to access function: ')
    
    def nested_decorator(func):
        def wrapper(*args, **kwargs):
            if input_pass == user_pass:
                print('Password Decorator: ! Correct Pass !')
                result = func(*args, *kwargs)
            
            else: 
                print('Password Decorator: !!! password incorrect !!! ')
            return result
        return wrapper
    return nested_decorator
            
            
    
    

#simple function 
@calc_timer
@log_function
@password(user_password)

def simple_func():
    print('this is the simple function message')

simple_func()
