#!/usr/bin/python3

print("Let us start the word count game")
sent_array = []

"""
sent_array.append("Getting started with python")
sent_array.append("Its 12:15 lunch time")
sent_array.extend(["Hopefully we will break by 5", "Need to get back to regular work"])
"""

print("Input a string to create the database,"
     +" input Q or Quit to end the input :")
while 1:
    in_str = input(">>> ")
    if in_str.lower() == 'q' or in_str.lower() == "quit":
        print("Let us continue to the word counting game")
        break
    sent_array.append(in_str)

for sentence in sent_array:
      u_cnt = int(input('Count the number of words in "%s" :'%(sentence)))
      words = sentence.split(' ')
      print(words)
      if u_cnt != len(words):
         print("You got this wrong its not {u_cnt} but rather {0}".
                 format(len(words), u_cnt = u_cnt))
         if input("Do you wish to continue ? press q to end :").lower() == 'q':
            break
      else:
         print("Congratulations you got this right lets try the next one")
