def vdecoder(message,keyword):
    # decoder for the vignere cipher. shifts each letter of a message to the left along the alphabet 
    # by the index of the corresponding letter of the keyword phrase in the alphabet.
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    
    i = 0
    j = 0 # counts length of keyword phrase
    while i < len(message):
        
        if message[i] in alphabet:
            # shift message[i] to the left by the index of keyword_phrase[j] in alphabet
            location_in_alphabet = alphabet.find(message[i])
            shift = alphabet.find(keyword[j%len(keyword)])
            output += alphabet[(location_in_alphabet-shift) % 26]
            j += 1
        else:
            output += message[i]
            
        i+= 1
        
    return output

print(vdecoder("dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!","friends"))
