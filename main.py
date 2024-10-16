import msvcrt
import os
import time
import random

STATE_NAMES = {"california":39,
               "texas":30,
               "florida":22,
               "new york":19,
               "pennsylvania":13,
               "illinois":12,
               "ohio": 11,
               "georgia":11,
               "north carolina":10,
               "michigan":10,
               "new jersey":9,
               "virginia":9,
               "washington":9,
               "arizona":7,
               "tennessee":7,
               "massachusetts":7,
               "indiana":7,
               "missouri":6,
               "maryland":6,
               "wisconsin":6,
               "colorado":6,
               "minnesota":5,
               "south carolina":5,
               "alabama":5,
               "louisiana":4,
               "kentucky":4,
               "oregon":4,
               "oklahoma":4,
               "connecticut":3,
               "utah":3,
               "iowa":3,
               "nevada":3,
               "arkansas":3,
               "kansas":3,
               "mississippi":3,
               "new mexico":2,
               "nebraska":2,
               "idaho":2,
               "west virginia":2,
               "hawaii":1,
               "new hampshire":1,
               "maine":1,
               "montana":1,
               "rhode island":1,
               "delaware":1,
               "south dakota":.9,
               "north dakota":.7,
               "alaska":.7,
               "vermont":.6,
               "wyoming":.5}

ELECTORAL_VOTES  = {"alabama":9,
                    "alaska":3,
                    "arizona":11,
                    "california":54,
                    "arkansas":6,
                    "colorado":10,
                    "connecticut":7,
                    "delaware":3,
                    "florida":30,
                    "georgia":16,
                    "hawaii":4,
                    "idaho":4,
                    "illinois":19,
                    "indiana":11,
                    "iowa":6,
                    "kansas":6,
                    "kentucky":8,
                    "louisiana":8,
                    "maine":4,
                    "maryland":10,
                    "massachusetts":11,
                    "michigan":15,
                    "minnesota":10,
                    "mississippi":8,
                    "missouri":10,
                    "montana":4,
                    "nebraska":5,
                    "nevada":5,
                    "new hampshire": 4,
                    "new jersey":13,
                    "new mexico":5,
                    "new york":28,
                    "north carolina":16,
                    "north dakota":3,
                    "ohio":17,
                    "oklahoma":7,
                    "oregon": 8,
                    "pennsylvania":19,
                    "rhode island":4,
                    "south carolina":9,
                    "south dakota":3,
                    "tennessee":11,
                    "texas":40,
                    "utah": 6,
                    "vermont":3,
                    "virginia":13,
                    "washington":12,
                    "west virginia":4,
                    "wisconsin":20,
                    "wyoming":3}


numbers = [[" ||_",
                "(_-<",
                "/ _/",
                " || "],
               [" _ ",
                "/ |",
                "| |",
                "|_|"],
               [" ___ ",
                "|_  )",
                " / / ",
                "/___|"],
               [" ____",
                "|__ /",
                " |_ \\",
                "|___/"],
               [" _ _  ",
                "| | | ",
                "|_  _|",
                "  |_| "],
               [" ___ ",
                "| __|",
                "|__ \\",
                "|___/"],
               ["  __ ",
                " / / ",
                "/ _ \\",
                "\___/"],
               [" ____ ",
                "|__  |",
                "  / / ",
                " /_/  "],
               [" ___ ",
                "( _ )",
                "/ _ \\",
                "\___/"],
               [" ___ ",
                "/ _ \\",
                "\_, /",
                " /_/ "],
               ["  __  ",
                " /  \ ",
                "| () |",
                " \__/ "]]

def intro():
    config()
    text = [" ________  __                        __      __                          ", 
            "/        |/  |                      /  |    /  |                         ", 
            "$$$$$$$$/ $$ |  ______    _______  _$$ |_   $$/   ______   _______       ", 
            "$$ |__    $$ | /      \  /       |/ $$   |  /  | /      \ /       \      ", 
            "$$    |   $$ |/$$$$$$  |/$$$$$$$/ $$$$$$/   $$ |/$$$$$$  |$$$$$$$  |     ", 
            "$$$$$/    $$ |$$    $$ |$$ |        $$ | __ $$ |$$ |  $$ |$$ |  $$ |     ", 
            "$$ |_____ $$ |$$$$$$$$/ $$ \_____   $$ |/  |$$ |$$ \__$$ |$$ |  $$ |     ", 
            "$$       |$$ |$$       |$$       |  $$  $$/ $$ |$$    $$/ $$ |  $$ |     ",
            "$$$$$$$$/ $$/  $$$$$$$/  $$$$$$$/    $$$$/  $$/  $$$$$$/  $$/   $$/      ",
            "\n\n",
            " __       __                                                             ",
            "/  \     /  |                                                            ",
            "$$  \   /$$ |  ______   _______    ______    ______    ______    ______  ",
            "$$$  \ /$$$ | /      \ /       \  /      \  /      \  /      \  /      \ ",
            "$$$$  /$$$$ | $$$$$$  |$$$$$$$  | $$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  |",
            "$$ $$ $$/$$ | /    $$ |$$ |  $$ | /    $$ |$$ |  $$ |$$    $$ |$$ |  $$/ ",
            "$$ |$$$/ $$ |/$$$$$$$ |$$ |  $$ |/$$$$$$$ |$$ \__$$ |$$$$$$$$/ $$ |      ",
            "$$ | $/  $$ |$$    $$ |$$ |  $$ |$$    $$ |$$    $$ |$$       |$$ |      ",
            "$$/      $$/  $$$$$$$/ $$/   $$/  $$$$$$$/  $$$$$$$ | $$$$$$$/ $$/       ",
            "                                           /  \__$$ |                    ",
            "                                           $$    $$/                     ",
            "                                            $$$$$$/                      ",
            "\n",
            "Press Enter to Start"]
    
    print("\n")
    for line in text:
        print(line.center(100))
        time.sleep(.05)
    input()

