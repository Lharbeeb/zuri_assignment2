from itertools import count


def read_file_content(filename):
    with open(filename) as f:
        lines = f.readline()
        return lines
# print(read_file_content("story.txt"))
def count_words():
    word1 = read_file_content("story.txt")
    list1 = word1.split()
    my_dictionary={}
    for word in list1:
        my_dictionary[word]= list1.count(word)
    return my_dictionary
print(count_words())
