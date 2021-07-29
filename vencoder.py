def vencoder(message,keyword):
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    
    i = 0
    j = 0 # counts length of keyword phrase
    while i < len(message):
        
        if message[i] in alphabet:
            # shift message[i] to the right by the index of keyword_phrase[j] in alphabet
            location_in_alphabet = alphabet.find(message[i])
            shift = alphabet.find(keyword[j % len(keyword)])
            output += alphabet[(location_in_alphabet+shift) % 26]
            j += 1
        else:
            output += message[i]
            
        i+= 1
        
    return output

print(vencoder("you were able to decode this? nice work! you are becoming quite the expert at crytography!","friends"))
