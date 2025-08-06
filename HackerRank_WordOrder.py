

"""

You are given n words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

"""

def wordOrder(file_path):
    words = []

    wordsCount ={}

    number_of_unique_words = 0

    with open(file_path, 'r') as file:
        number_of_unique_words = int(file.readline().strip())
        words = file.read().split("\n")

    for item in words:
        if(item in wordsCount):
            occurence = wordsCount[item]
            wordsCount[item] = occurence + 1
        else:
            wordsCount[item] = 1

    for value in wordsCount.values():
        print(value)

if __name__ == "__main__":
    wordOrder("/Users/alexbrito/Documents/Development/LeetCodePython/wordOrder.txt")

