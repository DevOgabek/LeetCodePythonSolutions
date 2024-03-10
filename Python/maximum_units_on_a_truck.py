# Maximum Units on a Truck

class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda nums: -nums[1])
        max_truck_size = 0
        
        for box in boxTypes:
            max_truck_size += min(truckSize, box[0]) * box[1]
            truckSize -= box[0]
            
        return max_truck_size
    
solution = Solution()
print(solution.maximumUnits([[1,3],[2,2],[3,1]], 4))