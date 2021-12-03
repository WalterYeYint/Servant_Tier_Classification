from os import closerange
from bs4 import BeautifulSoup
import requests

# servant_class = ['Moon_Cancer']
servant_class = ['Saber', 'Archer', 'Lancer', 'Rider', 'Caster', 'Assassin', 'Berserker', 
				'Ruler', 'Avenger', 'Moon_Cancer', 'Alter_Ego','Foreigner', 'Pretender', 'Beast']
labels = 'name,min_attack,max_attack,min_HP,max_HP,star_absorption,star_generation,NP_charge_attack,NP_charge_defense,death_rate,strength,endurance,agility,mana,luck,NP'

servant_info = []

def getServantInfo(servant_name):
	servant_info = []
	servant_info.append(servant_name)
	html_text = requests.get('https://fategrandorder.fandom.com/wiki/' + servant_name).text
	soup = BeautifulSoup(html_text, 'lxml')

	closetable = soup.find('table', class_ = 'closetable')
	closetable_td_s = closetable.find_all('td')
	# print(closetable_td_s)
	for td in closetable_td_s:
		if "ATK:" in td.b or "HP:" in td.b or "Star Absorption" in td.b or "Star Generation" in td.b or "NP Charge ATK" in td.b or "NP Charge DEF" in td.b or "Death Rate" in td.b:
			if "ATK:" in td.b or "HP:" in td.b:
				td.span.decompose()
				left_value, right_value = td.text.replace(' ', '').replace(',', '').replace('\n', '').split("/")
				servant_info.append(left_value)
				servant_info.append(right_value)
				# print(left_value, right_value)
			else:
				td.span.decompose()
				value = td.text.replace(' ', '').replace(',', '').replace('\n', '')
				servant_info.append(value)

	wikitable = soup.find_all('table', class_ = 'wikitable')
	for table in wikitable:
		if "Endurance:" in table.text:
			wikitable_td_s = table.find_all('td')
			for td in wikitable_td_s:
				td.b.decompose()
				value = td.text.replace(' ', '').replace(',', '').replace('\n', '')
				servant_info.append(value)
			# print(servant_info)
	return servant_info


for servant_class_name in servant_class:
	with open(servant_class_name + ".txt", "w") as f:
		f.write(labels + '\n')	
		html_text = requests.get('https://fategrandorder.fandom.com/wiki/' + servant_class_name).text
		soup = BeautifulSoup(html_text, 'lxml')
		servant_list = soup.find_all('figure', class_ = 'thumb tnone show-info-icon')
		servant_list_2 = soup.find_all('figure', class_ = 'thumb tnone')
		print(str(len(servant_list) + len(servant_list_2)) + " servants found in " + servant_class_name + " class.")
		for sl in servant_list:
			servant_name = sl.a['title'].replace(' ','_')
			servant_info = getServantInfo(servant_name)
			servant_info_string = ",".join(servant_info)
			f.write(servant_info_string + '\n')

		for sl_2 in servant_list_2:
			servant_name = sl_2.a['title'].replace(' ','_')
			servant_info = getServantInfo(servant_name)
			servant_info_string = ",".join(servant_info)
			f.write(servant_info_string + '\n')









