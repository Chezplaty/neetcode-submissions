class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []

        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        
        for car in sorted(cars, reverse = True):
            position, speed = car
            time = (target - position)/speed
            if not stack or time > stack[-1]:
                stack.append(time)
            
        return len(stack)
    
        