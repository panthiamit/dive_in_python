temp = int(input('enter the temprature value in celcius'))
humd = int(input('enter the humidity percentage'))
if temp >=30 :
    if humd >= 90 :
        print('weather is hot and humid')
    if humd < 90 :
        print('weather is hot')
if temp < 30 :
    if humd >= 90 :
        print('weather is cold and humid')
    if humd < 90 :
        print('weather is cold')