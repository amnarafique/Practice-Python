"""In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and two digits to the right of the decimal point."""

# oneL, twoL = input('enter the no of bottles you have of 1L or less and more than 1L ').split()
# oneLcash = int(oneL) * 0.25
# twolLcash = int(twoL) * 0.10
# print('you have', oneL, '1L bottles and your total deposit is $', oneLcash.__round__(2),
#       '\nyou have', twoL, ' 2L bottles and your total deposit is $', twolLcash.__round__(2),
#       '\nyour total deposit is', oneLcash + twolLcash)
#


# size = float(input('enter the size of your bottles'))
# total1 = no * 0.10
# total2 = no * 0.25
# if size <= 0.5 :
#     print("your total deposit is $", total1)
#     if size > 0.5:
#         print('your total depoist is $', total2,  end="")
# else:
#     print('check your input again')

# amna = int(input('amna enter your age'))
#
# if amna < 12:
#     print('she is child')
# else:
#     print('amna is adult')
import time

"""
The program that you create for this exercise will begin by reading the cost of a meal
ordered at a restaurant from the user. Then your program will compute the tax and
tip for the meal. Use your local tax rate when computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount (without the tax). The output from
your program should include the tax amount, the tip amount, and the grand total for
the meal including both the tax and the tip. Format the output so that all of the values
are displayed using two decimal places.
"""

# meal = int(input('enter the cost of your meal'))
# meal_tax = meal / 10
# tip = (18/100)* meal
# total_bill = meal + meal_tax + tip
# print("your total check  is ", total_bill.__round__(2), '\nincluding 10% meal tax which accounts for ', meal_tax.__round__(2),
#       '\nand tip of', tip.__round__(2), 'rupees')

"""
Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula:
sum =(n)(n + 1)
        2
"""

# n = int(input('enter any one number'))
# sum = n * (n+1)/2
# print(sum)

"""
Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added to the
balance of the savings account. Write a program that begins by reading the amount of
money deposited into the account from the user. Then your program should compute
and display the amount in the savings account after 1, 2, and 3 years. Display each
amount so that it is rounded to 2 decimal places."""
#
# balance = int(input('enter the cuurent balance of your account'))
# interest = (4/100)*balance
# one_year = balance + interest
# two_year = balance + (interest*2)
# three_year = balance + (interest*3)
# print('your total balance after year is ', one_year.__round__(2),
#       "\nyour total balace after 2 years is", two_year.__round__(2),
#       "\nyour total balance after 3 years is ", three_year.__round__(2))


"""
The surface of the Earth is curved, and the distance between degrees of longitude
varies with latitude. As a result, finding the distance between two points on the surface
of the Earth is more complicated than simply using the Pythagorean theorem.
Let (t 1 , g 1 ) and (t 2 , g 2 ) be the latitude and longitude of two points on the Earth’s
surface. The distance between these points, following the surface of the Earth, in
kilometers is:
distance = 6371.01 × arccos(sin(t 1 ) × sin(t 2 ) + cos(t 1 ) × cos(t 2 ) × cos(g 1 − g 2 ))
The value 6371.01 in the previous equation wasn’t selected at random. It is the
average radius of the Earth in kilometers.
Create a program that allows the user to enter the latitude and longitude of two
points on the Earth in degrees. Your program should display the distance between
the points, following the surface of the earth, in kilometers.
Hint: Python’s trigonometric functions operate in radians. As a result, you will
need to convert the user’s input from degrees to radians before computing the
distance with the formula discussed previously. The math module contains a
function named radians which converts from degrees to radians."""
#
# import math
# t1, g1, t2, g2 =input('enter t1, g1, t2, g2').split()
# T1 = math.radians(int(t1))
# T2 = math.radians(int(t2))
# G1 = math.radians(int(g1))
# G2 = math.radians(int(g2))
#
#
# distance = 6371.01 * math.acos(math.sin(T1) * math.sin(T2) + math.cos(T1) * math.cos(T2) * math.cos(G1 - G2))
# print('disctance bw two points is', distance)


