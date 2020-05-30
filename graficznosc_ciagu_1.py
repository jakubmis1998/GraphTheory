def obnizanie_stopni_wierzcholka(list):
    if sum(list) % 2 != 0:
        print("Warunek konieczny! - Nieparzysta suma elementów")
        return

    list.sort(reverse = True)
    print(list)

    while list[0] > 0:
        r = list[0]
        list.pop(0)
        for i in range(r):
            try:
                list[i] -= 1
                if list[i] < 0:
                    print("Ciąg nie jest graficzny, stopień wierzchołka poniżej 0!")
                    return
            except IndexError:
                print("Ciąg nie jest graficzny, wyjście poza listę!")
                return
        list.sort(reverse = True)
        print("{}".format(list))

    if list[0] == 0:
        print("Ciąg jest graficzny!")
    else:
        print("Ciąg nie jest graficzny!")


def erdos(list):
    if sum(list) % 2 != 0:
        print("Warunek konieczny! - Nieparzysta suma elementów")
        return

    list.sort(reverse = True)
    n = len(list)
    lewa = 0
    prawa = 0

    for k in range(1, n + 1): # k w przedziale 1 - n
        for i in range(1, k + 1): # suma lewej strony nierówności 1 - k
            lewa += list[i - 1]
        for i in range(k + 1, n + 1): # suma prawej strony nierówności k+1 - n
            prawa += min(k, list[i - 1])
        prawa += k * (k - 1)
        print("k = {} : lewa = {}\tprawa = {}".format(k, lewa, prawa))
        if lewa > prawa:
            print("Ciąg nie jest graficzny, niespełniona nierówność!")
            return
        lewa = 0
        prawa = 0
    print("Ciąg jest graficzny!")

ciag = [5, 5, 5, 5, 3, 3]
obnizanie_stopni_wierzcholka(ciag)
print("\n")
ciag = [5, 5, 5, 5, 3, 3]
erdos(ciag)