def printPartyText(text, selection, wait):
    for i, line in enumerate(text):
        if selection == 0:
            if i == 0:
                print("\n\n")
                print(f"{'_'*51}".center(100))
            elif i > 0 and i < 9:
                print(f"| {line} |".center(100))
            elif i == 9:
                print(f"|{'_'*51}|".center(100))
                print("\n\n")
            else:
                print(line.center(100))
        else:
            if i == 9:
                print("\n\n")
                print(f"{'_'*51}".center(100))
            elif i > 9 and i < 16:
                print(f"| {line} |".center(100))
            elif i == 16:
                print(f"|{'_'*51}|".center(100))
                print("\n")
            else:
                print(line.center(100))
        if wait: time.sleep(.05)

def selectParty() -> int:
    selection = 0
    text = ["\n\n\n",
            "______                 _     _ _                 ",
            "| ___ \               | |   | (_)                ",
            "| |_/ /___ _ __  _   _| |__ | |_  ___ __ _ _ __  ",
            "|    // _ \ '_ \| | | | '_ \| | |/ __/ _` | '_ \ ",
            "| |\ \  __/ |_) | |_| | |_) | | | (_| (_| | | | |",
            "\_| \_\___| .__/ \__,_|_.__/|_|_|\___\__,_|_| |_|",
            "          | |                                    ",
            "          |_|                                    ",
            "\n\n",
            "______                                    _      ",
            "|  _  \                                  | |     ",
            "| | | |___ _ __ ___   ___   ___ _ __ __ _| |_    ",
            "| | | / _ \ '_ ` _ \ / _ \ / __| '__/ _` | __|   ",
            "| |/ /  __/ | | | | | (_) | (__| | | (_| | |_    ",
            "|___/ \___|_| |_| |_|\___/ \___|_|  \__,_|\__|   ",
            "\n\n",
            "Press 'w' to move you selection up",
            "Press 's' to move your selection down",
            "Press 'Enter' to select your party"]
    
    os.system("cls")
    printPartyText(text, selection, True)
    
    while True:
        inp = msvcrt.getch()
        if "s" in str(inp): selection = 1
        elif "w" in str(inp): selection = 0
        elif "r" in str(inp): break

        os.system("cls")
        printPartyText(text, selection, False)
    return selection

def ifTutorial() -> bool:
    selection = True
    text = ["\n\n",
            "______                                                _           ",
            "|  _  \                                              | |          ",
            "| | | |___    _   _  ___  _   _  __      ____ _ _ __ | |_    __ _ ",
            "| | | / _ \  | | | |/ _ \| | | | \ \ /\ / / _` | '_ \| __|  / _` |",
            "| |/ / (_) | | |_| | (_) | |_| |  \ V  V / (_| | | | | |_  | (_| |",
            "|___/ \___/   \__, |\___/ \__,_|   \_/\_/ \__,_|_| |_|\__|  \__,_|",
            "               __/ |                                              ",
            "              |___/                                               ",
            "\n",
            " _         _             _       _ ___  ",
            "| |       | |           (_)     | |__ \ ",
            "| |_ _   _| |_ ___  _ __ _  __ _| |  ) |",
            "| __| | | | __/ _ \| '__| |/ _` | | / / ",
            "| |_| |_| | || (_) | |  | | (_| | ||_|  ",
            " \__|\__,_|\__\___/|_|  |_|\__,_|_|(_)  "]
    
    while True:
        os.system("cls")
        for line in text:
            print(line.center(100))
        print("\n\n")
        if selection:
            print("--> Yes <--      No  ".center(100))
        else:
            print("     Yes      --> No <--".center(100))
        print("\n\n")
        print("Press 'a' to move your selection left".center(100))
        print("Press 'd' to move your selection right".center(100))
        print("Press 'enter' to selection your option".center(100))
        inp = msvcrt.getch()
        if "a" in str(inp): selection = True
        elif "d" in str(inp): selection = False
        elif "r" in str(inp): return selection

def tutorial(run):
    print(run)

def printButtonText(text, selection):
    for i, line in enumerate(text):
        if selection == 0:
            if i < 6:print(f"    {line}")
            elif i == 6:
                line = line.split("_", 2)
                print(f"{'_'.join([line[0], line[1]])}_    {line[2]}")
            elif i == 7:
                line = line.split("|", 4)
                print(f"{'|'.join([line[0], line[1], line[2], line[3],])}|    {line[4]}")
            else: print(line)
        elif selection == 1:
            if i == 6:print(f"    {line[0:15]}{line[19:]}")
            elif i == 7:print(f"    {line[0:16]}{line[20:]}")
            elif i > 7 and i < 12:print(f"    {line}")
            else:print(line)
        elif selection == 2:
            if i > 11 and i < 16:print(f"    {line}")
            elif i == 16 or i == 17:print(f"{line[0:15]}    {line[15:]}")
            else:print(line)
        else:
            if i == 16 or i == 17: print(f"    {line[:15]}{line[19:]}")
            elif i > 17: print(f"    {line}")
            else: print(line)

