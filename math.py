#any time question gives you numbers for x + y and x * y and wants x ** 3 + y ** 3:
sumInput = input("Enter the sum of numbers: ")
multInput = input("Enter the multiple of numbers: ")
def result(sum, mult):
  return  (sum ** 3) - (3 * mult * sum)

print(result(sumInput, multInput))


