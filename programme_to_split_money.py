r = "number of objects"
s = "total cost of product"
t = "first letters"

print("-"*90)
x = input(f"Enter the {r:<25}: ")
while not x.isnumeric():
    print("You can only input numeric values for number of objects!")
    x = input(f"Enter the {r:25}: ")
x = int(x)


h1 = "Object Number"
h2 = "First letters of people"
h3 = "Amount"
h4 = "Cost per person"

all_letters = set()
split_names_ppl = []
cost = []
cost_object = []
for i in range(1,x+1):
    print("-"*90)
    first_letters_of_people = input(f"Enter the {t:<25}: ").split()
    split_names_ppl.append(first_letters_of_people)
    no_of_people = len(first_letters_of_people)
    all_letters.update(first_letters_of_people)
    amount = input(f"Enter the {s:<25}: ")
    while not amount.isnumeric():
        print("You can only input numeric values for amount of object!")
        amount = input(f"Enter the {s:<25}: ")
    amount = int(amount)
    cost_object.append(amount/no_of_people)
    cost.append(amount)
print("-"*90)
all_letters = list(all_letters)
all_letters.sort()
for name in range(len(all_letters)):
    all_letters[name] = input(f"Enter the name of {all_letters[name]}: ")

print("-"*90)
print("-"*75)
print(f"|{h1:^15}|{h2:^25}|{h3:^10}|{h4:^20}|")
print("-"*75)

for no in range(len(cost)):
    a = " ".join(split_names_ppl[no])
    print(f"|{no+1:^15}|{a:^25}|{cost[no]:^10}|{round(cost_object[no],2):^20}|")
print("-"*75)
print()


divided_money = []
final_obj = []
for ppl in all_letters:
    ppl_list = []
    ppl_obj = []
    for k in range(len(cost)):
        if ppl[0] in split_names_ppl[k]:
            ppl_obj.append(k+1)
            ppl_list.append(cost_object[k])
    divided_money.append(sum(ppl_list))
    final_obj.append(ppl_obj)

h5 = "Name"
h6 = "Objects they bought"
h7 = "Total"

print("-"*57)
print(f"|{h5:^15}|{h6:^25}|{h7:^13}|")
print("-"*57)

for l in range(len(final_obj)):
    final_obj[l] = map(str,final_obj[l])

for i in range(len(all_letters)):
    b = " ".join(final_obj[i])
    print(f"|{all_letters[i]:^15}|{b:^25}|{round(divided_money[i],2):^13}|")
print("-"*57)
