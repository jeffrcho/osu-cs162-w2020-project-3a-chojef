# Author: Jeffrey Cho
# Date: 1/14/2020
#Description: Write a program that asks the user how many integers they would like to enter. You can
# assume that this initial input will be an integer >= 1. The program will then prompt the user to
# enter that many integers. After all the numbers have been entered, the program should display the
# largest and smallest of those numbers



print('How many integers would you like to enter?')
volume = int(input())
print('Please enter', volume, 'integers.')
min = int(input())
max = min
for i in range(1, volume):
    num_total = int(input())
    if num_total < min:
        min = num_total
    if num_total > max:
        max = num_total
print('min:', min)
print('max:', max)




