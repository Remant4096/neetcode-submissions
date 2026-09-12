class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        temp_stack = list()
        index_stack = list()
        output = [0]*len(temperatures)

        for i, temp  in enumerate(temperatures):

           
            while(temp_stack and temp > temp_stack[-1]):

                temp_stack.pop()
                day =index_stack.pop()
                output[day] = i - day

                

            temp_stack.append(temp)
            index_stack.append(i)


        return output