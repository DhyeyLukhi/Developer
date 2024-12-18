import instaloader
import os
from datetime import datetime

def download_private_instagram_content(username, login_username, login_password):
    # Create an Instaloader instance with all download options enabled
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
        # Login with provided credentials (required for private profiles)
        print("Logging in...")
        L.login(login_username, login_password)
        
        # Get profile
        print(f"Accessing profile: {username}")
        profile = instaloader.Profile.from_username(L.context, username)
        
        if not profile.is_private:
            print("Note: This profile is public, login may not have been necessary")
        
        # Create directory structure
        base_dir = f"instagram_private_{username}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        os.makedirs(base_dir, exist_ok=True)
        
        # Download posts
        print(f"Downloading posts from {username}...")
        for post in profile.get_posts():
            try:
                # Download post content
                L.download_post(post, target=f"{base_dir}/posts")
                
                # Save comments
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
            except Exception as e:
                print(f"Error downloading post {post.shortcode}: {str(e)}")
                continue
        
        # Download stories
        print(f"Downloading stories...")
        try:
            L.download_stories(userids=[profile.userid], filename_target=f"{base_dir}/stories")
        except Exception as e:
            print(f"Error downloading stories: {str(e)}")
        
        # Download highlights
        print(f"Downloading highlights...")
        try:
            for highlight in L.get_highlights(profile):
                # Create directory for each highlight
                highlight_dir = f"{base_dir}/highlights/{highlight.title}"
                os.makedirs(highlight_dir, exist_ok=True)
                
                for item in highlight.get_items():
                    L.download_storyitem(item, highlight_dir)
        except Exception as e:
            print(f"Error downloading highlights: {str(e)}")
            
        # Download saved posts if available
        print(f"Attempting to download saved posts...")
        try:
            saved_posts = profile.get_saved_posts()
            for saved_post in saved_posts:
                L.download_post(saved_post, target=f"{base_dir}/saved_posts")
        except Exception as e:
            print(f"Error downloading saved posts: {str(e)}")
        
        print(f"\nDownload completed for {username}!")
        print(f"Content saved in directory: {base_dir}")
        
    except instaloader.exceptions.LoginRequiredException:
        print("Error: Login failed. Please check your credentials.")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Error: Profile {username} does not exist.")
    except instaloader.exceptions.PrivateProfileNotFollowedException:
        print(f"Error: {username} is a private profile and you are not following them.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    target_username = input("Enter Instagram username to download content from: ")
    login_user = input("Enter your Instagram username: ")
    login_pass = input("Enter your Instagram password: ")
    download_private_instagram_content(target_username, login_user, login_pass)
