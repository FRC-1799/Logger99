# Logger-99 Discord Bot
## For logging Member working hours.

### Usage Licence
This service is free-of-use for any member of FRC Team 1799
Other teams that would like to use this can do so by:

#### Offer via E-Mail
have your business subteam shoot an inquiry to `vanocry@proton.me`
I will personally Accept or decline if your Team sees fit.

##### reasons you can be declined:
- Your teams' logging system is error free
- Your team hasn't exhibited Gracious Profesionalism
- Your Request isn't Profesionally organized.
The reason for requsting Required is mostly all, just a test to see if you are graciously profesional in your inqueries.

#### Support the Team 1799:
Donate any amount of money, Get all of our management tools for free, no email required!

### Operands
General Syntax, `!logger <Operation> <arguments> <operands> <input> <output>`

### General Operations:
```
[---COMMAND-|-----ARGS-----|--DESCRIPTION--]
    log     | int H, int M | Log a Previous Session
    start   |              | start Logging from the current time on
    end     |              | Stop Logging time
    export  |  type, index | export data of all logs
    view    | index | date | view older logs that were exported
    admin   | Operation    | Basically SUDO, has administrative access over logged files.
```
There's only ONE Operand: [-v|verbose| /verbose]
this prints extra data into exported logs.

### Setup - data.json
Data.json is the File that holds Data about the Bot. Most importantly, your Discord API Key
In the Template, There is already a Object "DISCORD_API_KEY", I wonder what goes here.

Theres also Data Required for the export command, in the label "EXPORT_CONF"
If Left Blank, youd need to specify every command run.

### Setup - registry.json
this file holds all users.
there is a "demouser" in place, and thats the syntax needed for every user.
this is this way so data can be stored locally before exporting to a document.
