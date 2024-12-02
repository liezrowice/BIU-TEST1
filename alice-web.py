https://www.gutenberg.org/cache/epub/72577/pg72577.txfrom collections import Counter
import re
import requests

# Function to fetch content from a URL and find the most common word
def find_most_common_word(url):
    # Fetch the text from the URL
    response = requests.get(url)
    response.raise_for_status()  # Check for errors
    
    text = response.text.lower()  # Convert to lowercase to ignore case differences
    
    # Remove punctuation and split text into words
    words = re.findall(r'\b\w+\b', text)  # Only keep words
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Find the most common word
    most_common_word, count = word_counts.most_common(1)[0]
    
    print(f"The most common word is '{most_common_word}' which appears {count} times.")

# Example usage
url = "https://www.gutenberg.org/cache/epub/72577/pg72577.txt"# URL for "Alice's Adventures in Wonderland" on Project Gutenberg
find_most_common_word(url)
