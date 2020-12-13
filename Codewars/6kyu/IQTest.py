def iq_test(numbers):
    numberList = numbers.split(" ")
    numberList = [int(i) for i in numberList]
    # Check items in the list
    oddevenList = []
    for item in numberList:
        if item != 0:
            if item%2 == 0:
                oddevenList.append(0)
            else:
                oddevenList.append(1)
        else:
            oddevenList.append(0)
        
    

    # Search list

    odds = oddevenList.count(1)
    evens = oddevenList.count(0)

    if odds > evens:
        return oddevenList.index(0) + 1
    else:
        return oddevenList.index(1) + 1



print(iq_test("5 1 3 37 35 21 13 23 49 13 43 37 45 1 33 29 7 45 7 19 43 45 43 13 19 52"))