import art, game_data
import os, random


score = 0
option_A = random.choice(game_data.data)
while True:
    os.system("clear")
    print(art.logo)
    print(f"Compare A: {option_A['name']}, a {option_A['description']}, from {option_A['country']}.")
    print(art.vs)
    option_B = random.choice(list(filter(lambda option: option != option_A, game_data.data)))
    if option_A['follower_count'] > option_B['follower_count']:
        answer = "A"
        result = option_A
    else:
        answer = "B"
        result = option_B
    print(f"Compare B: {option_B['name']}, a {option_B['description']}, from {option_B['country']}.")
    choice = input("Who has more followers: Type 'A' or 'B': ").upper()
    if choice == answer:
        score += 1
        option_A = option_B
    else:
        break

print(f"\nSorry, {result['name']} has more followers! Your score is : {score}")