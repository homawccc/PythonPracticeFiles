from sys import argv

script, user_name = argv
prompt = ">> "

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live: {user_name}?")
lives = input(">> ") # can be used instead of prompt variable

computer = input(f"What kind of computer do you have?:\n{prompt}")
# combines the input & prompt variable on a new line after question

print(f"""
    Alright, so you said {likes} about liking me.
    You live in {lives}. Not sure where that is.
    And you have a {computer} computer. Nice.
    """)
#prints multi-line with triple quotes

