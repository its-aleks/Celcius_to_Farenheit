while True:
    temprature_str = input("Graden Celcius ")
    try:
        temprature_flt = float(temprature_str)
        break
    except:
        print ("Dit is geen geldig input. Vul een getal in ")

fareheit = (temprature_flt * 1.8)+32
print (temprature_flt, "graden Celsius is", fareheit, "graden Farenheit")
