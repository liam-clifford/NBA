
import requests
from urlparse import urljoin
from bs4 import BeautifulSoup
import string 
import csv
import urllib
import decimal
import re
import numpy as np
from datetime import datetime

p = requests.get("http://www.hoopsstats.com/basketball/fantasy/nba/playerstats/18/1/eff/2-1")
soup = BeautifulSoup(p.content, "html.parser")
data = soup.find_all("table",{"class": "statscontent"})	
csv_file = open('Home.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Rank', 'Player', 'Games', 'Minutes', 'Points', 'Rebounds', 'Assists', 'Steals', 'Blocks', 'TO', 'PF', 'Dreb', 'Oreb', 'FGperf', 'FGpercent', 'TreyPerf', 'TreyPercent', 'FTperf', 'FTpercent', 'Eff'])

for item in data:
	Rank = item.contents[1].find_all("td")[0].text
	Player = str(item.contents[1].find_all("a"))
	Games = item.contents[1].find_all("td")[2].text
	Minutes = item.contents[1].find_all("td")[3].text
	Points = item.contents[1].find_all("td")[4].text
	Rebounds = item.contents[1].find_all("td")[5].text
	Assists = item.contents[1].find_all("td")[6].text
	Steals = item.contents[1].find_all("td")[7].text
	Blocks = item.contents[1].find_all("td")[8].text
	TO = item.contents[1].find_all("td")[9].text
	PF = item.contents[1].find_all("td")[10].text
	Dreb = item.contents[1].find_all("td")[11].text
	Oreb = item.contents[1].find_all("td")[12].text
	FGperf = item.contents[1].find_all("td")[13].text
	FGpercent = item.contents[1].find_all("td")[14].text
	TreyPerf = item.contents[1].find_all("td")[15].text
	TreyPercent = item.contents[1].find_all("td")[16].text
	FTperf = item.contents[1].find_all("td")[17].text
	FTpercent = item.contents[1].find_all("td")[18].text
	Eff = item.contents[1].find_all("td")[19].text

	print Rank, Player.split('/')[6], Games, Minutes, Points, Rebounds, Assists, Steals, Blocks, TO, PF, Dreb, Oreb, FGperf, FGpercent, TreyPerf, TreyPercent, FTperf, FTpercent, Eff

	csv_writer.writerow([Rank, Player.split('/')[6], Games, Minutes, Points, Rebounds, Assists, Steals, Blocks, TO, PF, Dreb, Oreb, FGperf, FGpercent, TreyPerf, TreyPercent, FTperf, FTpercent, Eff])

csv_file.close()

print

csv_file = open('Roto.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Salary', 'Team', 'Position', 'Opponent', 'Ceiling', 'Floor', 'Projected FP'])
url = 'https://rotogrinders.com/projected-stats/nba-player.csv?site=fanduel'
r = requests.get(url)
text = r.iter_lines()
reader = csv.reader(text, delimiter=',')
for item in reader:
	print item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]
 	csv_writer.writerow([item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7]])	
csv_file.close()   

print

p = requests.get("http://www.hoopsstats.com/basketball/fantasy/nba/playerstats/18/1/eff/3-1")
soup = BeautifulSoup(p.content, "html.parser")

csv_file = open('Road.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Rank', 'Player', 'Games', 'Minutes', 'Points', 'Rebounds', 'Assists', 'Steals', 'Blocks', 'TO', 'PF', 'Dreb', 'Oreb', 'FGperf', 'FGpercent', 'TreyPerf', 'TreyPercent', 'FTperf', 'FTpercent', 'Eff'])

data = soup.find_all("table",{"class": "statscontent"})

for item in data:
	Rank = item.contents[1].find_all("td")[0].text
	Player = str(item.contents[1].find_all("a"))
	Games = item.contents[1].find_all("td")[2].text
	Minutes = item.contents[1].find_all("td")[3].text
	Points = item.contents[1].find_all("td")[4].text
	Rebounds = item.contents[1].find_all("td")[5].text
	Assists = item.contents[1].find_all("td")[6].text
	Steals = item.contents[1].find_all("td")[7].text
	Blocks = item.contents[1].find_all("td")[8].text
	TO = item.contents[1].find_all("td")[9].text
	PF = item.contents[1].find_all("td")[10].text
	Dreb = item.contents[1].find_all("td")[11].text
	Oreb = item.contents[1].find_all("td")[12].text
	FGperf = item.contents[1].find_all("td")[13].text
	FGpercent = item.contents[1].find_all("td")[14].text
	TreyPerf = item.contents[1].find_all("td")[15].text
	TreyPercent = item.contents[1].find_all("td")[16].text
	FTperf = item.contents[1].find_all("td")[17].text
	FTpercent = item.contents[1].find_all("td")[18].text
	Eff = item.contents[1].find_all("td")[19].text

	print Rank, Player.split('/')[6], Games, Minutes, Points, Rebounds, Assists, Steals, Blocks, TO, PF, Dreb, Oreb, FGperf, FGpercent, TreyPerf, TreyPercent, FTperf, FTpercent, Eff

	csv_writer.writerow([Rank, Player.split('/')[6], Games, Minutes, Points, Rebounds, Assists, Steals, Blocks, TO, PF, Dreb, Oreb, FGperf, FGpercent, TreyPerf, TreyPercent, FTperf, FTpercent, Eff])

