def cencoder(message,offset):
    # encoder for the caesar chipher. shifts all letters of a message by [offset] along the alphabet to the left.
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = []
    words = message.split()
    
    for word in words:
      
        encoded_word = []
        for i in range(len(word)):
          
            if word[i] in alphabet:
                # move left [offset] spaces and append to encoded_word
                location_in_alphabet = alphabet.find(word[i])
                encoded_word.append(alphabet[(location_in_alphabet-offset) % 26])
            else:
                encoded_word.append(word[i])
                
        encoded_word = "".join(encoded_word)
        output.append(encoded_word)
    
    return " ".join(output)

print(cencoder("‘bokanovsky’s process,’ repeated the director, and the students underlined the words in their little note-books.",10))
