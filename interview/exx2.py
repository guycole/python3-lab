import sys

class Counter:
    results = {}

    def parser(self, candidate):
        ndx1 = candidate.find("//")
        ndx2 = candidate.rfind(":")

        key = candidate[ndx1+2:ndx2]
        if key in self.results:
            self.results[key] = self.results[key] + 1
        else:
            self.results[key] = 1

    def execute(self, file_name):
        with open(file_name, newline='') as fp:
            buffer = fp.readline()
            while buffer:
                self.parser(buffer)
                buffer = fp.readline()

        print(self.results)
#        print(self.results.keys())
#        print(self.results.items())

#        x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
#        sorted_x = sorted(x.items(), key=lambda kv: kv[1])
#        print(sorted_x)

        xx = sorted(self.results.items(), key = lambda kv:kv[0])
        print(xx)

        for key, value in sorted(self.results.items(), key=lambda item: item[0]):
            print("%s %s" % (key, value))

#        print(self.results)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage exx2.py source_name")
        sys.exit(0)

    counter = Counter()
    counter.execute(sys.argv[1])