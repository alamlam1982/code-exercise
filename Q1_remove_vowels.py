# Python program to remove vowels from a string 
# Function to remove vowels 
def rem_vowel(string): 
    vowels = ('a', 'e', 'i', 'o', 'u','A','E','I','O','U')  
    for x in string: 
        if x in vowels: 
            string = string.replace(x, "") 
              
    # Print string without vowels 
    print(string) 
  
# Driver program 
string = "GeeksforGeeks - A Computer Science Portal for Geeks"
rem_vowel(string) 
