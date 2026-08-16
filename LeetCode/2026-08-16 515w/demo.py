class Solution1:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        mini = float("inf")
        ans = -1
        tx,ty = target
        for i in range(len(drones)):
            x,y,r = drones[i]
            dist = abs(tx-x) + abs(ty-y)
            # print(dist,i,mini)
            if dist <= r and dist < mini:
                ans = i
                mini = dist
        return ans
class Solution2:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        maxlight = max(lights)
        a = arrivalTime
        rem = [i%period for i in a]
        maxi = 0
        n = len(lights)
        for i in rem:
            if maxlight <= i:
                maxi = max(maxi, period - i)
        return maxi








