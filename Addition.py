# program to prompt for 8 numbers and report the total to the user
count = 0
total = 0

while count <=7:
    count = count + 1
    num = int(input("Please enter a number:  "))
    total = total+num
              

print('The total is {0}'.format(total))


