#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <path> <word>"
  exit 1
fi

# Assign arguments to variables
SEARCH_PATH="$1"
SEARCH_WORD="$2"

# Check if the provided path is valid
if [ ! -d "$SEARCH_PATH" ]; then
  echo "Error: Path '$SEARCH_PATH' is not a directory or does not exist."
  exit 1
fi

# Find files containing the word and print their names
echo "Searching for files containing the word '$SEARCH_WORD' in '$SEARCH_PATH'..."
grep -rl "$SEARCH_WORD" "$SEARCH_PATH" 2>/dev/null

# Exit successfully
exit 0
