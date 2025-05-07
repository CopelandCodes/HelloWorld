# salutation variable
greeting = "Hello World"

 
def main():
    """
    Prints the formatted greeting variable in the terminal.
    
    :global variable greeting: A String
    
    """
    print(f"{greeting}")
    
# Allows code execution when the script is run, not if it is imported as a module.
if __name__ == "__main__":
    main()