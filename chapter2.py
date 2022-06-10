"""
Exercise: 35
"""

# number = int(input('enter any no: '))
# if number % 2 == 0:
#     print(number, "is an even number")
# else:
#     print(number, 'is an odd number')

"""
Exercise: 36
"""
# years = int(input('enter the no. of years: '))
# two_years = 10.5
# three_to_so_on = 4
# if years == 2:
#     print('eqvilant dog years are 21')
# if years > 2:
#     human_years = 21 + (years - 2) * 4
#     print(human_years)

"""
Exercise: 37
"""
# letter = input('enter any letter you want: ')
#
# if letter == 'a' or letter == 'e' or letter == 'i' or letter == '0' or letter == 'u':
#     print('the entered letter is vowel')
# elif letter == 'y':
#     print('the entered letter is sometimes vowel sometimes constant')
# else:
#     print('the entered letter is constant')

"""
Exercise: 38
"""
# n = int(input('enter the no of sides of your shape: '))
#
# if n == 3:
#     print('your shape is triangle')
# elif n == 4:
#     print('your shape is square')
# elif n == 5:
#     print("your shape is pentagon")
# elif n == 6:
#     print('your shape is hexagon')
# elif n == 7:
#     print('your shape is heptagon')
# elif n == 8:
#     print('your shape is octagon')
# elif n == 9 :
#     print('your shape is nonagon')
# elif n == 10 :
#     print('your shape is decagon')
# else:
#     print('enter appropriate positive no of side greater than 2 and less than 11')

"""
Exercise: 39
"""

# month_name = input('Enter The Name of Month: ')
# days = "31"
# dayss = "30"
#
# if month_name == "January" or month_name == "March" \
#         or month_name == "May" or month_name == "July" \
#         or month_name == "August" or month_name == "October" \
#         or month_name == "December":
#     print("there are", days, "days in ", month_name, "month")
#
# elif month_name == "April" or \
#         month_name == "June" or month_name == "September" \
#         or month_name == "November":
#     print("there are", dayss, "days in ", month_name, "month")
#
# elif month_name == "February":
#     print('February has 28 or 29 days')
#
#

"""
Exercise: 40
Jackhammer 130 dB
Gas Lawnmower 106 dB
Alarm Clock 70 dB
Quiet Room 40 dB
"""
# level = int(input("enter the sound level in decibel: "))
#
# if level == 130:
#     print('the noise is of Jackhammer')
# elif level == 106:
#     print('the noise is Gas Lawnmower')
# elif level == 70:
#     print("the noise is of Alarm Clock")
# elif level == 40:
#     print("the noise is of quiet room")
# elif level in range(106, 131):
#     print('the noise is bw range of lawnmower and Jackhammer')
# elif level in range (40, 71):
#      print("the noise is bw range of Quiet room and alarm clock")
# elif level < 40:
#     print('this noise level is below the quietest level of noise ')
# elif level > 130:
#     print('the noise level is above the greatest noise ')

"""
Exercise 41: Classifying Triangles
"""

# length_a, length_b, length_c = input('enter the length of 3 sides of triangle: ').split()
# if length_a == length_b == length_c:
#     print("Its an equilateral triangle")
# elif length_a == length_b or length_b == length_c or length_c == length_a:
#     print("its and isosceles triangle")
# else:
#     print("its a scalene triangle")


"""
Exercise: 42
"""
#
# C4_FREQ = 261.63
# D4_FREQ = 293.66
# E4_FREQ = 329.63
# F4_FREQ = 349.23
# G4_FREQ = 392.00
# A4_FREQ = 440.00
# B4_FREQ = 493.88
#
# name = input("Enter the two character note name, such as C4: ")
# note = name[0]
# octave = int(name[1])
# if note == "C":
#     freq = C4_FREQ
# elif note == "D":
#     freq = D4_FREQ
# elif note == "E":
#     freq = E4_FREQ
# elif note == "F":
#     freq = F4_FREQ
# elif note == "G":
#     freq = G4_FREQ
# elif note == "A":
#     freq = A4_FREQ
# elif note == "B":
#     freq = B4_FREQ
#
# frequency = freq / 2 ** (4 - octave)
# print("The frequency of", name, "is", frequency)

