import inspect
import string

def is_str(value):
    return isinstance(value, str)

for name,value in inspect.getmembers(string, is_str):
    if name.startswith('_'):
        continue
    print(f'{name}={value}')