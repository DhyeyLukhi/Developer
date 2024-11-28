import os


def explore_folders(path):
    # Iterate over all the items in the given path
    for item_in_folder in os.listdir(path):
        item_path = os.path.join(path, item_in_folder)

        if os.path.isdir(item_path):
            print(item_path)  # Print the folder path

            explore_folders(item_path)
    return 0


print(explore_folders("C:\\Users"))