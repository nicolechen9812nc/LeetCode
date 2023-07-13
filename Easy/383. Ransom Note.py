#Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

#Each letter in magazine can only be used once in ransomNote.

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        magazine = list(magazine)
        for i in ransomNote:
            if (i not in magazine):
                return False
            magazine.remove(i)
        return True
