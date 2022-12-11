import csv


class Stock:
    def __init__(self):
        self.__data_dict = None
        self.__data_list = []
        self.__index_1 = []
        self.__num_que = []

    # show menu
    def reads(self):

        import pandas
        data = pandas.read_csv("meterial.csv")
        self.__data_dict = data.to_dict()  # import Menu
        print(" ")
        choic_1 = input("M(emu) or E(xit) ").upper()
        while choic_1 != "M" and choic_1 != "E":
            print("Please enter a valid answer")
            choic_1 = input("M(emu) or E(xit) ").upper()

        if choic_1 == "M":
            print(" \n ")
            print("------------------------------------------")
            print(data)
            print("29 C(harge)")
            print("30 E(xit)")
            print("------------------------------------------")

        if choic_1 == "E":
            exit()

        # for quqntity
        while True:
            try:
                index_code = int(input("Enter Product code: "))
                if 0 <= index_code <= 30:
                    if index_code == 30:
                        exit()
                    if index_code == 29:
                        print(" ")
                        break
                    num_qty = int(input("Enter Quantity: "))
                    with open("meterial.csv", "r", encoding='utf-8-sig') as f:
                        data = csv.DictReader(f)
                        lit_of_data = []
                        for i in data:
                            dic = {"Stock": i["Stock"], "quantity": int(i["quantity"])}
                            lit_of_data.append(dic)
                        if lit_of_data[index_code]["quantity"] >= num_qty:
                            self.__index_1.append(index_code)
                            self.__num_que.append(num_qty)
                        else:
                            print("Not enough quantity.")
                            print(f'There are {lit_of_data[index_code]["quantity"]} left in stock.')
                            print("Please select another product.🙏🏻")



                else:
                    print("Please enter a valid answer.")



            except ValueError:
                print("Please enter a valid answer.")
        return self.__index_1, self.__num_que

# x = Stock()
# x.reads()
# x.menu()
# print(x.reads())
