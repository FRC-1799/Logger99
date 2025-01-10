import discord      # gee i wonder

from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents="message_content")
g
@bot.command(name='log')
async def log(ctx, *args):
    if len(args) == 0:
        await ctx.send("This Operation Requiers Operands: <int Hour> <int Minute>")
        return
    # CommandLine Argument Parsing
    i = 0;
    while i < len(args):
        if isinstance(argv[i], int) == False:
            await ctx.send("This Requires Operand of type: Integer");
            return
        if 



bot.run("eL-pDOFl4UN3Qs_vVbWHqdCGiAXifxeQ")