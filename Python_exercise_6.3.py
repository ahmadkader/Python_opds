def average(x,y):
      a = [x,y]
      return (sum(a)/(len(a)))
 
x = 128
y = 255
z = average(x,y)
print ("The average of",x,"and", y, "is", z)