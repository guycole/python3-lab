class ClosestWordIndexSolver:
    dd = {}
    
    def __init__(self, word_list: list[str]):
        for ndx in range(len(word_list)):
            if word_list[ndx] in self.dd:
                temp = self.dd[word_list[ndx]]
                temp.append(ndx)
                self.dd[word_list[ndx]] = temp
            else:
                self.dd[word_list[ndx]] = [ndx]
      
    def min_index_distance(self, word1: str, word2: str) -> int:
        # quick, fox
        candidate1 = self.dd[word1]
        print(candidate1)
        candidate2 = self.dd[word2]
        print(candidate2)

        min_value = 100
        
        for ndx1 in range(len(candidate1)):
            for ndx2 in range(len(candidate2)):
#                print(f"candidate1 {ndx1} {candidate1} {word1}")
#                print(f"candidate2 {ndx2} {candidate2} {word2}")
                temp = candidate2[ndx2] - candidate1[ndx1]
#                print(temp)
                min_value = min(temp, min_value)

        return abs(min_value)

word_list = ['the','quick','brown','fox','jumped','over','the','lazy','fox']

cwis = ClosestWordIndexSolver(word_list)

#print(f"min distance {cwis.min_index_distance('quick', 'fox')}") #2
#print(f"min distance {cwis.min_index_distance('the', 'over')}") #1
print(f"min distance {cwis.min_index_distance('jumped', 'quick')}") #3
#print(f"min distance {cwis.min_index_distance('the', 'the')}")
#print(f"min distance {cwis.min_index_distance('fox', 'fox')}")

