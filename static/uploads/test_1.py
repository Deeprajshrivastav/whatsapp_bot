# import json
# import csv

# # Data as JSON
# data = [
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "Why do programmers hate nature?",
#     "punchline": "It has too many bugs.",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "Why did the developer go broke?",
#     "punchline": "Because he used up all his cache.",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "What do you call a programmer from Finland?",
#     "punchline": "Nerdic.",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "Why did the function break up with the variable?",
#     "punchline": "Because it couldn’t handle the relationship.",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "Why do Java developers wear glasses?",
#     "punchline": "Because they don’t see sharp.",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "Why can’t programmers tell jokes?",
#     "punchline": "Because they don’t know how to execute them.",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "Why do programmers love dark mode?",
#     "punchline": "Because light mode is too buggy.",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "What did the developer say after fixing the bug?",
#     "punchline": "“I’ve made some improvements!”",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "Why did the developer leave his job?",
#     "punchline": "He didn’t get arrays.",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "What do you call a programmer who can’t code?",
#     "punchline": "A debugger.",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "Why do web developers prefer to work in groups?",
#     "punchline": "Because they can’t handle the pressure on their own.",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "Why did the Python developer break up with the JavaScript developer?",
#     "punchline": "Because they didn’t have common classes.",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "How do programmers fix a broken webpage?",
#     "punchline": "They give it a refresh.",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "Why did the computer get cold?",
#     "punchline": "Because it left its Windows open.",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "Why do programmers prefer using Git?",
#     "punchline": "Because they love branching out.",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "What’s a programmer’s favorite hangout spot?",
#     "punchline": "The byte bar.",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "What do you call a bug in code that keeps coming back?",
#     "punchline": "A boomerang bug.",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "Why do programmers prefer to work alone?",
#     "punchline": "Because they don’t like to share their data.",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "What’s a developer’s favorite exercise?",
#     "punchline": "Push-ups.",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "Why do programmers always mix up Christmas and Halloween?",
#     "punchline": "Because Oct 31 == Dec 25.",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "What does a programmer say when they’re out of ideas?",
#     "punchline": "\"I need to debug this situation.\"",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "Why did the developer refuse to go to the party?",
#     "punchline": "Because they didn’t want to deal with the event handlers.",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "What does a SQL query say when it’s done?",
#     "punchline": "\"SELECT * FROM jokes WHERE humor = true;\"",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   },
#   {
#     "category": "Programming",
#     "type": "twopart",
#     "setup": "Why don’t programmers ever make good musicians?",
#     "punchline": "They don’t know how to handle the notes.",
#     "responses": ["FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "FALSE", "TRUE", "en"]
#   }
# ]

# # Specify CSV file path
# csv_file = "jokes.csv"

# # Write the data to a CSV
# with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.DictWriter(file, fieldnames=["category", "type", "setup", "punchline", "responses"])
#     writer.writeheader()
#     for entry in data:
#         writer.writerow({"category": entry["category"], "type": entry["type"], "setup": entry["setup"], "punchline": entry["punchline"], "responses": ', '.join(entry["responses"])})
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Path to your chromedriver
CHROME_DRIVER_PATH = r"C:\Users\deepr\Downloads\chromedriver_win32\chromedriver.exe"

# Create a Service object
service = Service(executable_path=CHROME_DRIVER_PATH)

# Initialize WebDriver with the service object
driver = webdriver.Chrome(service=service)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")


# from groq import Groq
# import base64


# # Function to encode the image
# def encode_image(image_path):
#   with open(image_path, "rb") as image_file:
#     return base64.b64encode(image_file.read()).decode('utf-8')

# # Path to your image
# image_path = "sf.jpg"

# # Getting the base64 string
# base64_image = encode_image('2.jpg')

# client = Groq(api_key="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")

# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": [
#                 {"type": "text", "text": "extract all the menu item in json format from the image with price and name, should be key and price is value return price in int "},
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": f"data:image/jpg;base64,{base64_image}",
#                     },
#                 },
#             ],
#         }
#     ],
#     model="llama-3.2-11b-vision-preview",
# )

# print(chat_completion.choices[0].message.content)
# import requests
# import pandas as pd
# import os

# # API URL
# url = "https://v2.jokeapi.dev/joke/Miscellaneous?amount=20?blacklistFlags=nsfw&amount=233"

# # Fetch data from the API
# response = requests.get(url)
# data = response.json()
# print(len(data.get("jokes", [])))
# # Extract relevant information
# jokes_list = []
# for joke in data.get("jokes", []):
#     jokes_list.append({
#         "category": joke.get("category", ""),
#         "type": joke.get("type", ""),
#         "setup": joke.get("setup", "") if joke.get("type") == "twopart" else "",
#         "delivery": joke.get("delivery", "") if joke.get("type") == "twopart" else "",
#         "joke": joke.get("joke", "") if joke.get("type") == "single" else "",
#         "nsfw": joke["flags"]["nsfw"],
#         "religious": joke["flags"]["religious"],
#         "political": joke["flags"]["political"],
#         "racist": joke["flags"]["racist"],
#         "sexist": joke["flags"]["sexist"],
#         "explicit": joke["flags"]["explicit"],
#         "safe": joke.get("safe", False),
#         "lang": joke.get("lang", "en"),
#     })

# # Create a DataFrame for the new jokes
# df_new = pd.DataFrame(jokes_list)

# # File path
# csv_file = "jokes.csv"

# if os.path.exists(csv_file):
#     # Load existing jokes
#     df_old = pd.read_csv(csv_file)
    
#     # Concatenate old and new data
#     df_combined = pd.concat([df_old, df_new], ignore_index=True)

#     # Remove duplicates based on 'setup' and 'joke' columns
#     df_combined.drop_duplicates(subset=["setup", "joke"], keep="first", inplace=True)

#     # Save back to CSV
#     df_combined.to_csv(csv_file, index=False)
# else:
#     # If file doesn't exist, create a new one
#     df_new.to_csv(csv_file, index=False)

# print("Jokes added to jokes.csv without duplication!")

