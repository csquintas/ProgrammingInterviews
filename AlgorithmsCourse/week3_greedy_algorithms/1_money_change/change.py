# Uses python3

# Uses python3


def get_change(money):
    #coins are of 1,5,10
    NumCoins = 0
    while money > 0:
        if money >= 10:
            money = money - 10
        elif money >= 5:
            money = money - 5
        else:
            money = money - 1
        NumCoins = NumCoins + 1

    return NumCoins

if __name__ == '__main__':
    money = int(input())
    print(get_change(money))

 