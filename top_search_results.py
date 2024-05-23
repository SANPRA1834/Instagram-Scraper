import instaloader

# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()

# Provide the search query here
search_results = instaloader.TopSearchResults(bot.context, 'music')

# Iterating over the extracted usernames
for username in search_results.get_profiles():
    print(username)

# Iterating over the extracted hashtags
for hashtag in search_results.get_hashtags():
    print(hashtag)