class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        #Read the array from the two ends and count the vowels
        
        vowel1 = 0
        vowel2 = 0
        for i in range(0,floor(len(s)/2)):
            if s[i] in "aieouAEIOU":
                vowel1 += 1
            if s[len(s)-1-i] in "aieouAEIOU":
                vowel2 += 1
        return vowel1 == vowel2
