def get_longer_word(word1: str, word2: str) -> str:
    wordlen_one = len(word1)
    wordlen_two = len(word2)
    if wordlen_one > wordlen_two:
        return word1
    elif wordlen_one < wordlen_two:
        return word2
    else:
        return word1

# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