""" Consider the software that runs on a self-checkout machine. One task that it must be
able to perform is to determine how much change to provide when the shopper pays
for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an
integer. Then your program should compute and display the denominations of the
coins that should be used to give that amount of change to the shopper. The change
should be given using as few coins as possible. Assume that the machine is loaded
with pennies, nickels, dimes, quarters, loonies and toonies.
A one dollar coin was introduced in Canada in 1987. It is referred to as a loonie
because one side of the coin has a loon (a type of bird) on it. The two dollar
coin, referred to as a toonie, was introduced 9 years later. It’s name is derived
from the combination of the number two and the name of the loonie."""

# total_bill = input('kindly enter your total shopped cost in cents')
# amt_given = input('enter the total amount of money you paid in cents')
# amount_returned = int(amt_given) - int(total_bill)
# print(amount_returned)
# peeny = "1 cent"
# nickle = "5 cents"
# dime = "10 cents"
# quarters = "25 cents"
# loonies = "100 cents"
# toonies = "200 cents"
#
# if amount_returned <= 0:
#     print('enter positive integer')
# else:
#     toonies = amount_returned // 200
#     loonies = (amount_returned % 200) // 100
#     quarters = (amount_returned % 200 % 100) // 25
#     dime = (amount_returned % 200 % 100 % 25)//10
#     nickle = (amount_returned % 200 % 100 % 25 % 10) // 5
#     peeny = amount_returned % 5
#     print('the no of coins for', amount_returned, 'cents are\n toonies', toonies, '\n loonies', loonies, '\n quarters', quarters, '\n dime', dime,'\n nickle', nickle,'\npeenies',peeny)

"""
Exercise 14: Height Units
(Solved, 16 Lines)
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.
Hint: One foot is 12 inches. One inch is 2.54 centimeters"""
#
# height_in_feet, inch = input('enter your height in feet and inches').split()
# feet_to_inch = int(height_in_feet) * 12
# inch_to_cm = int(inch) * 2.54
# feet_to_cm = int(feet_to_inch) * 2.54
# total_height = feet_to_cm + inch_to_cm
# print('your height in cm is', total_height)


"""Exercise 15: Distance Units
(20 Lines)
In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don’t have them memorized."""
#
# feet = int(input('enter your distance in feet'))
# in_inc = feet * 12
# in_yards = feet / 3
# in_miles = feet * 1760
# print('your distance in inches is:', in_inc , 'inches\n'
#       'your distance in yards is:',in_yards,'yards\n'
#       'your distance in miles is:' , in_miles, 'miles')

"""
Exercise 16: Area and Volume
(15 Lines)
Write a program that begins by reading a radius, r, from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r. Use the pi constant in the math module in your
calculations.
Hint: The area of a circle is computed using the formula area = πr 2. The
volume of a sphere is computed using the formula volume = 4
3πr 3.
"""
# import math
#
# radius = int(input('enter the radius'))
# area_formula = math.pi * radius * 2
# vol_formula = (4/3) * math.pi * (radius) *3
# print(area_formula, vol_formula)

"""
Exercise 17: Heat Capacity
(Solved, 23 Lines)
The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material’s specific heat capacity, C. The total amount
of energy, q, required to raise m grams of a material by ΔT degrees Celsius can be
computed using the formula:
q = mCΔT
Write a program that reads the mass of some water and the temperature change from
the user. Your program should display the total amount of energy that must be added
or removed to achieve the desired temperature change.
Hint: The specific heat capacity of water is 4.186 J
g◦C. Because water has a
density of 1.0 grams per milliliter, you can use grams and milliliters interchangeably in this exercise.
Extend your program so that it also computes the cost of heating the water. Electricity is normally billed using units of kilowatt hours rather than Joules. In this
exercise, you should assume that electricity costs 8.9 cents per kilowatt hour. Use
your program to compute the cost of boiling the water needed for a cup of coffee.
Hint: You will need to look up the factor for converting between Joules and
kilowatt hours to complete the last part of this exercise."""
#
# mass = int(input('enter the mass of water'))
# temp = int(input('enter the temp change'))
# c = 4.186
# energy = mass * c * temp
# print('the total energy is:', energy)
#
#
# units_of_electricity_in_cup_boioling = 24
# cost_per_unit = 9
# bill = int(units_of_electricity_in_cup_boioling) * int(cost_per_unit)
# bill_in_joules = int(bill) * 3.6e6
# print('the total billing cost is:', bill_in_joules)

