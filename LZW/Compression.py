# For read and write from file delete hashtags and hashtag the next line and last 3  lines
symbols = [chr(i) for i in range(128)]
ascii_list = []
# answer = open("Write.txt", "w")
answer = []
# file = open("Read.txt", "r")
file = input("Pls input the string you want to Compress : ")
x = ""
i=0
# h=file.read()

for j in symbols:
    ascii_list.append(ord(j))
#add h in len
while i < len(file):
    # x += h[i]
    x += file[i]
    # add h in len
    if i+1 == len(file):
        z = symbols.index(x)
        # answer.write(str(ascii_list[z]))
        answer.append(ascii_list[z])
        break
    if x in symbols:
        i+=1
        continue
    else:
        z = symbols.index(x[0:-1])
        # answer.write(str(ascii_list[z]) + " ")
        answer.append(ascii_list[z])
        symbols.append(x)
        ascii_list.append(ascii_list[-1]+1)
        x=""
print(symbols)
print(ascii_list)
print(answer)