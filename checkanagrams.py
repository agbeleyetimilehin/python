def checkanagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)

print(checkanagram("world", "lord"))
print(checkanagram("ocean", "canoe"))
print(checkanagram("artist", "strait"))