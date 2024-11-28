import os
import subprocess
import pyttsx3
import webbrowser
import datetime


def say(text):  # say: This function will speak
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    return text


def wish():  # wish: This function wish user
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        say("Good Morning Sir, I am Optimus")
    elif 12 <= hour < 18:
        say("Good Afternoon Sir, I am Optimus")
    else:
        say("Good Evening Sir, I am Optimus")


def assist():  # assist: Ready for your command
    print("Optimus is here for your Assist, Sir")
    print("Optimus - Your Desktop Assistant. Version 4.0")
    print("Now you can open any channel on Youtube")
    print("This has also Fixes some issues so, now Optimus will Run Better")
    say("Optimus is here for your Assist, Sir")


def take_command():  # This function will take command form user
    user_command = str(input("Command: "))
    return user_command


path1 = "E:\\"
path2 = "C:\\"

if __name__ == '__main__':  # The execution of the programme starts here
    wish()
    assist()
    print("Ready to execute your command")
    while True:
        command = take_command()
        if 'open youtube' in command.lower():  # Open youtube
            print("Executing...")
            say("Opening youtube, Sir")
            webbrowser.open("https://www.youtube.com")

        if 'open google' in command.lower():  # Open google
            print("Executing...")
            say("Opening google, Sir")
            webbrowser.open("https://www.google.com")

        if 'open wikipedia' in command.lower():  # Open wikipedia
            print("Executing...")
            say("Opening wikipedia, Sir")
            webbrowser.open("https://www.wikipedia.com")

        if 'what is the time now' in command.lower() or 'time now' in command.lower():  # Telling the time
            print("Executing...")
            hor = int(datetime.datetime.now().strftime("%H"))
            mnt = int(datetime.datetime.now().strftime("%M"))
            if hor > 12:
                hor = hor - 12
                if 0 < mnt < 10:
                    print(datetime.datetime.now().strftime(f"{hor} : {mnt} PM"))
                    say(f"The time is {hor} hours and 0{mnt} minutes PM")
                else:
                    print(datetime.datetime.now().strftime(f"{hor} : {mnt} PM"))
                    say(f"The time is {hor} hours and {mnt} minutes PM")
            elif hor < 12:
                if 0 < mnt < 10:
                    print(datetime.datetime.now().strftime(f"{hor} : {mnt} AM"))
                    say(f"The time is {hor} hours and 0{mnt} minutes AM")
                else:
                    print(datetime.datetime.now().strftime(f"{hor} : {mnt} AM"))
                    say(f"The time is {hor} hours and {mnt} minutes AM")
            elif hor == 12:
                if 0 < mnt < 10:
                    print(datetime.datetime.now().strftime(f"{hor} : {mnt} PM"))
                    say(f"The time is {hor} hours and 0{mnt} minutes PM")
                else:
                    print(datetime.datetime.now().strftime(f"{hor} : {mnt} PM"))
                    say(f"The time is {hor} hours and {mnt} minutes PM")

        if 'what is the date' in command.lower() or 'date of today' in command.lower() or 'date today' in command.lower():
            # Date of today
            print("Executing...")
            date = datetime.date.today()
            print(date)
            say(f"Today's Date is {date}")

        if 'open chatgpt' in command.lower():  # Open chatGPT
            print("Executing...")
            say("Opening ChatGPT, sir")
            webbrowser.open("https://chat.openai.com")

        if 'open pycharm' in command.lower():  # Open PyCharm
            print("Executing...")
            path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1.3\\bin\\pycharm64.exe"
            if os.path.exists(path):
                say("opening PyCharm, sir")
                subprocess.Popen(path)

        if 'open chrome' in command.lower() or 'open google chrome' in command.lower():  # pen Chrome
            print("Executing...")
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            say("Opening Chrome, Sir")
            subprocess.Popen(path)

        if 'open whatsapp' in command.lower():  # Open Whatsapp
            print("Executing...")
            say("Opening Whatsapp, Sir")
            webbrowser.open("https://web.whatsapp.com/")

        if 'open telegram' in command.lower():  # Open Telegram
            print("Executing...")
            say("Opening Telegram, Sir")
            webbrowser.open("https://web.telegram.org/k/")

        if 'open music library' in command.lower():
            print("Executing...")
            say("Opening Music Library form Youtube, Sir")
            webbrowser.open("https://studio.youtube.com/")

        if 'make folder' in command.lower() or 'make a folder' in command.lower():
            say("At which disk do you have to make a folder")
            disk = input("Enter 'c' dor C and 'e' for E disk: ")
            if 'c' in disk.lower():
                name_of_folder = input("Name of folder: ")
                try:

                    folder_path = os.path.join(path2, name_of_folder)
                    os.mkdir(folder_path)
                    print("Folder created successfully")
                    say("Folder created, Sir")

                except Exception as e:
                    tell = e
                    print("Some ERROR Founds")
                    say("I can't make Folder")

            if 'e' in disk.lower():
                name_of_folder = input("Entre the name of the folder: ")
                try:
                    folder_path = os.path.join(path1, name_of_folder)
                    os.mkdir(folder_path)
                    print("Folder created successfully")
                    say("Folder created, Sir")

                except Exception as e:
                    tell = e
                    print("Some ERROR Founds")
                    say("I can't make Folder")

        if 'make multiple folder' in command.lower() or 'make multiple folders' in command.lower():
            say("At which disk do you have to make Folders")
            disk = input("Enter 'c' dor C and 'e' for E disk: ")
            folders = int(input("How many folders do your have to made: "))
            if 'c' in disk.lower():
                for folders in range(0, folders):
                    name_of_folder = input(f"Name of {folders + 1} folder: ")
                    try:
                        folder_path = os.path.join(path2, name_of_folder)
                        os.mkdir(folder_path)
                        print("Folder created successfully")
                        say("Folder created, Sir")

                    except Exception as e:
                        tell = e
                        print("Some ERROR Founds")
                        say("I can't make Folder")

            if 'e' in disk.lower():
                for folders in range(0, folders):
                    name_of_folder = input(f"Name of {folders + 1} folder: ")
                    try:
                        folder_path = os.path.join(path1, name_of_folder)
                        os.mkdir(folder_path)
                        print("Folder created successfully")
                        say("Folder created, Sir")

                    except Exception as e:
                        tell = e
                        print("Some ERROR Founds")
                        say("I can't make Folder")

        if 'delete a folder' in command.lower() or 'delete folder' in command.lower():
            say("Which folder do you want to delete ?")
            deletefolder = input("Which folder do you want to delete: ")
            disk = input("Enter 'c' for C disk and 'e' for E disk: ")
            if 'c' in disk.lower():
                try:
                    folder_path = os.path.join(path2, deletefolder)
                    os.rmdir(folder_path)
                    print("Folder deleted Successfully")
                    say("Folder Deleted, Sir")

                except Exception as e:
                    tell = e
                    print("Some ERROR Founds")
                    say("I can't delete Folder")

            if 'e' in disk.lower():
                try:
                    folder_path = os.path.join(path1, deletefolder)
                    os.rmdir(folder_path)
                    print("Folder deleted Successfully")
                    say("Folder Deleted, Sir")

                except Exception as e:
                    tell = e
                    print("Some ERROR Founds")
                    say("I can't delete Folder")

        if 'delete multiple folder' in command.lower() or 'delete multiple folders' in command.lower() or 'delete multi folder' in command.lower() or 'delete multi folders' in command.lower():
            say("Where is the Folders ?")
            disk = input("Enter 'c' for C disk or 'e' for E disk: ")
            folders = int(input("How many Folder you have to Delete: "))
            if 'c' in disk.lower():
                for folders in range(0, folders):
                    name_of_folder = input(f"Name of {folders + 1} Folder: ")
                    try:
                        folder_path = os.path.join(path2, name_of_folder)
                        os.rmdir(folder_path)
                        print("Folder deleted Successfully")
                        say("Folder Deleted, Sir")

                    except Exception as e:
                        tell = e
                        print("Some ERROR Founds")
                        say("I can't delete Folder")

            if 'e' in disk.lower():
                for folders in range(0, folders):
                    name_of_folder = input(f"Name of {folders + 1} Folder: ")
                    try:
                        folder_path = os.path.join(path1, name_of_folder)
                        os.rmdir(folder_path)
                        print("Folder deleted Successfully")
                        say("Folder Deleted, Sir")

                    except Exception as e:
                        tell = e
                        print("Some ERROR Founds")
                        say("I can't delete Folder")

        if 'make file' in command.lower() or 'make a file' in command.lower():
            say("At which disk do you have to make a file")
            disk = input("Enter 'c' for C disk and 'e' for E disk: ")
            if 'c' in disk.lower():
                name_of_file = input("Name of the file: ")
                filepath = os.path.join(path2, name_of_file)
                try:
                    file = open(filepath + ".txt", "w")
                    file.close()
                    print("File created successfully")
                    say("File created, Sir")
                except Exception as e:
                    tell = e
                    print("Some ERROR Founds")
                    say("I can't make the File")

            if 'e' in disk.lower():
                name_of_file = input("Name of the file: ")
                filepath = os.path.join(path1, name_of_file)
                try:
                    file = open(filepath + ".txt", "w")
                    file.close()
                    print("File created successfully")
                    say("File created, Sir")
                except Exception as e:
                    tell = e
                    print("Some ERROR Founds")
                    say("I can't make the File")

        if 'make multiple file' in command.lower() or 'make multiple files' in command.lower() or 'make multi file' in command.lower() or 'make multi files' in command.lower():
            say("At which disk you want to make File ?")
            disk = input("Enter 'c' for C disk or 'e' for E disk: ")
            files = int(input("How many files you want to make: "))
            if 'c' in disk.lower():
                for files in range(0, files):
                    name_of_file = input(f"Name of {files + 1} File: ")
                    extension = input("Enter the Extension(Example = '.txt'): ")
                    name_of_file += extension
                    filepath = os.path.join(path2, name_of_file)
                    try:
                        file = open(filepath + ".txt", "w")
                        file.close()
                        print("File created successfully")
                        say("File created, Sir")
                    except Exception as e:
                        tell = e
                        print("Some ERROR Founds")
                        say("I can't make the File")

            if 'e' in disk.lower():
                for files in range(0, files):
                    name_of_file = input(f"Name of {files + 1} File: ")
                    filepath = os.path.join(path2, name_of_file)
                    extension = input("Enter the Extension(Example = '.txt'): ")
                    name_of_file += extension
                    try:
                        file = open(filepath + ".txt", "w")
                        file.close()
                        print("File created successfully")
                        say("File created, Sir")
                    except Exception as e:
                        tell = e
                        print("Some ERROR Founds")
                        say("I can't make the File")

        if 'delete a file' in command.lower() or 'delete file' in command.lower():
            say("Which file do you want to delete ?")
            delete_file = input("Which file do you want to delete: ")
            extension = input("Enter the extension of the file(Example = '.txt'): ")
            delete_file += extension
            disk = input("Enter 'c' for C disk and 'e' for E disk: ")
            if 'c' in disk.lower():
                try:
                    filepath = os.path.join(path2, delete_file)
                    os.remove(filepath)
                    print("File deleted Successfully")
                    say("File Deleted, Sir")
                except Exception as e:
                    tell = e
                    print("Some ERROR Founds")
                    say("I can't Delete the File")

            if 'e' in disk.lower():
                try:
                    filepath = os.path.join(path1, delete_file)
                    os.remove(filepath)
                    print("File deleted Successfully")
                    say("File Deleted, Sir")
                except Exception as e:
                    tell = e
                    print("Some ERROR Founds")
                    say("I can't Delete the File")

        if 'delete multiple file' in command.lower() or 'delete multiple file' in command.lower() or 'delete multi file' in command.lower() or 'delete multi file' in command.lower():
            say("Where is the Files ?")
            disk = input("Enter 'c' for C disk or 'e' for E disk: ")
            files = int(input("How many Files you have to Delete: "))
            if 'c' in disk.lower():
                for files in range(0, files):
                    name_of_file = input(f"Name of {files + 1} File: ")
                    extension = input("Enter the Extension(Example = '.txt'): ")
                    name_of_file += extension
                    try:
                        filepath = os.path.join(path2, name_of_file)
                        os.remove(filepath)
                        print("File deleted Successfully")
                        say("File Deleted, Sir")
                    except Exception as e:
                        tell = e
                        print("Some ERROR Founds")
                        say("I can't Delete the File")

            if 'e' in disk.lower():
                for files in range(0, files):
                    name_of_file = input(f"Name of {files + 1} File: ")
                    extension = input("Enter the Extension(Example = '.txt'): ")
                    name_of_file += extension
                    try:
                        filepath = os.path.join(path2, name_of_file)
                        os.remove(filepath)
                        print("File deleted Successfully")
                        say("File Deleted, Sir")
                    except Exception as e:
                        tell = e
                        print("Some ERROR Founds")
                        say("I can't Delete the File")

        if ('open ' in command.lower() and 'on' in command.lower() and ' youtube' in command.lower()) or ('open' in command.lower() and 'in' in command.lower() and 'youtube' in command.lower()) or ('open' in command.lower() and 'at' in command.lower() and 'youtube' in command.lower()):
            command = command.replace("open ", "").replace(" on youtube", "").replace(" in youtube", "").replace(" at youtube", "")
            command = command.replace(" ", "")
            print("Opening, Sir")
            say("Opening Channel, Sir")
            webbrowser.open(f"https://www.youtube.com/@{command}")

        if 'open' in command.lower() and ' website' in command.lower():
            command = command.replace("open ", "").replace("website", "")
            command = command.replace(" ", "")
            print("Opening, Sir")
            say("Opening Website, sir")
            webbrowser.open(f"https://www.{command}.com")
