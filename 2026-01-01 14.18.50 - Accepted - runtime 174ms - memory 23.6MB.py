class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        
        @cache
        def dp(pos, mask, tight, started):
            if pos == len(s):
                return 1 if started else 0
            
            limit = int(s[pos]) if tight else 9
            result = 0
            
            if not started:
                result += dp(pos + 1, mask, False, False)
            
            start = 0 if started else 1
            for d in range(start, limit + 1):
                if mask & (1 << d):
                    continue
                new_tight = tight and (d == limit)
                result += dp(pos + 1, mask | (1 << d), new_tight, True)
            
            return result
        
        return dp(0, 0, True, False)