"""
Exercise: 43
"""

"""
Exercise:44
"""

# one = "George Washington"
# two = 'Thomas Jefferson'
# five = 'Abraham Lincoln'
# ten = 'Alexander Hamilton'
# twenty = 'Andrew Jackson'
# fifty = 'Ulysses S.Grant'
# hundred = 'Benjamin Franklin'
#
# denomination = input("enter the note denomination: ")
# if denomination == "$1":
#     print(one)
# elif denomination == "$2":
#     print(two)
# elif denomination == "$5":
#     print(five)
# elif denomination == "$10":
#     print(ten)
# elif denomination == "$20":
#     print(twenty)
# elif denomination == "$50":
#     print(fifty)
# elif denomination == "$100":
#     print(hundred)
# else:
#     print("Sorry, enter the correct note denomination")

"""
Exercise: 45
"""
# January_1 = 'New Year’s Day'
# July_1 = 'Canada Day'
# December_25 = 'Christmas Day'
#
# user_input = input("enter the month name and date: ")
# if user_input == "1 January":
#     print(January_1)
# elif user_input == " 1 July":
#     print(July_1)
# elif user_input == "25 December":
#     print(December_25)
# else:
#     print("sorry there is no holiday on your entered day and month")

"""
Exercise: 46
"""
# x = list(input('enter the position: '))
# col = ''
#
# if x[0] in ['a', 'c', 'e', 'g']:
#     if int(x[1]) % 2 == 0:
#         col = 'white'
#     else:
#         col = 'black'
# elif x[0] not in ['a', 'c', 'e', 'g']:
#     if int(x[1]) % 2 == 0:
#         col = 'black'
#     else:
#         col = 'white'
#
# print(col)

"""
Exercise: 47
"""


# Spring March_20
# Summer June 21
# Fall September 22
# Winter December 21
#
# month = input('enter the month name: ')
# date = int(input('enter the date of month: '))
# season = ''
#
# if month in 'jan, feb' or (month == 'dec' and date >= 21):
#     season = 'winter'
# else:
#     season = "spring"
#
# if month in 'july, august' or (month == 'june' and date >= 21):
#     season = 'summer'
# else:
#     season = 'spring'
#
# if month in 'oct, nov' or (month == 'sept' and date >= 22):
#     season = 'autumn'
# else:
#     season = 'summer'
#
# if month in 'april, may' or (month == 'march' and date >= 20):
#     season = 'spring'
# else:
#     season = 'winter'
#
# print(season)
"""
Exercise: 48
"""
# birth_month = input('enter your birth month: ')
# birth_date = int(input('enter your birth date: '))
#
# if birth_month == 'dec' and birth_date >= 22 or birth_month == 'jan' and birth_date <= 19:
#     print('capricorn')
# elif birth_month == 'jan' and birth_date >= 20 or birth_month == 'feb' and birth_date <= 18:
#     print('Aquarius')
# elif birth_month == 'feb' and birth_date >= 19 or birth_month == 'march' and birth_date <= 20:
#     print('Pisces')
# elif birth_month == 'march' and birth_date >= 21 or birth_month == 'april' and birth_date <= 19:
#     print('Aries')
# elif birth_month == 'march' and birth_date >= 21 or birth_month == 'april' and birth_date <= 19:
#     print('Aries')
# elif birth_month == 'april' and birth_date >= 20 or birth_month == 'may' and birth_date <= 20:
#     print('Taurus')
# elif birth_month == 'may' and birth_date >= 21 or birth_month == 'june' and birth_date <= 20:
#     print('Gemini')
# elif birth_month == 'june' and birth_date >= 21 or birth_month == 'july' and birth_date <= 22:
#     print('Cancer')
# elif birth_month == 'july' and birth_date >= 23 or birth_month == 'aug' and birth_date <= 22:
#     print('leo')
# elif birth_month == 'aug' and birth_date >= 23 or birth_month == 'sep' and birth_date <= 22:
#     print('virgo')
# elif birth_month == 'sep' and birth_date >= 23 or birth_month == 'oct' and birth_date <= 22:
#     print('libra')
# elif birth_month == 'oct' and birth_date >= 23 or birth_month == 'nov' and birth_date <= 21:
#     print('scorpio')
# else:
#     print('sagittarius')

