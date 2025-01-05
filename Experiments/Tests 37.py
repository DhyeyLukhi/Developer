from instaloader import Instaloader, Profile
import getpass

def download_instagram_profile():
    # Create an instance of Instaloader
    L = Instaloader()
    
    # Get username and password
    username = input("Enter your Instagram username: ")
    password = getpass.getpass("Enter your Instagram password: ")
    
    try:
        # Login to Instagram
        L.login(username, password)
        print("Successfully logged in!")
        
        # Get target profile
        target_profile = input("Enter the Instagram username to download from: ")
        profile = Profile.from_username(L.context, target_profile)
        
        # Download profile picture
        print("Downloading profile picture...")
        L.download_profilepic(profile)
        
        # Download posts
        print("Downloading posts...")
        for post in profile.get_posts():
            L.download_post(post, target=profile.username)
            
        # Download stories
        print("Downloading stories...")
        L.download_stories(userids=[profile.userid])
        
        # Download highlights
        print("Downloading highlights...")
        for highlight in L.get_highlights(profile):
            for item in highlight.get_items():
                L.download_storyitem(item, ':highlights')
                
        print(f"\nDownload completed for {target_profile}!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    finally:
        print("\nLogging out...")
        L.close()

if __name__ == "__main__":
    print("Instagram Profile Downloader")
    print("Note: This script requires your Instagram login to access private profiles")
    print("----------------------------------------")
    download_instagram_profile()
