f = open('data_rev.txt','r')
d = {}
for line in f:
    words = line.strip().split()
    #print(line.strip())
    for word in words:
        if word in d:
            d[word] +=1
        else:
            d[word] = 1

for key in d:
    print("The word:" + key + "occurs" + str(d[key]) + "times")
