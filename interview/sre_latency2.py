#
# Title: sre_latency2.py
#
# 1155 1217
class Solution:

    def tokenizer(self, raw:str):
        tokens = raw.strip().split(",")
    
        duration = tokens[-1]
        url = tokens[-2]
        verb = tokens[-3]
    
        return (url, verb, duration)
    
    def all_durations(self, results:dict):
        durations = []

        for key in results:
            temp = results[key]
            if 'GET' in temp:
                durations.append(int(temp['GET'][:len(temp['GET'])-2]))
            elif 'POST' in temp:
                durations.append(int(temp['POST'][:len(temp['POST'])-2]))
            elif 'PUT' in temp:
                durations.append(int(temp['PUT'][:len(temp['PUT'])-2]))

        return durations
    
    def execute(self, file_name: str):
        print("execute")

        results = {}

        try:
            with open(file_name) as infile:
                buffer = infile.readlines()
        except:
            print("error")
            return

        for temp in buffer:
            tupelz = self.tokenizer(temp)
            results[tupelz[0]] = {tupelz[1]: tupelz[2]}

        durations = self.all_durations(results)
        durations = sorted(durations)
        print(durations)

        return

if __name__ == '__main__':
    print("main")

    solution = Solution()
    solution.execute("sre_latency1.dat") 

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
