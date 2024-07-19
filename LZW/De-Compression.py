# For read and write from file delete hashtags and hashtag the next lines and last line
symbols = [chr(i) for i in range(128)]
ascii_list = []
last_step =[]
for j in symbols:
    ascii_list.append(ord(j))
# answer = open("Write.txt", "w")
answer = ""
# code = open("Read.txt", "r")
code = [int(i) for i in input("Pls input the code you want to De-Compress : ").split(  )]
# m=[int(i) for i in code.read().split(  )]
#add m in len
for i in range(len(code)):
    if i == 0:
        # add m in ascii_list.index
        z = ascii_list.index(code[i])
        # answer.write(str(symbols[z]))
        answer+=symbols[z]
        last_step.append(symbols[z])
    elif code[i] in ascii_list:
        # add m in ascii_list.index
        z = ascii_list.index(code[i])
        x=symbols[z]
        # answer.write(str(x))
        answer += x
        symbols.append(last_step[-1]+x[0])
        last_step.append(x)
        ascii_list.append(ascii_list[-1] + 1)
    else:
        h=last_step[-1]
        symbols.append(h + h[0])
        ascii_list.append(ascii_list[-1]+1)
        # answer.write(h + h[0])
        answer+=(h + h[0])
        last_step.append(h + h[0])

print(symbols)
print(ascii_list)
print(answer)