class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = [1,1,1,1,1]
        if n==1:
            return sum(vowels)
        for i in range(2, n+1):
            new_vowels = vowels.copy()
            for j in range(3, -1, -1):
                new_vowels[j] = sum(vowels[j:])
            vowels = new_vowels
        return sum(vowels)