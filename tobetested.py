#With a number of numbers, the user chooses to multiply or add
nums = int(input ("Enter the numbers (q for quit) : "))

def add (*nums):
    total = 0
    for num in nums:
        total += num
    return total
def multiply (*nums):
    total = 1
    for num in nums:
        total *= num
    return total

while nums != "q":
    nums = input ("Enter another number (q for quit) :") #valuerror for q here
else:
    operation = input ("(+ for add, * for multiplication: ")
    if operation != "+" and operation != "*":
        print ("Invalid")
    elif operation == "+":
        add (nums)
    elif operation == "*":
        multiply (nums)



