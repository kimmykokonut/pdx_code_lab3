#Lab 3: Unit Converter
'''
This lab will involve writing a program that allows the user to convert a number between units.
Each version should be accomplished using a dictionary and each must be completed without the use of if/elif statements.
You do NOT need to use a while loop
'''
#Version 1: Ask user for number of feet and print equiv distance in meters
#1 ft = 0.3048m
'''
def ft2m(feet):  #attempt 1 using a function
  answer = feet * 0.3048
  return answer

ft_input = input('Provide a number in feet and I will tell you the distance in meters: ')
ft_input = float(ft_input)  

print(f'{ft_input} ft is {ft2m(ft_input)} m.')
'''
unit_conv = {       #make dictionary
  'ft to m': 0.3048,
}

ft_input = input('Provide a number in feet and I will tell you the distance in meters: ') #ask user for value
ft_input = float(ft_input) #make str to float

#print(unit_conv['ft to m']) #this equals 0.3048, value. conv factor. ft2m is 3ft*0.3048=~1
print(f"{ft_input} ft is {ft_input * unit_conv['ft to m']} m.") 
#--------------------
#Version 2. allow user to enter units. convert to meters. allow ft, mi, m, km
unit_conv = { #1x==m
  'ft': 0.3048,
  'mi': 1609.34,
  'm': 1,
  'km': 1000,
}
print('\nProvide a distance in ft, mi, m or km and I will convert to meters...') #intro
user_distance = float(input('What is the distance? ')) #user input for number
user_unit = input('What are the units? ') #user input for unit choice
print(user_distance * unit_conv[user_unit]) #distance * unit converter = m
#------------
#Version 3. add support for yards and inches
unit_conv = { #1x==m
  'ft': 0.3048,
  'mi': 1609.34,
  'm': 1,
  'km': 1000,
  'yd': 0.9144,
  'in': 0.0254,
}
print('\nProvide a distance in ft, mi, m, km, yd or in and I will convert to meters...') #intro
user_distance = float(input('What is the distance? ')) #user input for number
user_unit = input('What are the units? ') #user input for unit choice
print(user_distance * unit_conv[user_unit]) #distance * unit converter = m
#-------------------
#Extra Challenge. ask user for distance, starting unit, and unit to convert to.
unit_conv = { #dictionary for 1x==m
  'ft': 0.3048,
  'mi': 1609.34,
  'm': 1,
  'km': 1000,
  'yd': 0.9144,
  'in': 0.0254,
}
print("\n Let's convert some numbers! You can use: ft, mi, m, km, yd or in...")
user_distance = float(input('What is the distance? '))
user_unit_in = input('What are the input units? ')
user_unit_out = input('What are the output units? ')

answer_m = (user_distance * unit_conv[user_unit_in]) #conv to meters
print(answer_m)
final_answer = (answer_m / unit_conv[user_unit_out])
print(final_answer)
print(f'{user_distance} {user_unit_in} is {final_answer} {user_unit_out}')
#asked to not use if/elif or while loop so unsure how to catch incorrect input.
