number = int(input("Enter the size of the pattern: "))

outer_counter = 0
inner_counter = 0

while outer_counter < number:
    while inner_counter < number:
        print("*", end="")
        inner_counter += 1
    print()
    inner_counter = 0
    outer_counter += 1
