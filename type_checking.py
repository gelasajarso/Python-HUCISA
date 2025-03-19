# x = 10
# y = 3.14
# z = "HUCISA"
# a = True

variables = {
    "x": 10,
    "y": 3.14,
    "z": "HUCISA",
    "a": True
}

for name, value in variables.items():
    print(f"{name}: {type(value)}")
