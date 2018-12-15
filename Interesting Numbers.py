import wikipedia
numbersize = []



for j in range(0, 100):
    m = len(wikipedia.page("%s_(number)" % j).content)
    numbersize.append((j, m))
    print("%s has %s characters" % (j, m))

file = open("Interesting Numbers_raw", "w")
for i in numbersize:
    file.write("%s %s\n" % (i[0], i[1]))
file.close()



numbersize = sorted(numbersize, key = lambda x: x[1], reverse = True)

print("----------------------------\n\n")


file = open("Interesting Numbers", "w")
for i in numbersize:
    print("%s has %s characters" % (i[0], i[1]))
    file.write("%s has %s characters \n" % (i[0], i[1]))
file.close()


