import os

files = [
    r'Rules_and_Mechanics\_README.md',
    r'Quests_and_Campaigns\_README.md',
    r'Mysteries_and_Themes\Minor\_README.md',
    r'Mysteries_and_Themes\Major\_README.md',
    r'Locations\_README.md',
    r'Items\_README.md',
    r'History_and_Lore\_README.md',
    r'Factions_and_Organizations\_README.md',
    r'Characters\Player_Characters\_README.md',
    r'Characters\NPCs\_README.md',
    r'Characters\Ancestries\_README.md',
    r'Bestiary\_README.md'
]

for f in files:
    print(f'--- {f} ---')
    try:
        with open(f, 'r', encoding='utf-8') as file:
            print(file.read().strip())
    except Exception as e:
        print(e)
    print()