csv_file.close()

print 

p = requests.get("https://basketballmonster.com/dfsdvp.aspx")
soup = BeautifulSoup(p.content, "html.parser")

csv_file = open('DVP.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'PG', 'SG', 'SF', 'PF', 'C'])

statData = soup.find_all("tbody")

for a in statData:
	for i in range(30):
		Name = str(a.contents[i].text)[3:6]
		PG = str(a.contents[i].text)[13:17]
		SG = str(a.contents[i].text)[17:21]
		SF = str(a.contents[i].text)[21:25]
		PF = str(a.contents[i].text)[25:29]
		C = str(a.contents[i].text)[29:33]
		print Name, PG, SG, SF, PF, C
		csv_writer.writerow([Name, PG, SG, SF, PF, C])
csv_file.close()

print

p = requests.get("https://www.teamrankings.com/nba/stat/possessions-per-game?date")
soup = BeautifulSoup(p.content, "html.parser")

csv_file = open('Possessions.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Season', 'last3', 'last1', 'Home', 'Away', 'lastSeason'])

statData = soup.find_all("tbody")

for a in statData:
	for i in range(30):
		Name = str(a.find_all("td", {"class": "text-left nowrap"})[i]).split('=')[2]
		Name = Name.split('>')[0]
		Name = re.sub('"', '', Name)
		Season = str(a.find_all("td", {"class": "text-right"})[((i)*6)]).split('=')[2]
		Season = Season.split('>')[0]
		Season = re.sub('"', '', Season)
		last3 = str(a.find_all("td", {"class": "text-right"})[((i)*6)+1]).split('=')[2]
		last3 = last3.split('>')[0]
		last3 = re.sub('"', '', last3)
		last1 = str(a.find_all("td", {"class": "text-right"})[((i)*6)+2]).split('=')[2]
		last1 = last1.split('>')[0]
		last1 = re.sub('"', '', last1)
		Home = str(a.find_all("td", {"class": "text-right"})[((i)*6)+3]).split('=')[2]
		Home = Home.split('>')[0]
		Home = re.sub('"', '', Home)
		Away = str(a.find_all("td", {"class": "text-right"})[((i)*6)+4]).split('=')[2]
		Away = Away.split('>')[0]
		Away = re.sub('"', '', Away)
		lastSeason = str(a.find_all("td", {"class": "text-right"})[((i)*6)+5]).split('=')[2]
		lastSeason = lastSeason.split('>')[0]
		lastSeason = re.sub('"', '', lastSeason)
		
		print Name, Season, last3, last1, Home, Away, lastSeason
		
		csv_writer.writerow([Name, Season, last3, last1, Home, Away, lastSeason])
csv_file.close()

print

p = requests.get("https://www.teamrankings.com/nba/stat/defensive-efficiency?date")
soup = BeautifulSoup(p.content, "html.parser")

csv_file = open('Defensive_Rtg.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Season', 'last3', 'last1', 'Home', 'Away', 'lastSeason'])

statData = soup.find_all("tbody")

for a in statData:
	for i in range(30):
		Name = str(a.find_all("td", {"class": "text-left nowrap"})[i]).split('=')[2]
		Name = Name.split('>')[0]
		Name = re.sub('"', '', Name)
		Season = str(a.find_all("td", {"class": "text-right"})[((i)*6)]).split('=')[2]
		Season = Season.split('>')[0]
		Season = re.sub('"', '', Season)
		last3 = str(a.find_all("td", {"class": "text-right"})[((i)*6)+1]).split('=')[2]
		last3 = last3.split('>')[0]
		last3 = re.sub('"', '', last3)
		last1 = str(a.find_all("td", {"class": "text-right"})[((i)*6)+2]).split('=')[2]
		last1 = last1.split('>')[0]
		last1 = re.sub('"', '', last1)
		Home = str(a.find_all("td", {"class": "text-right"})[((i)*6)+3]).split('=')[2]
		Home = Home.split('>')[0]
		Home = re.sub('"', '', Home)
		Away = str(a.find_all("td", {"class": "text-right"})[((i)*6)+4]).split('=')[2]
		Away = Away.split('>')[0]
		Away = re.sub('"', '', Away)
		lastSeason = str(a.find_all("td", {"class": "text-right"})[((i)*6)+5]).split('=')[2]
		lastSeason = lastSeason.split('>')[0]
		lastSeason = re.sub('"', '', lastSeason)
		
		print Name, Season, last3, last1, Home, Away, lastSeason
		
		csv_writer.writerow([Name, Season, last3, last1, Home, Away, lastSeason])
csv_file.close()

print

p = requests.get("https://www.teamrankings.com/nba/stat/offensive-efficiency?date")
soup = BeautifulSoup(p.content, "html.parser")

