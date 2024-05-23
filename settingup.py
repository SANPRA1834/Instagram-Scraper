import instaloader

# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()

# Loading the profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, 'cristiano')

print(profile)