"""
There is a set of words and a query word.
You must change exactly one character of the query word.
Implement a function that determins whether the changed word can be the element of the set.

* Condition: Words consist of only lower-case alphabet(s) and no space.


>>>P10({"data", "science"}, "data")
False
Explanation: If you change one character of the query word, there is no matching word in the set.

>>>P10({"data", "science"}, "daaa")
True
Explanation: You can change one alphabet to make "daaa" -> "data" .

>>>P10({"data", "science"}, "scienzz")
False

>>>P10({"data", "science", "scienze"}, "scienzz")
True

>>>P10({"data", "science"}, "dataa")
False
"""

def P10(word_set, query_word):
    a = len(query_word)
    b = 0
    for i in word_set:
        if len(i) == a:
            for n in range(0,a):
                if i[n] == query_word[n]:
                    continue
                elif i[n] != query_word[n]:
                    b = b+1
        if b == 1:
            break
        if b != 1:
            b = 0
                    
    if b == 1:
        return True
    else:
        return False