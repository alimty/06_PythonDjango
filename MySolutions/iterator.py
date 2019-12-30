print(""""**********
Bir sayinin Bölenlerini bulma

Programdan cikmak icin 'q' ya basin.

****************
""")


def find_divider(num):
    divider_list = []
    for i in range(1, num+1):
        if num % i == 0:
            divider_list.append(i)
    return divider_list


while True:
    num = input("Give me a number : ")
    if num == "q":
        print("Exiting the Program")
        break
    else:
        num = int(num)
        print(f"This is your list :  {find_divider(num)} ")



