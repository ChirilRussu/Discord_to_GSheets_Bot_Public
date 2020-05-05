# BSD 3-Clause License
# Copyright (c) 2019, Hugonun(https://github.com/hugonun)
# All rights reserved.

import discord
import random

from gsheet import *

client = discord.Client()
sheet = gsheet()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Restrict the command to a role
    # Change REQUIREDROLE to a role id or None
    REQUIREDROLE = None
    if REQUIREDROLE is not None and discord.utils.get(message.author.roles, id=str(REQUIREDROLE)) is None:
        await message.channel.send('You don\'t have the required role!')
        return
    
    # lists
    # everything must be lower case
    resources = [
    "aloe", "aloes",      #1
    "anime bath water", "water", "contaminated water",
    "beeswax",
    "blood turnip", "blood turnips",
    "bone splinter", "bone splinters",     #5
    "cactus fruit", "cactus fruits",
    "cattail", "cattails",
    "charcoal", "charcoals",
    "chitin plate", "chitin plates",
    "clay", "clays",       #10
    "corn", "corns",
    "cotton", "cottons",
    "fiber", "fibers",
    "hide", "hides",
    "insect", "insects",   #15
    "iron ore", "iron ores",
    "mushroom", "mushrooms",
    "obsidian", "obsidians",
    "palm leaf", "palm leaves",
    "pearl", "pearls",     #20
    "redwood", "redwoods",
    "rupu camp", "rupu camps",
    "rupu gel", "rupu gels",
    "rupu pelt", "rupu pelts",
    "rupu vine", "rupu vines",     #25
    "stone", "stones",
    "sulfer", "sulfers",
    "temple", "temples",
    "thornberry", "thornberries",
    "torque",        #30
    "wood", "woods",
    "worm silk", "worm silks",
    "worm slime", "worm slimes",
    "nibiran", "nibirans",
    "lava poppy", "lava poppies",
    "black soil", "black soils",
    "magma seed", "magma seeds",
    ]
    
    accepted_responses =[
    "Marker added. "
    ]
    
    rejected_responses =[
    "Input rejected. "
    ]
    
    def is_number(str):
        try:
            float(str)
            return True     # Type-casting the string to `float`.
        except ValueError:  # If string is not a valid `float` it'll raise `ValueError` exception
            return False

    # start of all commands
    if message.content.startswith('!map-'):
        
        # Command to insert data to google sheet
        if message.content.startswith('!map-4') or message.content.startswith('!map-1') or message.content.startswith('!map-3'):
            if message.content.startswith('!map-4'):
                SPREADSHEET_ID = '' # Add Spreadsheet ID here
            elif message.content.startswith('!map-3'):
                SPREADSHEET_ID = '' # Add Spreadsheet ID here
            elif message.content.startswith('!map-1'):
                SPREADSHEET_ID = '' # Add Spreadsheet ID here
            
            RANGE_NAME = 'A2'
            FIELDS = 3 # Amount of fields/cells
                    
            msg = message.content[6:] # number here has to match the number of characters for the command in the first startswith to ignore storing that many characters
            result = [x.strip() for x in msg.split(',')]
            
            # checks that the coordinate fields have only integers
            if is_number(result[0]) == True and is_number(result[1]) == True:
                # checks against the list that the resource name is an acceptable input 
                if result[2].lower() in resources:
                    if len(result) == FIELDS or len(result) == FIELDS+1:
                        # Add
                        print(message.created_at)
                        DATA = [message.author.name] + [message.author.id] + [str(message.created_at)] + result
                        sheet.add(SPREADSHEET_ID, RANGE_NAME, DATA)
                        await message.channel.send(random.choice(accepted_responses))
                    else:
                        # Needs more/less fields
                        await message.channel.send(random.choice(rejected_responses) + "Error: " + message.author.name + ", you need to have {0} inputs seperated by {1} comma(s).".format(FIELDS,FIELDS-1))
                else:
                    await message.channel.send("Error: " + message.author.name + ", the resource name you entered doesn't match anything on the list, please check <https://docs.google.com/spreadsheets/d/1aJtahrAIlyfyLXni97tHqM_EvjTq9wbzGfmeS8GcbtM/edit?usp=sharing>.")
            else:
                await message.channel.send("Error: " + message.author.name + ", one of the coordinate fields has something other than a number.")
               
        # commands / info / help
        elif message.content.startswith('!map-commands') or message.content.startswith('!map-info') or message.content.startswith('!map-help'):
            await message.channel.send(  
            "The purpose of the bot is to fill out locations of resources on the maps." + '\n' +
            # add method of viewing here
            "Open the map: [INSERT LINK]" + '\n' +
            "Double click anywhere on the map, this will copy a command to your clipboard." + '\n' +
            "Paste it into discord then type the name of the resource you want to add from the list:"
            " <https://docs.google.com/spreadsheets/d/1aJtahrAIlyfyLXni97tHqM_EvjTq9wbzGfmeS8GcbtM/edit?usp=sharing>" + '\n' +
            "A sample command looks like this:" + '\n' +
            "!map-1 0,0,Cattail" + '\n' +
            "To see newly added markers you have to reload the page." + '\n' +
            "If you need help @Freezman or @Clearmind."
            )
        
        else: # unkown command after !map-
            msg = message.content[0:] # starts at 0 because it is testing the first string before a space
            result = [x.strip() for x in msg.split(' ')]
            await message.channel.send("Error: " + message.author.name + ", unkown command " + result[0])
        
client.run('') # Add bot token here
