def add_songs(*args):
    dic_songs = {}
    for el in args:
        name = el[0]
        lyrics = el[1]
        if name not in dic_songs:
            dic_songs[name] = []
            dic_songs[name].append(lyrics)

        else:
            if lyrics:
                dic_songs[name].append(lyrics)
    result = ""
    for key, value in dic_songs.items():
        result += f"- {key}\n"
        if value != [[]]:
            if len(value) == 1:
                for el in value:
                    for e in el:
                        result += f"{e}\n"
            else:
                for idx in range(len(value)):
                    element = value[idx]
                    for e in element:
                        result += f"{e}\n"

    return result

print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))

print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