csv_file = open('Offensive_Rtg.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Season', 'last3', 'last1', 'Home', 'Away', 'lastSeason'])

statData = soup.find_all("tbody")

for a in statData:
	for i in range(30):
		Name = str(a.find_all("td", {"class": "text-left nowrap"})[i]).split('=')[2]
		Name = Name.split('>')[0]
		Name = re.sub('"', '', Name)
		Season = str(a.find_all("td", {"class": "text-right"})[((i)*6)]).split('=')[2]
		Season = Season.split('>')[0]
		Season = re.sub('"', '', Season)
		last3 = str(a.find_all("td", {"class": "text-right"})[((i)*6)+1]).split('=')[2]
		last3 = last3.split('>')[0]
		last3 = re.sub('"', '', last3)
		last1 = str(a.find_all("td", {"class": "text-right"})[((i)*6)+2]).split('=')[2]
		last1 = last1.split('>')[0]
		last1 = re.sub('"', '', last1)
		Home = str(a.find_all("td", {"class": "text-right"})[((i)*6)+3]).split('=')[2]
		Home = Home.split('>')[0]
		Home = re.sub('"', '', Home)
		Away = str(a.find_all("td", {"class": "text-right"})[((i)*6)+4]).split('=')[2]
		Away = Away.split('>')[0]
		Away = re.sub('"', '', Away)
		lastSeason = str(a.find_all("td", {"class": "text-right"})[((i)*6)+5]).split('=')[2]
		lastSeason = lastSeason.split('>')[0]
		lastSeason = re.sub('"', '', lastSeason)
		
		print Name, Season, last3, last1, Home, Away, lastSeason
		
		csv_writer.writerow([Name, Season, last3, last1, Home, Away, lastSeason])
csv_file.close()

print

p = requests.get("https://www.basketball-reference.com/leagues/NBA_2018_per_game.html")
soup = BeautifulSoup(p.content, "html.parser")

csv_file = open('AvgData.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Rank', 'Player', 'Pos', 'Age', 'Team', 'G', 'GS', 'MP', 'FG', 'FGA', 'FGperc', 'treysMade', 'treyAttempts', 'treyPerc', 'twosMade', 'twosAttempted', 'twoPerc', 'eFGperc', 'FT', 'FTA', 'FTperc', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'ppg'])

data = soup.find_all("tr",{"class": "full_table"})

for item in data:
	Rank = str(item.find_all("th", {"scope": "row"}))
	Rank = Rank.split('csk="')[1]
	Rank = Rank.split('"')[0]
	Player = str(item.find_all("td", {"class": "left"}))
	Player = Player.split('">')[2]
	Player = Player.split('</a>')[0]
	Pos = str(item.find_all("td", {"class": "center"}))
	Pos = Pos.split('>')[1]
	Pos = Pos.split('<')[0]
	Age = str(item.find_all("td", {"class": "right"}))
	Age = Age.split('>')[1]
	Age = Age.split('<')[0]

	try:
		i = 4
		Team = str(item.find_all("td", {"class": "left"}))
		Team = Team.split('">')[i]
		Team = Team.split('</a>')[0]
		pass
	except:
		Team = str(item.find_all("td", {"class": "left"}))
		Team = Team.split('">')[i-1]
		Team = Team.split('</td>')[0]

	G = str(item.find_all("td", {"class": "right"}))
	G = G.split('>')[3]
	G = G.split('<')[0]
	GS = str(item.find_all("td", {"class": "right"}))
	GS = GS.split('>')[5]
	GS = GS.split('<')[0]
	MP = str(item.find_all("td", {"class": "right"}))
	MP = MP.split('>')[7]
	MP = MP.split('<')[0]
	FG = str(item.find_all("td", {"class": "right"}))
	FG = FG.split('>')[9]
	FG = FG.split('<')[0]
	FGA = str(item.find_all("td", {"class": "right"}))
	FGA = FGA.split('>')[11]
	FGA = FGA.split('<')[0]
	FGperc = str(item.find_all("td", {"class": "right"}))
	FGperc = FGperc.split('>')[13]
	FGperc = FGperc.split('<')[0]
	treysMade = str(item.find_all("td", {"class": "right"}))
	treysMade = treysMade.split('>')[15]
	treysMade = treysMade.split('<')[0]
	treyAttempts = str(item.find_all("td", {"class": "right"}))
	treyAttempts = treyAttempts.split('>')[17]
	treyAttempts = treyAttempts.split('<')[0] 
	treyPerc = str(item.find_all("td", {"class": "right"}))
	treyPerc = treyPerc.split('>')[19]
	treyPerc = treyPerc.split('<')[0]
	twosMade = str(item.find_all("td", {"class": "right"}))
	twosMade = twosMade.split('>')[21]
	twosMade = twosMade.split('<')[0]
	twosAttempted = str(item.find_all("td", {"class": "right"}))
	twosAttempted = twosAttempted.split('>')[23]
	twosAttempted = twosAttempted.split('<')[0]
	twoPerc = str(item.find_all("td", {"class": "right"}))
	twoPerc = twoPerc.split('>')[25]
	twoPerc = twoPerc.split('<')[0]
	eFGperc = str(item.find_all("td", {"class": "right"}))
	eFGperc = eFGperc.split('>')[27]
	eFGperc = eFGperc.split('<')[0]
	FT = str(item.find_all("td", {"class": "right"}))
	FT = FT.split('>')[29]
	FT = FT.split('<')[0]
	FTA = str(item.find_all("td", {"class": "right"}))
	FTA = FTA.split('>')[31]
	FTA = FTA.split('<')[0]
	FTperc = str(item.find_all("td", {"class": "right"}))
	FTperc = FTperc.split('>')[33]
	FTperc = FTperc.split('<')[0]
	ORB = str(item.find_all("td", {"class": "right"}))
	ORB = ORB.split('>')[35]
	ORB = ORB.split('<')[0]
	DRB = str(item.find_all("td", {"class": "right"}))
	DRB = DRB.split('>')[37]
	DRB = DRB.split('<')[0]
	TRB = str(item.find_all("td", {"class": "right"}))
	TRB = TRB.split('>')[39]
	TRB = TRB.split('<')[0] 
	AST = str(item.find_all("td", {"class": "right"}))
	AST = AST.split('>')[41]
	AST = AST.split('<')[0]
	STL = str(item.find_all("td", {"class": "right"}))
	STL = STL.split('>')[43]
	STL = STL.split('<')[0]
	BLK = str(item.find_all("td", {"class": "right"}))
	BLK = BLK.split('>')[45]
	BLK = BLK.split('<')[0]
	TOV = str(item.find_all("td", {"class": "right"}))
	TOV = TOV.split('>')[47]
	TOV = TOV.split('<')[0]
	PF = str(item.find_all("td", {"class": "right"}))
	PF = PF.split('>')[49]
	PF = PF.split('<')[0]
	ppg = str(item.find_all("td", {"class": "right"}))
	ppg = ppg.split('>')[51]
	ppg = ppg.split('<')[0]

	print Rank, Player, Pos, Age, Team, G, GS, MP, FG, FGA, FGperc, treysMade, treyAttempts, treyPerc, twosMade, twosAttempted, twoPerc, eFGperc, FT, FTA, FTperc, ORB, DRB, TRB, AST, STL, BLK, TOV, PF, ppg
	
	csv_writer.writerow([Rank, Player, Pos, Age, Team, G, GS, MP, FG, FGA, FGperc, treysMade, treyAttempts, treyPerc, twosMade, twosAttempted, twoPerc, eFGperc, FT, FTA, FTperc, ORB, DRB, TRB, AST, STL, BLK, TOV, PF, ppg])