def history():
    for item in gameHistory:
        print(f" --[ {item}\n")

def states():
    os.system("cls")
    text = ["\n",
            "     _        _            ",
            "    | |      | |           ",
            " ___| |_ __ _| |_ ___  ___ ",
            "/ __| __/ _` | __/ _ \/ __|",
            "\__ \ || (_| | ||  __/\__ \\",
            "|___/\__\__,_|\__\___||___/"]
    for i, line in enumerate(text):
        print(line, end="")
        if i == 5: print(" "*15 + "Press any button to go back")
        else: print("")
    
    out = ""
    end = False
    for i, item in enumerate(STATE_NAMES):
        if out != "": 
            #out += (" " * (15 - len(item)))
            out += "        "
            end = True
        else:
            end = False
            #if i % 4 != 0: out += "\033[48;5;237m"
            #else: out += "\033[0m"
        if perc[item] >= 50: displayPerc = f"\033[32m{perc[item]}%\033[0m"
        else: displayPerc = f"\033[31m{perc[item]}%\033[0m"
        out += f"{item}:{' '*(15-len(item))}{displayPerc}{' '*(5-len(str(perc[item])))}"
        if party == 0: out += "Republican,"
        else: out += "Democrat,"
        population = str(STATE_NAMES[item])
        out += f"{' '*(4-len(population))}{population}M"
        if end: 
            print(out)
            out = ""
    inp = msvcrt.getch()
    home()

def printCampaignSelection(selection: int, text: str) -> str:
    print("\n")
    print("Select a campaign option".center(100))
    print("\n")
    arrows = [[" __  ", " \ \ ", "  > >", " /_/ ", ""], ["   __", "  / /", " < < ", "  \_\\", ""]]
    arrowCount = 0
    for i, line in enumerate(text):
        if selection == 0:
            if i < 4: print(f"{arrows[0][i]} {line} {arrows[1][i]}".center(100))
            else: print(line.center(100))
        elif selection == 1:
            if i > 3 and i < 9: print(f"{arrows[0][arrowCount]} {line} {arrows[1][arrowCount]}".center(100))
            else: print(line.center(100))
            if arrowCount == 4: arrowCount = 0
            else: arrowCount += 1
        else:
            if i > 8: print(f"{arrows[0][arrowCount]} {line} {arrows[1][arrowCount]}".center(100))
            else: print(line.center(100))
            if arrowCount == 4: arrowCount = 0
            else: arrowCount += 1
    print("\n\n")
    print("Press 'backspace' to go back".center(100))

def action(act: str):
    global gameHistory
    global gameStats
    global perc

    doActionBool = True

    if "ad" in act:
        gameStats["ads"] = [3*(int(act.split('-')[1])), 3]
        gameHistory.append(f"Bought an ad with an impact score of {act.split('-')[1]} for 4 rounds")
    elif act[0] == "r":
        if gameStats["money"] > int(act.split("-")[1]): gameStats["money"] -= int(act.split("-")[1])
        else:
            os.system("cls")
            print("\n\n\n\n\n\n\n\n")
            print("You do not have enough money to do this".center(100))
            print("\n")
            input("Press 'enter' to continue".center(100))
        perc[act.split("-")[3]] += int(act.split("-")[2])
        gameHistory.append(f"Had a rally in {act.split('-')[3]}; increased influence by {act.split('-')[2]}% and costed ${act.split('-')[1]}")
        gameStats["recentlySpent"] = int(act.split("-")[1])
    elif act[0] == "s":
        gameStats["money"] -= 5
        perc[act.split("-")[1]] += 8
        gameHistory.append(f"Gave a speech in {act.split('-')[1]}; increased influence by 8% and costed $5")
        gameStats["recentlySpent"] = 5
    elif act[0] == "f":
        profit = int(act.split("-")[1])
        gameStats["money"] += profit
        gameStats["recentIncome"] = profit
        gameHistory.append(f"You raised ${profit} in a fundraiser")       ##### fix whatever is breaking the money page when you get money
        doActionBool = False

    if doActionBool: doActions()

def doActions():
    global gameStats
    gameStats["round"] += 1

    if gameStats['round'] == 15:
        endGame()

    if gameStats["ads"][0] != 0:
        global perc
        for item in STATE_NAMES: 
            if perc[item] <= 100:
                perc[item] = perc[item] + gameStats["ads"][0]
            if perc[item] > 100: perc[item] == 100
        gameStats["ads"][1] -= 1
        if gameStats["ads"][1] == 0: gameStats["ads"][0] = 0
    
    if gameStats["sponsorCooldown"] != 0:
        gameStats["sponsorCooldown"] -= 1

def getPopular() -> list:
    votes = [0, 0] # your party, opposing party
    for item in STATE_NAMES:
        votes[0] += STATE_NAMES[item]*(perc[item]/100)
        votes[1] += STATE_NAMES[item]*(1-(perc[item]/100))
    return [int(votes[0]), int(votes[1])]

