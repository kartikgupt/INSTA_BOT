from instabot import Bot
import schedule
import time

# Initialize the InstaBot
bot = Bot()

# Instagram credentials
username = "your_username"
password = "your_password"
def upload_photo():
    try:
        # Login to Instagram
        bot.login(username=username, password=password)
        botphoto_path = "path/to/your/photo.jpg"
        caption = "Your photo caption here"

        # Upload the photo
        bot.upload_photo(photo_path, caption=caption)
        bot.logout()

        print("Photo uploaded successfully!")

    except Exception as e:
        print(f"Failed to upload photo. Error: {str(e)}")

# Schedule the photo upload job to run every day at a specific time
schedule.every().day.at("12:00").do(upload_photo)

# Run the scheduler
while True:
    schedule.run_pending()

