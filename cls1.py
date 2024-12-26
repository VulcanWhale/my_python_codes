n = input('Please enter a string: ')

i,upr,lwr,num,ch = 0,'','','',''

while i<len(n):
    if 'A' <= n[i] <= 'Z':
        upr += n[i]
    elif 'a' <= n[i] <= 'z':
        lwr += n[i]
    elif '1' <= n[i] <= '9':
        num += n[i]
    else:
        ch += n[i]
    i+=1

if len(upr) != 0:
    print(f'the upper case characters are: {upr}')

if len(lwr) != 0:
    print(f'the lower case characters are: {lwr}') 

if len(num) != 0:
    print(f'the numeric characters are: {num}')

if len(ch) != 0:
    print(f'the Special case characters are: {ch}')

"""print(f"The upper case characters are: {upr} \nThe lower case characters are: {lwr} \nThe numeric characters are: {num} \nThe special characters are: {ch}")"""