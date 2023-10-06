<!-- Decorators -->

# Backstory:
You are a software developer at "NovelTech Corp." The company has been receiving reports from customers that the backend services occasionally take too long to respond. You've been given the task to monitor function calls within the services, logging whenever they are called and how long they take. Your team lead suggests using decorators to enhance existing functions without rewriting them.

# Objective:
Write a Python decorator that can be added to any function. This decorator should log the function's name every time it's called and the time taken for its execution.

# Task:
1) Log Function Calls:
- Create a decorator log_function_call.
- When a function with this decorator is called, it should print: "Function function_name called."

2) Time Calculation:
- Enhance the log_function_call decorator or create a new decorator calculate_time.
- When a function with this decorator is called, it should print: "Function function_name took X.XXXX seconds to execute."

3) (Optional Challenge) Secure Function Calls:
- Create a decorator secure_function.
- This decorator should ask for a password before running the function.
- If the password is correct, it should proceed with the function execution; otherwise, it should print "Access Denied."

# Example:
- Log Function Calls:
For a function named example_function, it should print: "Function example_function called."

- Time Calculation:
For the same function, if it took 2.5 seconds to execute, it should print: "Function example_function took 2.5000 seconds to execute."

- (Optional Challenge) Secure Function Calls:
On calling a secured function, it should prompt: "Enter the password to 
run the function:"
If the password is "secure123", proceed; otherwise, print "Access Denied."

# Requirements:
1)  Use decorators to achieve logging and timing.
2) Do not modify the original function's behavior outside of the added functionality.
3) Ensure that decorators can be applied to any function and will function as described.