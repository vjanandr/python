print("Let us start the word count game")
sent_array = []


sent_array.append("Getting started with python")
sent_array.append("Its 12:15 lunch time python")
sent_array.extend(["Hopefully we will break by 5 python", "Need to get back to regular work python"])
"""
print("Input a string to create the database,"
     +" input Q or Quit to end the input :")
while 1:
    in_str = input(">>> ")
    if in_str.lower() == 'q' or in_str.lower() == "quit":
        print("Let us continue to the word counting game")
        break
    sent_array.append(in_str)
"""
    
common_words = set(sent_array[0].split(' '))
#common_words = set()
print(common_words)
skip_game = input("Do you wish to play the word count game ?: ").lower()== "n"
for sentence in sent_array:   
    if (not skip_game):
        u_cnt = int(input('Count the unique number of words in "%s" :'%(sentence)))
    words = sentence.split(' ')
    word_set = set(words)
    common_words.intersection_update(word_set)
    print("Common words set {}".format(common_words))
    print(words)
    print(word_set)
    if (not skip_game):
        if (u_cnt != len(word_set)):
            print("You got this wrong its not {u_cnt} but rather {0}".
                format(len(word_set), u_cnt = u_cnt))
            if input("Do you wish to continue ? press q to end :").lower() == 'q':
                skip_game = True
        else :
            print("Congratulations you got this right lets try the next one")

print("The common words in the sentences are {}".format(common_words))