import os
import asyncio
import random
import string
import aiohttp
from pyfiglet import Figlet
from flask import Flask
import asyncio


# Credits to GOD
print("Credits to @We_areGOD ")
print()

# Colors for console output
green_console = "\033[92m"
red_console = "\033[91m"
yellow_console = "\033[93m"

# Print introductory messages
print("\033[1;33;40m  ~ Pяσɢяαммεя • @We_areGOD • -> @We_areGOD |  ~")
print("\x1b[1;39m", "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print('\n')

# Figlet logo
fig = Figlet(font='poison')
logo = fig.renderText('GOD')
print("\033[1;36;40m")
print(logo)

# Function to generate a random username based on type
async def generate_username(length=4, username_type='4C'):
    if username_type == '4L':
        characters = string.ascii_lowercase
        username = ''.join(random.choice(characters) for _ in range(length))
    elif username_type == '4D':
        numbers = string.digits
        if length < 3:
            raise ValueError("Length should be at least 3 for the dot placement.")

        username_list = [random.choice(string.digits) for _ in range(length - 1)]
        dot_position = random.randint(1, length - 2)  # Dot should not be at the beginning or end
        username_list.insert(dot_position, '.')
        username = ''.join(username_list)
    else:  # Default to '4C'
        characters = string.ascii_lowercase + string.digits
        username = ''.join(random.choice(characters) for _ in range(length))
        separator = random.choice(['.', '_'])
        index = random.randint(1, length - 2)
        username = username[:index] + separator + username[index:]
    return username

# Function to create an Instagram account
async def create_instagram_account(session, username_type):
    while True:
        username = await generate_username(username_type=username_type)
        headers = {
            "Host": "i.instagram.com",
            "cookie": "mid=Y16iBgABAAFggfUYwajggkGFz-hs",
            "x-ig-capabilities": "AQ==",
            "cookie2": "$Version=1",
            "x-ig-connection-type": "WIFI",
            "user-agent": "Instagram 6.12.1 Android (30/11; 480dpi; 1080x2298; HONOR; ANY-LX2; HNANY-Q1; qcom; en_IQ)",
            "content-type": "application/x-www-form-urlencoded",
            "accept-encoding": "gzip"
        }
        data = {
            "password": "zxcvbm1@",
            "device_id": "android-2793e055-2a92-4df2-890f-f88f52538de5",
            "guid": "2793e055-2a92-4df2-890f-f88f52538de5",
            "email": "zodhokxbsbdbsbsksbs@gmail.com",
            "username": username
        }
        async with session.post("https://i.instagram.com/api/v1/accounts/create/", headers=headers, data=data) as response:
            try:
                content_type = response.headers.get('Content-Type', '')
                if 'application/json' in content_type:
                    json_response = await response.json()
                    error_type = json_response.get('error_type')
                    if error_type == 'needs_upgrade':
                        print(f'{green_console}GooD UserName : {username}   BY @We_areGOD')
                        await send_telegram_message(username)
                    elif error_type == 'taken':
                        print(f'{red_console}BaD UserName : {username}')
                    else:
                        print(f'{yellow_console}{error_type} : {username}')
                else:
                    # Print the raw response if it's not JSON
                    text_response = await response.text()
                    print(f'{yellow_console}Non-JSON Response: {text_response}')
            except Exception as e:
                print(f'{red_console}Error: {e}')

# Function to send a message via Telegram bot
async def send_telegram_message(username):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        params = {
            "chat_id": telegram_user_id,
            "text": username
        }
        await session.get(url, params=params)

# Main function to run the tasks
async def main(username_type):
    async with aiohttp.ClientSession() as session:
        tasks = [create_instagram_account(session, username_type) for _ in range(10)]
        await asyncio.gather(*tasks)

# Get user inputs
token = "7904586048:AAFVPi_uKsHyl96xPvV80mxRfkBEhZyjCrM"
telegram_user_id = "7606711394"

# Display menu for username type
print('\033[1;34mSelect username type:')
print('1: 4L (Letters only)')
print('2: 4C (Letters and numbers)')
print('3: 4D (Numbers and dots)')

choice = "1"
username_type = '4C'  # Default

if choice == '1':
    username_type = '4L'
elif choice == '3':
    username_type = '4D'

# Run the main function
asyncio.run(main(username_type))
