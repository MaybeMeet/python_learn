'''
chenpanpan

'''
'''
magicians = ['chenpanpan','wangtiting','alice','marry']
for magician in magicians:
	print(magician + " is our guest")

for value in range(1,5):
	print(value)

num = list(range(1,1000001))
sum = sum(num)
print(sum)
'''
'''
nums = []
for value in range(1,1000000):
    num = value**2
    nums.append(num)

print(nums)
'''
'''
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
'''
''' 元组 tuple
menus = ('tomato','potato','banana scala','juice','rice')
for food in menus:
    print(food)
'''
'''
#usr if synx, we need notice not forgot the :
cars = ['audi','bwm','toyato','subaru']

for car in cars:
    if car == 'bwm':
        print(car.upper())
    else:
        print(car.title())
'''
'''
import sys
print(sys.version)
'''
'''
alien_color = 'red'

if alien_color == 'green':
    print("You got 5 degrade")
elif alien_color == 'red':
    print('you got 10 degrade')
elif alien_color == 'black':
    print('you got 15 degrade')
'''
'''
users = ['admin','chen','wang','ting','david']

for user in users:
    if user == 'admin':
        print('Hello admin,would you like to see the status report?')
    else:
        print('hello ' + user + ',thank you for logging in again.')
'''
'''

# function
def sales(grocery_store, item_on_sale, cost):
    print(grocery_store + " is selling " + item_on_sale + " for " + cost + ".")

sales("The Farmer's Market", "toothpaste", "$1")
print(sales)
'''
'''
alien_0 = {'color':'green','point':'5'}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
input('enter any key to return')
'''
'''
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
    }

for key,value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
    print(user_0.items())
'''
'''
# 有待改正，关于数据格式转换和运算符
aliens = []

for n in range(30):
    new_alien = {'alien_color':'green','point':5,'velocity':'slow','number':n}
    aliens.append(new_alien)

for alien in aliens:
    if alien['number']%3 == 0: # 数据转换和运算
        alien['alien_color'] = 'red'
        alien['point'] = 15
        alien['velocity'] = 'fast' 
print(aliens)


print("The total number of aliens is " + str(len(aliens)) + ".")
'''
'''
message = input("Enter someting and I will repeat it ： ")

print(message)
'''
'''
promt = "\nTell me someting,and I will repeat it back to you : \n(Enter 'quit' when you are finished.)"


active = True
message = ""
while active:
    message = input(promt)
    if message == "quit":
        active = False
        print("quit")
    else:
        print("\n" + message)
print("end")
'''
'''
i = 1
while i >= 1:
    print("the number is :" + str(i))
    i += 1
'''
'''
sandwich_orders = ["tuna","sour","sweet","hot"]
finished_sandwiches = []
for sandwich in sandwich_orders:
    print("I made your " + sandwich + " sandwich,")
    finished_sandwiches.append(sandwich)

print("I made those sandwiches : ")
for sandwich_type in finished_sandwiches:
    print(sandwich_type)
    '''
'''
def animal_des(animal_type,name):
    print("I have a " + animal_type)
    print("My " + animal_type + "'s name is "+ name + ".")

animal_des("cat", "tt")
'''
'''
import show

magicians = ["Alice","Colar","marry","socol"]
show.show_list(magicians)
'''
'''
class Dog():
    "an easy try"
    def __init__(self,name,age):
        "init the propety"
        self.name = name
        self.age = age

    def sit(self):
        "dog sit"
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over.")

my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

'''
'''
class Solution():
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target-num], i]
            else:
                lookup[num] = i
                nums = [2,7,11,15]
    nums = [2,7,11,15]
    target = 9
    twoSum(nums,target)
    '''
'''
def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target-num], i]
            else:
                lookup[num] = i
                nums = [2,7,11,15]
nums = [2,7,11,15]
target = 9
print(twoSum(nums,target))
'''
'''
with open('pi_digits.txt') as file_object:
    #contents = file_object.read()
    lines = file_object.readlines()
    #print(contents.rstrip())

#print("contents :" + contents)
#print("lines :" + str(lines))

for line in lines:
    print(line.rstrip())
'''
'''
file_name = "guest.txt"

with open(file_name,'a') as file_object:
    active = True
    while active:
        guest = input("Enter the guest'name : ")
        print(guest)
        if guest == "end":
            print("That's all.")
            active = False
        else:
            file_object.write(guest + "\n")
'''


def count_words(file_name):
    "count the words of the txt file"
    try:
        with open(file_name) as f_object:
            contents = f_object.read()
    except FileExistsError:
        msg = "sorry,the file " + file_name + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The book has " + str(num_words) + " words.")

file_name = "ItHappenedInJapan.txt"
count_words(file_name)