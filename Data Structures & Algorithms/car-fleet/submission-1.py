class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        """
        position of the ith car
        speed of the ith car
        destination at target
        car can not pass
        car fleet
        car fleet non empty set of cars
        if  car catches up to car fleet the moment the fleet reaches the destination
        car part of the fleet
        what is the number of fleet
        """
        stack = []
        joined = []
        for i in range(len(position)):
            joined.append([position[i], speed[i]])
        joined  = sorted(joined)
        joined = joined[::-1]
        for i in range(len(joined)):
            time = (target - joined[i][0]) / joined[i][1]
            if stack:
                if time <= stack[-1]:
                    continue
                else:
                    stack.append(time)
            else:
                stack.append(time)
        return len(stack)

