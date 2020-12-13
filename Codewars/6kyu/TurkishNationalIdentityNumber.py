def check_valid_tr_number(number):
    if type(number) == int:
        temp0 = [int(i) for i in str(number)]
        if len(temp0) == 11 and temp0[0] != 0:
            a = (temp0[0] + temp0[2] + temp0[4] + temp0[6] + temp0[8]) * 7
            b = a - (temp0[1] + temp0[3] + temp0[5] + temp0[7])
            if b % 10 == temp0[-2]:
                if sum(temp0[:-1]) % 10 == temp0[-1]:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False