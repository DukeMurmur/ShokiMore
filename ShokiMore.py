#Imports and global values cell

import requests
import json
import bs4
import os
import platform
import shlex
import struct
from pathlib import Path
from time import localtime as time
from time import sleep
from math import floor

global users_list
global sort
global alphabet
global info_logo
global main_logo

main_logo = ' |\\___/|                                                    \n )     (           _=,_                                     \n=\\     /=       o_/6 /#\\                                    \n  )===(         \\__ |##/                                    \n /     \\         =\'|--\\                                     \n |     |           /   #\'-.                                 \n/       \\          \\#|_   _\'-. /                            \n\\       /           |/ \\_( # |"                             \n \\__  _/           C/ ,--___/                               \n   ( (                                                      \n    ) )                     Developed by:                   \n    (_(                           Duke Murmur & Count Furfur'

alphabet = ['А','а','Б','б','В','в','Г','г','Д','д','Е','е','Ё','ё','Ж','ж','З','з','И','и','Й','й','К','к','Л','л',
            'М','м','Н','н','О','о','П','п','Р','р','С','с','Т','т','У','у','Ф','ф','Х','х','Ц','ц','Ч','ч','Ш','ш',
            'Щ','щ','Ъ','ъ','Ы','ы','Ь','ь','Э','э','Ю','ю','Я','я',' ', ':', '%', '?', '!', '@', '#', ';', '%', '*',
            '(', ')', '.', ',', '—', '-']

sort = 0

info_logo = ['  ___ _  _ ___ ___  ',
             ' |_ _| \\| | __/ _ \\ ',
             '  | || .` | _| (_) |',
             ' |___|_|\\_|_| \\___/ ']

#Anime Class cell

class Anime():
    def __init__(self, idt : str, name : str, russian : str, url : str, description : str, kind : str, score : float, 
                 status : str, episodes : int, episodes_aired : int, aired_on : str, released_on : str,
                 rating : str, duration : int, anons : bool, ongoing : bool, myanimelist_id : str, rates_scores_stats : list,
                 rates_statuses_stats : list, next_episode_at : str, user_status : str, user_episodes : int):
        self.idt = idt
        self.name = name
        self.russian = russian
        self.url = url
        self.description = description
        self.kind = kind
        self.score = score
        self.status = status
        self.episodes = episodes
        self.episodes_aired = episodes_aired
        self.aired_on = aired_on
        self.released_on = released_on
        self.rating = rating
        self.duration = duration
        self.anons = anons
        self.ongoing = ongoing
        self.myanimelist_id = myanimelist_id
        self.rates_scores_stats = rates_scores_stats
        self.rates_statuses_stats = rates_statuses_stats
        self.next_episode_at = next_episode_at
        self.user_status = user_status
        self.user_episodes = user_episodes
        
    def filt(self):
        new_string = ''
        for letter in self.description:
            if letter in alphabet:
                new_string += letter
        self.description = new_string

def variables():
    global f0 
    global f1
    global f2
    global f3
    global f4
    global f5
    global f6
    global f7
    global f8
    global f9
    global dot

    f0 = '  ___   \n / _ \\  \n| | | | \n| | | | \n| |_| | \n \\___/  '
    f1 = ' __  \n/_ | \n | | \n | | \n | | \n |_| '
    f2 = ' ___   \n|__ \\  \n   ) | \n  / /  \n / /_  \n|____| '
    f3 = ' ____   \n|___ \\  \n  __) | \n |__ <  \n ___) | \n|____/  '
    f4 = ' _  _    \n| || |   \n| || |_  \n|__   _| \n   | |   \n   |_|   '
    f5 = ' _____  \n| ____| \n| |__   \n|___ \\  \n ___) | \n|____/  '
    f6 = "   __   \n  / /   \n / /_   \n| '_ \\  \n| (_) | \n \\___/  "
    f7 = ' ______  \n|____  | \n    / /  \n   / /   \n  / /    \n /_/     '
    f8 = '  ___   \n / _ \\  \n| (_) | \n > _ <  \n| (_) | \n \\___/  '
    f9 = '  ___   \n / _ \\  \n| (_) | \n \\__, | \n   / /  \n  /_/   '
    dot = '   \n   \n   \n   \n _ \n(_)'

