
import clc as c

while(True):
    number1= int(input('please enter the frist num'))
    number2=int(input('please enter the secand num'))
    operator=input('please enter the operator')

    if operator=='add':
        print(c.add(number1,number2))
    elif operator=='sub':
        print(c.sub(number1,number2))
    elif operator=='dev':
        print(c.dev(number1,number2))
    elif operator=='mut':
        print(c.mut(number1,number2))


    ans=input('do you want to repeat the opration?')
    if ans=='y':
        continue
    elif ans=='n':
        break

