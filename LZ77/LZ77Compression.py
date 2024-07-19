s = []
index = []
answer = []
file = input("Pls input the string you want to Compres : ")
x = ""
h=0
cnt=0
for i in range(len(file)):
    if x == "":
        index.append(i)
    x += file[i]
    if i+1 == len(file):
        h = file[0:(index[-1])].rindex(x[0:-1])
        s.append(x)
        z = "<" + str(index[cnt] - h) + "," + str(len(x) - 1) + "," + x[-1] + ">"
        answer.append(z)
        cnt += 1
        x = ""
        break
    if x in file[0:(index[-1])]:
            continue
    else:
        h = file[0:index[-1]].rindex(x[0:-1])
        if x[0] not in file[0:(index[-1])]:
            s.append(x)
            z = "<" + str(0) + "," + str(len(x) - 1) + "," + x[-1] + ">"
        else:
            s.append(x)
            z = "<" + str(index[cnt]-h) + "," + str(len(x) - 1) + "," + x[-1] + ">"
        answer.append(z)
        cnt +=1
        x=""

print(s)
print(answer)