csv_file.close()

print

i = datetime.now()
year = "%s" %i.year
month = "%s" %i.month
day = "%s" %i.day
day = int(day)
print day

dk = str("draftkings")
fd = str("fanduel")

i = fd
t = dk

def DFFfd():
	csv_file = open('DFF.csv', 'w')

	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(['firstname', 'lastname', 'Pos', 'tm', 'opp', 'Salary', 'FP'])

	p = requests.get("http://www.dailyfantasyfuel.com/nba/projections/" + "{}".format(i) + "/" + "{}".format(year) + '-' + "{}".format(month) + '-' + "{}".format(day))
	soup = BeautifulSoup(p.content, "html.parser")
	data = soup.find_all("div",{"class": "col-12 table-row hov-bg-offwhite bg-white border-bottom-1 border-vlt vertical-full"})

	for item in data:
		firstname = str(item.contents[0].find_all("div"))
		firstname = firstname.split('<span class="hidden-sm">')[1].split('</span')[0]
		lastname = str(item.contents[0].find_all("div"))
		lastname = lastname.split('</span> <span>')[1].split('</span')[0]
		Pos = str(item.contents[0].find_all("div"))
		Pos = Pos.split('<span class="text-blue-lt bold">')[1].split('</span')[0]
		Salary = str(item.contents[0].find_all("div"))
		Salary = Salary.split('xb7')[1].split('</span')[0]
		tm = str(item.contents[0].find_all("div"))
		tm = tm.split('src="http://cdn.dailyfantasyfuel.com/logos/nba/')[1].split('.svg')[0]
		opp = str(item.contents[0].find_all("div"))
		opp = opp.split('src="http://cdn.dailyfantasyfuel.com/logos/nba/')[3].split('.svg')[0]
		FP = str(item.contents[0].find_all("div"))
		FP = FP.split('border-offwhite rel">')[1].split(' <span')[0]
		print firstname, lastname, Pos, tm, opp, Salary, FP

	 	csv_writer.writerow([firstname, lastname, Pos, tm, opp, Salary, FP])
	csv_file.close()   

