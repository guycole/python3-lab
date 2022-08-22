# artistic if distance p to a between X and Y (inclusive)
# distance betwen a, b also betwen X and Y (inclusive)
# a must be between pb
import typing

def calculateNdxLimit(origin: int, distance: int, max: int) -> tuple:
    start = origin-distance
    if start < 0:
        start = 0
    stop = origin+distance+1
    if stop > max:
        stop = max-1

    return (start, stop)

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    print(C)

    counter = 0
    
    a_ndx = C.find('A')
    while a_ndx >= 0:        
        print(f"A {a_ndx}")
        if a_ndx < 0: # all A have been evaluated
            return counter

        (start, stop) = calculateNdxLimit(a_ndx, Y, len(C))

        b_ndx = C.find('B', start, stop)
        while b_ndx >= 0: # evaluate each B
            print(f"B {b_ndx}")
            if b_ndx >= 0:
                delta1 = abs(a_ndx-b_ndx)
                if delta1 >= X and delta1 <= Y:
                    print(f"b match {a_ndx} {b_ndx}")
                    p_ndx = C.find('P', start, stop)
                    while p_ndx >= 0: # evaluate each P
                        print(f"P {p_ndx}")
                        print(f"p candidate {a_ndx} {b_ndx} {p_ndx}")
                        delta2 = abs(a_ndx-p_ndx)
                        if delta2 >= X and delta2 <= Y:
                            print(f"p match -1-> {a_ndx} {b_ndx} {p_ndx}")
                            if b_ndx < a_ndx and a_ndx < p_ndx:
                                print("hit1")
                                counter += 1
                            elif p_ndx < a_ndx and a_ndx < b_ndx:
                                print("hit2")
                                counter += 1
                            else:
                                print('skipping match failure')
                        else:
                            print("p fail")

                        p_ndx = C.find('P', p_ndx+1, stop)           
                else:
                    print("b fail")

            b_ndx = C.find('B', b_ndx+1, stop)
        a_ndx = C.find('A', a_ndx+1)
      
    return counter

if __name__ == '__main__':
    print("begin")

    n = 5 # cell population
    c = 'APABA' # actor, photog, actor, backdrop, actor
    x = 1
    y = 2
    result = getArtisticPhotographCount(n, c, x, y)
    print(f"result {result}")
  
    n = 5
    c = 'APABA'
    x = 2
    y = 3
    result = getArtisticPhotographCount(n, c, x, y)
    print(f"result {result}")

    n = 8
    #     x  x  x
    #    01234567
    c = '.PBAAP.B'
    x = 1
    y = 3
    result = getArtisticPhotographCount(n, c, x, y)
    print(f"result {result}")

    print("end")
