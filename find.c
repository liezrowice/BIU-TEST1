#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>

// Function to check if a file contains the word
int file_contains_word(const char *filepath, const char *word) {
    FILE *file = fopen(filepath, "r");
    if (file == NULL) {
        perror("Error opening file");
        return 0;
    }

    char line[1024];
    int found = 0;
    while (fgets(line, sizeof(line), file)) {
        if (strstr(line, word)) {
            found = 1;
            break;
        }
    }

    fclose(file);
    return found;
}

// Recursive function to traverse the directory
void search_directory(const char *path, const char *word) {
    struct dirent *entry;
    DIR *dir = opendir(path);

    if (dir == NULL) {
        perror("Error opening directory");
        return;
    }

    while ((entry = readdir(dir)) != NULL) {
        // Skip . and ..
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0) {
            continue;
        }

        char full_path[1024];
        snprintf(full_path, sizeof(full_path), "%s/%s", path, entry->d_name);

        // Check if the entry is a directory
        if (entry->d_type == DT_DIR) {
            // Recursively search in subdirectory
            search_directory(full_path, word);
        } else if (entry->d_type == DT_REG) {
            // Check if the file contains the word
            if (file_contains_word(full_path, word)) {
                printf("File containing the word '%s': %s\n", word, full_path);
            }
        }
    }

    closedir(dir);
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <path> <word>\n", argv[0]);
        return EXIT_FAILURE;
    }

    const char *path = argv[1];
    const char *word = argv[2];

    search_directory(path, word);

    return EXIT_SUCCESS;
}
