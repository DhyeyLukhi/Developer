import instaloader
import os
from datetime import datetime

def download_instagram_content(username):
    # Create an Instaloader instance
    L = instaloader.Instaloader(
        download_pictures=True,
        download_videos=True, 
        download_video_thumbnails=True,
        download_geotags=True,
        download_comments=True,
        save_metadata=True,
        compress_json=False
    )
    
    try:
        # Login (required for private profiles and stories)
        # Replace with your Instagram credentials
        L.login('YOUR_USERNAME', 'YOUR_PASSWORD')
        
        # Get profile
        profile = instaloader.Profile.from_username(L.context, username)
        
        # Create directory for the user
        base_dir = f"instagram_data_{username}"
        os.makedirs(base_dir, exist_ok=True)
        
        # Download posts and save comments
        print(f"Downloading posts for {username}...")
        for post in profile.get_posts():
            # Download post
            L.download_post(post, target=f"{base_dir}/posts")
            
            # Save comments to txt file
            comments_file = os.path.join(base_dir, "posts", f"comments_{post.shortcode}.txt")
            with open(comments_file, "w", encoding="utf-8") as f:
                f.write(f"Comments for post {post.shortcode}\n")
                f.write(f"Posted on: {post.date}\n")
                f.write("-" * 50 + "\n\n")
                
                for comment in post.get_comments():
                    f.write(f"User: {comment.owner.username}\n")
                    f.write(f"Comment: {comment.text}\n")
                    f.write(f"Date: {comment.created_at_utc}\n")
                    f.write("-" * 30 + "\n")
        
        # Download stories
        print(f"Downloading stories for {username}...")
        L.download_stories(userids=[profile.userid], filename_target=f"{base_dir}/stories")
        
        # Download highlights
        print(f"Downloading highlights for {username}...")
        for highlight in L.get_highlights(profile):
            # Each highlight has multiple items
            for item in highlight.get_items():
                L.download_storyitem(item, f"{base_dir}/highlights/{highlight.title}")
                
        print(f"\nDownload completed for {username}!")
        print(f"Content saved in directory: {base_dir}")
        
    except instaloader.exceptions.LoginRequiredException:
        print("Error: Login required. Please provide valid Instagram credentials.")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Error: Profile {username} does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    username = input("Enter Instagram username to download content: ")
    download_instagram_content(username)
