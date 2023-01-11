from collections import defaultdict

def group_anagrams(a):
    defdict = defaultdict(list)
    for i in a:
        sorted_i = " ".join(sorted(i))
        defdict[sorted_i].append(i)
    return defdict.values()

words = ["earth", "prince", "listen", "silent", "heart", "pincer", "crane"]
print(group_anagrams(words))