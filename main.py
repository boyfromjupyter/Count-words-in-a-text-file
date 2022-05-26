# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename) as f:
        contents = f.read()
    return contents


def count_words(input):
    text = read_file_content(input).split( )
    dictn = {}
    for word in text:
        dictn[word] = text.count(word)
    return dictn

print(count_words('story.txt'))