s = []
index = []
answer = []
file = input("Pls input the string you want to Compress : ")
sBuffer = int(input("Pls input the Search Buffer : "))
laBuffer = int(input("Pls input the Look Ahead Buffer : "))
x = ""
h = 0
counter = 1

for i in range(len(file)):
    if x == "":
        index.append(i)
    x += file[i]
    if i+1 == len(file):
        h = file[0:(index[-1])].rindex(x[0:-1])
        s.append(x)
        z = "<" + str(index[-1] - h) + "," + str(len(x) - 1) + "," + x[-1] + ">"
        answer.append(z)
        x = ""
        break

    if index[-1]-sBuffer < 0:
        var = 0
    else:
        var = index[-1]-sBuffer

    if x in file[var:(index[-1])]:
            if counter == laBuffer:
                h = file[var:index[-1]].rindex(x[0:-1])
                h+= var
                if x[0] not in file[0:(index[-1])]:
                    s.append(x)
                    z = "<" + str(0) + "," + str(len(x) - 1) + "," + x[-1] + ">"
                else:
                    s.append(x)
                    z = "<" + str(index[-1] - h) + "," + str(len(x) - 1) + "," + x[-1] + ">"
                answer.append(z)
                x = ""
                counter=1
            else:
                counter += 1
                continue
    else:
        h = file[var:index[-1]].rindex(x[0:-1])
        h += var
        if x[0] not in file[0:(index[-1])]:
            s.append(x)
            z = "<" + str(0) + "," + str(len(x) - 1) + "," + x[-1] + ">"
        else:
            s.append(x)
            z = "<" + str(index[-1]-h) + "," + str(len(x) - 1) + "," + x[-1] + ">"
        answer.append(z)
        x = ""
        counter=1

print(s)
print(answer)