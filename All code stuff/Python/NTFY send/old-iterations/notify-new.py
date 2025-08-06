# import requests
# 
# # Prompt the user for input
# topics_input = input("Enter the topic(s) (comma-separated for multiple topics): ").strip()
# message = input("Enter the message to send: ")
# servers_input = input("Enter the NTFY server URL(s) (comma-separated): ").strip()
# 
# # Parse inputs
# topics = [t.strip() for t in topics_input.split(",") if t.strip()]
# servers = [s.strip().rstrip("/") for s in servers_input.split(",") if s.strip()]
# 
# # Send message to each combination of server and topic
# for server in servers:
#     for topic in topics:
#         url = f"{server}/{topic}"
#         try:
#             response = requests.post(
#                 url,
#                 data=message.encode(encoding='utf-8'),
#                 timeout=5
#             )
#             print(f"✅ Message sent to {url} - Status code: {response.status_code}")
#         except requests.exceptions.RequestException as e:
#             print(f"❌ Error sending to {url}: {e}")
# 

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

# Get topic and message
topic = input("Enter the topic: ").strip()
message = input("Enter the message to send: ")

# Send message to each selected server
for server in selected_servers:
    url = f"{server}/{topic}"
    try:
        response = requests.post(
            url,
            data=message.encode(encoding='utf-8'),
            timeout=5
        )
        print(f"✅ Message sent to {url} - Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error sending to {url}: {e}")

