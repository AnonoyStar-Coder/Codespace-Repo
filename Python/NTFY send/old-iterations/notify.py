import requests

# Prompt the user for topic and message
topic = input("Enter the topic: ").strip()
message = input("Enter the message to send: ")

# Construct the full URL
url = f"https://ntfy.chaco-vibes.ts.net/{topic}"

# Send the message
try:
    response = requests.post(
        url,
        data=message.encode(encoding='utf-8'),
        timeout=5
    )
    
    # Optional: print status
    print(f"Message sent to {url} - Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Error sending message: {e}")
