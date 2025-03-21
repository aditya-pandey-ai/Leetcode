class Solution:
    def smallestNumber(self, s):
        res, stack = [], []
        for i,c in enumerate(s + 'I', 1):
            stack.append(str(i))
            if c == 'I':
                res += stack[::-1]
                stack = []
        return ''.join(res)

    def smallestNumber(self, s):
        res = []
        for i,c in enumerate(s + 'I', 1):
            if c == 'I':
                res += range(i, len(res), -1)
        return ''.join(map(str,res))

    def smallestNumber(self, s):
        res, pool = [], list('987654321')
        for k in map(len,s.split('I')):
            res += [pool.pop() for _ in range(k + 1)][::-1]
        return ''.join(res)
        