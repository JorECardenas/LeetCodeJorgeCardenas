class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = {}
        for n in nums:
            if n not in counter:         
                counter[n] = 0
            counter[n] += 1


        counter = dict(reversed(sorted(counter.items(), key=lambda x:x[1])))

        solution = [[] for _ in range(max(counter.values()))]

        for i in counter.keys():
            for j in range(counter[i]):
                solution[j].append(i)


        return solution

