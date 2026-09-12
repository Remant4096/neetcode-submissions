class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:

        #sorting based on position

        def sort_together(a, b):
            n = len(a)

            def heapify(i, size):
                while True:
                    largest = i
                    left = 2 * i + 1
                    right = 2 * i + 2

                    if left < size and a[left] > a[largest]:
                        largest = left

                    if right < size and a[right] > a[largest]:
                        largest = right

                    if largest == i:
                        break

                    a[i], a[largest] = a[largest], a[i]
                    b[i], b[largest] = b[largest], b[i]

                    i = largest

            # Build max heap
            for i in range(n // 2 - 1, -1, -1):
                heapify(i, n)

            # Sort
            for i in range(n - 1, 0, -1):
                a[0], a[i] = a[i], a[0]
                b[0], b[i] = b[i], b[0]

                heapify(0, i)

        sort_together(position,speed)
        # time = [(target- position[i])/speed[i] for i in range(len(speed))]

        # print(position,speed,time)

        if(speed[-1] != 0):
            top = (target - position[-1])/speed[-1]
        else:
            top = math.inf

        fleet = 1

        for i in range(len(position)-1,-1,-1):

            if(speed[i] != 0):
                time = (target - position[i])/speed[i]
            else:
                time = math.inf

            if(time>top):
                top = time
                fleet += 1

        return fleet