def DFFdk():
	csv_file = open('DFF.csv', 'w')

	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(['firstname', 'lastname', 'Pos', 'tm', 'opp', 'Salary', 'FP'])

	p = requests.get("http://www.dailyfantasyfuel.com/nba/projections/" + "{}".format(t) + "/" + "{}".format(year) + '-' + "{}".format(month) + '-' + "{}".format(day))
	soup = BeautifulSoup(p.content, "html.parser")
	data = soup.find_all("div",{"class": "col-12 table-row hov-bg-offwhite bg-white border-bottom-1 border-vlt vertical-full"})

	for item in data:
		firstname = str(item.contents[0].find_all("div"))
		firstname = firstname.split('<span class="hidden-sm">')[1].split('</span')[0]
		lastname = str(item.contents[0].find_all("div"))
		lastname = lastname.split('</span> <span>')[1].split('</span')[0]
		Pos = str(item.contents[0].find_all("div"))
		Pos = Pos.split('<span class="text-blue-lt bold">')[1].split('</span')[0]
		Salary = str(item.contents[0].find_all("div"))
		Salary = Salary.split('xb7')[1].split('</span')[0]
		tm = str(item.contents[0].find_all("div"))
		tm = tm.split('src="http://cdn.dailyfantasyfuel.com/logos/nba/')[1].split('.svg')[0]
		opp = str(item.contents[0].find_all("div"))
		opp = opp.split('src="http://cdn.dailyfantasyfuel.com/logos/nba/')[3].split('.svg')[0]
		FP = str(item.contents[0].find_all("div"))
		FP = FP.split('border-offwhite rel">')[1].split(' <span')[0]
		print firstname, lastname, Pos, tm, opp, Salary, FP

	 	csv_writer.writerow([firstname, lastname, Pos, tm, opp, Salary, FP])
	csv_file.close()   

if DFFfd() is None:
	print DFFdk()
else:
	print DFFfd()

print 

p = requests.get("https://www.basketball-reference.com/leagues/NBA_2018_advanced.html")
soup = BeautifulSoup(p.content, "html.parser")

csv_file = open('AdvData.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Rank', 'Player', 'Pos', 'Age', 'Team', 'G', 'MP', 'PER', 'TSperc', 'treyPAr', 'FTr', 'ORBperc', 'DRBperc', 'TRBperc', 'ASTperc', 'STLperc', 'BLKperc', 'TOVperc', 'USGperc', 'OWS', 'DWS', 'WS', 'WinSharesPerTotal', 'OBPM', 'DBPM', 'BPM', 'VORP'])

data = soup.find_all("tr",{"class": "full_table"})

for item in data:
	Rank = str(item.find_all("th", {"scope": "row"}))
	Rank = Rank.split('csk="')[1]
	Rank = Rank.split('"')[0]
	Player = str(item.find_all("td", {"class": "left"}))
	Player = Player.split('">')[2]
	Player = Player.split('</a>')[0]
	Pos = str(item.find_all("td", {"class": "center"}))
	Pos = Pos.split('>')[1]
	Pos = Pos.split('<')[0]
	Age = str(item.find_all("td", {"class": "right"}))
	Age = Age.split('>')[1]
	Age = Age.split('<')[0]
	
	try:
		i = 4
		Team = str(item.find_all("td", {"class": "left"}))
		Team = Team.split('">')[i]
		Team = Team.split('</a>')[0]
		pass
	except:
		Team = str(item.find_all("td", {"class": "left"}))
		Team = Team.split('">')[i-1]
		Team = Team.split('</td>')[0]

	G = str(item.find_all("td", {"class": "right"}))
	G = G.split('>')[3]
	G = G.split('<')[0]
	MP = str(item.find_all("td", {"class": "right"}))
	MP = MP.split('>')[5]
	MP = MP.split('<')[0]
	PER = str(item.find_all("td", {"class": "right"}))
	PER = PER.split('>')[7]
	PER = PER.split('<')[0]
	TSperc = str(item.find_all("td", {"class": "right"}))
	TSperc = TSperc.split('>')[9]
	TSperc = TSperc.split('<')[0]
	treyPAr = str(item.find_all("td", {"class": "right"}))
	treyPAr = treyPAr.split('>')[11]
	treyPAr = treyPAr.split('<')[0]
	FTr = str(item.find_all("td", {"class": "right"}))
	FTr = FTr.split('>')[13]
	FTr = FTr.split('<')[0]
	ORBperc = str(item.find_all("td", {"class": "right"}))
	ORBperc = ORBperc.split('>')[15]
	ORBperc = ORBperc.split('<')[0]
	DRBperc = str(item.find_all("td", {"class": "right"}))
	DRBperc = DRBperc.split('>')[17]
	DRBperc = DRBperc.split('<')[0] 
	TRBperc = str(item.find_all("td", {"class": "right"}))
	TRBperc = TRBperc.split('>')[19]
	TRBperc = TRBperc.split('<')[0]
	ASTperc = str(item.find_all("td", {"class": "right"}))
	ASTperc = ASTperc.split('>')[21]
	ASTperc = ASTperc.split('<')[0]
	STLperc = str(item.find_all("td", {"class": "right"}))
	STLperc = STLperc.split('>')[23]
	STLperc = STLperc.split('<')[0]
	BLKperc = str(item.find_all("td", {"class": "right"}))
	BLKperc = BLKperc.split('>')[25]
	BLKperc = BLKperc.split('<')[0]
	TOVperc = str(item.find_all("td", {"class": "right"}))
	TOVperc = TOVperc.split('>')[27]
	TOVperc = TOVperc.split('<')[0]
	USGperc = str(item.find_all("td", {"class": "right"}))
	USGperc = USGperc.split('>')[29]
	USGperc = USGperc.split('<')[0]
	OWS = str(item.find_all("td", {"class": "right"}))
	OWS = OWS.split('>')[33]
	OWS = OWS.split('<')[0]
	DWS = str(item.find_all("td", {"class": "right"}))
	DWS = DWS.split('>')[35]
	DWS = DWS.split('<')[0]
	WS = str(item.find_all("td", {"class": "right"}))
	WS = WS.split('>')[37]
	WS = WS.split('<')[0]
	WinSharesPerTotal = str(item.find_all("td", {"class": "right"}))
	WinSharesPerTotal = WinSharesPerTotal.split('>')[39]
	WinSharesPerTotal = WinSharesPerTotal.split('<')[0]
	OBPM = str(item.find_all("td", {"class": "right"}))
	OBPM = OBPM.split('>')[43]
	OBPM = OBPM.split('<')[0] 
	DBPM = str(item.find_all("td", {"class": "right"}))
	DBPM = DBPM.split('>')[45]
	DBPM = DBPM.split('<')[0]
	BPM = str(item.find_all("td", {"class": "right"}))
	BPM = BPM.split('>')[47]
	BPM = BPM.split('<')[0]
	VORP = str(item.find_all("td", {"class": "right"}))
	VORP = VORP.split('>')[49]
	VORP = VORP.split('<')[0]

	print Rank, Player, Pos, Age, Team, G, MP, PER, TSperc,	treyPAr, FTr, ORBperc, DRBperc, TRBperc, ASTperc, STLperc, BLKperc, TOVperc, USGperc, OWS, DWS, WS, WinSharesPerTotal, OBPM, DBPM, BPM, VORP

	csv_writer.writerow([Rank, Player, Pos, Age, Team, G, MP, PER, TSperc,	treyPAr, FTr, ORBperc, DRBperc, TRBperc, ASTperc, STLperc, BLKperc, TOVperc, USGperc, OWS, DWS, WS, WinSharesPerTotal, OBPM, DBPM, BPM, VORP])
