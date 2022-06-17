import random
f = open("me.txt", 'w')
f.write("")
f.close()

f = open("me.txt", 'a')
w = str(input("width"))
h = str(input("height"))
f.write("w" + w + "\n")
f.write("h" + h + "\n")
for i in range(int(w) * int(h)):
  var = random.randint(1, 262144)
  print(var)
  f.write(str(var) + '\n')

f.close()
  
