# Write a program to accept a string from the user and display characters that are present at an even index number.

def display_chars_at_even_indices():
    # Receive a string from the user
    user_string = input("Enter a string: ")

    # Extract characters at even index numbers
    even_index_chars = user_string[::2]
    
    # Print characters at even index numbers
    print("Characters at even index numbers:", even_index_chars)

# Call the function to execute the program
display_chars_at_even_indices()




