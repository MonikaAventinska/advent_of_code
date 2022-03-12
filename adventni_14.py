inputs = ["V", "O", "K", "K", "V", "S", "K", "K", "P", "S", "B", "V", "O", "O", "K", "V", "C", "F", "O", "V"]

deposits = {"PK": "P", "BB": "V", "SO": "O", "OO": "V", "PV": "O", "CB": "H", "FH": "F", "SC": "F", "KF": "C", "VS": "O", "VP": "V", "FS": "K", "SP": "C", "FC": "N", "CF": "C", "BF": "V", "FN": "K", "NH": "F", "OB": "F", "SV": "H", "BN": "N", "OK": "K", "NF": "S", "OH": "S", "FV": "B", "OC": "F", "VF": "V", "HO": "H", "PS": "N", "NB": "N", "NS": "B", "OS": "P", "CS": "S", "CH": "N", "PC": "N", "BH": "F", "HP": "P", "HH": "V", "BK": "H", "HC": "B", "NK": "S", "SB": "C", "NO": "K", "SN": "H", "VV": "N", "ON": "P", "VN": "H", "VB": "P", "BV": "O", "CV": "N", "HV": "C", "SH": "C", "KV": "F", "BC": "O", "OF": "P", "NN": "C", "KN": "F", "CO": "C", "HN": "P", "PP": "V", "FP": "O", "CP": "S", "FB": "F", "CN": "S", "VC": "C", "PF": "F", "PO": "B", "KB": "H", "HF": "P", "SK": "P", "SF": "H", "VO": "N", "HK": "C", "HB": "C", "OP": "B", "SS": "V", "NV": "O", "KS": "N", "PH": "H", "KK": "B", "HS": "S", "PN": "F", "OV": "S", "PB": "S", "NC": "B", "BS": "N", "KP": "C", "FO": "B", "FK": "N", "BP": "C", "NP": "C", "KO": "C", "VK": "K", "FF": "C", "VH": "H", "CC": "F", "BO": "S", "KH": "B", "CK": "K", "KC": "C"}

"""
def takeCouple():
    global elementList
    global q
    elementA = inputs[q]
    q += 1
    elementB = inputs[q]
    elementList = [elementA, elementB]
    element = ''.join(elementList)
    return element


def insert():
    global outputs
    outputs = []
    while len(inputs) > q + 1:
        variable = takeCouple()
        elementList.insert(1, deposits.get(variable))
        outputs.append(elementList[0])
        outputs.append(elementList[1])
        if len(inputs) == q + 1:
            outputs.append(elementList[2])


def main():
    global inputs
    global q
    q = 0
    step = 1
    while step < 41:
        insert()
        q = 0
        step += 1
        inputs = outputs
        print(outputs, step)
    mylist = list(dict.fromkeys(outputs))
    u = 0
    while len(mylist) > u:
        count = outputs.count(mylist[u])
        print(count)
        u += 1


main()

"""

################################# 2. cast #################################

outputs = []
q = 0
step = 1

while step < 41:
    outputs = []
    while len(inputs) > q+1:
        variable = ''.join([inputs[q], inputs[q+1]])
        outputs.append(inputs[q])
        outputs.append(deposits.get(variable))
        if len(inputs) == q + 2:
            outputs.append(inputs[q+1])
        q += 1
    q = 0
    print(step)
    step += 1
    inputs = outputs

mylist = list(dict.fromkeys(outputs))
u = 0
while len(mylist) > u:
    count = outputs.count(mylist[u])
    print(count)
    u += 1