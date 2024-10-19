class runcodes:

    def forloops():
        for x in range(1,21):
            if x == 13:
                break
            else:
                print(x, end=" ")
        print("woahhh")

    def whileloops():
        n = 5
        while n > 0:
            print(n)
            n -= 1
        print('Blastoff!')

    def whileloops2():
        loop_variable = 1
        while (loop_variable <= 4):
            print("Name")
            print("Surname")
            loop_variable += 1

    def whileloops3():
        found = False
        print('Before', found)
        for value in [9, 41, 12, 3, 74, 15]:
            if value == 3:
                found = True
            print(found, value)
        print('After', found)

    def forinfor():
        fruits = ["apple", "pear", "banana", "coconut"]
        vegetables = ["celery", "carrots", "potatoes"]
        meats = ["chicken", "fish", "turkey"]
        groceries = [fruits, vegetables, meats]

        for collection in groceries:
            for food in collection:
                print(food, end=" ")
            print()

a = runcodes
a.forloops()