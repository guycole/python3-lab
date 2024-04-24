#
# Title:benchly.py
# Description: benchly interview, html formatter
#
# 1618 1634
def addBinary(a: str, b: str) -> str:
    l1 = list(a)
    l2 = list(b)

    carry = 0
    run_flag = True
    result = ""

    while run_flag is True:
        if len(l1) == 0 and len(l2) == 0:
            run_flag = False
            continue

        if len(l1) > 0:
            temp1 = int(l1.pop())
        else:
            temp1 = 0
        
        if len(l2) > 0:
            temp2 = int(l2.pop())
        else:
            temp2 = 0

        temp = temp1 + temp2 + carry
        carry = temp // 2

        temp = temp % 2
        result = str(temp) + result
        
    if carry > 0:
        result = str(carry) + result

    return(result)

if __name__ == '__main__':
    print(addBinary('11', '1'))
    print(addBinary('1010', '1011'))

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
