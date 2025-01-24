# ;;
# ;;    logger99
# ;;    By KICHANe
# ;;    For FRC Team #1799
# ;;

# ;;
# ;;
# ;;    INCLUDE
# ;;
# ;;

import discord      # gee i wonder
import sqlite3
from discord.ext import commands

# ;;
# ;;
# ;;    INIT
# ;;
# ;;

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents="message_content")
MAIN = sqlite3.connect("placeholder.db")
MAINC = MAIN.cursor()

# ;;
# ;;
# ;;    SQLITE DATABASE INIT CHECKS
# ;;
# ;;

MAINC.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    discord_id TEXT NOT NULL UNIQUE,
    username TEXT NOT NULL
)
CREATE TABLE IF NOT EXISTS user_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    discord_id TEXT NOT NULL,
    hours INTEGER NOT NULL,
    FOREIGN KEY (discord_id) REFERENCES users (discord_id)
)
""")

MAINC.commit()

# ;;
# ;;
# ;;    DECLARATIONS | GENERAL FUNCTIONS
# ;;
# ;;

def WriteSQL(DATA, ID, UNAME):
    try:
        MAINC.execute("INSERT INTO users (discord_id, username) VALUES (?, ?)", (ID, UNAME))
        MAIN.commit()
    except sqlite3.IntegrityError:
        return "[ SQLITE ] : INTEGRITYERROR"

    MAINC.execute("SELECT * FROM users WHERE discord_id = ?", (ID,))
    user = MAINC.fetchone()
    
    if user:
        # Insert the value into the user_data table
        MAINC.execute("INSERT INTO user_data (discord_id, value) VALUES (?, ?)", (ID, DATA))
        MAIN.commit()
        return
    else:
        return "[ DATAERROR ] : USERNAME NOT IDENTIFIED"

# ;;
# ;;
# ;;    DECLARATIONS | API - SPECIFIC FUNCTIONS
# ;;
# ;;

# @bot.command(name='view')
# async def view(ctx):
#     # Retrieve all users from the 'users' table
#     MAINC.execute("SELECT * FROM users")
#     users = MAINC.fetchall()
    
#     # Retrieve all data from the 'user_data' table
#     MAINC.execute("SELECT * FROM user_data")
#     user_data = MAINC.fetchall()
    
#     # Format the data
#     user_info = "### Users Table ###\n"
#     for user in users:
#         user_info += f"ID: {user[0]}, Discord ID: {user[1]}, Username: {user[2]}\n"
    
#     user_data_info = "\n### User Data Table ###\n"
#     for data in user_data:
#         user_data_info += f"ID: {data[0]}, Discord ID: {data[1]}, Value: {data[2]}\n"

#     full_log = user_info + user_data_info

#     if len(full_log) > 2000:  # Discord message limit
#         with open("log.txt", "w", encoding="utf-8") as file:
#             file.write(full_log)
#         await ctx.send("Oversize Log: Written to File", file=discord.File("log.TXT"))
#     else:
#         await ctx.send(f"```\n{full_log}\n```")

@bot.command(name='log')
async def log(ctx, *args):
    if len(args) == 0:
        await ctx.send("This Operation Requiers Operands: <int Hour> <int Minute>")
        return
    
    # CommandLine Argument Parsing
    i = 0
    while i < len(args):
        if isinstance(args[i], int) == False:
            await ctx.send("This Requires Operand of type: Integer")
            return 
        if i > 1:
            break
        if isinstance(args[i], int):
            uname = ctx.author.id
            user = ctx.author.name
            await ctx.send(WriteSQL(*args[i], user, uname))
        else:
            await ctx.send("This Requires Operand of type: Integer")
            return

# ;;
# ;;
# ;;    EXECUTION: MAINLOOP
# ;;
# ;;

bot.run("apiKey Goes Here :3 :3")