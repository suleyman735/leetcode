
class Palindrome:
    @staticmethod
    def isPolindrama(x):
        x = str(x) # Convert integer to string
        rev = ''
        for y in x:
            rev = y+rev
        return rev ==x    

    # or   
    #     x = str(x)
    # return x == x[::-1]  # Reverse the string and compare  
result = Palindrome.isPolindrama(121)
print(result)