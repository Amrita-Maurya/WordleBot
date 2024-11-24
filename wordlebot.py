import random
NO_OF_LETTERS = 5
RED = "🟥"
YELLOW = "🟨"
GREEN = "🟩"
ATTEMPTS_USED = 1

def gen_word_from_list(list_of_words = get_wordlist()) -> str:
    return random.choice(list_of_words) 
  
def check_word(correct_word: str, guess: str) -> str:
    result = []
    for i in range(NO_OF_LETTERS):
        if guess[i] == correct_word[i]:
            result.append(GREEN)
        elif guess[i] in correct_word:
            result.append(YELLOW)
        else:
            result.append(RED)
    return "".join(result)
  
def feedback_check(result, word, guess):
    match = True
    for i in range(5):
        if result[i] == GREEN and word[i] != guess[i]:
            match = False
        elif result[i] == YELLOW and ( guess[i] not in word  or word[i] == guess[i]):
            match = False
        elif result[i] == RED and guess[i] in word:
            match = False
    return match
  
def filter_words(guess, list_of_words, result):
  return [word for word in list_of_words if feedback_check(result, word, guess)]
  
def auto_play(list_of_words, correct_word):
    possible_words = list_of_words[:]
    print("correct word", correct_word)
    attempts = 0
    while attempts < 6 and possible_words:
        guess = random.choice(possible_words).lower()
        print("guess:", guess)
        result = check_word(correct_word, guess)
        print("result", result)
        if guess == correct_word:
            print("CORRECT ANSWER")
            print("YOU WON IN :", attempts+1, " Attempts")
            break
        possible_words = filter_words(guess , list_of_words, result)
        attempts += 1
        print("possible words:", possible_words)
    else:
        if attempts == 6:
            print("GAME OVER \nNo more attempts left")
        else:
            print("WORD List EXHAUSTED")


def get_wordlist() -> list[str]:
    words = []
    with open('wordle.txt', 'r') as f:
        for line in f.readlines():
            words.append(line.split('\n')[0])
    return words
  
def auto_play(list_of_words, correct_word):
    possible_words = list_of_words[:]
    attempts = 0
    while attempts < 6 and possible_words:
        guess = random.choice(possible_words).lower()
        result = check_word(correct_word, guess)
        if guess == correct_word:
            return attempts + 1
        possible_words = filter_words(guess , list_of_words, result)
        attempts += 1
    if attempts == 6 or possible_words == []:
        return 0
      
def attempts_to_correct_guess():
    count = 0
    total_attempts = 0
    for _ in range(100):
        attempts = auto_play(get_wordlist(), gen_word_from_list())
        if attempts > 0:
            count += 1
            total_attempts += attempts
    print("count of correct word guess:", count, "\nnumber of attempts for the correct guess:", total_attempts, "\naverage attempts to correct guess:", total_attempts / count)

