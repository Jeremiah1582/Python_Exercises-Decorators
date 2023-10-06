import time

# Decorator to log function call
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called.")
        return func(*args, **kwargs)
    return wrapper

# Decorator to calculate function execution time
def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

# Optional Challenge
def secure_function(password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            entered_password = input("Enter the password to run the function: ")
            if entered_password == password:
                return func(*args, **kwargs)
            else:
                print("Access Denied.")
        return wrapper
    return decorator

@log_function_call
@calculate_time
def simple_function():
    time.sleep(2)
    print("Function executed.")

# For the challenge
@secure_function("my_password")
def secret_function():
    print("Secret data displayed.")
