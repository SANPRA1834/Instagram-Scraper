# Importing Libraries
import instaloader
import pandas as pd 

# Create an instance of Instaloader class
bot = instaloader.Instaloader()
bot.login(user="Your_username",passwd="Your_password")

# Loading a profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'Your_target_account_insta_handle')

# Retrieving all posts in an object
posts = profile.get_posts()

# Iterating and downloading all the individual posts
for index, post in enumerate(posts, 1):
    bot.download_post(post, target=f"{profile.username}_{index}")