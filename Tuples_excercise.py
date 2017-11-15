# This is an excersise
with open("weather.csv","r") as reader:
   y=reader.readline()
   print y
   rain=[]
   for x in reader:
       print x
       r=x.strip().split(",")[-1]
       r=float(r)
       rain.append(r)
print rain
with open("myrain.txt","w") as writer:
    for z in rain:
        writer.write(str(z) + "\n")

