for countdown in 5, 4, 3, 2, 1, "hello":
    print(countdown)

# hello 주석

cliches = [
    "At the end of the day",
    "Having said that",
    "The fact of the matter is",
    "Be that as it may",
    "The bottom line is",
    "If you will",
]


print(cliches[3])


quotes = {
    "Moe": "A wise guy, huh?",
    "Larry": "Owl",
    "Curly": "Nyuk nyuk!",
}

print("Curly", "says:", quotes["Curly"])


import json
from urllib.request import urlopen

url = "https://api.github.com/users/soongon"
response = urlopen(url)
contents = response.read();
text = contents.decode('utf8')
data = json.loads(text)
print(data)