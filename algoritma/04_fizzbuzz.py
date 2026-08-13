class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        sonuc=[]
        for sayi in range(1,n+1):
            if sayi % 3 == 0 and sayi % 5 == 0:
                sonuc.append("FizzBuzz")
            elif sayi % 3== 0:
                 sonuc.append("Fizz")  
            elif sayi % 5 == 0:
                sonuc.append("Buzz")
            else:
                sonuc.append(str(sayi))
        return(sonuc)  