#Progress bar function

def printProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):

    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    if iteration == total: 
        print('\r%s |%s| %s%% %s' % (prefix, bar, ("{0:." + str(decimals) + "f}").format(100 * (total / float(total))), suffix), end = printEnd)

#Get user data from internet

def get_user_data(nick):
    def get_data(user_id : str):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}
        url = 'https://shikimori.one/' + user_id + '/list_export/animes.json'
        data = requests.get(url, headers = headers, allow_redirects = True)
        return json.loads(data.content.decode())

    def get_id(nick):
        raw_data = get_data(nick)
        id_list = []
        for item in raw_data:
            id_list.append(item['target_id'])
        return id_list, raw_data

    def return_api(nick):
        ids, raw_data = get_id(nick)
        api_data = []
        count = 0
        for item in ids:
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}
            url = 'https://shikimori.one/api/animes/' + str(item)
            data = requests.get(url, headers = headers, allow_redirects = True)
            printProgressBar(count, len(ids), prefix = 'Processing: ', suffix = 'Complete', decimals = 1, length = (size()[0] - 33), fill = '█', printEnd = "\r")
            while len(data.content.decode()) <= 20:
                data = requests.get(url, headers = headers, allow_redirects = True)
            api_data.append(json.loads(data.content.decode()))
            count += 1
        printProgressBar(len(ids), len(ids), prefix = 'Processing: ', suffix = 'Complete', decimals = 1, length = (size()[0] - 33), fill = '█', printEnd = "\r")
        return api_data, raw_data

    def final(nick):
        data = []
        api_data, raw_data = return_api(nick)
        for item in api_data:
            dct = {}
            dct['idt'] = item['id']
            dct['name'] = item['name']
            dct['russian'] = item['russian']
            dct['url'] = item['url']
            dct['description'] = item['description']
            dct['kind'] = item['kind']
            dct['score'] = item['score']
            dct['status'] = item['status']
            dct['episodes'] = item['episodes']
            dct['episodes_aired'] = item['episodes_aired']
            dct['aired_on'] = item['aired_on']
            dct['released_on'] = item['released_on']
            dct['rating'] = item['rating']
            dct['duration'] = item['duration']
            dct['anons'] = item['anons']
            dct['ongoing'] = item['ongoing']
            dct['myanimelist_id'] = item['myanimelist_id']
            dct['rates_scores_stats'] = item['rates_scores_stats']
            dct['rates_statuses_stats'] = item['rates_statuses_stats']
            dct['next_episode_at'] = item['next_episode_at']
            for item_2 in raw_data:
                if item['id'] == item_2['target_id']:
                    dct['user_status'] = item_2['status']
                    dct['user_episodes'] = item_2['episodes']
            data.append(dct)
        return data

    def transfer(nick):
        data = final(nick)
        data_list = []
        for item in data:
            data_list.append(Anime(item['idt'], item['name'], item['russian'], item['url'], item['description'], 
                                   item['kind'], item['score'], item['status'], item['episodes'], 
                                   item['episodes_aired'], item['aired_on'], item['released_on'],
                                   item['rating'], item['duration'], item['anons'], item['ongoing'], item['myanimelist_id'], 
                                   item['rates_scores_stats'], item['rates_statuses_stats'], item['next_episode_at'], 
                                   item['user_status'], item['user_episodes']))
        return data_list

    final_list = transfer(nick)
    for item in final_list:
        try:
            item.filt()
        except:
            None
    return final_list

# Time class to save files

class Custom_time():
    def __init__(self, year, month, day, hour, minute, sec, wday):
        self.year = year
        if len(str(month)) == 1:
            self.month = '0' + str(month)
        else:
            self.month = month
        if len(str(day)) == 1:
            self.day = '0' + str(day)
        else:
            self.day = day
        if len(str(hour)) == 1:
            self.hour = '0' + str(hour)
        else:
            self.hour = hour
        if len(str(minute)) == 1:
            self.minute = '0' + str(minute)
        else:
            self.minute = minute
        if len(str(sec)) == 1:
            self.sec = '0' + str(sec)
        else:
            self.sec = sec
        self.wday = weekdays(wday)

def weekdays(wday):
    if wday == 6:
        return 'Sunday'
    elif wday == 0:
        return 'Monday'
    elif wday == 1:
        return 'Tuesday'
    elif wday == 2:
        return  'Wednesday'
    elif wday == 3:
        return  'Thursday'
    elif wday == 4:
        return  'Friday'
    elif wday == 5:
        return  'Saturday'

def create_time():
    current_time = time()
    current_time = Custom_time(current_time.tm_year, current_time.tm_mon, current_time.tm_mday, current_time.tm_hour,
                               current_time.tm_min, current_time.tm_sec, current_time.tm_wday)
    string = 'Created at: ' + str(current_time.hour) + ':' + str(current_time.minute) + ':' + str(current_time.sec)
    string += ', ' + str(current_time.day) + '/' + str(current_time.month) + '/' + str(current_time.year)
    string += ', ' + current_time.wday
    return string

# Save data to file

def save(data):
    path = str(os.getcwd())
    path += '\\ShokiMore_Data'
    try:
        os.mkdir(path)
    except:
        None
    c = 0
    td = {}
    nd = {}
    print('\nList of users: \n')
    for key in data:
        print(str(c + 1) + '. ' + key)
        td[str(c + 1)] = key
        c += 1
    print(str(c + 1) + '. All items' )
    inp = input('\nEnter numbers of users which data should be saved separated by spaces: ')
    print('')
    if inp == '':
        return 0
    if inp == str(c + 1):
        nd = data
    else:
        inp = inp.split(' ')
        for item in inp:
            try:
                nd[td[item]] = data[td[item]]
            except:
                print('Type error!')
                return 0
    for key in nd:
        first_dict = []
        first_dict.append(create_time())
        for item in data[key]:
            second_dict = {}
            second_dict['idt'] = item.idt
            second_dict['name'] = item.name
            second_dict['russian'] = item.russian
            second_dict['url'] = item.url
            second_dict['description'] = item.description
            second_dict['kind'] = item.kind
            second_dict['score'] = item.score
            second_dict['status'] = item.status
            second_dict['episodes'] = item.episodes
            second_dict['episodes_aired'] = item.episodes_aired
            second_dict['aired_on'] = item.aired_on
            second_dict['released_on'] = item.released_on
            second_dict['rating'] = item.rating
            second_dict['duration'] = item.duration
            second_dict['anons'] = item.anons
            second_dict['ongoing'] = item.ongoing
            second_dict['myanimelist_id'] = item.myanimelist_id
            second_dict['rates_scores_stats'] = item.rates_scores_stats
            second_dict['rates_statuses_stats'] = item.rates_statuses_stats
            second_dict['next_episode_at'] = item.next_episode_at
            second_dict['user_status'] = item.user_status
            second_dict['user_episodes'] = item.user_episodes
            first_dict.append(second_dict)
        check = 0
        count = 0
        if 'Created at: ' in key:
            for i in range(len(key)):
                if key[i : i + 12] == 'Created at: ':
                    new = key[0 : i - 2]
                    break
            tmp = new
            key = new
        else:
            tmp = key
        while check != 1:
            count += 1
            tmp = key + '_' + str(count)
            temp_path = path + '\\' + tmp + '.json'
            try:
                file = open(temp_path, 'r')
                tmp = key + '_' + str(count)
            except:
                file = open(temp_path, 'w')
                check = 1
        file.write(json.dumps(first_dict))
        file.close()
        print(key + ' data was saved successfully!')
    return 0

# Load data from file

def supreme_load():
    path = str(os.getcwd())
    path += '\\ShokiMore_Data'
    current_working_direction = path
    rootdir = Path(current_working_direction)
    file_list = [f for f in rootdir.glob('**/*') if f.is_file()]
    temp_dict = {}
    temp_dict_sup = {}
    temp_list = []
    count = 0
    for item in file_list:
        file = open(item, 'rb')
        data = json.load(file)
        file.close
        tm = data[0]
        temp_dict[item] = tm
    for key in temp_dict:
        temp_list_2 = str(key).split('\\')
        temp_list.append(temp_list_2[len(temp_list_2) - 1])
    temp_list_simple = [item[0:len(item) - 7] for item in temp_list]
    count = 0
    for key in temp_dict:
        temp_dict_sup[temp_list_simple[count] + '  ' + temp_dict[key]] = key
        count += 1
    count = 0
    choice_dict = {}
    for key in temp_dict_sup:
        print((str(count + 1)) + '. ' + key)
        choice_dict[str(count + 1)] = key
        count += 1
    inp = input('\nEnter a numbers of users which data should be loaded separated by a space: ')
    print('')
    if inp == '':
        return 0
    inp = inp.split(' ')
    load_dict = {}
    for letter in inp:
        try:
            load_dict[choice_dict[letter]] = temp_dict_sup[choice_dict[letter]]
        except:
            print('Type error!')
    final_dict = {}
    for key in load_dict:
        final_dict[key] = load(load_dict[key])
        print('Data for user ' + key + ' has been loaded!')
    return final_dict

def load(path):
    file = open(path, 'rb')
    data = json.load(file)
    file.close
    ret_d = {}
    tm = data[0]
    del data[0]
    data_list = []
    for item in data:
        data_list.append(Anime(item['idt'], item['name'], item['russian'], item['url'], item['description'], 
                               item['kind'], item['score'], item['status'], item['episodes'], 
                               item['episodes_aired'], item['aired_on'], item['released_on'],
                               item['rating'], item['duration'], item['anons'], item['ongoing'], item['myanimelist_id'], 
                               item['rates_scores_stats'], item['rates_statuses_stats'], item['next_episode_at'], 
                               item['user_status'], item['user_episodes']))
    for item in data_list:
        try:
            item.filt()
        except:
            None
    return data_list

#Main body cell

def generate_users():
    global users_list
    users_list = {}
    inp_1 = input('Enter a number of users: ')
    try:
        inp_1 = int(inp_1)
    except:
        print('Type Error!')
        return 0
    nick_list = []
    for i in range(inp_1):
        print('Enter ' + str(i + 1) + ' nickname: ', end = '')
        nick_list.append(input())
    for i in range(inp_1):
        users_list[nick_list[i]] = get_user_data(nick_list[i])
    print('\nDone!')

def create_custom_lists():
    temp_dict = {}
    count = 0
    print('\nExisting users: \n')
    for key in users_list:
        print(str(count + 1) + '. ' + key)
        temp_dict[str(count + 1)] = key
        count += 1
    inp = input('Choose users that should be compared separated by spaces: ')
    if inp == '':
        return 0
    temp_dict_2 = {}
    inp = inp.split(' ')
    for letter in inp:
        try:
            temp_dict_2[temp_dict[letter]] = users_list[temp_dict[letter]]
        except:
            print('Type error!')
            return 0
    return temp_dict_2

def compare():
    item_list_merge = []
    ban_list = []
    global_dict = create_custom_lists()
    
    if global_dict == 0:
        return 0
    
    if len(global_dict) < 2:
        print('Not enough users to compare!')
        return 0
    
    else:
        all_merged = [item for key in global_dict for item in global_dict[key]]
        id_list = [item.idt for item in all_merged]
        id_list_merge = [item for item in id_list if id_list.count(item) == len(global_dict)]
        for item in all_merged:
            if item.idt in id_list_merge:
                if item.idt not in ban_list:
                    item_list_merge.append(item)
                    ban_list.append(item.idt)
        return item_list_merge, 'List of animes that appear in all lists: '
    
def print_sort(data : tuple):
    if data == 0:
        return 0
    text = data[1]
    data = data[0]
    if sort == 0:
        working_dict = create_working_dict(data)
        print('\n' + text + '\n')
        for key in working_dict:
            print(str(key) + '. ' + working_dict[key].russian)
        info(working_dict)

def info(working_dict):
    inp = input('\nEnter a anime number to see more detatils, or 0 to see the list again or enter to exit: ')
    while inp != '':
        if inp == '0':
            count = 0
            anime_list = list(working_dict.values())
            print('')
            for item in anime_list:
                print(str(count + 1) + '. ' + item.russian)
                count += 1
        else:
            try:
                current_anime = working_dict[int(inp)]
                sub_info(current_anime)
            except:
                print('\nType error!\n')
        
        inp = input('\nEnter a anime number to see more detatils, or 0 to see the list again or enter to exit: ')
        
def create_working_dict(data : list):
    count = 0
    working_dict = {}
    for item in data:
        working_dict[count + 1] = item
        count += 1
    return working_dict

def different():
    item_list_unmerge = []
    ban_list = []
    users_dict = {}
    global_dict = create_custom_lists()
    
    if global_dict == 0:
        return 0
    
    if len(global_dict) < 2:
        print('Not enough users to compare!')
        return 0
    
    else:
        all_merged = [item for key in global_dict for item in global_dict[key]]
        id_list = [item.idt for item in all_merged]
        count = 1
        print('\nPick a user, from which point of view all other lists will be compared')
        print('Choose a last avaliable option to make module work as an inverse of compare module\n')
        for key in global_dict:
            users_dict[str(count)] = key
            print(str(count) + '. ' + key)
            count += 1
        print(str(count) + '. Compare inverse')
        inp = input('Enter a number: ')
        if inp == str(count):
            primary_user = 'All'
        else:
            try:
                primary_user = users_dict[inp]
            except:
                print('Type error!')
                return 0
        try:
            primary_user_dict = global_dict[primary_user]
            primary_user_id_list = [item.idt for item in primary_user_dict]
        except:
            primary_user_id_list = {}
        id_list_unmerge = [item for item in id_list if id_list.count(item) < len(global_dict)]
        for item in all_merged:
            if item.idt in id_list_unmerge:
                if item.idt not in ban_list:
                    if item.idt not in primary_user_id_list:
                        item_list_unmerge.append(item)
                        ban_list.append(item.idt)
        return item_list_unmerge, 'List of animes that differ from primary list'

def sub_info(current_anime):
    print('\n')
    for item in info_logo:
        tsize = size()[0]
        tsize = floor(tsize) / 2 - len(item) / 2
        print(' ' * int(tsize) + item)
    print('')
    zero_module(current_anime)
    print('\n')
    try:
        first_module(current_anime.description, current_anime.rates_scores_stats)
    except:
        print('\nUnable to display additional information')
        
def create_bars(figures):
    render_list = []
    render_list.append('               Shikimori rating')
    render_list.append('')
    dict_converted = {}
    dict_frames = {}
    for item in figures:
        dict_converted[item['name']] = item['value']
    step = max(list(dict_converted.values()))/40
    frames = [0 + step * i for i in range(41)]
    for key in dict_converted:
        for i in range(40):
            if frames[i] <= dict_converted[key] <= frames[i + 1]:
                dict_frames[key] = i + 1
    fill = '█'
    for key in dict_converted:
        render_list.append(str(key) + ' ' * (2 - len(str(key))) + ' : ' + fill * dict_frames[key] + ' (' + str(dict_converted[key]) + ')')
    return render_list

def pad_text(text, pad):
    string = ''
    lst = []
    lst.append('                    Описание')
    lst.append('')
    error = 0
    for i in range(len(text)):
        if i % pad == 0:
            if i != 0:
                if text[i] == ' ':
                    lst.append(string)
                    string = ''
                    string += text[i]
                    error = 1
                else:
                    if len(text) - i == 1:
                        None
                    if text[i - 1] == ' ':
                        lst.append(string)
                        string = ''
                        string += text[i]
                        error = 1
                    else:
                        string += '-'
                        lst.append(string)
                        string = ''
                        string += text[i]
                        error = 1
        if error == 0:
            string += text[i]
        if error == 1:
            error = 0
    lst.append(string)
    return lst

def first_module(text, figures):
    try:
        text = pad_text(text, 50)
        bar = create_bars(figures)
        len_text = [len(item) for item in text]
        len_bar = [len(item) for item in bar]
        max_text = max(len_text)
        max_bar = max(len_bar)
        gap = size()[0] - (max(len_text) + max(len_bar))
        print_list = []
        while len(text) < len(bar):
            text.append('')
        count = 0
        for item in text:
            lenght = len(item)
            current_gap = max_text - lenght
            current_gap = current_gap + gap
            try:
                string = item + (current_gap - 1) * ' ' + bar[count]
                print(string)
            except:
                string = item
                print(string)
            count += 1
    except:
        for item in create_bars(figures):
            print(item)
        print('\nОписание отсутствует')
        
def zero_module(current_anime):
    left_block = []
    try:
        left_block.append('Title: ' + current_anime.name + ' / ' + current_anime.russian)
    except:
        left_block.append('Title: Unable to display title')
    try:
        left_block.append('Status: ' + current_anime.status)
    except:
        left_block.append('Status: Unable to display status')
    try:
        left_block.append('Type: ' + current_anime.kind)
    except:
        left_block.append('Type: Unable to display type')
    try:
        left_block.append('Total episodes: ' + str(current_anime.episodes))
    except:
        left_block.append('Total episodes: Unable to display episodes')
    try:
        left_block.append('Episodes aired: ' + str(current_anime.episodes_aired))
    except:
        left_block.append('Episodes aired: Unable to display episodes aired')
    try:
        left_block.append('Premiere: ' + current_anime.aired_on)
    except:
        left_block.append('Premiere: Unable to display premiere')
    try:
        left_block.append('Released: ' + current_anime.released_on)
    except:
        left_block.append('Released: Unable to display release date')
    try:
        left_block.append('Duration: ' + str(current_anime.duration) + ' min')
    except:
        left_block.append('Duration: unable to display duration')
    try:
        print_url = current_anime.url
        print_url = print_url.split('-')
        print_url = print_url[0]
        left_block.append('URL link: ' + 'https:shikimori.one' + str(print_url))
    except:
        left_block.append('URL link: Unable to display link')
    try:
        if current_anime.anons == True:
            left_block.append('Anons')
        elif current_anime.ongoing == True:
            left_block.append('Ongoing')
            left_block.append('Next episode at: ' + current_anime.next_episode_at)
        else:
            None
    except:
        None
    try:
        lenght = [len(item) for item in left_block]
        left_max = max(lenght)
        s = size()[0]
        big_f = big_figures(current_anime.score)
        big_l = [len(item) for item in big_f]
        big_max = max(big_l)
        gap = s - left_max - big_max - 14
        while len(left_block) < len(big_f):
            left_block.append('')
        c = 0
        while len(left_block) >= 7:
            print(left_block[c])
            del left_block[c]
            c += 1
        for i in range(6):
            l = len(left_block[i])
            d = left_max - l
            g = d + gap
            if i != 5:
                print(left_block[i] + ' ' * g + big_f[i])
            else:
                print(left_block[i] + ' ' * g + big_f[i] + '   User score')
        count = 0
        for item in left_block:
            if count <= 5:
                None
            else:
                print(item)
            count += 1
    except:
        for item in left_block:
            print(item)

def big_figures(score):
    lst = []
    sup_lst = []
    for figure in score:
        if figure == '0':
            lst.append(f0)
        if figure == '1':
            lst.append(f1)
        if figure == '2':
            lst.append(f2)
        if figure == '3':
            lst.append(f3)
        if figure == '4':
            lst.append(f4)
        if figure == '5':
            lst.append(f5)
        if figure == '6':
            lst.append(f6)
        if figure == '7':
            lst.append(f7)
        if figure == '8':
            lst.append(f8)
        if figure == '9':
            lst.append(f9)
        if figure == '.':
            lst.append(dot)
    sup_lst = [item.split('\n') for item in lst]
    line1 = sup_lst[0][0] + sup_lst[1][0] + sup_lst[2][0] + sup_lst[3][0]
    line2 = sup_lst[0][1] + sup_lst[1][1] + sup_lst[2][1] + sup_lst[3][1]
    line3 = sup_lst[0][2] + sup_lst[1][2] + sup_lst[2][2] + sup_lst[3][2]
    line4 = sup_lst[0][3] + sup_lst[1][3] + sup_lst[2][3] + sup_lst[3][3]
    line5 = sup_lst[0][4] + sup_lst[1][4] + sup_lst[2][4] + sup_lst[3][4]
    line6 = sup_lst[0][5] + sup_lst[1][5] + sup_lst[2][5] + sup_lst[3][5]
    return [line1, line2, line3, line4, line5, line6]

def size():
    def get_terminal_size():
        current_os = platform.system()
        tuple_xy = None

        if current_os == 'Windows':
            tuple_xy = _get_terminal_size_windows()

            if tuple_xy is None:
                tuple_xy = _get_terminal_size_tput()

        if current_os in ['Linux', 'Darwin'] or current_os.startswith('CYGWIN'):
            tuple_xy = _get_terminal_size_linux()

        if tuple_xy is None:
            tuple_xy = (80, 25)
        return tuple_xy


    def _get_terminal_size_windows():

        try:
            from ctypes import windll, create_string_buffer
            h = windll.kernel32.GetStdHandle(-12)
            csbi = create_string_buffer(22)
            res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
            if res:
                (bufx, bufy, curx, cury, wattr,
                 left, top, right, bottom,
                 maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
                sizex = right - left + 1
                sizey = bottom - top + 1
                return sizex, sizey
        except:
            pass


    def _get_terminal_size_tput():

        try:
            cols = int(subprocess.check_call(shlex.split('tput cols')))
            rows = int(subprocess.check_call(shlex.split('tput lines')))
            return (cols, rows)
        except:
            pass


    def _get_terminal_size_linux():

        def ioctl_GWINSZ(fd):
            try:
                import fcntl
                import termios
                cr = struct.unpack('hh',
                                   fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
                return cr

            except:
                pass

        cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)

        if not cr:
            try:
                fd = os.open(os.ctermid(), os.O_RDONLY)
                cr = ioctl_GWINSZ(fd)
                os.close(fd)

            except:
                pass

        if not cr:
            try:
                cr = (os.environ['LINES'], os.environ['COLUMNS'])

            except:
                return None

        return int(cr[1]), int(cr[0])

    def det_size():
        if __name__ == "__main__":
            sizex, sizey = get_terminal_size()

            return [sizex, sizey]
    return det_size()

def print_loop():
    print('\n\n      List of option: \n\n0. Print this menu\n1. Load data from internet\n2. Load data from local file\n3. Save data to local file')
    print('4. Merges search\n5. Basic difference search\nEnter to exit')

def sub_menu():
    global users_list
    print('')
    inp = input('Enter a number: ')
    print('')
    if inp == '1':
        try:
            generate_users()
        except:
            print('Unable to load data. Check the internet connection and correctness of nicknames')
    if inp == '2':
        try:
            users_list = supreme_load()
        except:
            print('Some errors occured, retry later')
    if inp == '3':
        try:
            save(users_list)
        except:
            print('Some errors occured, retry later')
    if inp == '4':
        try:
            print_sort(compare())
        except:
            print('Some errors occured, retry later')
    if inp == '5':
        try:
            print_sort(different())
        except:
            print('Some errors occured, retry later')
    if inp == '0':
        print_loop()
    if inp == '':
        if input('Press ENTER again to exit: ') == '':
            return "exit"

def menu():
    print_loop()
    while sub_menu() != 'exit':
        None

def logo():
    beta = 1
    print(main_logo)
    if beta == 1:
        print('')
        print('')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('!!!                                             !!!')
        print('!!!                                             !!!')
        print('!!!          Это БЕТА ВЕРСИЯ программы          !!!')
        print('!!!        Некоторые модули не работают!        !!!')
        print('!!!                                             !!!')
        print('!!!                                             !!!')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

def exit():
    print('\nExited')
    sleep(2)

def start():
    logo()
    variables()
    menu()
    exit()

start()
