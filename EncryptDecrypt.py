import os
#
#  This program allows a user to convert between Pig Latin.
#  The user also has the option to encrypt or decrypt (symmetric encryption algorithm)
#

# Prompt for Text
def promptText():
   """ Prompt for text """
   os.system('cls')
   text = input("\n\tEnter the text to be manipulated: ")
   while text == "":
      text = input("\tEnter the text to be manipulated: ")
   return text

# Prompt for key
def promptKey():
   """ Prompt for key """
   os.system('cls')
   key = input("\n\tEnter the key: ")
   while key == "":
      key = input("\tEnter the key: ")
   return key

# Convert from plain text to Pig Latin
def toPigLat(pText):
   """ Converts a plain text message to Pig Latin """
   pWords = pText.split(' ') # split the plain words into an array
   latWords = [] # create an empty array to hold the Pig Latin words
   for word in pWords:
      if word != "":
         word = "{}{}ay".format(word[1:len(word)], word[0]) # format the word into Pig Latin
         latWords.insert(len(latWords), word) # add the Pig Latin word to the end of the array
   return " ".join(latWords) # return the Pig Latin words joined by spaces

# Convert from Pig Latin to plain text
def toPlainText(latText):
   """ Converts a Pig Latin message to plain text """
   lWords = latText.split(' ') # split string into words and place in array
   plainWords = [] # create empty array to hold plain words
   for word in lWords:
      lat = word.replace(word[-2:len(word)], "") # remove the 'ay' from word
      first = lat[-1] # collect the first letter of the plain word from end of lat
      rest = lat.replace(lat[-1], "") # isolate the rest of the word
      plainWord = "{}{}".format(first, rest) # put the plain word together
      plainWords.insert(len(plainWords), plainWord) # add the plain word to end of array
   return " ".join(plainWords) # return the plain words joined by spaces

# Convert from plain text to Pig Latin then cipher text
def encrypt(eText):
   pigText = toPigLat(eText) # Convert to Pig Latin
   key = promptKey() # Get the key
   os.system('cls') # clear console
   cipherText = "" # To hold final cipher text
   for p in pigText:
      charTotal = ord(p) # initialize the total ascii value to that of the current character
      for k in key:
         charTotal += ord(k) # add the ascii values of each key character
      c = chr(charTotal) # make the final character
      cipherText += c # add the character to
   return cipherText # return the cipher text

# Convert from ciper text to Pig Latin then plain text
def decrypt(dText):
   key = promptKey() # get key
   os.system('cls') # clear the console (windows)
   latText = "" # create an empty string to hold the Pig Latin text
   for p in dText:
      charDiff = ord(p) # initialize the ascii difference to that of the current character
      for k in key:
         charDiff -= ord(k) # subtract the ascii value of each character in the key
      c = chr(charDiff) # make the character after subtracting each of the key chars
      latText += c # append the character to the Pig Latin string
   pText = toPlainText(latText) # convert the Pig Latin to plain text
   return pText # return the plain text


# Program flow
def main():
   os.system('cls')
   text = promptText() # Prompt for string to be manipulated
   os.system('cls')

   while True:
      print("\n\tText:", text) # print the working string

      print("\tChoose an operation:")
      print("\t  1. Convert to Pig Latin")
      print("\t  2. Encrypt")
      print("\t  3. Contert to plain text")
      print("\t  4. Decrypt")
      print("\t  5. Exit")
      choice = input("\t>> ")

      # Decifer choice
      if choice == '1' or choice == 'latin':
         # Convert to Pig Latin
         # Print
         os.system('cls')
         print('')
         newText = toPigLat(text)
         print("\n\tPig Latin:", newText)
         input("\n\tPress ENTER to continue...")
         text = newText
         os.system('cls')
      elif choice == '2' or choice == 'encrypt':
         # Convert to Pig Latin and Ecrypt
         # Print
         os.system('cls')
         print('')
         newText = encrypt(text)
         print("\n\tCipher text:", newText)
         input("\n\tPress ENTER to continue...")
         text = newText
         os.system('cls')
      elif choice == '3' or choice == 'plain':
         # Convert to plain text
         # Print
         os.system('cls')
         print('')
         newText = toPlainText(text)
         print("\n\tPlain text:", newText)
         input("\n\tPress ENTER to continue...")
         text = newText
         os.system('cls')
      elif choice == '4' or choice == 'decrypt':
         # Convert to Pig Latin then plain text
         # Print
         os.system('cls')
         newText = decrypt(text)
         print("\n\tPlain text:", newText)
         input("\n\tPress ENTER to continue...")
         text = newText
         os.system('cls')
      elif choice == '5' or choice == 'exit':
         # Exit the program
         os.system('cls')
         exit()
      else:
         # Error Message
         print("\tThat was not and option.")
         os.system('cls')
   os.system('cls')


if __name__ == '__main__':
   main()
