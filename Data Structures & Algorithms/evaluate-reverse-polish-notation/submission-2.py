class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = deque()

        def evaluate(a,b,sign):
            if (sign == '+'):
                return a+b
            elif (sign ==  '-'):
                return a-b
            elif (sign ==  '*'):
                return a*b
            elif (sign ==  '/'):
                return int(a/b)

        for val in tokens:
            if (val == '+' or val == '*' or val == '/' or val == '-'):
                b = stack.pop()
                a = stack.pop()
                stack.append(evaluate(a,b,val))
            else:
                stack.append(int(val))



        return stack[-1]
