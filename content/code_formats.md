# Code Formats for LTR Dictation

## Basic Syntax Elements

### Variables
```python
variable_name = value
```

### Functions
```python
def function_name(parameter1, parameter2):
    # Function body
    return result
```

### Classes
```python
class ClassName:
    def __init__(self, parameter):
        self.parameter = parameter
    
    def method_name(self):
        # Method body
        pass
```

### Control Structures
```python
# If statement
if condition:
    # Code block
elif another_condition:
    # Code block
else:
    # Code block

# For loop
for item in sequence:
    # Code block

# While loop
while condition:
    # Code block
```

### Comments
```python
# Single line comment

"""
Multi-line
comment
"""
```

## Data Structures

### Lists
```python
my_list = [item1, item2, item3]
```

### Tuples
```python
my_tuple = (item1, item2, item3)
```

### Dictionaries
```python
my_dict = {
    'key1': 'value1',
    'key2': 'value2'
}
```

### Sets
```python
my_set = {item1, item2, item3}
```

## Common Operations

### String Operations
```python
# String concatenation
result = "Hello" + " " + "World"

# String formatting
result = f"Hello {name}"

# String methods
string.upper()
string.lower()
string.strip()
```

### List Operations
```python
# Adding elements
my_list.append(item)
my_list.extend(another_list)

# Removing elements
my_list.remove(item)
my_list.pop(index)

# List comprehension
new_list = [x for x in old_list if condition]
```

### Dictionary Operations
```python
# Adding/updating
my_dict['new_key'] = 'new_value'

# Removing
del my_dict['key']
my_dict.pop('key')

# Dictionary comprehension
new_dict = {k: v for k, v in old_dict.items() if condition}
```

## Error Handling
```python
try:
    # Code that might raise an exception
except ExceptionType as e:
    # Handle exception
finally:
    # Cleanup code
```

## File Operations
```python
# Reading
with open('file.txt', 'r') as file:
    content = file.read()

# Writing
with open('file.txt', 'w') as file:
    file.write(content)
```

## Import Statements
```python
# Single import
import module_name

# Specific import
from module_name import specific_function

# Alias import
import module_name as alias
```

## Decorators
```python
@decorator_name
def function_name():
    # Function body
    pass
```

## Context Managers
```python
with context_manager() as variable:
    # Code block
```

## Type Hints
```python
def function_name(param1: type1, param2: type2) -> return_type:
    # Function body
    pass
``` 