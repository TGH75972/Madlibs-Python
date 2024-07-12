import random

def get_word(word_type):
    return input(f"Please enter a {word_type}: ")

def create_story(words, template):
    return template.format(**words)

def main():
    print("Welcome to the Mad Libs weird game!")

    stories = [
        {
            "title": "A Day with Pickles",
            "template": """
            Once upon a time, there was a {adjective1} pickle named {name}. This pickle loved to {verb} every day.
            One day, {name} found a {adjective2} {noun1} and decided to {verb_past} it. It was a {adjective3} day!
            """
        },
        {
            "title": "The Hacker's Life",
            "template": """
            In a {adjective1} room, a hacker named {name} was busy trying to {verb}. Suddenly, the {noun1} beeped.
            It was a message from {adjective2} {noun2} asking for help to {verb_past}. This was going to be an {adjective3} day!
            """
        },
        {
            "title": "A Day at the Job",
            "template": """
            {name} was a {adjective1} worker at the local {noun1}. Every day, {name} would {verb} to make sure everything was {adjective2}.
            One day, {name} found a {adjective3} {noun2} in the office and decided to {verb_past}. It was the most {adjective4} day at work!
            """
        },
        {
            "title": "College Life",
            "template": """
            College life was {adjective1} for {name}. Every day, {name} would {verb} with friends at the {noun1}.
            One day, they decided to {verb_past} a {adjective2} {noun2}. It turned out to be the most {adjective3} experience of their college life!
            """
        },
        {
            "title": "Life in the Village",
            "template": """
            In the {adjective1} village of {name}, everyone knew how to {verb}. The villagers were {adjective2} and always helped each other with {noun1}.
            One day, {name} found a {adjective3} {noun2} and decided to {verb_past}. It was a {adjective4} day in the village!
            """
        }
    ]

    selected_story = random.choice(stories)

    print(f"\nTry Reading this first?:\n{selected_story['template']}\n")

    words_needed = [
        "adjective1", "name", "verb", "noun1", "adjective2", "verb_past"
    ]
    
    if "{adjective3}" in selected_story["template"]:
        words_needed.append("adjective3")
    if "{noun2}" in selected_story["template"]:
        words_needed.append("noun2")
    if "{adjective4}" in selected_story["template"]:
        words_needed.append("adjective4")

    words = {word: get_word(word) for word in words_needed}

    story = create_story(words, selected_story["template"])
    print(f"\nHere's your Mad Libs story: {selected_story['title']}")
    print(story)

    print("\nHere are the words you used:")
    for key, value in words.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
