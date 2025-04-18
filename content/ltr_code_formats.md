# قوانین نمایش فرمت کد LTR (چپ به راست)

## قوانین کلی فرمت بندی LTR

1. تمام کد باید از چپ به راست نوشته و نمایش داده شود.
2. تو رفتگی باید منظم و به سمت چپ تراز شود.
3. برای حفظ خوانایی، باید از شکست‌های خط استفاده شود.
4. نظرات باید در سمت راست کدی که توضیح می‌دهند، قرار بگیرند.

# مثال‌های بلوک کد

### Basic LTR Structure

```python
# Correct LTR format
def function_name():
    # Comment explaining the function
    return result
```

### English Section


```python
# Correct LTR format
def function_name():
    # Comment explaining the function
    return result

# Incorrect RTL format
def function_name():
    # Comment explaining the function
    return result  # Comment on the left
```

### Variable Declarations

```python
# Correct LTR format
variable_name = value  # Comment explaining the variable

# Incorrect RTL format
variable_name = value  # Comment on the left
```

### Function Calls

```python
# Correct LTR format
result = function_name(parameter1, parameter2)  # Comment explaining the call

# Incorrect RTL format
result = function_name(parameter1, parameter2)  # Comment on the left
```

### Control Structures

```python
# Correct LTR format
if condition:  # Comment explaining the condition
    # Comment explaining the block
    do_something()
elif another_condition:  # Comment explaining the condition
    do_something_else()
else:  # Comment explaining the else case
    do_default()

# Incorrect RTL format
if condition:  # Comment on the left
    do_something()
```

### Class Definitions

```python
# Correct LTR format
class ClassName:  # Comment explaining the class
    def __init__(self, parameter):  # Comment explaining the constructor
        self.parameter = parameter  # Comment explaining the attribute
    
    def method_name(self):  # Comment explaining the method
        # Comment explaining the method body
        return result

# Incorrect RTL format
class ClassName:  # Comment on the left
    def __init__(self, parameter):  # Comment on the left
        self.parameter = parameter  # Comment on the left
```

### Data Structures

```python
# Correct LTR format
my_list = [  # Comment explaining the list
    item1,  # Comment for item1
    item2,  # Comment for item2
    item3   # Comment for item3
]

my_dict = {  # Comment explaining the dictionary
    'key1': 'value1',  # Comment for key1
    'key2': 'value2'   # Comment for key2
}

# Incorrect RTL format
my_list = [  # Comment on the left
    item1,  # Comment on the left
    item2,  # Comment on the left
    item3   # Comment on the left
]
```

### Error Handling

```python
# Correct LTR format
try:  # Comment explaining the try block
    # Comment explaining the operation
    do_something()
except Exception as e:  # Comment explaining the exception
    # Comment explaining the error handling
    handle_error(e)
finally:  # Comment explaining the cleanup
    # Comment explaining the cleanup code
    cleanup()

# Incorrect RTL format
try:  # Comment on the left
    do_something()
except Exception as e:  # Comment on the left
    handle_error(e)
```

### Import Statements

```python
# Correct LTR format
import module_name  # Comment explaining the import
from package import (  # Comment explaining the imports
    function1,  # Comment for function1
    function2,  # Comment for function2
    function3   # Comment for function3
)

# Incorrect RTL format
import module_name  # Comment on the left
```
