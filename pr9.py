#python program to convert celcius to fahrenheir and vice versa


#function for converting the temperature from celcius to fahrenheit
def tofah():
    print(f"The temperature in Fahrenheit is = {((c := float(input('\nPlease enter the celcius temperature: '))) * 1.8) + 32 :0.2f}")


#function for converting the temperature from fahrenheit to celcius
def tocel():
    print(f"The temperature in celcius is = {((f := float(input('\nPlease enter the Fahrenheit temperature: '))) - 32) / 1.8 :0.2f}")


#showing a message and taking the input
print('Press 1 for entering temperature in celcius. \nPress 2 for entering temperature in fahrenheit. \n')
t = float(input("PLEASE ENTER AN OPTION: "))


#checking the user input
if t == 1:
    tofah()
elif t == 2:
    tocel()
else:
    print("please enter a valid input....")