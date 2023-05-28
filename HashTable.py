hash = {}

while True:
    menu = ("""1) Add
2) Exit""")
    print(menu)
    option = input("Chose option:")
    if option == '1':
        key_input = input("Key: ")
        value_input = input("Value: ")

        hash[key_input] = value_input
    elif option == '0':
        break

print("Content:")
for key_input, value_input in hash.items():
    print(f"Key: {key_input} - Value: {value_input}")