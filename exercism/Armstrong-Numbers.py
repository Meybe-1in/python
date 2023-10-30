def is_armstrong_number(number):
    items = str(number)
    collector = 0 

    for i in range (len(items)):
        collector += (int(items[i]) ** len(items))
        print (collector)


    if collector == number:
        return True
    else:
        return False
    

print (is_armstrong_number(153))