csv_file.close()

print

i = datetime.now()

year = "%s" %i.year
month = "%s" %i.month
day = "%s" %i.day
day = int(day)-1

p = requests.get("https://www.basketball-reference.com/friv/dailyleaders.fcgi?month='month'&day='day'&year='year'") 
soup = BeautifulSoup(p.content, "html.parser")

csv_file = open('GameData1.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twentyone', 'twentytwo', 'twentythree', 'twentyfour', 'twentyfive', 'twentysix'])

data = soup.find_all("tr")

for item in data:
	one = str(item.find_all("th", {"scope": "row"}))
	if one.split('csk="')[0].split('"')[0] == '[]':
		pass	
	else:
		one.split('csk="')[1].split('"')[0]
		one = one.split('csk="')[1].split('"')[0]
	two = str(item.find_all("td", {"class": "left"}))
	if two.split('">')[0].split('</a>')[0] == '[]':
		pass
	else:
		two.split('">')[2].split('</a>')[0]
		two = two.split('">')[2].split('</a>')[0]
	three = str(item.find_all("td", {"class": "left"}))
	if three.split('">')[0].split('</a>')[0] == '[]':
		pass
	else:
		three.split('">')[4].split('</a>')[0]
		three = three.split('">')[4].split('</a>')[0]
	four = str(item.find_all("td", {"class": "center "}))
	if four.split('>')[0].split('<')[0] == '[]':
		pass
	else:
		four.split('>')[1].split('<')[0]
		four = four.split('>')[1].split('<')[0]
	five = str(item.find_all("td", {"class": "left"}))
	if five.split('">')[0].split('</a>')[0] == '[]':
		pass
	else:
		five.split('">')[6].split('</a>')[0]
		five = five.split('">')[6].split('</a>')[0]
	six = str(item.find_all("td", {"class": "center "}))
	if six.split('>')[0].split('<')[0] == '[]':
		pass
	else:
		six.split('>')[4].split('<')[0]
		six = six.split('>')[4].split('<')[0]
	seven = str(item.find_all("td", {"class": "right"}))
	if seven.split('">')[0].split('</td>')[0] == '[]':
		pass
	else:
		seven.split('">')[1].split('</td>')[0]
		seven = seven.split('">')[1].split('</td>')[0]
		seven = re.sub(':', '.', seven)
	eight = str(item.find_all("td", {"class": "right"}))
	if eight.split('">')[0].split('</td>')[0] == '[]':
		pass
	else:
		eight.split('">')[2].split('</td>')[0]
		eight = eight.split('">')[2].split('</td>')[0]

	nine = str(item.find_all("td", {"class": "right"}))
	if nine.split('">')[0].split('</td>')[0] == '[]':
		pass
	else:
		nine.split('">')[3].split('</td>')[0]
		nine = nine.split('">')[3].split('</td>')[0]
	ten = str(item.find_all("td", {"class": "right"}))
	if ten.split('">')[0].split('</td>')[0] == '[]':
		pass
	else:
		ten.split('">')[4].split('</td>')[0]
		ten = ten.split('">')[4].split('</td>')[0]
	eleven = str(item.find_all("td", {"class": "right"}))
	if eleven.split('">')[0].split('</td>')[0] == '[]':
		pass
	else:
		eleven.split('">')[5].split('</td>')[0]
		eleven = eleven.split('">')[5].split('</td>')[0]
	twelve = str(item.find_all("td", {"class": "right"}))
	if twelve.split('">')[0].split('</td>')[0] == '[]':
		pass
	else:
		twelve.split('">')[6].split('</td>')[0]
		twelve = twelve.split('">')[6].split('</td>')[0]
	thirteen = str(item.find_all("td", {"class": "right"}))
	if thirteen.split('">')[0].split('</td>')[0] == '[]':
		pass
	else:
		thirteen.split('">')[7].split('</td>')[0]
		thirteen = thirteen.split('">')[7].split('</td>')[0]
	fourteen = str(item.find_all("td", {"class": "right"}))
	if fourteen.split('">')[0].split('</td>')[0] == '[]':
		pass
	else:
		fourteen.split('">')[8].split('</td>')[0]
		fourteen = fourteen.split('">')[8].split('</td>')[0]
	fifteen = str(item.find_all("td", {"class": "right"}))
	if fifteen.split('">')[0].split('</td>')[0] == '[]':
		pass
	else:
		fifteen.split('">')[9].split('</td>')[0]
		fifteen = fifteen.split('">')[9].split('</td>')[0]
	sixteen = str(item.find_all("td", {"class": "right"}))
	if sixteen.split('">')[0].split('</td>')[0] == '[]':
		pass
	else:
		sixteen.split('">')[10].split('</td>')[0]
		sixteen = sixteen.split('">')[10].split('</td>')[0]
	seventeen = str(item.find_all("td", {"class": "right"}))
	if seventeen.split('">')[0].split('</td>')[0] == '[]':
		pass
	else:
		seventeen.split('">')[11].split('</td>')[0]
		seventeen = seventeen.split('">')[11].split('</td>')[0]
	eighteen = str(item.find_all("td", {"class": "right"}))
	if eighteen.split('">')[0].split('</td>')[0] == '[]':
		pass
	else:
		eighteen.split('">')[12].split('</td>')[0]
		eighteen = eighteen.split('">')[12].split('</td>')[0]
	nineteen = str(item.find_all("td", {"class": "right"}))
	if nineteen.split('">')[0].split('</td>')[0] == '[]':
		pass
	else:
		nineteen.split('">')[13].split('</td>')[0]
		nineteen = nineteen.split('">')[13].split('</td>')[0]
	twenty = str(item.find_all("td", {"class": "right"}))
	if twenty.split('">')[0].split('</td>')[0] == '[]':
		pass
	else:
		twenty.split('">')[14].split('</td>')[0]
		twenty = twenty.split('">')[14].split('</td>')[0]
	twentyone = str(item.find_all("td", {"class": "right"}))
	if twentyone.split('">')[0].split('</td>')[0] == '[]':
		pass
	else:
		twentyone.split('">')[15].split('</td>')[0]
		twentyone = twentyone.split('">')[15].split('</td>')[0]
	twentytwo = str(item.find_all("td", {"class": "right"}))
	if twentytwo.split('">')[0].split('</td>')[0] == '[]':
		pass
	else:
		twentytwo.split('">')[16].split('</td>')[0]
		twentytwo = twentytwo.split('">')[16].split('</td>')[0]
	twentythree = str(item.find_all("td", {"class": "right"}))
	if twentythree.split('">')[0].split('</td>')[0] == '[]':
		pass
	else:
		twentythree.split('">')[17].split('</td>')[0]
		twentythree = twentythree.split('">')[17].split('</td>')[0]
	twentyfour = str(item.find_all("td", {"class": "right"}))
	if twentyfour.split('">')[0].split('</td>')[0] == '[]':
		pass
	else:
		twentyfour.split('">')[18].split('</td>')[0]
		twentyfour = twentyfour.split('">')[18].split('</td>')[0]
	twentyfive = str(item.find_all("td", {"class": "right"}))
	if twentyfive.split('">')[0].split('</td>')[0] == '[]':
		pass
	else:
		twentyfive.split('">')[19].split('</td>')[0]
		twentyfive = twentyfive.split('">')[19].split('</td>')[0]
	twentysix = str(item.find_all("td", {"class": "right"}))
	if twentysix.split('">')[0].split('</td>')[0] == '[]':
		pass
	else:
		twentysix.split('">')[20].split('</td>')[0]
		twentysix = twentysix.split('">')[20].split('</td>')[0]
		print one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, twentyone, twentytwo, twentythree, twentyfour, twentyfive, twentysix
	
		csv_writer.writerow([one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, twentyone, twentytwo, twentythree, twentyfour, twentyfive, twentysix])