"""
Exercise: 49
"""
# year = int(input('enter the year: '))
#
# if year % 12 == 8:
#     print('Dragon')
# elif year % 12 == 9:
#     print('snake')
# elif year % 12 == 10:
#     print('horse')
# elif year % 12 == 11:
#     print('sheep')
# elif year % 12 == 0:
#     print('monkey')
# elif year % 12 == 1:
#     print('rooster')
# elif year % 12 == 2:
#     print('dog')
# elif year % 12 == 3:
#     print('pig')
# elif year % 12 == 4:
#     print('rat')
# elif year % 12 == 5:
#     print('ox')
# elif year % 12 == 6:
#     print('tiger')
# elif year % 12 == 7:
#     print('hare')

"""
Exercise: 50
"""
# elif mag == 2.0 or mag < 3.0:
# mag = float(input('enter the magnitude of earth quick: '))
#
# if mag < 2:
#     print('micro')
# elif mag == 2.0 or mag < 3.0:
#     print('very minor')
# elif mag == 3.0 or mag < 4.0:
#     print('minor')
# elif mag == 4.0 or mag < 5.0:
#     print('light')
# elif mag == 5.0 or mag < 6.0:
#     print('moderate')
# elif mag == 6.0 or mag < 7.0:
#     print('strong')
# elif mag == 7.0 or mag < 8.0:
#     print('major')
# elif mag == 8.0 or mag < 10.0:
#     print('great')
# elif mag > 10.0:
#     print('meteoric')
#

"""
Exercise: 51
"""
# from math import sqrt
#
# a = int(input('enter non-zero value of a: '))
# b = int(input('enter the value of b: '))
# c = int(input('enter the value of c: '))
#
# D = (b ** 2) - (4 * a * c)
# dis = sqrt(D)
# if D == 0:
#     root = (-b) / (2 * a)
#     print(root, ' has 1 real root')
# elif D > 0:
#     ps = (-b) + dis
#     neg = (-b) - dis
#     post = ps / (2*a)
#     negv = neg / (2 *a)
#     print('it has 2 real roots with', round(post, 2), 'and', round(negv, 2), 'values')
# elif D < 0:
#     print('it has no real roots')

"""
Exercise 52
"""

# grade = input('enter the your letter grade: ')
# if grade == 'A+' or 'A':
#     print('you got 4.0')
# elif grade == 'A-':
#     print('you got 3.7')
# elif grade == 'B+':
#     print('you got 3.3')
# elif grade == 'B':
#     print('you got 3.0')
# elif grade == 'B-':
#     print('2.7')
# elif grade == 'C+':
#     print('you got 2.3')
# elif grade == 'C':
#     print('2.0')
# elif grade == 'C-':
#     print('you got 1.7')
# elif grade == 'D+':
#     print('you got 1.3')
# elif grade == 'D':
#     print('you got 1.0')
# elif grade == 'F' :
#     print('you got 0')

"""
Exercise: 53
"""

