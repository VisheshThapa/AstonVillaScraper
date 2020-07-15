# AstonVillaScraper
This code scrapes the premiere league website and finds the score and next game that a chosen team will play

The way I made this program is that it looks at the offical premiere league website's table https://www.premierleague.com/tables 
and  looks for the team that the person specified. Currently the hard coded team is my faovurite team Aston Villa. It finds their current win, loss and draw they have. The way this scraper works is that it access the Premiere League Website using the Beautiful Soup package and looks through the html of the website. It finds the 
html which houses every imformation of Aston Villa. Then it is able to extract that imformation into a string or integer format and display it anywhere the user likes.

Addtionally I have connected this screen scraper to a twitter bot which is able to replay to people and answer where or not Aston Villa won or lost thier last game.
The way this works is that the bot looks for changes in the win, loss or draw record. If there is a change present it finds where that change is present. For example: If the change is present in the loss section then the Aston Villa bot will replay with loss. This allows for the user to find if the last game Aston Vill played either a win, loss or draw. This twitter bot code is very simple and is akin to the way many other twitter bots work.

Most of the work for this program was in creating the screen scraper which read the Premiere League table. Even thought I am familir with HTML and CSS, the formatting of the webpage made it difficult to understand completely where each imformation was stored. Addtionally, this is my first time coding a project in python, I am more familir with C++ 11 and it was a good way for me to learn a new programming language. The screen scraper is something that can I be used to extract any Premiere League team's data and I want to use it in the future to create a program which is able to read it  from the website and extract the imformation to the spreadsheet.

Currently the code and the bot isn't being hosted online and was just run on my personal computer. This is due to many online hosting websites are a paid subscription and I do not obtain that sort of money. I plan to create a Rasberry PI server inside my own room and run the code on that server so it doesn't impact that performance of my personal computer. 

Addtionally, now that I have learnt the fundamentals of screen scraping I would like to learn how to use this ability to relay stock imformation onto an excel spreadsheet. I think this would make it easy for me to look how my stocks are doing and properly track them in excel. 