def endGame():
    text = ["  ___ _        _   _            ___             _ _      ",
            " | __| |___ __| |_(_)___ _ _   | _ \___ ____  _| | |_ ___",
            " | _|| / -_) _|  _| / _ \ ' \  |   / -_|_-< || | |  _(_-<",
            " |___|_\___\__|\__|_\___/_||_| |_|_\___/__/\_,_|_|\__/__/",
            " --------------------------------------------------------",
            "",
            "  ___               _           __   __   _       _ ",
            " | _ \___ _ __ _  _| |__ _ _ _  \ \ / /__| |_ ___(_)",
            " |  _/ _ \ '_ \ || | / _` | '_|  \ V / _ \  _/ -_)_ ",
            " |_| \___/ .__/\_,_|_\__,_|_|     \_/\___/\__\___(_)",
            "         |_|                                        "]
    
    electoral = ["  ___ _        _                _  __   __   _       _ ",
                 " | __| |___ __| |_ ___ _ _ __ _| | \ \ / /__| |_ ___(_)",
                 " | _|| / -_) _|  _/ _ \ '_/ _` | |  \ V / _ \  _/ -_)_ ",
                 " |___|_\___\__|\__\___/_| \__,_|_|   \_/\___/\__\___(_)"]
    votes = getPopular()
    if party == 1: 
        demo = votes[0]
        repub = votes[1]
    else:
        demo = votes[1]
        repub = votes[0]

    for line in text: print(line.center(100))
    print(f"Democratic Vote: {demo}M".center(100))
    print("\n")
    print(f"Republican Vote: {repub}M".center(100))
    #print("\n")
    
    print("\n")
    for line in electoral: print(line.center(100))
    electoralVotes = [0,0] #in favor, not in favor of you
    for item in STATE_NAMES:
        if perc[item] <50: electoralVotes[1] += ELECTORAL_VOTES[item]
        else: electoralVotes[0] += ELECTORAL_VOTES[item]
    
    print("\n")
    if party == 1:
        print(f"Democrat: {electoralVotes[0]}".center(100))
        print("\n")
        print(f"Republican: {electoralVotes[1]}".center(100))
    else:
        print(f"Democrat: {electoralVotes[1]}".center(100))
        print("\n")
        print(f"Republican: {electoralVotes[0]}".center(100))
    
    print("\n")
    input("Press 'enter' to continue".center(100))

    os.system("cls")
    if electoralVotes[0] >= electoralVotes[1]:
        print("\n\n\n\n\n\n\n")
        print("You Win".center(100))
        print("\n\n\n\n\n\n\n")
        print("Press 'enter' to exit".center(100))
    else:
        print("\n\n\n\n\n\n\n")
        print("You Lose".center(100))
        print("\n\n\n\n\n\n\n")
        print("Press 'enter' to exit".center(100))

    input()
    exit(0)