# """
# 1xt method
# solved by converting points in integers as range doesnt work in float
# """
# points = float(input('enter the grade points: '))
# in_int = points * 10
#
# if in_int == 40 or points > 40:
#     print('You Got A and A+ grade')
# elif in_int in range(37, 39):
#     print('you got  A- grade')
# elif in_int in range(33, 37):
#     print('you got B+ grade')
# elif in_int in range(30, 33):
#     print('you got B grade')
# elif in_int in range(27, 30):
#     print('you got B- grade')
# elif in_int in range(23, 27):
#     print('you got C+ grade')
# elif in_int in range(20, 23):
#     print('you got C grade')
# elif in_int in range(17, 20):
#     print('you got C- grade')
# elif in_int in range(13, 17):
#     print('you got D+ grade')
# elif in_int in range(10, 13):
#     print('you got D grade')
# elif in_int in range(0, 10):
#     print('you got F grade')
#
#
# """
# 2nd solution
# """
#
# points = float(input('enter the grade points: '))
#
# if points == 4.0 or points > 4.0:
#     print('You Got A and A+ grade')
# elif 3.7 <= points <= 3.9:
#     print('You Got A- grade')
# elif 3.3 <= points <= 3.6:
#     print('you got B+ grade')
# elif 3.0 <= points <= 3.2:
#     print('you got B grade ')
# elif 2.7 <= points <= 2.9:
#     print('you Got B- grade')
# elif 2.3 <= points <= 2.6:
#     print('you got C+ grade')
# elif 2.0 <= points <= 2.2:
#     print('you got C grade')
# elif 1.7 <= points <= 1.9:
#     print('you got C- grade')
# elif 1.3 <= points <= 1.6:
#     print('you got D+ grade')
# elif 1.0 <= points <= 1.2:
#     print('you got D grade')
# elif 0 <= points <= 0.9:
#     print('you Got F grade')
#

"""
Exercise: 54
"""

# rating = float(input('enter your rating as either 0.0 or 0.4 , 0.6 or greater: '))
# increment = rating * 2400
#
# if rating == 0.0:
#     print('your rating is unacceptable and u did not get any raise')
# elif rating == 0.4:
#     print('your rating shows acceptable performance and you got $%.2f' % increment, 'raise')
# elif rating >= 0.6:
#     print('your rating shows that you have meritorious performance and you got $%.2f' % increment, 'raise')
#
# else:
#     print('Error! kindly enter from given ratings')
#

"""
Exercise: 55
 """
# wave = int(input('enter the wave length of visible light: '))
# if wave  in range(380, 451):
#     print('its violet')
# elif wave in range(450, 496):
#     print('its blue')
# elif wave in (495, 571):
#     print('green')
# elif wave in range(570, 591):
#     print('yellow')
# elif wave in range(590, 621):
#     print('orange')
# elif wave in range(620, 751):
#     print('red')
# else:
#     print('enter the appropriate wavelength')
#

"""
Exercise: 56
"""
#
# freq = int(float(input('enter the frequency of the radiation: ')))
# if freq < 3e9:
#     print('Radio waves')
# elif freq >= 3E9 and freq < 3E12:
#     print('Micro waves')
# elif freq >= 3e12 and freq < 4.3e14:
#     print('Infrared Light')
# elif freq >= 4.3e14 and freq < 7.5e14:
#     print('Visible Light')
# elif freq >= 7.5e14 and freq < 3e17:
#     print('Ultraviolet light')
# elif freq >= 3e17 and freq < 3e19:
#     print('X-Rays')
# elif freq >= 3e19:
#     print('Gamma Rays')

"""
Exercise: 57
"""
# user_input = input('enter f if you want to get bill of your additional minutes and messages other wise enter e: ')
# base_pkg = 15.00
# per_mint = 0.25
# per_text = 0.15
# call_center = 0.44
# if user_input == 'f':
#     extra_mint = int(input('enter the additional minutes: '))
#     extra_msgs = int(input('enter the additional text messages: '))
#     print('cost of your additional minutes is %.2f' % (extra_mint * 0.25), '\ncost of additional text messages is %.2f'
#           % (extra_msgs * 0.15))
# else:
#     mints = int(input('enter the number of mints: '))
#     txt = int(input('enter the number of msgs: '))
#     add_mint = (mints - 50) * 0.25
#     add_txt = (txt -50) * 0.15
#     total = base_pkg + call_center + add_mint + add_txt
#     tax = (total * 5)/ 100
#     grand = tax + total
#     if mints > 50 and txt > 50:
#         print('you have', (mints - 50), 'extra minutes\n',(txt - 50),
#               'extra text messages\n''cost of your additional minutes is %.2f' % (
#                (mints - 50) * 0.25),'\n cost of additional text messages is %.2f'
#               % ((txt - 50) * 0.15), '\n your total bill is %.2f' % grand)
#     elif mints == 50 and txt == 50:
#         print('your total bill is 16.19')


