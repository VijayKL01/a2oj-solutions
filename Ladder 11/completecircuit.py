#CIRCUITCOMPLETE
import sys
class Solution:
    def canCompleteCircuit(self, A, B):
        s=0
        for i in range(len(A)):
            s+=A[i]-B[i]
        if(s<0):
            return(-1)
        k=sys.maxsize
        l=0
        for i in range(len(A)):
            l+=(A[i]-B[i])
            if(l>=0):
                k=min(k,i)
            else:
                k=sys.maxsize
                l=0
        return(k)
