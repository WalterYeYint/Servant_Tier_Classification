from bs4 import BeautifulSoup
import requests

servant_class = ['Shielder', 'Saber', 'Archer', 
				'Lancer', 'Rider', 'Caster', 'Assassin', 'Berserker', 'Ruler', 'Avenger', 'Moon_Cancer', 'Alter_Ego','Foreigner', 'Pretender', 'Beast']

for servant_class_name in servant_class:
	with open(servant_class_name + ".txt", "w") as f:	
		html_text = requests.get('https://fategrandorder.fandom.com/wiki/' + servant_class_name).text
		soup = BeautifulSoup(html_text, 'lxml')
		servant_list = soup.find_all('figure', class_ = 'thumb tnone show-info-icon')
		servant_list_2 = soup.find_all('figure', class_ = 'thumb tnone')
		print(str(len(servant_list) + len(servant_list_2)) + " servants found in " + servant_class_name + " class.")
		for sl in servant_list:
			servant_name = sl.a['title'].replace(' ','_')
			f.write(servant_name + '\n')
		for sl_2 in servant_list_2:
			servant_name = sl_2.a['title'].replace(' ','_')
			f.write(servant_name + '\n')





