from instagrapi import Client

# Create a client instance
client = Client()

# Login to Instagram
client.login("your_username", "your_password")

# Get the list of pending follow requests
requests = client.user_pending_follow_requests()

# Iterate through each follow request and accept it
for request in requests:
    client.friendships_approve(request.pk)

# Logout from Instagram
client.logout()
