import time
import random

def get_random_text():
    # Sample text for typing test
    texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Programming is fun and rewarding.",
        "Practice makes perfect.",
        "Python is a versatile programming language.",
        "Type fast, type accurately!"
    ]
    return random.choice(texts)

def typing_speed_test():
    print("Welcome to Typing Speed Test!")
    input("Press Enter when you are ready to start...")
    
    original_text = get_random_text()
    print("\nType the following text:")
    print(original_text)

    input("Press Enter to start typing...")

    start_time = time.time()

    user_input = input("Type the text here: ")

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Calculate words per minute (WPM)
    words_per_minute = len(original_text.split()) / (elapsed_time / 60)

    # Check accuracy
    correct_words = sum(a == b for a, b in zip(original_text.split(), user_input.split()))
    accuracy = (correct_words / len(original_text.split())) * 100

    print("\nResults:")
    print(f"Time taken: {elapsed_time:.2f} seconds")
    print(f"Words per minute (WPM): {words_per_minute:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")

    if accuracy == 100:
        print("Congratulations! You typed the text perfectly.")
    else:
        print("Keep practicing to improve your typing skills.")

if __name__ == "__main__":
    typing_speed_test()
