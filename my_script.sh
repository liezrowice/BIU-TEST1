#!/usr/bin/python3

# A simple bash script to check if a directory exists and create it if not.

# Define a variable for the directory name
DIR_NAME="example_directory"

# Check if the directory exists
if [ -d "$DIR_NAME" ]; then
    echo "Directory $DIR_NAME already exists."
else
    echo "Directory $DIR_NAME does not exist. Creating now..."
    mkdir $DIR_NAME
    echo "Directory $DIR_NAME created."
fi

# Loop through files in the directory
echo "Listing contents of the directory:"
for file in $DIR_NAME/*; do
    if [ -e "$file" ]; then
        echo "$file"
    else
        echo "No files in $DIR_NAME"
    fi
done

# Ask the user if they want to delete the directory
read -p "Do you want to delete the directory? (y/n): " choice
if [[ "$choice" == "y" ]]; then
    rm -rf "$DIR_NAME"
    echo "Directory deleted."
else
    echo "Directory not deleted."
fi