def section2(selection: int):
    os.system("cls")
    #minimum cost will be $2 -- anything with a pop less then 2 will get rounded up to 2
    #max cost will be $30 -- anything with a pop higher than 30 will get rounded down to 30
    options = ["    _      _             _   _         ",
               "   /_\  __| |_ _____ _ _| |_(_)___ ___ ",
               "  / _ \/ _` \ V / -_) '_|  _| (_-</ -_)",
               " /_/ \_\__,_|\_/\___|_|  \__|_/__/\___|",
               "  ___      _ _                         ",
               " | _ \__ _| | |_  _                    ",
               " |   / _` | | | || |                   ",
               " |_|_\__,_|_|_|\_, |                   ",
               "               |__/                    ",
               "  ___                  _               ",
               " / __|_ __  ___ ___ __| |_             ",
               " \__ \ '_ \/ -_) -_) _| ' \            ",
               " |___/ .__/\___\___\__|_||_|           ",
               "     |_|                               "]
    impact = ["  _                     _   _ ",
              " (_)_ __  _ __  __ _ __| |_(_)",
              " | | '  \| '_ \/ _` / _|  _|_ ",
              " |_|_|_|_| .__/\__,_\__|\__(_)",
              "         |_|                  "]
    numbers = [["  _ ", " / |", " | |", " |_|", "    "], ["  ___ ", " |_  )", "  / / ", " /___|", "      "], ["  ____", " |__ /", "  |_ \\", " |___/", "      "]]
    back = False

    if selection == 0:
        impactScore = 0
        while True:
            os.system("cls")
            for i in range(4): print(options[i].center(100))
            print(f"{'-'*47}".center(100))
            print("\n\n")
            print("Buying an Advertisment will slowly increase your influnce".center(100))
            print("in areas across the country for several turns".center(100))
            print("The impact score you choose will change how strongly your ads influence people".center(100))
            print("Having a higher impact score will also increase the cost".center(100))
            print("\n")
            print("Current Cost:".center(100))
            print(f"${5*(impactScore+1)}".center(100))

            for i in range(5): print(f"{impact[i]}  {numbers[impactScore][i]}".center(100))
            
            print("\n\n")
            print("Controls: 'w', 's', 'enter', 'backspace'".center(100))
            
            inp = msvcrt.getch()
            if "w" in str(inp) and impactScore != 0: impactScore -= 1
            elif "s" in str(inp) and impactScore != 2: impactScore += 1
            elif "r" in str(inp): break
            elif "x08" in str(inp):
                back = True
                break
        if back: campaign()
        else: 
            action(f"ad-{impactScore}")
            home()

    elif selection == 1:
        stateIndex = 0
        stateList = []
        for item in STATE_NAMES: stateList.append(item)
        stateList.sort()

        while True:
            os.system("cls")
            for i in range(5): print(options[i+4][1:20].center(100))
            print(f"{'-'*47}".center(100))
            print("\n\n")
            print("Rallying in each state has a different cost depending on population".center(100))
            print("States with higher populations cost more to have rallies at".center(100))
            print("")
            print("However, rallies in more populated states can have more impact on your vote".center(100))
            print("and can increase your vote in the electoral college".center(100))
            print("\n")
            print("Select a state to rally in:".center(100))
            print("\n")

            if stateIndex == 0:
                print(f"...".center(100))
                print(f"--> {stateList[stateIndex]} <--".center(100))
                print(f"{stateList[stateIndex+1]}".center(100))
            elif stateIndex == 48:
                print(f"{stateList[stateIndex-1]}".center(100))
                print(f"--> {stateList[stateIndex]} <--".center(100))
                print(f"...".center(100))
            else:
                print(f"{stateList[stateIndex-1]}".center(100))
                print(f"--> {stateList[stateIndex]} <--".center(100))
                print(f"{stateList[stateIndex+1]}".center(100))

            if STATE_NAMES[stateList[stateIndex]] <= 2: cost = 2
            elif STATE_NAMES[stateList[stateIndex]] >= 30: cost = 30
            else: cost = STATE_NAMES[stateList[stateIndex]]
            influnce = getInfluence(stateList[stateIndex])

            print("\n")
            print(f"Cost: ${cost}".center(100))
            print(f"Influence: {influnce}%".center(100))

            print("\n")
            print("Controls: 'w', 's', 'enter', 'backspace'".center(100))

            inp = msvcrt.getch()
            if "w" in str(inp) and stateIndex != 0: stateIndex -= 1
            elif "s" in str(inp) and stateIndex != 48: stateIndex += 1
            elif "r" in str(inp): break
            elif "x08" in str(inp):
                back = True
                break
        if back: campaign()
        else:
            action(f"r-{cost}-{influnce}-{stateList[stateIndex]}")
            home()
    
    elif selection == 2:
        stateIndex = 0
        stateList = []
        for item in STATE_NAMES: stateList.append(item)
        stateList.sort()

        while True:
            os.system("cls")
            for i in range(5): print(options[i+9][1:28].center(100))
            print(f"{'-'*47}".center(100))
            print("\n\n")
            print("Giving a speech in a state has the same amount of influence evrywhere".center(100))
            print("It also has the same cost for every state".center(100))
            print("\n")
            print("This makes it easier to get states in favor of you party".center(100))
            print("But it might take several purchases".center(100))
            print("\n\n")

            if stateIndex == 0:
                print(f"...".center(100))
                print(f"--> {stateList[stateIndex]} <--".center(100))
                print(f"{stateList[stateIndex+1]}".center(100))
            elif stateIndex == 48:
                print(f"{stateList[stateIndex-1]}".center(100))
                print(f"--> {stateList[stateIndex]} <--".center(100))
                print(f"...".center(100))
            else:
                print(f"{stateList[stateIndex-1]}".center(100))
                print(f"--> {stateList[stateIndex]} <--".center(100))
                print(f"{stateList[stateIndex+1]}".center(100))
            
            print("\n")
            print("Cost: $5".center(100))
            print("Influence: 8%".center(100))

            print("\n")
            print("Controls: 'w', 's', 'enter', 'backspace'".center(100))

            inp = msvcrt.getch()
            if "w" in str(inp) and stateIndex != 0: stateIndex -= 1
            elif "s" in str(inp) and stateIndex != 48: stateIndex += 1
            elif "r" in str(inp): break
            elif "x08" in str(inp):
                back = True
                break
        if back: campaign()
        else:
            action(f"s-{stateList[stateIndex]}")
            home()


def getInfluence(state: str) -> int:
    pop = STATE_NAMES[state]
    if pop >= 15:
        dist = abs(perc[state] - 50)
        if dist >= 25: return random.randint(8, 13)
        else: return random.randint(10, 25)
    else:
        return random.randint(10, 20)

