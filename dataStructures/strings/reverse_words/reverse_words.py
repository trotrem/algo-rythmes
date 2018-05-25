# reverse words
# solution 1: add words into stack then print to stringIO in LIFO order
# word: split by whitespaces and at least 1 char long
#  _word_w___end
import io

def reverse_words(string):
    words = []
    start = 0
    end = 0
    while end < len(string):
        while start < len(string) and string[start] == " ":
            start += 1
        end = start
        while end < len(string) and string[end] != " ":
            end += 1
        if start < len(string):
            words.append(string[start:end])
        start = end
    buff = io.StringIO()
    while words:
        buff.write(words.pop())
        if words:
            buff.write(" ")
    return buff.getvalue()
