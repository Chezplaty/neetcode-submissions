class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position or not speed:
            return 0

        cars = [0] * len(position)

        for i in range(len(position)):
            cars[i] = (position[i], speed[i])

        cars.sort(reverse=True)
        #insert first element
        stack = [(target - cars[0][0])/cars[0][1]]
        
        for pos, spd in cars:
            hours = (target - pos)/spd

            if stack and hours > stack[-1]:
                stack.append(hours)
        
        return len(stack)