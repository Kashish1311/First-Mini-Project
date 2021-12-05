#broken travel corrected code

year = int(input("Greetings! What is your year of origin? "))

if year <= 1899:
   print ("Woah, that's the past!")
elif year > 1899 and year < 2021:
   print ("That's totally the present!")
else:
   print ("Far out, that's the future!!")
