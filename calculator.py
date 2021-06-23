# simple-python-calculato
def calculator():

    arithmetic_charakter = input("choose an arthimetic charakter(+|-|/|*) ")

    if arithmetic_charakter == ("*"):

     x = input("number 1: ")
     y = input("number 2: ")
     result = int(x) * int(y)


     print("result = " + str(result))


    if arithmetic_charakter == ("+"):

      x = input("number 1: ")
      y = input("number 2: ")
      result = int(x) + int(y)

      print("result = " + str(result))

    if arithmetic_charakter == ("-"):

     x = input("number 1: ")
     y = input("number 2: ")
     result = int(x) - int(y)


     print("result = " + str(result))

    if arithmetic_charakter == ("/"):

     x = input("number 1: ")
     y = input("number 2: ")
     result = int(x) / int(y)


     print("result = " + str(result))


calculator()

#this calculator is only able to calculate whole numbers

