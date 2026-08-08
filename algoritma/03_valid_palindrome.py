class Solution:
    def isPalindrome(self, s):
        temiz = ""
        for karakter in s:
            if karakter.isalnum():
                temiz = temiz + karakter.lower()
        sol = 0
        sag = len(temiz) - 1
        while sol < sag:
            if temiz[sol] != temiz[sag]:
                return False
            sol = sol + 1
            sag = sag - 1
        return True