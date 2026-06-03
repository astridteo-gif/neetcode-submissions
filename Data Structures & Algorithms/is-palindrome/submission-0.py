class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_s = "".join(char.lower() for char in s if char.isalnum())

        front_pointer = 0
        back_pointer = len(cleaned_s) - 1 

        while front_pointer < back_pointer: 
            if cleaned_s[front_pointer] != cleaned_s[back_pointer]:
                return False

            front_pointer += 1 
            back_pointer -= 1

            
        return True
