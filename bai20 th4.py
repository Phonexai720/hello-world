a = input('Enter a value: ')

b = input('Enter a value: ')

c = input('Enter a value: ')

d = input('Enter a value: ')

e = input('Enter a value: ')

f = input('Enter a value: ')

g = input('Enter a value: ')

h = input('Enter a value: ')

i = input('Enter a value: ')

j = input('Enter a value: ')



list1 = [a, b, c, d, e, f, g, h, i, j]

list2 = [] # used to sort the ODD values into 

list3 = (a+b+c+d+e+f+g+h+i+j) # used this bc all 10 values could have used     value'3'

                             # and had the total value become an EVEN value

if (list3 % 2 == 0): # does list 3 mod 2 have no remainder

       if (a % 2 == 0): # and if so then by checking if 'a' has an EVEN value     it rules out

                    # the possibility of all values having an ODD value entered

           print('All declared variables have even values')

       else:

           for odd in list1: # my FOR loop to loop through and pick out the     ODD values

               if (odd % 2 == 1):# if each value tested has a  remainder of one to mod 2

                   list2.append(odd) # then append that value into list 2

           odd = str(max(list2)) # created the variable 'odd' for the highest ODD value   from list 2 so i can concatenate it with a string.

           print ('The largest ODD value is ' + odd) 
