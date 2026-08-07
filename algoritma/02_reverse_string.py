class Solution:
    def reverseString(self, s):
        sol = 0
        sag = len(s) - 1
        while sol < sag:
            s[sol], s[sag] = s[sag], s[sol]
            sol = sol + 1
            sag = sag - 1