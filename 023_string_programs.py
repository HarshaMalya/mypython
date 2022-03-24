def split_string(line_of_text):
    words = line_of_text.split()
    print(words)
    return words

text = input("Enter a lime of text: ")
my_word_list = split_string(text)
print( "The words in given line are:{}".format( my_word_list))
print( "The number of words in line are: {}".format( len(my_word_list)))
