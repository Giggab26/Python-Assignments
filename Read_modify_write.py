def read_and_modify_file():
    """
    Program that reads a file, modifies its content, and writes to a new file
    with comprehensive error handling.
    """
    
    # Get filename from user
    filename = input("Enter the filename to read: ")
    
    try:
        # Attempt to read the file
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            
        print(f"✅ Successfully read {filename}")
        print(f"Original file has {len(content)} characters")
        
        # Modify the content (example modifications)
        modified_content = modify_text(content)
        
        # Create output filename
        output_filename = f"modified_{filename}"
        
        # Write modified content to new file
        try:
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(modified_content)
            
            print(f"✅ Successfully created {output_filename}")
            print(f"Modified file has {len(modified_content)} characters")
            
        except PermissionError:
            print(f"❌ Error: Permission denied when trying to write {output_filename}")
        except OSError as e:
            print(f"❌ Error writing file: {e}")
            
    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"❌ Error: Permission denied. Cannot read '{filename}'.")
    except IsADirectoryError:
        print(f"❌ Error: '{filename}' is a directory, not a file.")
    except UnicodeDecodeError:
        print(f"❌ Error: Cannot decode '{filename}'. File may be binary or use unsupported encoding.")
    except OSError as e:
        print(f"❌ Error reading file: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def modify_text(content):
    """
    Modify the text content - you can customize these modifications
    """
    # Example modifications:
    modified = content.upper()  # Convert to uppercase
    modified = modified.replace("THE", "***THE***")  # Highlight "THE"
    modified = f"--- MODIFIED FILE ---\n{modified}\n--- END OF FILE ---"
    
    return modified

def create_sample_file():
    """
    Helper function to create a sample file for testing
    """
    sample_content = """Hello World!
This is a sample file for testing.
The quick brown fox jumps over the lazy dog.
Python file handling is powerful and flexible."""
    
    try:
        with open("sample.txt", 'w') as file:
            file.write(sample_content)
        print("✅ Created sample.txt for testing")
    except Exception as e:
        print(f"❌ Error creating sample file: {e}")

# Main program
if __name__ == "__main__":
    print("File Read & Write Challenge with Error Handling")
    print("=" * 50)
    
    # Ask if user wants to create a sample file
    create_sample = input("Create a sample file for testing? (y/n): ").lower()
    if create_sample == 'y':
        create_sample_file()
    
    print()
    read_and_modify_file()