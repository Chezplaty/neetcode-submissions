class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p, s] for p, s in zip(position, speed)]

        cars.sort(reverse=True)
        #insert first element
        stack = [(target - cars[0][0])/cars[0][1]]

        for pos, spd in cars:
            hours = (target - pos)/spd

            if stack and hours > stack[-1]:
                stack.append(hours)
        
        return len(stack)