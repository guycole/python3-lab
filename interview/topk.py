#
# Title: topk.py
# Description: discover the top k values
#

if __name__ == '__main__':
    print("main")

    xx = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    yy = {k: v for k, v in sorted(xx.items(), key=lambda item: item[1])}
    print(yy)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
