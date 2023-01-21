riddle = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"


def decode(riddle):
    answer = ""
    for c in riddle:
        pos = ord(c)
        if c.isalpha():
            pos = (ord(c)+2-ord("a")) % 26 + ord("a")

        answer += chr(pos)

    return answer


print(decode(riddle))
print(decode("map"))
