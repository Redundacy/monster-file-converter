import sys

def main():
    sys.stdin = open(sys.argv[1], 'r')
    data = []
    filestr = sys.stdin.readline()
    inquotes = False
    index = 0
    openquote = 0
    closequote = 0
    left_data = ""
    open_right_data = 0
    close_right_data = 0
    bracket_count = 0
    curlybrace_count = 0
    for char in filestr:
        if(char == '['):
            bracket_count = bracket_count + 1
        elif(char == ']'):
            bracket_count = bracket_count - 1
        if(char == '\"'):
            inquotes = not inquotes
            if(inquotes):
                openquote = index
            else:
                closequote = index
                if(left_data == ""):
                    left_data = filestr[openquote+1:closequote]
        if(left_data != "" and char == ':' and not inquotes and bracket_count == 0):
            open_right_data = index
        if(left_data != "" and char == ',' and not inquotes and bracket_count == 0):
            close_right_data = index
            data.append((left_data, filestr[open_right_data+1:close_right_data]))
            left_data = ""
        index = index + 1
    name = cut_quotes([item[1] for item in data if item[0] == 'name'][0])
    tag = cut_quotes([item[1] for item in data if item[0] == 'tag'][0])
    size = cut_quotes([item[1] for item in data if item[0] == 'size'][0])
    type = cut_quotes([item[1] for item in data if item[0] == 'type'][0])
    alignment = cut_quotes([item[1] for item in data if item[0] == 'alignment'][0])
    otherArmorDesc = cut_quotes([item[1] for item in data if item[0] == 'otherArmorDesc'][0])
    hpText = cut_quotes([item[1] for item in data if item[0] == 'hpText'][0])
    speedDesc = cut_quotes([item[1] for item in data if item[0] == 'speedDesc'][0])

    strPoints = cut_quotes([item[1] for item in data if item[0] == 'strPoints'][0])
    strMod = int((int(strPoints) - 10)/2)
    dexPoints = cut_quotes([item[1] for item in data if item[0] == 'dexPoints'][0])
    dexMod = int((int(dexPoints) - 10)/2)
    conPoints = cut_quotes([item[1] for item in data if item[0] == 'conPoints'][0])
    conMod = int((int(conPoints) - 10)/2)
    intPoints = cut_quotes([item[1] for item in data if item[0] == 'intPoints'][0])
    intMod = int((int(intPoints) - 10)/2)
    wisPoints = cut_quotes([item[1] for item in data if item[0] == 'wisPoints'][0])
    wisMod = int((int(wisPoints) - 10)/2)
    chaPoints = cut_quotes([item[1] for item in data if item[0] == 'chaPoints'][0])
    chaMod = int((int(chaPoints) - 10)/2)
    customProf = int([item[1] for item in data if item[0] == 'customProf'][0])
    legendariesDescription = cut_quotes([item[1] for item in data if item[0] == 'legendariesDescription'][0])
    lairDescription = cut_quotes([item[1] for item in data if item[0] == 'lairDescription'][0])

    conditionsList = listify([item[1] for item in data if item[0] == 'conditions'][0])
    conditions = ''
    for condition in conditionsList:
        if (conditions == ''):
            conditions = conditions + cut_quotes(condition[0][1])
        else: 
            conditions = conditions + ", " + cut_quotes(condition[0][1])
    # print(conditions)

    languagesList = listify([item[1] for item in data if item[0] == 'languages'][0])
    understandsBut = cut_quotes([item[1] for item in data if item[0] == 'understandsBut'][0])
    languages = ''
    for language in languagesList:
        if (languages == ''):
            languages = languages + cut_quotes(language[0][1])
        else:
            languages = languages + ", " + cut_quotes(language[0][1])
    if (understandsBut != ''):
        languages = languages + ' (understands but ' + understandsBut + ')'
    # print(languages)

    abilitiesList = listify([item[1] for item in data if item[0] == 'abilities'][0])
    # print(abilitiesList)
    actionsList = listify([item[1] for item in data if item[0] == 'actions'][0])
    # print(actionsList)
    bonusActionsList = listify([item[1] for item in data if item[0] == 'bonusActions'][0])
    # print(bonusActionsList)
    reactionsList = listify([item[1] for item in data if item[0] == 'reactions'][0])
    # print(reactionsList)
    legendariesList = listify([item[1] for item in data if item[0] == 'legendaries'][0])
    # print(legendariesList)
    lairsList = listify([item[1] for item in data if item[0] == 'lairs'][0])
    # print(lairsList)
    regionalsList = listify([item[1] for item in data if item[0] == 'regionals'][0])
    # print(regionalsList)
    mythicsList = listify([item[1] for item in data if item[0] == 'mythics'][0])
    # print(mythicsList)

    skillsList = listify([item[1] for item in data if item[0] == 'skills'][0])
    # print(skillsList)
    skills = ''
    for skill in skillsList:
        modifier = 0
        if (skill[1][1] == '"str"'):
            modifier = strMod
        elif (skill[1][1] == '"dex"'):
            modifier = dexMod
        elif (skill[1][1] == '"con"'):
            modifier = conMod
        elif (skill[1][1] == '"int"'):
            modifier = intMod
        elif (skill[1][1] == '"wis"'):
            modifier = wisMod
        elif (skill[1][1] == '"cha"'):
            modifier = chaMod
        skills = skills + ' ' + cut_quotes(skill[0][1]) + " +" + str(customProf + modifier)

    sthrowsList = listify([item[1] for item in data if item[0] == 'sthrows'][0])
    # print(sthrowsList)
    sthrows = ''
    for sthrow in sthrowsList:
        modifier = 0
        if (int(sthrow[1][1]) == 0):
            modifier = strMod
        elif (int(sthrow[1][1]) == 1):
            modifier = dexMod
        elif (int(sthrow[1][1]) == 2):
            modifier = conMod
        elif (int(sthrow[1][1]) == 3):
            modifier = intMod
        elif (int(sthrow[1][1]) == 4):
            modifier = wisMod
        elif (int(sthrow[1][1]) == 5):
            modifier = chaMod
        sthrows = sthrows + ' ' + cut_quotes(sthrow[0][1]) + " +" + str(customProf + modifier)

    damagetypesList = listify([item[1] for item in data if item[0] == 'damagetypes'][0])
    resistances = ''
    immunities = ''

    senses = ''
    blindsight = cut_quotes([item[1] for item in data if item[0] == 'blindsight'][0])
    if (blindsight != '0'):
        senses = ' Blindsight: ' + blindsight + 'ft'
    blind = [item[1] for item in data if item[0] == 'blind'][0]
    if (senses != '' and blind != 'false'):
        senses = senses + " (blind beyond that point)"
    darkvision = cut_quotes([item[1] for item in data if item[0] == 'darkvision'][0])
    if (senses != '' and darkvision != '0'):
        senses = senses + ", Darkvision: " + darkvision + "ft"
    elif (darkvision != '0'):
        senses = ' Darkvision: ' + darkvision + "ft"
    tremorsense = cut_quotes([item[1] for item in data if item[0] == 'tremorsense'][0])
    if (senses != '' and tremorsense != '0'):
        senses = senses + ", Tremorsense: " + tremorsense + "ft"
    elif(tremorsense != '0'):
        senses = ' Tremorsense: ' + tremorsense + "ft"
    truesight = cut_quotes([item[1] for item in data if item[0] == 'truesight'][0])
    if (senses != '' and truesight != '0'):
        senses = senses + ", Truesight: " + truesight + "ft"
    elif(truesight != '0'):
        senses = ' Truesight: ' + truesight + "ft"
    telepathy = [item[1] for item in data if item[0] == 'telepathy'][0]
    if (senses != '' and telepathy != '0'):
        senses = senses + ", Telepathy: " + telepathy + "ft,"
    elif(telepathy != '0'):
        senses = ' Telepathy: ' + telepathy + "ft,"
    if([item for item in skillsList if item[0][1] == '"perception"'] != '[]'):
        senses = senses + " passive Perception " + str(10 + wisMod + customProf)
    else:
        senses = senses + " passive Perception " + str(10 + wisMod)

    customCr = cut_quotes([item[1] for item in data if item[0] == 'customCr'][0])


    # print(name[0])
    # print(data)
    sys.stdout = open('converted_text.txt', 'w')
    print("{{monster,frame")
    print(f"## {name}")
    if(tag ==''):
        print(f"*{size} {type}, {alignment}*")
        # print("placeholder")
    else:
        print(f"*{size} {type} ({tag}), {alignment}*")
        # print("placeholder")
    print("___")
    print(f"**Armor Class** :: {otherArmorDesc}")
    print(f"**Hit Points** :: {hpText}")
    print(f"**Speed** :: {speedDesc}")
    print("___")
    print("|  STR  |  DEX  |  CON  |  INT  |  WIS  |  CHA  |")
    print("|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|")
    print(f"|{strPoints} ({strMod})|{dexPoints} ({dexMod})|{conPoints} ({conMod})|{intPoints} ({intMod})|{wisPoints} ({wisMod})|{chaPoints} ({chaMod})|")
    print("___")
    # saving throws
    print(f"**Saving Throws** ::{sthrows}")
    # skills
    print(f"**Skills** ::{skills}")
    # damage immunities
    print(f"**Damage Resistances** ::{resistances}")
    print(f"**Damage Immunities** ::{immunities}")
    print(f"**Condition Immunities** :: {conditions}")
    print(f"**Senses** ::{senses}")
    print(f"**Languages** :: {languages}")
    print(f"**Challenge Rating** :: {customCr}")
    print("___")
    if (abilitiesList !=[]):
        for ability in abilitiesList:
            print(f'***{cut_quotes(ability[0][1])}.*** {cut_quotes(ability[1][1])}')
            print(":")
    # if actions, listify, features and iterate them here
    if (actionsList != []):
        print("### Actions")
        for action in actionsList:
            print(f'***{cut_quotes(action[0][1])}.*** {cut_quotes(action[1][1])}')
            print(":")
    # same for bonus actions, reactions, legendary actions, lair actions, and mythic actions
    if (bonusActionsList != []):
        print("### Bonus Actions")
        for baction in bonusActionsList:
            print(f'***{cut_quotes(baction[0][1])}.*** {cut_quotes(baction[1][1])}')
            print(":")
    if (reactionsList != []):
        print("### Reactions")
        for reaction in reactionsList:
            print(f'***{cut_quotes(reaction[0][1])}.*** {cut_quotes(reaction[1][1])}')
            print(":")
    if (legendariesList != []):
        print("### Legendary Actions")
        print(legendariesDescription)
        for legendary in legendariesList:
            print(f'***{cut_quotes(legendary[0][1])}.*** {cut_quotes(legendary[1][1])}')
            print(":")
    if (lairsList != []):
        print("### Lair Actions")
        print(lairDescription)
        for lair in lairsList:
            print(f'***{cut_quotes(lair[0][1])}.*** {cut_quotes(lair[1][1])}')
            print(":")
    print("}}")

    
def cut_quotes(string):
    return string[1:len(string)-1]

def listify(string):
    data = []
    inbrace = 0
    opensegment = 0
    index = 0
    inquotes = False
    left_data = ''
    object = []
    for char in string:
        if (char == '{'):
            inbrace = inbrace + 1
        elif (char == '}'):
            inbrace = inbrace - 1
            object.append((left_data, string[opensegment+1:index]))
            left_data = ''
            data.append(object)
            object = []
        if (char == '\"'):
            inquotes = not inquotes
            if (not inquotes and left_data == ''):
                left_data = string[opensegment+1:index]
            elif(left_data == ''):
                opensegment = index
        if (char == ':' and inbrace > 0 and not inquotes):
            opensegment = index
        if (char == ',' and inbrace > 0 and not inquotes):
            object.append((left_data, string[opensegment+1:index]))
            left_data = ''
        index = index + 1
    return data


if __name__ == '__main__':
    # print(sys.argv)
    main()