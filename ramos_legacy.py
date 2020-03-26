def sel1(n):
    givn = 100
    amm = 100
    n -= 1
    stri = "| 100 "
    for i in range(n):
        givn -= 10
        if givn == 0:
            stri += "| No money given this year |"
            return stri
        amm += givn
        stri += "| {} ".format(amm)

def sel2(n):
    givn = 10
    amm = 10
    n -= 1
    stri = "| 10 "
    for i in range(n):
        givn += 10
        amm += givn
        stri += "| {} ".format(amm)
    stri += "|"
    return stri

def sel3(n):
    givn = 10
    amm = 10
    n -= 1
    stri = "| 10 "
    for i in range(n):
        givn *= 1.5
        amm += givn
        stri += "| {} ".format(int(amm))
    stri += "|"
    return stri

def sel4(n):
    givn = 2
    amm = 2
    n -= 1
    stri = "| 2 "
    for i in range(n):
        givn *= 2
        amm += givn
        stri += "| {} ".format(int(amm))
    stri += "|"
    return stri
