def cdecoder(message,offset):
    # decoder for the caesar chipher. shifts all letters of a message by [offset] along the alphabet to the right.
 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = []
    words = message.split()
    
    for word in words:
      
        decoded_word = []
        for i in range(len(word)):
          
            if word[i] in alphabet:
                # move right [offset] spaces and append to decoded_word
                location_in_alphabet = alphabet.find(word[i])
                decoded_word.append(alphabet[(location_in_alphabet+offset) % 26])
            else:
                decoded_word.append(word[i])
                
        decoded_word = "".join(decoded_word)
        output.append(decoded_word)
    
    return " ".join(output)

print(cdecoder("xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!",10))
