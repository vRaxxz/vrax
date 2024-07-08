import random
import time

# A list of words for the typing test
words = ["apple", "banana", "orange", "grape", "watermelon", "peach", "cherry", "strawberry", "blueberry", "kiwi"]

def generate_text(word_list, num_words=10):
    """Generates a random sequence of words."""
    return ' '.join(random.choice(word_list) for _ in range(num_words))

def typing_test():
    """Conducts a typing test."""
    test_text = generate_text(words)
    print("Type the following text as fast as you can:")
    print(test_text)
    print()
    
    input("Press Enter to start...")
    start_time = time.time()
    
    typed_text = input("Start typing here: ")
    end_time = time.time()
    
    time_taken = end_time - start_time
    words_per_minute = (len(typed_text.split()) / time_taken) * 60
    
    print("\nResults:")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Words per minute: {words_per_minute:.2f} WPM")
    
    if typed_text == test_text:
        print("You typed the text correctly!")
    else:
        print("You made some mistakes.")
        print("Typed text:   ", typed_text)
        print("Original text:", test_text)

if __name__ == "__main__":
    typing_test()
