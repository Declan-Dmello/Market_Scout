import requests

# Word
my_word = ("Stock Split")

# Get Info
req = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{my_word}")

# Print result
print(req.text)

#Work on the design and other section of the page
#include news here