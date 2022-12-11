import csv


class Charge:
    def __init__(self):
        pass

    # minus quantity when customer buy the product.
    def charged(self, ordinal, minus):
        with open("meterial.csv", "r", encoding='utf-8-sig') as f:
            data = csv.DictReader(f)
            lit_of_data = []
            for i in data:
                dic = {"Stock": i["Stock"], "quantity": int(i["quantity"]), "price": float(i["price"])}
                lit_of_data.append(dic)

            for i in range(len(ordinal)):
                lit_of_data[ordinal[i]]["quantity"] -= minus[i]

        l_new = []
        for update in lit_of_data:
            collect = []
            collect.append(update["Stock"])
            collect.append(update["quantity"])
            collect.append(update["price"])
            l_new.append(collect)

        with open("meterial.csv", "w", encoding='utf-8-sig') as f:
            data = csv.writer(f)
            data.writerow(["Stock", "quantity", "price"])
            data.writerows(l_new)

    def treasury(self, ordinal, minus, skip):
        with open("meterial.csv", "r", encoding='utf-8-sig') as f:
            data = csv.DictReader(f)
            display = []
            p = []
            for i in data:
                dic = {"Stock": i["Stock"], "quantity": int(i["quantity"]), "price": float(i["price"])}
                p.append(dic)
                display.append(i)

        total = 0
        number = []
        for order in range(len(ordinal)):
            total += (float(display[ordinal[order]]["price"]) * minus[order])
            number.append(float(display[ordinal[order]]['price']) * minus[order])

        discount = total
        discount -= total * 0.1
        finish = ((total - (total * 0.1)) + (discount * 7) / 100)
        vat = total + (total * 0.07)
        print("-------Bill-------")
        print("   Material Shop")
        print("Receipt/Tax invoice")
        print(" ")
        print("    Qty     Name     Price")
        for lit in range(len(number)):
            print(f"{lit + 1}.   {minus[lit]}   {display[ordinal[lit]]['Stock']}   {number[lit]:.2f}")
        print(" ")
        print(f"Subtotal   {total:.2f} baht.")
        # for User
        if skip != 0:
            print(f"Discount 10%  {total * 0.1:.2f} baht.")
            print(f"Vat 7%   {(discount * 7) / 100:.2f} baht.")
        else:
            print(f"Vat 7%   {(total * 7) / 100:.2f} baht.")

        # for User
        if skip != 0:
            print(f"Total   ({len(number)})   {finish:.2f} bath.")
        else:
            print(f"Total   ({len(number)})   {vat:.2f} bath.")

        print("-----------------------------\n")
        print("This new year, material shop wish everyone happiness.")

# x = Charge()
# x.tax_10()
# x.charged()
# print(x.charged())