"""Exercise 18: Volume of a Cylinder
(15 Lines)
The volume of a cylinder can be computed by multiplying the area of its circular
base by its height. Write a program that reads the radius of the cylinder, along with
its height, from the user and computes its volume. Display the result rounded to one
decimal place."""

# import math
#
# rad = int(input('enter the radius'))
# height = int(input('enter the height'))
# area_of_circle = math.pi * rad * 2
# vol = area_of_circle * height
# print(round(vol, 2))

"""Exercise 19: Free Fall
(Solved, 15 Lines)
Create a program that determines how quickly an object is travelling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0 m/s. Assume that the acceleration
due to gravity is 9.8 m/s2. You can use the formula vf =

v2
i + 2ad to compute the
final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known. 
"""
# import math
#
# height = int(input('enter the height in meters'))
# acc = 9.8
# v = math.sqrt(2*acc*height)
# print(v)

"""
Exercise 20: Ideal Gas Law
"""

# p = 20000000
# v = 12
# R = 8.314
# T = 20 + 273.15
# a = (p*v)
# b = (R*T)
# formula = a/b
# print(formula)


"""Exercise 21: Area of a Triangle
(13 Lines)
The area of a triangle can be computed using the following formula, where b is the
length of the base of the triangle, and h is its height:
area = b × h
2
Write a program that allows the user to enter values for b and h. The program should
then compute and display the area of a triangle with base length b and height h."""
#
# length = int(input('enter the length of triangle'))
# height = int(input('enter the height of triangle'))
# formula =(length * height) / 2
# print('the area of yoyr triangle is:',formula)

"""Exercise 22: Area of a Triangle (Again)
(16 Lines)
In the previous exercise you created a program that computed the area of a triangle
when the length of its base and its height were known. It is also possible to compute
the area of a triangle when the lengths of all three sides are known. Let s1, s2 and s3
be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle
can be calculated using the following formula:
area =
s × (s − s1) × (s − s2) × (s − s3)
Develop a program that reads the lengths of the sides of a triangle from the user and
displays its area
"""

# import math
#
# s1 = int(input("enter the s1"))
# s2 = int(input("enter the s2"))
# s3 = int(input("enter the s3"))
# s = (s1+s2+s3)/2
# print(s)
# s11 = s-s1
# s22 = s-s2
# s33 = s-s3
#
# area = s * s11 * s22 * s33
# a = math.sqrt(area)
# print(a)

"""
Exercise 23: Area of a Regular Polygon
"""

# from math import tan, pi
#
# s = int(input('enter the length'))
# n = int(input('enter the no of sides'))
# area = (n * s**2) / (4 * tan(pi / n))
# print(area)

"""
Exercise 24: Units of Time
(22 Lines)
Create a program that reads a duration from the user as a number of days, hours,
minutes, and seconds. Compute and display the total number of seconds represented
by this durationn
"""
# days = int(input('enter the no of days'))
# days_to_sec = days * 86400
# hours = int(input('enter no of hours'))
# hours_to_sec = hours * 3600
# minutes = int(input('enter the no of minutes'))
# mint_to_sec = minutes * 60
# seconds = int(input('enter the no of sec'))
# duration_in_sec = days_to_sec + hours_to_sec + mint_to_sec + seconds
# print(duration_in_sec)

"""
Exercise 25: time change again
"""
#
# sec_in_day = 86400
# sec_in_hour = 3600
# sec_in_min = 60
#
# time = int(input('enter the total seconds'))
#
# days = time // sec_in_day
# day1 = time % sec_in_day
# hours = day1 // sec_in_hour
# hour1 = day1 % sec_in_hour
# minutes = hour1 // sec_in_min
# mint1 = hour1 % sec_in_min
# seconds = mint1 % 60
#
# print("%02d" % days, "%02d" % hours, "%02d" % minutes, "%02d" % seconds)

