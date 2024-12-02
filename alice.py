from collections import Counter
import re

# Function to read file and find the most common word
def find_most_common_word(file_path):
    # Open and read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()  # Convert to lowercase to ignore case differences
        
    # Remove punctuation and split text into words
    words = re.findall(r'\b\w+\b', text)  # Only keep words
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Find the most common word
    most_common_word, count = word_counts.most_common(1)[0]
    
    print(f"The most common word is '{most_common_word}' which appears {count} times.")

# Example usage
file_path = "/mnt/c/alice/pg35688.txt"
find_most_common_word(file_path)
