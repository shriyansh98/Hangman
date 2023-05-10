
my_file = open("wordsfile.txt", "r")

data = my_file.read()
  

data_into_list = data.split("\n")
hangman_words = data_into_list
#print(hangman_words)
my_file.close()