Pirate speak translator translates any sentences typed in English by the client to Pirate speak by modifying a slected list of words into pirate speak. 

The working of the translator can be split into three stages,

Stage 1: The server is modified to send the message it recieved from the client back to the client. The client then prints out the message. This keeps happening until the user closes the client. 

Stage 2: A list of selected pirate speak words and it's english translation is put into a dictionary. 

Stage 3: When the client, types in a word that is in the dictionary, the server checks the pirate translation for that word in the dictionary and it translates it into pirate speak. The server does this for every word in the sentence that matches the list of English words stored in the dictionary. After, the translation is done, the server sends the translated sentence to the client. 
