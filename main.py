from tkinter import mainloop
from dotenv import load_dotenv
import discord
import os
import asyncio
import requests

load_dotenv()

TOKEN = os.getenv('DISCORDTOKENTOKEN') 
SERVER = os.getenv("BACKEND")

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        CLIENT = self
        self.channel_target = self.get_channel(990303036297592852)
        await self.main_loop()
    
    async def main_loop(self):
        while True:
            req = requests.get(SERVER + "message")
            if not req.json()["message"] == "": 
                message = req.json()['message']
                print(message)
                await self.channel_target.send(message)
                requests.post(SERVER + "message", json={"message": ""})

            await asyncio.sleep(1)


    async def on_message(self, message: discord.Message):
        if message.channel.id != self.channel_target.id : return
        if message.author == self.user: return

        if message.content == 'ping':
            await message.channel.send("Pong 🏓")

if __name__ == "__main__":
    MyClient().run(TOKEN)