"""
Exercise: 58
"""
# year = int(input('enter the year: '))
#
# if year % 400 == 0 and year % 4 == 0 :
#     print('its a leap year')
# elif year % 100 == 0:
#     print('its not a leap year')
# else:
#     print('not leap year')

"""
Exercise: 59
"""
# date = int(input('enter the date: '))
# month = int(input('enter the month: '))
# year = int(input('enter the year: '))
#
# x = (1, 3, 5, 7, 10)
# y = (4, 6, 8, 9, 11)
# if month in x and date == 31:
#     month = month + 1
#     date = 1
#
# elif month in x and date < 31:
#     date = date + 1
#
# elif month in y and date == 30:
#     month = month + 1
#     date = 1
#
# elif month in y and date < 31:
#     date = date + 1
#
# elif month == 2 and date == 28 or date == 29:
#     month = month+1
#     date = 1
#
# elif month == 2 and date < 29:
#     date = date+1
#
# elif month == 12 and date < 31:
#     date = date + 1
#
# elif month == 12 and date == 31:
#     month = 1
#     date = 1
#     year = year + 1
#
# print('%02d-' % date, '%02d-' % month, '%02d' % year)


# import datetime
# from datetime import timedelta
#
# d = int(input('enter the day: '))
# m = int(input('enter the month: '))
# y = int(input('enter the year: '))
#
# today = datetime.date(y, m, d)
# tom = today + timedelta(days=1)
# print('next day is', tom)

"""
Exercise: 60
"""
# from math import floor
#
# year = int(input('enter the year: '))
# day = (year + floor(year - 1) / 4 - floor(year - 1) / 100 + floor((year - 1) / 400)) % 7
# print(day)
# z = int(day)
#
# x = ['sunday', 'monday', 'tuesday', 'wed', 'thu', 'fri', 'sat']
# print(x[z])

"""
Exercise: 61
"""
#
# plate = str(input('enter your number plate: '))
#
# if len(plate) == 6 and \
#         "A" <= plate[0] <= "Z" and \
#         "A" <= plate[1] <= "Z" and \
#         "A" <= plate[2] <= "Z" and \
#         "0" <= plate[3] <= "9" and \
#         "0" <= plate[4] <= "9" and \
#         "0" <= plate[5] <= "9":
#     print("The plate is a valid older style plate.")
# elif len(plate) == 7 and \
#         "0" <= plate[0] <= "9" and \
#         "0" <= plate[1] <= "9" and \
#         "0" <= plate[2] <= "9" and \
#         "0" <= plate[3] <= "9" and \
#         "A" <= plate[4] <= "Z" and \
#         "A" <= plate[5] <= "Z" and \
#         "A" <= plate[6] <= "Z":
#     print("The plate is a valid newer style plate.")
# else:
#     print("The plate is not valid.")

"""
Exercise: 62
"""
# from random import randrange
#
# red = [1, 3, 5, 7, 9, 12, 14,16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
# black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
# green = [0, 00]
#
# bet = randrange(0, 37)
# print('The Spin resulted in: ', bet, '\npay', bet)
# if bet in red:
#     print('Pay Red')
# if bet in black:
#     print('Pay Black')
# if bet in green:
#     print('Pay Green')
# if bet % 2 == 0:
#     print('Pay Even')
# else:
#     print('Pay Odd')
# if bet in range(1, 19):
#     print('pay 1 to 18')
# if bet in range(19, 37):
#     print('Pay 9 to 36')
# if bet == 37:
#     print('Spin resulted in 00\nPay 00')
