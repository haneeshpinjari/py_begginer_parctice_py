from prettytable import PrettyTable
# made with pretty table module
num = int(input("enter a number:"))
table = PrettyTable()
table.field_names = ["multiplier", "X", "product"]
for i in range(1, 11):
    table.add_row([num, i, num * i])
print(table)