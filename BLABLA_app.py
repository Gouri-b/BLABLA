#BLABLA
"""TO BLABLA THROUGH LIFE"""
import random

# Nonsensical phrase database
nonsense_phrases = [
    "Bla bla buu buu, flibberdigibbet?",
    "Wizzle whim wham, wum wum wah woo!",
    "Flapdoodle frolic, jimjam wizzle.",
    "Gobbledygook, jabberwocky, blerg!",
    "Pish posh, tiddledee, wuggle wum!",
    "Meow meow bow bow quack quack"
]

def generate_nonsense():
    """Return a random nonsensical phrase."""
    return random.choice(nonsense_phrases)

def conversation_mode():
    """Simulate a conversation."""
    print("You: Hi!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        print("Bla.. Bla:", generate_nonsense())

def debate_mode():
    """Simulate a debate."""
    topics = ["cats vs dogs", "pineapple pizza", "Monday blues"]
    topic = random.choice(topics)
    print(f"Debate topic: {topic}")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        print("Bla.. Bla:", generate_nonsense())

def storytelling_mode():
    """Generate an absurd story."""
    story = []
    for _ in range(10):
        story.append(generate_nonsense())
    print(" ".join(story))

def main():
    print("Welcome to Bla.. Bla!")
    while True:
        print("1. Conversation mode")
        print("2. Debate mode")
        print("3. Storytelling mode")
        print("4. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            conversation_mode()
        elif choice == "2":
            debate_mode()
        elif choice == "3":
            storytelling_mode()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
    

