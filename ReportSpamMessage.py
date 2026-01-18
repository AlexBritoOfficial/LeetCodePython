# You are given an array of strings message and an array of strings bannedWords.
#
# An array of words is considered spam,
# if there are at least two words in it that exactly match any word in bannedWords.
# Return true if the array message is spam, and false otherwise.

# Example 1:
# Input: message = ["hello", "world", "leetcode"], bannedWords = ["world", "hello"]
# Output: true
# Explanation: The words "hello" and "world" from the message array both appear in the bannedWords array.

# Example 2:
# Input: message = ["hello", "programming", "fun"], bannedWords = ["world", "programming", "leetcode"]
# Output: false

# Constraints:
#  1 <= message.length, bannedWords.length <= 105
# 1 <= message[i].length, bannedWords[i].length <= 15
# message[i] and bannedWords[i] consist only of lowercase English letters.


def reportSpam(message, bannedWords):
    """
    :type message: List[str]
    :type bannedWords: List[str]
    :rtype: bool
    """

    count = 0
    bannedSet = set(bannedWords)

    for val in message:
        if val in bannedSet:
            count = count + 1

        if count >= 2:
            return True
    return False




if __name__ == "__main__":

    # message = ["hello","world","leetcode"]
    # banneedWords = ["world","hello"]

    message = ["hello","world","leetcode"]
    banneedWords = ["world","hello"]


    print(reportSpam(message, banneedWords))