# AstonVillaScraper
This code scrapes the premiere league website and finds the score and next game that a chosen team will play

The way I made this program is that it looks at the offical premiere league website's table https://www.premierleague.com/tables 
and  looks for the team that the person specified. Currently the hard coded team is my faovurite team, Aston Villa. It finds their current win, loss and draw they have. The way this scraper works is that it access the Premiere League Website using the Beautiful Soup package and looks through the html of the website. It finds the 
html which houses every imformation of Aston Villa. Then it is able to extract that imformation into a string or integer format and display it anywhere the user likes.

Addtionally I have connected this screen scraper to a twitter bot which is able to replay to people and answer where or not Aston Villa won or lost thier last game.
The way this works is that the bot looks for changes in the win, loss or draw record. If there is a change present it finds where that change is present. For example: If the change is present in the loss section then the Aston Villa bot will replay with loss. This allows for the user to find if the last game Aston Vill played either a win, loss or draw. This twitter bot code is very simple and is akin to the way many other twitter bots work. Addtionally, it also checks if Aston Villa is currently playing a game by the use of screen scraping. It finds their next game and check the current time (in GMT-7 timezone) thus even their next game imformation is available. I made it so that the bot sleep when AstonVilla is playing their next game 
