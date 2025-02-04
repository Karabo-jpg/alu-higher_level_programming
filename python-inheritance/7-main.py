#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

# Test: check instantiation
bg = BaseGeometry()
print(dir(bg))  # Check available attributes of bg

# Test: Valid integer for integer_validator
bg.integer_validator("age", 1)
bg.integer_validator("width", 89)

# Test: Invalid string value for integer_validator
try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

# Test: Value 0 for integer_validator
try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

# Test: Negative value for integer_validator
try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

# Test: Float value for integer_validator
try:
    bg.integer_validator("height", 13.5)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

# Test: Tuple for integer_validator
try:
    bg.integer_validator("age", (4,))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

# Test: List for integer_validator
try:
    bg.integer_validator("age", [3])
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

# Test: Boolean for integer_validator
try:
    bg.integer_validator("age", True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

# Test: Set for integer_validator
try:
    bg.integer_validator("age", {3, 4})
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

# Test: None for integer_validator
try:
    bg.integer_validator("age", None)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

# Test: area() method raising exception
try:
    bg.area()
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

