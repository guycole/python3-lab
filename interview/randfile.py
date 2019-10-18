import random

print('start')
if __name__ == '__main__':
    print('main')

    with open('big_rand.dat', 'w') as writer:
        for _ in range(1 << 100):
            writer.write("%s\n" % str(random.randint(0, 1000000000)))

print('stop')