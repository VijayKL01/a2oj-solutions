#HIGHESTPRODUCT
class Solution:
	# @param A : list of integers
	# @return an integer
	def maxp3(self, A):
       N=len(A)
       A.sort()
       p1=A[N-1]*A[N-2]*A[N-3]
       p2=A[0]*A[1]*A[N-1]
       return max(p1,p2)