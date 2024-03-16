# Destination City

class Solution(object):
    def destCity(self, paths):
        outgoing_cities = set()
        for path in paths:
            outgoing_cities.add(path[0])
        
        for path in paths:
            city = path[1]
            if city not in outgoing_cities:
                return city
    
solution = Solution()
print(solution.destCity([["pYyNGfBYbm","wxAscRuzOl"],["kzwEQHfwce","pYyNGfBYbm"]]))
