from member import Member
from stock import Stock
from charge import Charge
import json
import csv

member = Member()
stock = Stock()
charge = Charge()

LIT = 0


def calculate():
    while True:
        users, named = member.login()
        try:
            if js_1[users] == named:
                print("Login Success")
                index_of_in, num_qyt = stock.reads()
                charge.charged(ordinal=index_of_in, minus=num_qyt)
                break   
            else:
                print("Login Failed")

        except KeyError:
            print("No User Found")


print("_____WELCOME TO THE METERIAL SHOP_____")
print("You have Account Or Not?")
que_1 = input("N(o) or Y(es) ").upper()

# check if u have acc or not.
while que_1 != "N" and que_1 != "Y":
    print("Please enter a valid answer")
    que_1 = input("N(o) or Y(es) ").upper()
# u gonna create or buy with out no acc.
if que_1 == "N":
    que_2 = input("R(egister) or S(kip) or E(xit) ").upper()
    while que_2 != "R" and que_2 != "S" and que_2 != "E":
        print("Please enter a valid answer")
        que_2 = input("R(egister) or S(kip) or E(xit) ").upper()
    if que_2 == "R":
        while True:
            cal_l = member.password()
            with open("customer.json", "r") as data:
                js_1 = json.load(data)
            js_1.update(cal_l)
            with open("customer.json", "w") as data:
                json.dump(js_1, data, indent=4)
            with open("customer.txt", "a") as data:
                data.writelines(f"\n{member.new_name.upper()}")
                while True:
                    user, name = member.login()
                    try:
                        if js_1[user] == name:
                            print("----Login Success----")
                            index, num = stock.reads()
                            charge.charged(ordinal=index, minus=num)
                            LIT += 1
                            charge.treasury(ordinal=index, minus=num, skip=LIT)
                            exit()
                        else:
                            print("Login Failed")

                    except KeyError:
                        print("No User Found")

    if que_2 == "S":
        index, num = stock.reads()
        charge.treasury(ordinal=index, minus=num, skip=LIT)

    if que_2 == "E":
        exit()


elif que_1 == "Y":
    while True:
        user, name = member.login()
        with open("customer.json", "r") as data:
            js_1 = json.load(data)
        try:
            if js_1[user] == name:
                print("-----Login Success-----")
                index, num = stock.reads()
                charge.charged(ordinal=index, minus=num)
                LIT += 1
                charge.treasury(ordinal=index, minus=num, skip=LIT)
                break
            else:
                print("Login Failed.")

        except KeyError:
            print("No User Found.")

# from check import Check
# check = Check()
# check.methot()
