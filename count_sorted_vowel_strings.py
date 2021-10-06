class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ["a","e","i","o","u"]
        ans_set = vowels.copy()
        if n==1:
            return len(ans_set)
        for i in range(2, n+1):
            new_set = []
            for j in ans_set:
                start = vowels.index(j[-1])
                for k in vowels[start:]:
                    j+=k
                    new_set.append(j)
            ans_set = new_set
        return len(ans_set)
        