import requests
import base64
from google.oauth2 import service_account
import google.auth.transport.requests

# Load your service account credentials from your focal pager JSON file
credentials = service_account.Credentials.from_service_account_file(
    'focal_pager.json',  # replace with the correct filename/path
    scopes=['https://www.googleapis.com/auth/cloud-platform']
)

# Refresh credentials to get an access token
request = google.auth.transport.requests.Request()
credentials.refresh(request)
access_token = credentials.token
print("Access Token:", access_token)

# Set up the Text-to-Speech API request
url = "https://texttospeech.googleapis.com/v1/text:synthesize"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json; charset=utf-8"
}

payload = {
    "input": {"text": "Thank you for sharing that—it sounds like you're carrying a lot beneath the surface, even if it's hard to put into words. What you're describing, that sense of numbness or disconnection, is something many people experience, especially when they've been in survival mode for a while. You're not alone in this, and it's okay to not have it all figured out. Together, we can explore what might be contributing to that feeling, and gently work toward reconnecting you with meaning, joy, or even just a sense of presence. No pressure—just curiosity."},
    "voice": {
        "languageCode": "en-US",
        "ssmlGender": "FEMALE",
        "name": "en-US-Chirp-HD-F"
    },
    "audioConfig": {
        "audioEncoding": "MP3"
    }
}

# Make the API call
response = requests.post(url, headers=headers, json=payload)
result = response.json()

if "audioContent" in result:
    # Decode and save the base64-encoded audio content to a file
    audio_content = base64.b64decode(result["audioContent"])
    with open("output.mp3", "wb") as out_file:
        out_file.write(audio_content)
    print("Audio content written to file 'output.mp3'")
else:
    print("Error:", result)
