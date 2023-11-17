# factoriel 

x = int(input("enter the number you wanna see it fact"))

def fact(number, total):
        if number == 1: 
            total = 1
        else: 
            if number %2 == 0:
                    while number != 2:
                        total = total * (number * (number - 1))
                        number = number - 2
                    total = 2 * total
            else:
                 while number != 1:
                    total = total * (number * (number - 1))
                    number = number - 2
        return total    

result = fact(x, 1)
print(f"fact of your number is {result}")