#
"""
Exercise 26: Current Time
"""

# import time
#
# t = time.localtime()
# time.asctime(t)
# print(t)

"""
Exercise 28: Body Mass Index
"""

# height = int(input('enter your height in inches'))
# weight = int(input('enter your weight'))
# BMI = (weight) / (height*height) * 703
# print(BMI)

"""
Exercise 30: Celsius to Fahrenheit and Kelvin
"""

# temp = int(input('enter your temp in degree celsius'))
#
# kelvin = temp + 273.15
# print('your temp in kelvin is:', kelvin)
# fahrenheit = (temp * 1.8) + 32
# print('your temp in Fahrenheit is:', fahrenheit)

"""
Exercise 31: Units of Pressure
"""
#
# pressure = int(input('enter pressure in kp'))
# p_in_pounds = pressure / 6.895
# p_in_mmhg = pressure * 7.50
# p_in_atm =  pressure / 101.3
# print("pressure in pounds per square inch is",p_in_pounds, "\n"
#       "pressure in mmHg is:", p_in_mmhg, "\npressure in atm is:", p_in_atm)

"""
Exercise 32: Sum of the Digits in an Integer
"""
# n = input('enter the 4 digit number')
# sum = 0
# for i in n:
#     sum += int(i)
# print(sum)
#

"""
Exercise 33: Sort 3 Integers
"""
# n = input('enter 3 integers')
# print(sorted(n))
# a = print(max(n))
# b = print(min(n))
# sum = 0
# for i in str(n):
#     sum += int(i)
# c = print(sum)
#
# median = int(sum) - int(min(n)) - int(max(n))
# print(median)

"""
Exercise 34: Day Old Bread
"""

# bread = 3.49
# old_bread = "60% off"
# loaves_no = int(input('enter the no of loaves you purchased'))
# price = loaves_no * bread
# percentage_off = price * 0.6
#
# total_bill = price - percentage_off
# print('the price of your bread is:', price, "\nyou got", percentage_off,"discount on your bread, "
#                                                                        "\nnow your total price after discount is:", round(total_bill,2))

"""
Exercise 29: Wind Chill
(Solved, 22 Lines)
When the wind blows in cold weather, the air feels even colder than it actually is
because the movement of the air increases the rate of cooling for warm objects, like
people. This effect is known as wind chill.
In 2001, Canada, the United Kingdom and the United States adopted the following formula for computing the wind chill index. Within the formula Ta is the
air temperature in degrees Celsius and V is the wind speed in kilometers per hour.
A similar formula with different constant values can be used for temperatures in
degrees Fahrenheit and wind speeds in miles per hour.
WCI = 13.12 + 0.6215Ta − 11.37V0.16 + 0.3965TaV0.16
Write a program that begins by reading the air temperature and wind speed from the
user. Once these values have been read your program should display the wind chill
index rounded to the closest integer.
"""
# temp = int(input('enter the air temp in celsius'))
# velocity = float(input('enter the wind speed in km/h'))
# formula = (13.12 )+ (0.6215 * temp) - (11.37 * velocity ** 0.16) + ((0.3965) * temp * velocity ** 0.16)
# print('wind chill index is', round(formula))

"""
EXERCISE 27: WHEN IS EASTER
"""
from math import floor
year = int(input('enter the year'))
a = year % 19
b = floor(year / 100)
c = year % 100
d = floor(b)/4
e = b % 4
f = floor((b+8) / 25)
g = floor((b - f + 1) / 3)
hi = 19 * a + b - d - g + 15
h = hi % 30
i = floor(c)/4
k = c % 4
li = 32 + (2 * e) + (2 * i) - h - k
l = li / 7
mi = a + (11 * h) + (22 * l)
mi2 = mi /  (45 * l)
mi3 = mi / mi2
m = floor(mi3)
month1 = h + l + (7*m) + 114
month2 = 3 * l
month = floor(month1/month2)
day1 = h + l - (7 * m ) + 114
day2 = day1 % 31
day = 1 + day2

print("day", day,"and month" ,month)
