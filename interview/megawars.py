#
# Title:megawars.py
# Description: create the megawars standard map
# Development Environment:OS X 10.13.6/Python 3.8.2
# Author:G.S. Cole (guycole at gmail dot com)
#
MAX_XX = 75
MAX_YY = 75

class Solution:
    def __init__(self):
        self.empty_row = ['.'] * MAX_XX
        self.sectors = [self.empty_row[:] for _ in range(MAX_YY)]

    def header_footer(self):
        rows = []
        for yy in range(2):
            buffer = "--:" 
            for xx in range(MAX_XX):
                xxx = xx+1

                if yy < 1:
                    buffer += str((xxx // 10) % 10)
                else:
                    buffer += str(xxx % 10)

            rows.append(buffer)

        print("\n".join("".join(row) for row in rows))

    def loc_fix(self, location: list[int]) -> tuple:
        yy, xx = location
        return MAX_YY - yy, xx - 1
    
    def planets(self):
        pass

    def stargates(self):
        candidates = []
        candidates.append([65, 10])
        candidates.append([65, 65])
        candidates.append([36, 10])
        candidates.append([36, 36])
        candidates.append([36, 65])
        candidates.append([ 9, 36])

        for candidate in candidates:
            location = self.loc_fix(candidate)
            self.sectors[location[0]][location[1]] = 'X'

    def stars(self):
        candidates = []
        candidates.append([75, 18])
        candidates.append([74, 13])
        candidates.append([74, 43])
        candidates.append([74, 46])
        candidates.append([73, 21])
        candidates.append([73, 35])
        candidates.append([71, 42])
        candidates.append([71, 47])
        candidates.append([70, 14])
        candidates.append([70, 20])
        candidates.append([70, 50])
        candidates.append([70, 64])
        candidates.append([69,  7])
        candidates.append([69, 17])
        candidates.append([69, 52])
        candidates.append([69, 55])
        candidates.append([69, 61])
        candidates.append([69, 67])
        candidates.append([68, 25])
        candidates.append([68, 44])
        candidates.append([67,  4])
        candidates.append([67,  5])
        candidates.append([66, 43])
        candidates.append([66, 50])
        candidates.append([66, 60])
        candidates.append([65, 63])
        candidates.append([64, 15])
        candidates.append([63,  7])
        candidates.append([63, 12])
        candidates.append([63, 47])
        candidates.append([63, 52])
        candidates.append([63, 66])
        candidates.append([63, 73])
        candidates.append([62,  8])
        candidates.append([62, 19])
        candidates.append([62, 44])
        candidates.append([62, 48])
        candidates.append([62, 71])
        candidates.append([62, 75])
        candidates.append([61,  6])
        candidates.append([61,  8])
        candidates.append([61, 38])
        candidates.append([61, 39])
        candidates.append([61, 41])
        candidates.append([61, 45])
        candidates.append([61, 49])
        candidates.append([61, 52])
        candidates.append([60, 20])
        candidates.append([60, 50])
        candidates.append([60, 58])
        candidates.append([60, 71])
        candidates.append([59, 18])
        candidates.append([59, 22])
        candidates.append([58, 16])
        candidates.append([58, 23])
        candidates.append([58, 47])
        candidates.append([58, 58])
        candidates.append([57, 27])
        candidates.append([57, 36])
        candidates.append([57, 68])
        candidates.append([56, 10])
        candidates.append([56, 44])
        candidates.append([56, 59])
        candidates.append([56, 67])
        candidates.append([55,  1])
        candidates.append([55, 26])
        candidates.append([55, 43])
        candidates.append([55, 63])
        candidates.append([54, 27])
        candidates.append([54, 44])
        candidates.append([54, 54])
        candidates.append([53,  3])
        candidates.append([53,  5])
        candidates.append([53, 19])
        candidates.append([53, 33])
        candidates.append([53, 38])
        candidates.append([53, 63])
        candidates.append([52, 15])
        candidates.append([52, 23])
        candidates.append([52, 26])
        candidates.append([52, 49])
        candidates.append([52, 52])
        candidates.append([52, 59])
        candidates.append([52, 74])
        candidates.append([51,  2])
        candidates.append([51, 16])
        candidates.append([51, 28])
        candidates.append([50,  1])
        candidates.append([50,  5])
        candidates.append([50, 10])
        candidates.append([50, 21])
        candidates.append([50, 64])
        candidates.append([50, 71])
        candidates.append([49, 15])
        candidates.append([49, 22])
        candidates.append([49, 39])
        candidates.append([49, 57])
        candidates.append([49, 68])
        candidates.append([48, 10])
        candidates.append([48, 35])
        candidates.append([47,  1])
        candidates.append([47,  9])
        candidates.append([47, 19])
        candidates.append([47, 46])
        candidates.append([46, 21])
        candidates.append([46, 52])
        candidates.append([45, 34])
        candidates.append([45, 52])
        candidates.append([45, 67])
        candidates.append([44, 33])
        candidates.append([44, 46])
        candidates.append([44, 51])
        candidates.append([43, 19])
        candidates.append([43, 21])
        candidates.append([43, 42])
        candidates.append([43, 53])
        candidates.append([43, 70])
        candidates.append([42, 52])
        candidates.append([40, 44])
        candidates.append([39, 21])
        candidates.append([39, 46])
        candidates.append([38, 34])
        candidates.append([38, 48])
        candidates.append([38, 51])
        candidates.append([37, 42])
        candidates.append([35,  3])
        candidates.append([35, 18])
        candidates.append([35, 31])
        candidates.append([34, 28])
        candidates.append([34, 41])
        candidates.append([34, 58])
        candidates.append([32,  5])
        candidates.append([30, 26])
        candidates.append([30, 55])
        candidates.append([29, 47])
        candidates.append([29, 48])
        candidates.append([29, 54])
        candidates.append([28, 47])
        candidates.append([28, 48])
        candidates.append([28, 49])
        candidates.append([28, 59])
        candidates.append([27, 49])
        candidates.append([27, 54])
        candidates.append([27, 64])
        candidates.append([26,  4])
        candidates.append([26, 10])
        candidates.append([26, 29])
        candidates.append([25, 37])
        candidates.append([25, 42])
        candidates.append([25, 43])
        candidates.append([25, 56])
        candidates.append([24, 34])
        candidates.append([23, 45])
        candidates.append([23, 54])
        candidates.append([23, 74])
        candidates.append([22, 31])
        candidates.append([22, 42])
        candidates.append([22, 72])
        candidates.append([21, 22])
        candidates.append([21, 29])
        candidates.append([21, 30])
        candidates.append([21, 34])
        candidates.append([20, 15])
        candidates.append([20, 21])
        candidates.append([20, 31])
        candidates.append([20, 70])
        candidates.append([19, 25])
        candidates.append([19, 72])
        candidates.append([18, 41])
        candidates.append([17, 33])
        candidates.append([17, 50])
        candidates.append([17, 56])
        candidates.append([17, 74])
        candidates.append([16, 17])
        candidates.append([16, 56])
        candidates.append([16, 73])
        candidates.append([15, 24])
        candidates.append([15, 52])
        candidates.append([15, 74])
        candidates.append([14, 19])
        candidates.append([14, 71])
        candidates.append([13, 39])
        candidates.append([12, 25])
        candidates.append([12, 44])
        candidates.append([12, 47])
        candidates.append([10, 22])
        candidates.append([10, 52])
        candidates.append([ 9, 26])
        candidates.append([ 9, 44])
        candidates.append([ 9, 51])
        candidates.append([ 7, 40])
        candidates.append([ 5, 35])
        candidates.append([ 3, 28])
        candidates.append([ 3, 46])
        candidates.append([ 2, 22])
        candidates.append([ 1, 33])

        for candidate in candidates:
            location = self.loc_fix(candidate)
            self.sectors[location[0]][location[1]] = '*'

    def voids(self):
        candidates = []

        for ndx in range(20, 49):
            candidates.append([75, ndx])

        for ndx in range(22, 38):
            candidates.append([74, ndx])

        for ndx in range(25, 34):
            candidates.append([73, ndx])

        for ndx in range(26, 35):
            candidates.append([72, ndx])

        for ndx in range(25, 35):
            candidates.append([71, ndx])

        for ndx in range(27, 37):
            candidates.append([70, ndx])

        for ndx in range(28, 41):
            candidates.append([69, ndx])
            candidates.append([68, ndx])

        for ndx in range(29, 40):
            candidates.append([67, ndx])
            candidates.append([66, ndx])
            candidates.append([65, ndx])

        for ndx in range(30, 39):
            candidates.append([64, ndx])

        for ndx in range(30, 38):
            candidates.append([63, ndx])

        for ndx in range(30, 37):
            candidates.append([62, ndx])

        for ndx in range(29, 36):
            candidates.append([61, ndx])
            candidates.append([60, ndx])
            candidates.append([59, ndx])

        for ndx in range(29, 35):
            candidates.append([58, ndx])
            candidates.append([57, ndx])

        for ndx in range(29, 34):
            candidates.append([56, ndx])

        for ndx in range(29, 33):
            candidates.append([55, ndx])

        for ndx in range(29, 32):
            candidates.append([54, ndx])
            
        for ndx in range(30, 31):
            candidates.append([53, ndx])

        for ndx in range(64, 67):
            candidates.append([17, ndx])

        for ndx in range(63, 67):
            candidates.append([16, ndx])

        for ndx in range(62, 67):
            candidates.append([15, ndx])

        for ndx in range(62, 68):
            candidates.append([14, ndx])

        for ndx in range(61, 68):
            candidates.append([13, ndx])

        for ndx in range(60, 68):
            candidates.append([12, ndx])
            candidates.append([11, ndx])

        for ndx in range(60, 69):
            candidates.append([10, ndx])

        for ndx in range(59, 69):
            candidates.append([ 9, ndx])

        for ndx in range(73, 76):
            candidates.append([ 9, ndx])

        for ndx in range(59, 70):
            candidates.append([ 8, ndx])

        for ndx in range(73, 76):
            candidates.append([ 8, ndx])

        for ndx in range(59, 76):
            candidates.append([ 7, ndx])

        for ndx in range(58, 76):
            candidates.append([ 6, ndx])

        for ndx in range(57, 76):
            candidates.append([ 5, ndx])

        for ndx in range(55, 76):
            candidates.append([ 4, ndx])

        for ndx in range(52, 76):
            candidates.append([ 3, ndx])

        for ndx in range(51, 76):
            candidates.append([ 2, ndx])

        for ndx in range(49, 76):
            candidates.append([ 1, ndx])

        for ndx in range(5, 11):
            candidates.append([16, ndx])

        for ndx in range(4, 12):
            candidates.append([15, ndx])

        for ndx in range(3, 13):
            candidates.append([14, ndx])
            candidates.append([13, ndx])
            candidates.append([12, ndx])

        for ndx in range(3, 14):
            candidates.append([11, ndx])
            candidates.append([10, ndx])

        for ndx in range(2, 15):
            candidates.append([ 9, ndx])

        for ndx in range(1, 15):
            candidates.append([ 8, ndx])

        for ndx in range(1, 17):
            candidates.append([ 7, ndx])

        for ndx in range(1, 18):
            candidates.append([ 6, ndx])

        for ndx in range(1, 19):
            candidates.append([ 5, ndx])
            candidates.append([ 4, ndx])

        for ndx in range(1, 20):
            candidates.append([ 3, ndx])
            candidates.append([ 2, ndx])

        for ndx in range(1, 22):
            candidates.append([ 1, ndx])

        for candidate in candidates:
            location = self.loc_fix(candidate)
            self.sectors[location[0]][location[1]] = ' '

    def execute(self):
        self.planets()
        self.stargates()
        self.stars()
        self.voids()

        self.header_footer()

        ndx = 75
        for row in self.sectors:
            print(f"{ndx:02}:", end='')
            print("".join(row))
            ndx -= 1

        self.header_footer()

if __name__ == '__main__':
    driver = Solution()
    driver.execute()

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
