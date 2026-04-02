class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        #condition for new fleet, if the car reaches the target after the car infront

        #we append a car to the fleet if the total time taken is greater than (current fleet)stack[-1]        

        #we then sort that array by current position with car closest to end (largest value) at the beggining

        #we then iterate through the array calculating time and implement our stack logic

        #the length of the stack is the number of fleets


        stack = []

        cars = []

        #create an array that is sorted in reverse order with position:speed pairs

        cars = sorted(zip(position, speed), reverse=True)

        for pos,spd in cars:

            #we calculate total time by subtracting each cars position from the target and dividing by speed of the car

            time = ((target - pos) / float(spd))

            if not stack or (time > stack[-1]):

                stack.append(time)

        return len(stack)