#x08 is for backspace using msvcrt
def campaign():
    text = ["  ___ __ _ _ __ ___  _ __   __ _ _  __ _ _ __  ",
            " / __/ _` | '_ ` _ \| '_ \ / _` | |/ _` | '_ \ ",
            "| (_| (_| | | | | | | |_) | (_| | | (_| | | | |",
            " \___\__,_|_| |_| |_| .__/ \__,_|_|\__, |_| |_|",
            "____________________| |____________ __/ |______",
            "                    |_|            |___/       "]
    options = ["    _      _             _   _         ",
               "   /_\  __| |_ _____ _ _| |_(_)___ ___ ",
               "  / _ \/ _` \ V / -_) '_|  _| (_-</ -_)",
               " /_/ \_\__,_|\_/\___|_|  \__|_/__/\___|",
               "  ___      _ _                         ",
               " | _ \__ _| | |_  _                    ",
               " |   / _` | | | || |                   ",
               " |_|_\__,_|_|_|\_, |                   ",
               "               |__/                    ",
               "  ___                  _               ",
               " / __|_ __  ___ ___ __| |_             ",
               " \__ \ '_ \/ -_) -_) _| ' \            ",
               " |___/ .__/\___\___\__|_||_|           ",
               "     |_|                               "]

    
    selection = 0
    goHome = False

    while True:
        os.system("cls")
        for line in text: print(line.center(100))
        printCampaignSelection(selection, options)
        
        inp = msvcrt.getch()
        if "w" in str(inp) and selection != 0 : selection -=1
        elif "s" in str(inp) and selection != 2: selection += 1
        elif "r" in str(inp): break
        elif "x08" in str(inp):
            goHome = True
            break
    
    if goHome: home()
    else: section2(selection)



    '''
    stateIndex = 0
    while True:
        os.system("cls")
        for line in text: print(line)
        print("\n", "Choose what type of campaign to do:".center(47))
        print("")
        if stateIndex == 0:
            print("...".center(47))
            print(f"{stateList[stateIndex]}".center(47))
            print(f"{stateList[stateIndex+1]}".center(47))
        elif stateIndex == 48:
            print(f"{stateList[stateIndex-1]}".center(47))
            print(f"{stateList[stateIndex]}".center(47))
            print("...".center(47))
        else:
            print(f"{stateList[stateIndex-1]}".center(47))
            print(f"{stateList[stateIndex]}".center(47))
            print(f"{stateList[stateIndex+1]}".center(47))
        print(len(stateList), stateIndex)
        inp = msvcrt.getch()
        if "w" in str(inp) and stateIndex != 0: stateIndex -= 1
        elif "s" in str(inp) and stateIndex != 48: stateIndex += 1
        elif "r" in str(inp): break
    '''
    

    input()
    home()

def money():
    global gameStats
    # total money, fundrasing, sponsors, recently spent, recent income
    moneyText = [" _ __ ___   ___  _ __   ___ _   _ ",
            "| '_ ` _ \ / _ \| '_ \ / _ \ | | |",
            "| | | | | | (_) | | | |  __/ |_| |",
            "|_| |_| |_|\___/|_| |_|\___|\__, |",
            "-------------------------------------__/ |--------",
            "                            |___/ "]
    info = [["  _____    _        _   __  __                   _ ", 
             " |_   _|__| |_ __ _| | |  \/  |___ _ _  ___ _  _(_)", 
             "   | |/ _ \  _/ _` | | | |\/| / _ \ ' \/ -_) || |_ ",
             "   |_|\___/\__\__,_|_| |_|  |_\___/_||_\___|\_, (_)",
             "                                 |__/   "],
            ["  ___               _   _ ",
             " / __|_ __  ___ _ _| |_(_)",
             " \__ \ '_ \/ -_) ' \  _|_ ",
             " |___/ .__/\___|_||_\__(_)",
             "     |_|                  "],
            ["  ___                       _ ",
             " |_ _|_ _  __ ___ _ __  ___(_)",
             "  | || ' \/ _/ _ \ '  \/ -_)_ ",
             " |___|_||_\__\___/_|_|_\___(_)"]]
    options = [["  ___             _          _    _           ",
               " | __|  _ _ _  __| |_ _ __ _(_)__(_)_ _  __ _ ",
               " | _| || | ' \/ _` | '_/ _` | (_-< | ' \/ _` |",
               " |_| \_,_|_||_\__,_|_| \__,_|_/__/_|_||_\__, |",
               "                                        |___/ "],
               ["  ___                               ",
               " / __|_ __  ___ _ _  ___ ___ _ _ ___",
               " \__ \ '_ \/ _ \ ' \(_-</ _ \ '_(_-<",
               " |___/ .__/\___/_||_/__/\___/_| /__/",
               "     |_|                            "]]
    
    
    selection = True
    back = False
    while True:
        os.system("cls")
        print("")
        for line in moneyText: print(f"{line}".center(100))
        
        #print the total money
        print("\n")
        for i in range(5):
            totalMoney = str(gameStats["money"])
            try:
                numberLine = f"{numbers[0][i]    }"
                for j in range(len(totalMoney)):
                    if totalMoney[j] == "0" : numberLine += numbers[10][i]
                    else: numberLine += numbers[int(totalMoney[j])][i]
            except: numberLine = ""
            print(f"{info[0][i]}  {numberLine}".center(100))

        #print the spent and income on the same line
        print("")
        for i in range(0):     #### THIS LINE MAKES IT SO SPENT/INCOME ISN'T DISPLAYER
                               #### THIS IS BECAUSE IT IS MAKING EACH LINE > 100 WHEN YOU DO FUNDRASISING
                               #### ORIGINALLY SET AT range(5):
            line = ""
            line += info[1][i]
            spent = str(gameStats["recentlySpent"])
            try:
                line += f"  {numbers[0][i]}"
                totalLength = 0
                for j in range(len(spent)):
                    if spent[j] == "0": addition = numbers[10][i]
                    else: addition = numbers[int(spent[j])[i]]
                    line += addition
                    totalLength += len(addition)
                line += " "*(8-totalLength)
            except:
                line += " "*8
            
            try: line += info[2][i]
            except: pass
            income = str(gameStats["recentIncome"])
            try:
                line += f"  {numbers[0][i]}"
                for j in range(len(income)):
                    if income[j] == "0": line += numbers[10][i]
                    else: line += numbers[int(income[j])[i]]
            except:
                line += " "*47
            #if len(line) > 100: line = line[:100].center(100) #### fix this crap, it is cutting off numbers in the money page and I dont know why
            print(line.center(100))
            print(len(line))

        print("\n")
        for i in range(5):
            if selection and i == 4: print(f"{options[0][i].replace(' ', '-')}{' '*10}{options[1][i]}".center(100))
            elif not(selection) and i == 4: print(f"{options[0][i]}{' '*10}{options[1][i].replace(' ', '-')}".center(100))
            else: print(f"{options[0][i]}{' '*10}{options[1][i]}".center(100))
        
        print("\n")
        print("Controls: 'a', 'd', 'enter', 'backspace'".center(100))

        inp = msvcrt.getch()
        if "d" in str(inp): selection = False
        elif "a" in str(inp): selection = True
        elif "r" in str(inp): break
        elif "x08" in str(inp): 
            back = True
            break
    
    if back: home()
    else: money2(selection)
    
