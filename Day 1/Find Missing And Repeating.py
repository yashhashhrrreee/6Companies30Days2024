#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        arr.sort()
        dic = {}
        res = []
        es = 0
        s = 0
        for i in range(0, len(arr)):
            dic[arr[i]] = dic.get(arr[i], 0)+1
        for i in dic:
            if dic[i] == 2:
                res.append(i)
                break
    
        n = len(set(arr)) + 1
        s = sum(set(arr))
        es = n * (n+1)//2
        mis = es - s
        res.append(mis)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends