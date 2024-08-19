import json
import os
import time
import urllib.request, json 
from prettytable import PrettyTable

myapi = "api_key"

def callpuuids(name, tag):
    import urllib.request, json
    with urllib.request.urlopen("https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/"+ str(name)+ "/"+ str(tag)+ "?api_key="+ myapi) as url:
        data = json.load(url)
        puuid = str(data.get("puuid"))
    with urllib.request.urlopen("https://tr1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+ str(puuid) +"?api_key="+ myapi) as url:
        data = json.load(url)
        
        sID = str(data.get("id"))
        aID = str(data.get("accountId"))
        puuid = str(data.get("puuid"))
        return sID, aID, puuid
        
def doeverything(puuID, s, a):

    with urllib.request.urlopen("https://ddragon.leagueoflegends.com/api/versions.json") as url:
        versions = json.load(url)
        currentver = versions[0]
    with urllib.request.urlopen("https://ddragon.leagueoflegends.com/cdn/"+ currentver +"/data/en_US/champion.json") as url2:
        championsjson = json.load(url2)
    charnum = str(len(championsjson["data"]))

    def getchamp(champid):
        for key, value in championsjson["data"].items():
            if value['key'] == str(champid):
                return value['name']


    def extract_champion_ids():
        with urllib.request.urlopen("https://tr1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/"+ puuID +"/top?count="+charnum+"?api_key="+ myapi) as url:
            data = json.load(url)
        requireds = []
        champion_ids = []
        timea = []
        for entry in data:
            if entry.get('nextSeasonMilestone', {}).get('rewardConfig', {}).get('rewardType') == "HEXTECH_CHEST":
                champion_ids.append(entry['championId'])
                requireds.append(entry['nextSeasonMilestone']['requireGradeCounts'])
                timea.append(entry['lastPlayTime'])
        return champion_ids, requireds, timea

    champids = extract_champion_ids()[0]
    requiredd = extract_champion_ids()[1]
    timee = extract_champion_ids()[2]
    os.system("cls")
    print("Champ IDs: ")

    print(champids)
    print(requiredd)

    print("")
    print("cikti sayisi:"+ str(len(champids)))
    print("")
    x = 0

    chmp = []
    while x <= int(len(champids))-1:
        champid=int(champids[x])
    
    
        championis = getchamp(champid)
        x=x+1
        chmp.append(championis)
    """
    SAMPIYON ADLARI CHAMPIONIS ILE CAGIRILIR
    """
    print(chmp)



    utctime = []
    x = 0
    while x <= int(len(timee))-1:
    
        timex=int(timee[x])
        timex=timex/1000
        ut = time.strftime("%Y/%m/%d %H:%M", time.localtime(int(timex)))
        utctime.append(ut)
        x=x+1


    table = PrettyTable(["Champion Code", "Champion Name", "   Requirements   ", "Last Played Time"])
    for champc, champn, req, tm in zip(champids, chmp ,  requiredd, utctime):
        table.add_row([champc, champn, req, tm])


    table.sortby = "Last Played Time"
    print(chmp)
    print(utctime)
    print(requiredd)
    
    


    print(table) 
    return table
    print("------------------------")
    print("|         DEBUG        |")
    print("------------------------")
    # print(len(requireds))
    # print(chmp)
    # print(utctime)
    print("")



    print("SUMMONER ", s)
    print("ACCOUNT ", a)
    print("PUUID ", puuID)