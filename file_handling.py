def main():
    # Ask the user for the filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try to open and read the file
        with open(filename, 'r') as infile:
            content = infile.read()

        # Modify the content to upper case
        modified_content = content.upper()

        # Define the output filename
        output_filename = "modified_" + filename

        # Write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Success! Modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read from the file '{filename}'.")

if __name__ == "__main__":
    main()
      
