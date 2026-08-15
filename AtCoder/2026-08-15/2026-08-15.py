import sys
input = sys.stdin.readline
import heapq
def main():
    n,v = map(int,input().split())

    pq = []
    for _ in range(n):
        query = list(map(int,input().split()))
        if len(query) == 3:
            ty,t,w = query
            heapq.heappush(pq,-(w-t))
        else:
            ty,t = query
            if pq:
                temp = -heapq.heappop(pq)
                ans = min(v,t + temp)
                print(ans)
            else:
                print(-1)

 
main()

# import sys
# input = sys.stdin.readline

# class Node:
#     def __init__(self,val):
#         self.val = val
#         self.next = None
#         self.prev = None

# def main():
#     n = int(input())
#     nums = list(map(int, input().split()))
#     left,right = [],[]
#     for i in nums:
#         if i<0: left.append(i)
#         else:
#             right.append(i)
#     left.sort()
#     right.sort(reverse=True)
#     m1 = len(left)
#     m2 =n - m1
#     ans = cur = 0
#     while left or right:
#         if not left:
#             ans += abs(cur - right[-1])
#             cur = right.pop()
#         elif not right:
#             ans += abs(cur-left[-1])
#             cur = left.pop()
#         else:
#             l = abs(cur-left[-1])
#             r = abs(cur - right[-1])
#             if l<=r:
#                 ans += l
#                 cur = left.pop()
#             else:
#                 ans += r
#                 cur = right.pop()
#     print(ans)
#     # -1 -4 -7 2 -11
# main()



# import sys
# input = sys.stdin.readline

# def main():
#     n = int(input())
#     mp ={}
#     for _ in range(n):
#         x = input().lower()
#         mp[x] =mp.get(x,0) +1
#     print(max(mp.values()))

# main()










