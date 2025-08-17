"""
You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.

In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i] are anagrams,
 and delete words[i] from words. Keep performing this operation as long as you can select an index that satisfies the conditions.

Return words after performing all operations.

It can be shown that selecting the indices for each operation in any arbitrary order will lead to the same result.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once. For example, "dacb" is an anagram of "abdc".



"""
from collections import Counter


def removeAnagrams(words):
    """"
        1 <= words.length <= 100
        1 <= words[i].length <= 10
        words[i] consists of lowercase English letters.

        First Case: if the words array contains only one element, return the list.

        ["abba","baba","bbaa","cd","cd"]

    """

    list = []
    for i in range(len(words)):
        print(Counter(words[i]))
        if not list or not (Counter(words[i]) == Counter(list[-1])):
            list.append(words[i])

    return list






if __name__ == "__main__":
    list = ["abba", "baba", "bbaa", "cd", "cd"]
    removeAnagrams(words=list)
