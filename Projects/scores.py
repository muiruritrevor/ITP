def get_int(prompt):
    return int(input(prompt))


def score():
    scores = []
    for i in range (3):
        score = get_int("Score: ")
        scores.append(score)

    
    average = sum(scores) / len(scores)

    print(f"Average: {average}")

score()



