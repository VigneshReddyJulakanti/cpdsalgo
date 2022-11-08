https://leetcode.com/contest/biweekly-contest-78/problems/maximum-white-tiles-covered-by-a-carpet/
class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        q=collections.deque()
        best=0
        current=0
        for ltil,rtil in tiles:
            q.append((ltil,rtil))
            current+=rtil-ltil+1
            
            while(len(q)>0):
                tlef,trig=q[0]
                leftmost=rtil-carpetLen+1
                
                if trig<leftmost:
                    current-=trig-tlef+1
                    q.popleft()
                    continue
                if tlef <leftmost:
                    current-=leftmost-tlef
                    q.popleft()
                    q.appendleft((leftmost,trig))
                    break
                break
            best=max(current,best)
        return best
        
class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        arr=[0]
        tiles.sort()
        for i,j in tiles:
            arr.append(arr[-1]+j-i+1)
        n=len(tiles)
        ans=0
        for i in range(n):
            rightmost=tiles[i][0]+carpetLen-1
            l=i
            r=n-1
            while(l<=r):
                mid=int((l+r)/2)
                if tiles[mid][1]==rightmost:
                    r=mid
                    break
                    
                elif tiles[mid][1]>rightmost:
                    r=mid-1
                else:
                    l=mid+1
            curr=arr[r+1]-arr[i]
            if(r+1<n):
                curr+=max(0,rightmost-tiles[r+1][0]+1)
            ans=max(curr,ans)
        return ans
            
            
            
        
        
            
        
        