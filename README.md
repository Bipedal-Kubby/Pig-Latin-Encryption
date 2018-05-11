Pig-Latin-Encryption
This is a Python encryption program.
In this program, the user is first prompted for a string to be manipulated.
Afterword, the user selects an option from a menu about what action to perform on the string.
The options are as follows:
  1. Convert to Pig Latin
  2. Encrypt
  3. Convert to plain text
  4. Decrypt
  5. Exit
To these, the user can respond with the number or 'latin', 'encrypt', 'plain', 'decrypt', or 'exit', respectively.

Within the encrypt function, the user is prompted for a key.
Then, the text is converted to Pig Latin. (orFay xample,eay histay entence.say)
The encryption consists of taking the ASCII value of each character in the Pig Latin text and adding the ASCII values of each character in the key. Then the resulting sum is converted back into a character and appended to a new string holding the result. 