def money2(selection: bool):
    text = [["  ___             _          _    _           ",
            " | __|  _ _ _  __| |_ _ __ _(_)__(_)_ _  __ _ ",
            " | _| || | ' \/ _` | '_/ _` | (_-< | ' \/ _` |",
            " |_| \_,_|_||_\__,_|_| \__,_|_/__/_|_||_\__, |",
            " ---------------------------------------|___/ "],
           ["  ___                               ",
            " / __|_ __  ___ _ _  ___ ___ _ _ ___",
            " \__ \ '_ \/ _ \ ' \(_-</ _ \ '_(_-<",
            " |___/ .__/\___/_||_/__/\___/_| /__/",
            " ----|_|----------------------------"]]

    if selection: #fundraising
        stateIndex = 0
        stateList = []
        for item in STATE_NAMES: stateList.append(item)
        stateList.sort()
        back = False

        moneyTable = [[2, 4, 6], #pop < 10: 50-70%->2, 71-85%->4, 86-100%->6
                      [3, 6, 9], #pop 11-25: 50-70%-> 3, 71-85%->6, 86-100%->9
                      [4, 8, 12]] #pop > 25: 50-70%->4, 71-85%->8. 86-100%->12

        while True:
            os.system("cls")
            for i in range(5): print(f"{text[0][i]}".center(100))
            print("\n")
            print("Fundrasing lets you earn donations from supporters".center(100))
            print("The amount of money you recieve depends on the state and how much they supoport you".center(100))
            print("\n")
            print("If you are not the majority party in a state then you may get little or no funds".center(100))
            print("If a state is in favor of you, you will recieve more money for a higher population".center(100))
            print("However, the more populated the state, the more it will cost to fundraise in it".center(100))
            print("\n")
            print("Select a state to fundraise in:".center(100))
            print("\n")
            
            if stateIndex == 0:
                print("...".center(100))
                print(f"{stateList[stateIndex]}".center(100))
                print(f"{stateList[stateIndex+1]}".center(100))
            elif stateIndex == 48:
                print(f"{stateList[stateIndex-1]}".center(100))
                print(f"{stateList[stateIndex]}".center(100))
                print("...".center(100))
            else:
                print(f"{stateList[stateIndex-1]}".center(100))
                print(f"{stateList[stateIndex]}".center(100))
                print(f"{stateList[stateIndex+1]}".center(100))
            
            if perc[stateList[stateIndex]] < 50: profit = random.randint(0,2)
            else:
                pop = STATE_NAMES[stateList[stateIndex]]
                statePerc = perc[stateList[stateIndex]]
                if pop < 10:
                    if statePerc >=50 and statePerc <= 70: profit = moneyTable[0][0]
                    elif statePerc > 70 and statePerc <= 85: profit = moneyTable[0][1]
                    elif statePerc > 85: profit = moneyTable[0][2]
                elif pop >= 10 and pop < 25:
                    if statePerc >=50 and statePerc <= 70: profit = moneyTable[1][0]
                    elif statePerc > 70 and statePerc <= 85: profit = moneyTable[1][1]
                    elif statePerc > 85: profit = moneyTable[1][2]
                elif pop >= 25:
                    if statePerc >=50 and statePerc <= 70: profit = moneyTable[2][0]
                    elif statePerc > 70 and statePerc <= 85: profit = moneyTable[2][1]
                    elif statePerc > 85: profit = moneyTable[2][2]

            print("\n")
            print(f"Net Profit: {profit}".center(100))

            print("\n")
            print("controls: 'w', 's', 'enter', 'backspace'".center(100))

            inp = msvcrt.getch()
            if "w" in str(inp) and stateIndex != 0: stateIndex -= 1
            elif "s" in str(inp) and stateIndex != 48: stateIndex += 1
            elif "r" in str(inp): break
            elif "x08" in str(inp):
                back = True
                break
        if back: money()
        else: 
            action(f"f-{profit}")
            home()

    else: #Sponsor
        os.system("cls")
        global gameStats
        for line in text[1]: print(line.center(100))
        print("\n")
        print("Sponsors give you money to help support your campaigns".center(100))
        print("These sponsors are not gaurenteed to be given to you".center(100))
        print("There is a 20% chance of you receiving a sponsorship".center(100))
        print("\n")
        print("You can only apply for a sponsorship once every three turns".center(100))
        print("(Every 3 campaigns)".center(100))
        print("\n\n")

        if gameStats["sponsorCooldown"] != 0:
            print("|-----------------------------------------------|".center(100))
            print(f"|  You have {gameStats['sponsorCooldown']} turns until you can apply again  |".center(100))
            print("|-----------------------------------------------|".center(100))

            print("\n\n\n\n")
            print("Controls: 'enter', 'backspace'".center(100))
        
            while True:
                inp = msvcrt.getch()
                if "r" in str(inp) or "x08" in str(inp): break 
        else:
            print("|-------------------------|".center(100))
            print("|  Apply for Sponsorship  |".center(100))
            print("|-------------------------|".center(100))

            print("\n\n\n\n")
            print("Controls: 'enter', 'backspace'".center(100))
        
            apply = False
            while True:
                inp = msvcrt.getch()
                if "r" in str(inp):
                    apply = True
                    break
                elif "x08" in str(inp): break
            
            if apply:
                if random.randint(1,5) == 5:
                    giveSponsor()
                else:
                    noSponsor()
        
    home()

