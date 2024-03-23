# Maximum Units on a Truck

class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        total_units = 0
        boxes_added = 0
        
        for boxes, units_per_box in boxTypes:
            if boxes_added + boxes <= truckSize:
                total_units += boxes * units_per_box
                boxes_added += boxes
            else:
                remaining_space = truckSize - boxes_added
                total_units += remaining_space * units_per_box
                break
        
        return total_units
    
solution = Solution()
print(solution.maximumUnits([[1,3],[2,2],[3,1]], 4))