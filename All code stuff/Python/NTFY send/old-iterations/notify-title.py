import requests

# Define hard-coded servers
servers = {
    1: "https://ntfy.chaco-vibes.ts.net",
    2: "https://ntfy.sh",
    3: "https://my.custom.ntfy.server"  # Add more if needed
}

# Display server options
print("Select NTFY server(s) to send to (comma-separated numbers):")
for num, url in servers.items():
    print(f"{num}. {url}")

# Get user selection
selection = input("Your selection: ").strip()
selected_numbers = [int(s.strip()) for s in selection.split(",") if s.strip().isdigit()]
selected_servers = [servers[num].rstrip("/") for num in selected_numbers if num in servers]

# Validate selection
if not selected_servers:
    print("No valid servers selected. Exiting.")
    exit(1)

# Get topic, title, and message
topic = input("Enter the topic: ").strip()
title = input("Enter the message title (optional, press Enter to skip): ").strip()
message = input("Enter the message to send: ")

# Prepare headers
headers = {}
if title:
    headers["X-Title"] = title

# Send message to each selected server
for server in selected_servers:
    url = f"{server}/{topic}"
    try:
        response = requests.post(
            url,
            data=message.encode('utf-8'),
            headers=headers,
            timeout=5
        )
        print(f"✅ Message sent to {url} - Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error sending to {url}: {e}")