#### TEST THE SPONSORSHIP TAB


def giveSponsor():
    global gameStats
    sponsor = random.randint(15,23)
    os.system("cls")
    print("\n\n\n\n\n\n\n\n")
    print("You receieved a sponsorship of:".center(100))
    print(f"${sponsor}".center(100))
    print("\n\n\n\n\n\n")
    print("Press 'enter' to continue".center(100))
    gameStats["money"] += sponsor
    gameStats["recentIncome"] += sponsor
    gameStats["sponsorCooldown"] = 3
    while True:
        if "r" in str(msvcrt.getch()): break


def noSponsor():
    global gameStats
    os.system("cls")
    print("\n\n\n\n\n\n\n\n")
    print("You did not receieved a sponsorship".center(100))
    print("\n\n\n\n\n\n")
    print("Press 'enter' to continue".center(100))
    gameStats["sponsorCooldown"] = 1
    while True:
        if "r" in str(msvcrt.getch()): break

def runPage(selection):
    if selection == 0: campaign()
    elif selection == 1: states()
    elif selection == 2: money()
    elif selection == 3: history()

def home():
    # home page will show general stats like net money, recent income, recent spending, total % of your party, sponsors, current round
    # there will be several sub pages: money, campaign, states, event history
    buttons = ["                                 _             ",
               "                                (_)            ",
               "  ___ __ _ _ __ ___  _ __   __ _ _  __ _ _ __  ",
               " / __/ _` | '_ ` _ \| '_ \ / _` | |/ _` | '_ \ ",
               "| (_| (_| | | | | | | |_) | (_| | | (_| | | | |",
               " \___\__,_|_| |_| |_| .__/ \__,_|_|\__, |_| |_|",
               "     _        _     | |             __/ |      ",
               "    | |      | |    |_|            |___/       ",
               " ___| |_ __ _| |_ ___  ___                     ",
               "/ __| __/ _` | __/ _ \/ __|                    ",
               "\__ \ || (_| | ||  __/\__ \                    ",
               "|___/\__\__,_|\__\___||___/                    ",
               " _ __ ___   ___  _ __   ___ _   _              ",
               "| '_ ` _ \ / _ \| '_ \ / _ \ | | |             ",
               "| | | | | | (_) | | | |  __/ |_| |             ",
               "|_| |_| |_|\___/|_| |_|\___|\__, |             ",
               " _     _     _               __/ |             ",
               "| |   (_)   | |             |___/              ",
               "| |__  _ ___| |_ ___  _ __ _   _               ",
               "| '_ \| / __| __/ _ \| '__| | | |              ",
               "| | | | \__ \ || (_) | |  | |_| |              ",
               "|_| |_|_|___/\__\___/|_|   \__, |              ",
               "                            __/ |              ",
               "                           |___/               "]
    selection = 0

    while True:
        os.system("cls")
        printButtonText(buttons, selection)
        
        inp = msvcrt.getch()
        if "s" in str(inp) and selection != 3: selection += 1
        elif "w" in str(inp) and selection != 0: selection -= 1
        elif "r" in str(inp): break#runPage(selection)
        try: os.system(f"color {int(inp.decode('utf-8'))}")
        except: pass
    
    runPage(selection)

def makePercentages(perc=dict):
    for item in STATE_NAMES:
        perc[item] = random.randint(1, 100)#normalize(STATE_NAMES[item])

def config():
    os.system("cls")
    os.system("mode 100, 30")

if __name__ == "__main__":
    #'''
    intro()
    party = selectParty() #1 = democrat, 2 = republican
    gameStats = {"ads":[0,0], 
                 "money":15,
                 "round":0,
                 "recentlySpent":0,
                 "recentIncome":0,
                 "sponsorCooldown":0}
    gameHistory = []

    perc = {}
    makePercentages(perc)
    
    tutorial(ifTutorial())
    
    #config()
    try: home()
    except Exception as e: print(e)
    #'''
    #config()
    #campaign()
    #print(perc)
    #endGame()

    input()