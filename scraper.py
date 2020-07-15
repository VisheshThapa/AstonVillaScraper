import requests
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime


result = requests.get("https://www.premierleague.com/tables")

src = result.content

soup = BeautifulSoup(src, 'html.parser')

aston = soup.find("tr", {"data-filtered-table-row-name": "Aston Villa"})

aston_wins  = aston.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text
aston_draws = aston.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text
aston_loss = aston.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text

#find date of next match

next_match = aston.td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling

next_match_date = next_match.find("span", {"class": "matchInfo"}).text

next_match_time = next_match.find("time").text

today_date = date.today().strftime("%X %A %d %B %Y")

today_time = datetime.now().time().strftime("%H:%M")

#check
aston_file = "aston_track.txt"
def check_if_win():
    file_read = open(aston_file, 'r')
    last_result = file_read.readlines()
    if(int(last_result[0]) > int(aston_wins)):
        file_read.close()
        return "Win"
    elif(int(last_result[1]) > int(aston_draws)):
        file_read.close()
        return "Draw"
    elif(int(last_result[2]) > int(aston_loss)):
        file_read.close()
        return "Loss"
    file_read.close()

status = check_if_win()

def replay_last_game():
    file_read = open(aston_file, 'r')
    last_result = file_read.readlines()
    if((int(last_result[0]) == int(aston_wins)) and (int(last_result[1]) == int(aston_draws)) and (int(last_result[2]) == int(aston_loss))):
        return_statement = last_result[3]
        file_read.close()
        return return_statement


def store_aston_track(aston_file, aston_wins, aston_draws, aston_loss):
    file_write = open(aston_file, 'w')
    file_write.write(str(aston_wins) + "\n")
    file_write.write(str(aston_draws) + "\n")
    file_write.write(str(aston_loss) + "\n")
    file_write.write(str(status) + "\n")
    file_write.close()

