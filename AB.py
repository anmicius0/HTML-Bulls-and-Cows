import random

def check_input(guess):
    """
    Args
        guess: user's input
    Return
        result: a boolen value
    """
    result = True

    if len(guess) != 4:
        result = False

    try:
        temp = int(guess)
    except ValueError:
        result = False

    return result

def check_answer(guess, answer):
    """
        Args:
            guess: the number player guess (str)
            answer: the answer (str)
        Return:
            a: a
            b: b
    """
    a = 0
    b = 0
    list_answer = []

    # turn answer into type "list"
    for x in answer:
        list_answer.append(x)
    
    # check amount of "b"
    for i in range(4):
        if guess[i] == answer[i]:
            b += 1
    # check the amount of "a"
    for i in guess:
        if i in list_answer:
            a += 1
            list_answer.remove(i)

    return a,b

def generate_answer():
    answer = str(random.randint(1000, 9999))

