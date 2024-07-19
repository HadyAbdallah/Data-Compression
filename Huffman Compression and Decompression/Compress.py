from collections import Counter
import math


def dfs(node, code, adj, codes):
    if len(node) == 1:
        if code == "":
            code += '0'
        codes[node] = code
        return
    dfs(adj[node][0], code + '1', adj, codes)  # 1 left
    dfs(adj[node][1], code + '0', adj, codes)  # 0 right
    return


def encoder(data):
    codes = {}
    rdic = []
    adj = {}
    dic = Counter(data)
    for character in dic:
        rdic.append((dic[character], character))

    while len(rdic) > 1:
        rdic = sorted(rdic)
        pair1 = rdic[0]
        rdic.remove(rdic[0])
        pair2 = rdic[0]
        rdic.remove(rdic[0])
        pair3 = (pair1[0] + pair2[0], pair1[1] + pair2[1])
        adj[pair3[1]] = (pair1[1], pair2[1])
        rdic.append(pair3)
    dfs(rdic[0][1], "", adj, codes)
    codes = dict(sorted(codes.items()))
    encoded_data = ""
    for i in data:
        encoded_data += codes[i]
    rcodes = {}
    for code in codes:
        rcodes[codes[code]] = code
    return [rcodes, encoded_data]


def decoder(data):
    rtable = data[0]
    encoded_data = data[1]

    code = ""
    message = ""

    for i in encoded_data:
        code += i
        if code in rtable:
            message += rtable[code]
            code = ""
    if code != "":
        message += rtable[code]
    return message

message = open("Input.txt", "r").read()
file = open("outputCompress.txt", "w")
compress = encoder(message)
file.write(compress[1])
print(compress)
file.close()


file = open("outputdecompress.txt", "w")
decompress = decoder(compress)
file.write(decompress)
print(decompress)
file.close()
