https://leetcode.com/discuss/interview-question/3229839/Benchling-or-Phone-or-Generate-Protein
https://leetcode.com/discuss/interview-question/1386125/Benchling-Phone-interview

sequences

('acG', 0, 5)
('Bf5', 0, 22)
('e5c', 5, 16)
('6a5d', 5, 17)
('7f6c', 2, 13)
('0Pf', 13, 23)
('0f5c', 0, 13)

protein // sequence start and end
[
('acG', 0, 5)
('Bf5', 0, 22),
('e5c', 5, 16),
('6a5d', 5, 17)
('7f6c', 2, 13),
('0Pf', 13, 23), 
('0f5c', 0, 13),
('acG_e5c', 0, 16),
('acG_6a5d', 0, 17),
('7f6c_0Pf', 2, 23),
('0f5c_0Pf', 0, 23),
]


The question is, given a list of gene sequences, find generate all possible proteins.
In the exampe above, the answer would be:


class ProteinSequencing:

    def generateProteins(self, sequences):
        ## map that indexes from start index to protein and end index
        ## e.g. ('acG', 0, 5) creates entry
        ## 0 -> ('acG', 5)
        startToProteinAndIndex = {}
        for seq in sequences:
            ## current algorithm fails because ('6a5d', 5, 17) overwrites ('e5c', 5, 16)
            ## can account for this by pointing to a list
            startToProteinAndIndex[seq[1]] = (seq[0], seq[2])
        results = []
        results.extend(sequences)
        index = 0
        proteinAdded = True
        while proteinAdded:
            proteinAdded = False
            newResults = []
            for i in range(index, len(results)):
                protein = results[i]
                # if end index is in the map, add to the protein
                if protein[2] in startToProteinAndIndex:
                    prevProteinName, prevProteinEnd = startToProteinAndIndex.get(protein[2])
                    newProtein = protein[0] + '_' + prevProteinName
                    newResult = (newProtein, protein[1], prevProteinEnd)
                    newResults.append(newResult)
                    proteinAdded = True
            ## avoid infinite while loop by adding the same protein over and over
            index = len(results)
            results.extend(newResults)
        return results

sequences = [('acG', 0, 5), ('Bf5', 0, 22), ('e5c', 5, 16), ('7f6c', 2, 13), ('0Pf', 13, 23), ('0f5c', 0, 13)]
expected = [('acG', 0, 5), ('Bf5', 0, 22),('e5c', 5, 16),('7f6c', 2, 13),('0Pf', 13, 23),('0f5c', 0, 13),('acG_e5c', 0, 16),('acG_6a5d', 0, 17),('7f6c_0Pf', 2, 23),('0f5c_0Pf', 0, 23),]

proteinSeq = ProteinSequencing()
answer = proteinSeq.generateProteins(sequences)

assert(sorted(answer) == sorted(expected))

They asked me a slightly different question

for this input:

acG,0,5
Bf5,0,22
e5c,5,16
6a5d,5,17
7f6c,2,13
0Pf,13,23
0f5c,0,13
abc,0,4
def,4,7
ghi,7,9

this is the output:
acG-e5c,0,16
acG-6a5d,0,17
7f6c-0Pf,2,23
0f5c-0Pf,0,23
abc-def-ghi,0,9

the difference is that items can be chained (potentially endlessly), notice the last 3 inputs
abc,0,4
def,4,7
ghi,7,9

generate a single output
abc-def-ghi,0,9

