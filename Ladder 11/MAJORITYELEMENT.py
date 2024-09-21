#MAJORITYELEMENT
class Solution:
    def majorityElement(self,A):
        vote = 0
        cand = sys.maxsize
        for num in A:
            if(vote == 0):
                cand = num
                vote = 1
            elif(num==cand):
                vote+=1
            else:
                vote-=1
        return cand