csv_file.close()

print

csv_file = open('playerinfo.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'team'])

pageNumber = range(1,35)
for count in pageNumber:
	url = ("https://www.foxsports.com/nba/players?teamId=0&season=2017&position=0")
	#full url = https://www.foxsports.com/nba/players?teamId=0&season=2017&position=0&page=[loop over # of pages]
	p = requests.get(url + "&page={}".format(count))
	soup = BeautifulSoup(p.content, "html.parser")
	data = soup.find_all("tr",{"class": "wisbb_fvStand"})
	for item in data:
		Names = str(item.find_all("a",{"class": "wisbb_fullPlayer"})).split("nba/")[0]
		if Names == '[]':
			continue
		else:
			try:
				Names = str(item.find_all("a",{"class": "wisbb_fullPlayer"})).split("nba/")[1].split("-player")[0]
				Names = re.sub('-', " ",Names)
				Names = re.sub(' 3',"",Names)
				Names = re.sub(' 2',"",Names)
				Names = re.sub(' 1',"",Names)
				Names = re.sub(' jr',"",Names)
				Names = re.sub(' iv',"",Names)
				Names = re.sub(' ii',"",Names)
				Names = re.sub(' iii',"",Names)
				#format these names off the top
				team = str(item.find("td",{"class": "wisbb_priorityColumn"}))
				if team == 'None':
					continue
				else:
					team = team.split(">")[2]
					team = re.sub("</a",'',team)
					#format teams
					try:
						if Names.index(len(Names)-1,len(Names)) == ' i':
							Names = str(item.find_all("a",{"class": "wisbb_fullPlayer"})).split("nba/")[1].split("-player")[0]
							Names = re.sub('-', " ",Names)
							#try to substitute the occurances of 'i' (if any)	
						else:
							pass
					except:
						pass
			except:
				pass		
			print Names, team
			csv_writer.writerow([Names, team])
csv_file.close()

print

p = requests.get("https://www.numberfire.com/nba/daily-fantasy/daily-basketball-projections")
soup = BeautifulSoup(p.content, "html.parser")

csv_file = open('NF.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'fp', 'price', 'value', 'min', 'pts', 'reb', 'ast', 'stl', 'blk', 'to'])

statData = soup.find_all("tbody", {"class": "stat-table__body"})

fullData = str(soup.find_all("a", {"class": "full"}))
fullData = fullData
sub = "href"
count = fullData.count(sub,0,100000)	
count = int(count)
if count < 208:
	count = int(count)
else:
	count = 208
for a in statData:
	for i in range(count):
		if i > 0:
				Name = str(a.find_all("span", {"class": "player-info"})[i-1]).split('>')[4]
				Name = Name.split('>')[0]
				Name = re.sub('"', '', Name)
				Name = Name.split('  ')[18]			
				Pos = str(a.find_all("span", {"class": "player-info"})[i-1]).split('>')[6]
				Pos = Pos.split('<')[0]
				fp = str(a.find_all("td", {"class": "fp active"})[i-1]).split('>')[1]
				fp = fp.split('<')[0]
				fp = fp.split(' ')[28]
				price = str(a.find_all("td", {"class": "cost"})[i-1]).split('>')[1]
				price = price.split('<')[0]
				price = price.split(' ')[28]
				value = str(a.find_all("td", {"class": "value"})[i-1]).split('>')[1]
				value = value.split('<')[0]
				value = value.split(' ')[28]
				min = str(a.find_all("td", {"class": "min"})[i-1]).split('>')[1]
				min = min.split('<')[0]
				min = min.split(' ')[28]
				pts = str(a.find_all("td", {"class": "pts"})[i-1]).split('>')[1]
				pts = pts.split('<')[0]
				pts = pts.split(' ')[28]
				reb = str(a.find_all("td", {"class": "reb"})[i-1]).split('>')[1]
				reb = reb.split('<')[0]
				reb = reb.split(' ')[28]
				ast = str(a.find_all("td", {"class": "ast"})[i-1]).split('>')[1]
				ast = ast.split('<')[0]
				ast = ast.split(' ')[28]
				stl = str(a.find_all("td", {"class": "stl"})[i-1]).split('>')[1]
				stl = stl.split('<')[0]
				stl = stl.split(' ')[28]
				blk = str(a.find_all("td", {"class": "blk"})[i-1]).split('>')[1]
				blk = blk.split('<')[0]
				blk = blk.split(' ')[28]
				to = str(a.find_all("td", {"class": "to"})[i-1]).split('>')[1]
				to = to.split('<')[0]
				to = to.split(' ')[28]
				print Name + " " + Pos, fp, price, value, min, pts, reb, ast, stl, blk, to
				
				csv_writer.writerow([Name + " " + Pos, fp, price, value, min, pts, reb, ast, stl, blk, to])
csv_file.close()



