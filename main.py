import random
from game_data import data
from art import logo, vs

def play():
    game_over = False
    score = 0

    #Create an empty list and randomly populate with 2 persons 
    block = []
    # Create a function that adds persons to the list
    def add_person():
        block.append(random.choice(data))

    for _ in range(2):
        add_person()

    while not game_over:
        person_a = block[0]
        person_b = block[1]

        print(logo)
        # Ask the user to make comparism
        print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")

        print(vs)
        print(f"\nAgainst B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.")

        # Get user input
        user_choice = input("\nWho has more followers? Type 'A' or 'B' :\n").lower()


        if user_choice == 'a' and person_a['follower_count'] >= person_b['follower_count']:
            print('Right Answer')
            block[0] = person_a
            block.pop()
            add_person()
            score += 1
            print(f"score : {score}")

        elif user_choice == 'b' and person_b['follower_count'] >= person_a['follower_count']:
            print('************* Right Answer **************')
            block[0] = person_b
            block.pop()
            add_person()
            score += 1
            print(f"score : {score}")

        else:
            print('**********  Nope! that was incorrect.************\n')
            print(f"final score: {score}")

            game_over = True

    play_again = input("\nWould you like to play again? Type 'y' or 'n' :\n")

    if play_again == 'y':
        play()
play()







