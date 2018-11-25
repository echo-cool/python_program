import os



flie_name = open("IC.EML","w")
money = raw_input("money:")
money2 = raw_input("money2:")
for i in range(16):
    data = [
    "06319031960804006263646566676869",
    "30303130303132313630323037333600",
    "63303033343131333435623000000000",
    "FFFFFFFFFFFFFF078069FFFFFFFFFFFF",
    ]
    if i == 5:
        data = [
        "AF9900005066FFFFFFFF000014EB14EB",
        "AF9900005066FFFFFFFF000014EB14EB",
        "5227005AAA1601003227000014EB14EB",
        "322180123456FF078069705002022160",

        ]
    for i in data:
        flie_name.write(i +"\n")