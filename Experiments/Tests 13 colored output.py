# items = ["Folder 1", "FolDer 2", "FoldER 3"]  # List of folder names
#
# # Function to find the correct folder name
#
# def find_folder(name, folder_list):
#     input_name_lower = name.lower()  # Convert input to lowercase
#     for folder in folder_list:
#         if folder.lower() == input_name_lower:
#             return folder  # Return the correctly spelled folder name
#     return None  # Return None if no match is found
#
#
# # Example usage
# command = input("Enter the name of the folder in lowercase: ")
# correctone = find_folder(command, items)
# if correctone:
#     print("Correct folder name:", correctone)
# else:
#     print("Folder not found.")
# ANSI color codes
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Example usage
print(color.RED + 'This is red text!' + color.END)
print(color.GREEN + 'This is green text!' + color.END)
print(color.BOLD + 'This is bold text!' + color.END)
print(color.UNDERLINE + 'This is underlined text!' + color.END)
