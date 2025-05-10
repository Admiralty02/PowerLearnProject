def remove_whitespace(input.txt, output.txt):
    try:
        # Open and read the input file
        with open(input.txt, 'r') as infile:
            content = infile.read()

        # Remove all whitespace characters
        modified_content = ''.join(content.split())

        # Write the modified content to a new file
        with open(output.txt, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Success! Whitespace removed and content written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: File '{input.txt}' not found.")
    except IOError as e:
        print(f"I/O error occurred: {e}")
