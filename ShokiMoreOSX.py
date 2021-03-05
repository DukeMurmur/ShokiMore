import os
import sys
import time
import math
import random
import json
import pickle
import requests
import binascii
import operator
import textwrap
import zlib
import platform
import shlex
import struct
import tty
import termios

from pathlib import Path
from datetime import datetime
from itertools import chain

from colorama import init

init()

from colorama import Fore, Back, Style

def sinp():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return ch

def on_start_up():

    try:
        os.mkdir('ShokiMore_Data')

    except:
        None

    os.chdir('ShokiMore_Data')

class Terminal():

    class Size():
        def __init__(self, size_list):
            self.x = size_list[0]
            self.y = size_list[1]
            
    def __init__(self):
        self.size = self.Size(self.terminal_size())

    def terminal_size(self):

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

def author_logo(lenght : int):

    author_logo = ' |\\___/|                                                    \n )     (           _=,_                                     \n=\\     /=       o_/6 /#\\                                    \n  )===(         \\__ |##/                                    \n /     \\         =\'|--\\                                     \n |     |           /   #\'-.                                 \n/       \\          \\#|_   _\'-. /                            \n\\       /           |/ \\_( # |"                             \n \\__  _/           C/ ,--___/                               \n   ( (                                                      \n    ) )                     Developed by:                   \n    (_(                           Duke Murmur & Count Furfur'
    
    pattern = ['|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|',
               '|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|\\/|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|/\\|']

    print(Style.BRIGHT, end = '')
    print(Fore.MAGENTA, end = '')

    print(pattern[0][0 : lenght - 1])
    print(pattern[1][0 : lenght - 1])
    print('\n')

    print(Fore.YELLOW, end = '')

    print(author_logo[0 : len(author_logo) - 93], end = '')
    
    print(Fore.CYAN, end = '')

    print(author_logo[len(author_logo) - 93 : len(author_logo) - 75], end = '')

    print(Fore.YELLOW, end = '')

    print(author_logo[len(author_logo) - 75 : len(author_logo) - 45], end = '')

    print(Fore.CYAN, end = '')

    print(author_logo[len(author_logo) - 45 : len(author_logo)], end = '')
    print('\n')

    print(Fore.MAGENTA, end = '')

    print(pattern[0][0 : lenght - 1])
    print(pattern[1][0 : lenght - 1])

    output = '© All rights reserved, 2021'
    spaces = ' ' * (lenght - len(output))
    output = spaces + output

    print(Fore.RED, end = '')
    print('\n\n' + output)

    print(Style.RESET_ALL, end = '')

    time.sleep(3)
    os.system('clear')
    
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
        self.clear_text(description)

    def clear_text(self, description):

        try:

            self.description = self.description.replace('[[', '')
            self.description = self.description.replace(']]', '')
            self.description = self.description.replace(' .', '.')
            self.description = self.description.replace(' ,', ',')
            self.description = self.description.replace('\n', ' ')
            self.description = self.description.replace('\r', ' ')
            self.description = self.description.replace('  ', ' ')

            while True:

                if self.description.find('[') == -1:

                    self.description = self.description.replace(' .', '.')
                    self.description = self.description.replace(' ,', ',')
                    self.description = self.description.replace('  ', ' ')

                    return self.description

                else:

                    self.description = self.description.replace(self.description[self.description.find('[') : self.description.find(']') + 1], '', 1)

        except:

            self.description = 'Нет описания'


    def pad_text(self, length):

        return textwrap.fill(self.description, length)
        
class AnimeList():

    def __init__(self, nickname, options, filepath = None):

        self.nickname = nickname
        self.filepath = filepath
        self.options = options

        self.parameters = {'c' : 'completed', 'd' : 'dropped', 'o' : 'on_hold', 'p' : 'planned',
                           'r' : 'rewatching', 'w' : 'watching', 'b' : 'released', 'n' : 'ongoing',
                           'm' : 'anons'}

        self.load()

    def load(self):

        if self.options == 'webload':

            try:
                self.animelist = self.webload()
                self.raw_data = self.convert_to_dictionary()
                self.type = 'Loaded form Shikimori'
                self.date = datetime.strptime('23595922221231Monday','%H%M%S%Y%m%d%A')

            except:
                sys_output = 'Unable to load data for ' + self.nickname + '. Check the username correctness and internet connection'
                length = Terminal().size.x - len(sys_output)
                Print().cprint(sys_output + ' ' * length, 'r')

                self.animelist = 'Error: Download_error'
                return 0

        elif self.options == 'locaload':
            self.type = 'Local file at ' + datetime.strptime(binascii.a2b_hex(self.filepath.stem.encode()).decode().split('|')[0],'%H%M%S%Y%m%d%A').__format__('Date: %H:%M:%S %Y/%m/%d %A')
            self.date = datetime.strptime(binascii.a2b_hex(self.filepath.stem.encode()).decode().split('|')[0],'%H%M%S%Y%m%d%A')
            self.raw_data = self.locaload()
            self.animelist = self.convert_to_class_objects()

        else:
            None
        
        self.completed = [item for item in self.animelist if item.user_status == 'completed']
        self.dropped = [item for item in self.animelist if item.user_status == 'dropped']
        self.on_hold = [item for item in self.animelist if item.user_status == 'on_hold']
        self.planned = [item for item in self.animelist if item.user_status == 'planned']
        self.rewatching = [item for item in self.animelist if item.user_status == 'rewatching']
        self.watching = [item for item in self.animelist if item.user_status == 'watching']
        self.released = [item for item in self.animelist if item.status == 'released']
        self.ongoing = [item for item in self.animelist if item.status == 'ongoing']
        self.anons = [item for item in self.animelist if item.status == 'anons']

        self.custom = []

    def webload(self):

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'}
        animelist = list()
        
        url = 'https://shikimori.one/' + self.nickname + '/list_export/animes.json'
        data = requests.get(url, headers = headers, allow_redirects = True)
        raw_data = json.loads(data.content.decode())
        
        count = 0
        
        for item in raw_data:
            
            (progress_bar(count, len(raw_data) - 1, 'Processing data for ' + self.nickname, 'Completed'))
            count += 1
            
            url = 'https://shikimori.one/api/animes/' + str(item['target_id'])
            data = requests.get(url, headers = headers, allow_redirects = True)
            
            while len(data.content.decode()) <= 20:
                    data = requests.get(url, headers = headers, allow_redirects = True)
            
            api_data = json.loads(data.content.decode())
            
            animelist.append(Anime(api_data['id'], 
                                    api_data['name'], 
                                    api_data['russian'], 
                                    api_data['url'], 
                                    api_data['description'], 
                                    api_data['kind'], 
                                    api_data['score'], 
                                    api_data['status'], 
                                    api_data['episodes'], 
                                    api_data['episodes_aired'], 
                                    api_data['aired_on'],
                                    api_data['released_on'], 
                                    api_data['rating'], 
                                    api_data['duration'], 
                                    api_data['anons'], 
                                    api_data['ongoing'],
                                    api_data['myanimelist_id'], 
                                    api_data['rates_scores_stats'], 
                                    api_data['rates_statuses_stats'], 
                                    api_data['next_episode_at'],
                                    item['status'],
                                    item['episodes']))

        progress_bar(1, 1, 'Processing data for ' + self.nickname, 'Completed')
        print('')
            
        return animelist

    def locaload(self):
        with open(self.filepath, 'rb') as file:
            return pickle.load(file)

    def save(self):

        filename = binascii.b2a_hex((datetime.strftime(datetime.today(), '%H%M%S%Y%m%d%A') + '|' + self.nickname).encode()).decode() + '.smf'

        with open(filename, 'wb') as file:
            pickle.dump(self.convert_to_dictionary(), file)

    def convert_to_dictionary(self):
        
        return [{'idt' : item.idt, 
                 'name' : item.name, 
                 'russian' : item.russian, 
                 'url' : item.url, 
                 'description' : item.description, 
                 'kind' : item.kind, 
                 'score' : item.score, 
                 'status' : item.status, 
                 'episodes' : item.episodes, 
                 'episodes_aired' : item.episodes_aired, 
                 'aired_on' : item.aired_on, 
                 'released_on' : item.released_on, 
                 'rating' : item.rating, 
                 'duration' : item.duration, 
                 'anons' : item.anons, 
                 'ongoing' : item.ongoing,
                 'myanimelist_id' : item.myanimelist_id,
                 'rates_scores_stats' : item.rates_scores_stats,
                 'rates_statuses_stats' : item.rates_statuses_stats,
                 'next_episode_at' : item.next_episode_at, 
                 'user_status' : item.user_status, 
                 'user_episodes' : item.user_episodes
                 } for item in self.animelist]

    def convert_to_class_objects(self):
        
        return [(Anime(item['idt'], 
                 item['name'], 
                 item['russian'], 
                 item['url'], 
                 item['description'], 
                 item['kind'], 
                 item['score'], 
                 item['status'], 
                 item['episodes'], 
                 item['episodes_aired'], 
                 item['aired_on'],
                 item['released_on'], 
                 item['rating'], 
                 item['duration'], 
                 item['anons'], 
                 item['ongoing'],
                 item['myanimelist_id'], 
                 item['rates_scores_stats'], 
                 item['rates_statuses_stats'], 
                 item['next_episode_at'],
                 item['user_status'],
                 item['user_episodes'])) for item in self.raw_data]

    def custom_list(self, parameters):

        self.custom = []
        [(duplicate_list := [item.idt for item in self.custom], [self.custom.append(item) 
        for item in operator.attrgetter(self.parameters[letter])(self) 
        if letter in parameters if item.idt not in duplicate_list]) for letter in parameters]

class Convertation():
    def __init__(self, users_list):
        self.users_list = users_list

    def resort(self):
        return sorted(sorted(self.users_list, key=operator.attrgetter('date'), reverse = True), key=operator.attrgetter('nickname'))

    def convert_to_dictionary(self):
        return {str(n + 1) : self.users_list[n] for n in range(len(self.users_list))}

    def convert_to_id_dictionary(self):
        return {self.users_list[n] : self.users_list[n].idt for n in range(len(self.users_list))}

    def convert_to_anime_dictionary(self):
        return {str(n + 1) : self.users_list[n] for n in range(len(self.users_list))}

class Merges():
    def __init__(self, users_list):
        self.users_list = users_list

    def search_for_merges(self):
        merged_list = list(chain.from_iterable([item.custom for item in self.users_list]))
        id_list = [operator.attrgetter('idt')(merged_list[n]) for n in range(len(merged_list))]
        return [merged_list[item] for item in list(set([id_list.index(item) for item in id_list if id_list.count(item) == len(self.users_list)]))]

    def search_for_differences(self):
        merged_list = list(chain.from_iterable([item.custom for item in self.users_list]))
        id_list = [operator.attrgetter('idt')(merged_list[n]) for n in range(len(merged_list))]

        os.system('clear')
        Print().merges_header()
        Print().merges_list_header()
        Print().cprint(Print(self.users_list).print_users_list(), 'g', 1)

        while True:
            Print().merges_reference_user_input()
            inp = input()

            if inp == '':
                self.reference = []
                break

            try:
                self.reference = [item.idt for item in self.users_list[int(inp) - 1].custom]
                Print(self.users_list[int(inp) - 1].nickname).merges_reference_user_name()
                break

            except:
                Print().merges_reference_user_input_error()

        Print(self.users_list).merges_list_print() 

        while True:
            
            try:
                Print().merges_list_input()
                inp = int(input())
                
                if 1 <= inp <= (len(self.users_list) + 1):
                    break
                
                else:
                    raise Error
            
            except:
                Print().merges_list_type_error()

        return [[merged_list[item] for item in list(set([id_list.index(item) for item in id_list if id_list.count(item) < len(self.users_list) if item not in self.reference]))] if len(self.users_list) == int(inp) else [merged_list[item] for item in list(set([id_list.index(item) for item in id_list if id_list.count(item) == inp if item not in self.reference]))]][0]
        
class Load():
    def __init__(self, path):
        self.path = path
        self.name = binascii.a2b_hex(path.stem.encode()).decode().split('|')[1]
        self.date = datetime.strptime(binascii.a2b_hex(path.stem.encode()).decode().split('|')[0], '%H%M%S%Y%m%d%A')
        self.string_date = datetime.strptime(binascii.a2b_hex(path.stem.encode()).decode().split('|')[0],'%H%M%S%Y%m%d%A').__format__('Date: %H:%M:%S %Y/%m/%d %A')

class Manage():
    def __init__(self, users_list):
        self.users_list = users_list

    def ui(self):

        while True:
            os.system('clear')
            if self.users_list == []:
                Print().manage_empty_list_error()
                time.sleep(2)
                return self.users_list
            Print().manage_header()
            Print().manage_list_header()
            Print().cprint(Print(self.users_list).print_users_list(), 'g', 1)
            Print().manage_menu()

            Print().manage_input()
            inp = sinp()

            if inp == '1':
                self.view_list()

            if inp == '2':
                while self.remove_list() != 0:
                    None

            elif inp == '3':
                self.users_list = []
                return self.users_list

            elif inp == '4':
                self.remove_files()

            elif inp == '\r':
                return self.users_list

    def remove_list(self):
        users_to_delete = list()
        inp = 'defaults'

        if self.users_list == []:
            return 0

        os.system('clear')
        Print().remove_users_header()
        Print().manage_list_header()
        Print().cprint(Print(self.users_list).print_users_list(), 'g', 1)

        Print().manage_delete_input()
        inp = input()

        if inp == '':
            return 0

        try:
            user = self.users_list[int(inp) - 1]
            self.users_list.remove(user)
            Print().cprint('User data ' + user.nickname + ' has been removed.', 'g')

        except:
            Print().cprint('Unable to find user. Type error', 'r')

    def view_list(self):

        while True:
            os.system('clear')
            Print().view_anime_list_header()
            Print().manage_list_header()
            Print().cprint(Print(self.users_list).print_users_list(), 'g', 1)

            Print().view_anime_list_input()
            inp = input()

            if inp == '':
                break

            try:
                Main_Output(self.users_list[int(inp) - 1].animelist).ui()
            except:
                Print().cprint('Unable to find user. Type error', 'r')
                time.sleep(0.5)

    def remove_files(self):
        users_to_load = list()
        os.system('clear')
        Print().remove_files_header()

        classlist = {str(n + 1) : sorted(sorted([Load(item) for item in [f for f in Path(os.getcwd()).glob('**/*.smf') if f.is_file()]], key=operator.attrgetter('date'), reverse = True), key=operator.attrgetter('name'))[n] for n in range(len([f for f in Path(os.getcwd()).glob('**/*.smf') if f.is_file()]))}
        Print('locaload_list', classlist).remove_files_list()

        while True:
            Print().remove_files_input()
            inp = input()

            if inp == '':
                break

            try:
                filename = classlist[inp].name
                os.remove(classlist[inp].path)
                Print().cprint('File ' + filename + ' has been removed', 'g')
            except:
                Print().cprint('Unable to remove file', 'r')

class Print():
    def __init__(self, options = None, data = None):
        self.options = options
        self.data = data
        self.terminal = Terminal()

    #Global
    def print_users_list(self):
        users_dict = Convertation(self.options).convert_to_dictionary()
        return [item for item in [str(key) + '. ' + ((len(str(len(users_dict))) - len(str(key))) * ' ') + (max([len(users_dict[key].nickname) for key in users_dict]) - (len(users_dict[key].nickname))) * ' ' + users_dict[key].nickname + ' | ' + users_dict[key].type for key in users_dict]]

    def generate_users_list(self):
        output = ''

        users_dict = Convertation(self.options).convert_to_dictionary()

        for key in users_dict:
            output += (max([len(users_dict[key].nickname) for key in users_dict]) - (len(users_dict[key].nickname))) * ' ' + users_dict[key].nickname + ' | ' + users_dict[key].type + '\n'

        return output

    def reset(self):
        print(Style.RESET_ALL, end = '')

    def print_color(self, text = None, color = None):

        if color == None:
            print(Fore.WHITE, end = '')
            print(text, end = '')

        elif color == 'r':
            print(Fore.RED, end = '')
            print(text, end = '')

        elif color == 'g':
            print(Fore.GREEN, end = '')
            print(text, end = '')

        elif color == 'b':
            print(Fore.BLUE, end = '')
            print(text, end = '')

        elif color == 'y':
            print(Fore.YELLOW, end = '')
            print(text, end = '')

        elif color == 'm':
            print(Fore.MAGENTA, end = '')
            print(text, end = '')

        elif color == 'c':
            print(Fore.CYAN, end = '')
            print(text, end = '')

        else:
            None

    def cprint(self, text, color, mode = 0, mode_2 = 0):
        if mode == 0:
            text = text.split('\n')

        max_value = math.floor((self.terminal.size.x - max([len(item) for item in text])) / 2)
        if mode_2 == 0:
            [(print(max_value * ' ', end = ''), self.print_color(item, color), print('')) for item in text]
        else:
            [(print(max_value * ' ', end = ''), self.print_color(item, color)) for item in text]

    def cprint_progress(self, text, color, mode = 0, mode_2 = 0):
        self.print_color(text, random.choice(['b', 'c', 'y']))
        print('\r', end = '')

    # Menu printing
    def menu(self):
        self.cprint('----------------------------------', 'r')
        self.cprint(" _ __ ___   ___ _ __  _   _ \n| '_ ` _ \\ / _ \\ '_ \\| | | |\n| | | | | |  __/ | | | |_| |\n|_| |_| |_|\\___|_| |_|\\__,_|", 'y')
        self.cprint('\nList of option: \n\n1. Load data from internet\n2. Load data from local file\n3. Save data to local file\n4. Manage loaded lists\n5. Search for simmilar animes\n6. Search for different animes\n\nEnter to exit', 'c')

    def input_menu(self):
        [self.cprint('\nEnter number from menu:     ', 'm'), sys.stdout.flush()]
        self.cprint('----------------------------------', 'r')
        [self.cprint('\nList of all users loaded: ', 'y') for n in range(1) if self.options != []]
        self.cprint(self.generate_users_list(), 'g')
        self.reset()
    # / Menu printing

    # Web load printing
    def header_webload(self):
        self.cprint(" _       _                       _        _                 _ \n(_)     | |                     | |      | |               | |\n _ _ __ | |_ ___ _ __ _ __   ___| |_     | | ___   __ _  __| |\n| | '_ \\| __/ _ \\ '__| '_ \\ / _ \\ __|    | |/ _ \\ / _` |/ _` |\n| | | | | ||  __/ |  | | | |  __/ |_     | | (_) | (_| | (_| |\n|_|_| |_|\\__\\___|_|  |_| |_|\\___|\\__|    |_|\\___/ \\__,_|\\__,_|", 'y')
    
    def input_webload(self):
        self.cprint('\nEnter usernames to be loaded (Press ENTER to start loading): ', 'm')

    def webload_list(self):
        self.cprint(str(self.options) + ' User nickname: ', 'm', 0, 1)

    def webload_start(self):
        self.cprint('\nStarting processing users...\n', 'g')
    # / Web load printing 

    # Local load printing
    def locaload_list(self):
        # for dict with Load objects
        return [([(item) for item in [(key + '. ' + (len(str(len(self.data))) - len(key)) * ' ' + 
                self.data[key].name + (max([len(self.data[key].name) for key in self.data]) - 
                len(self.data[key].name)) * ' ' + ' | ' + self.data[key].string_date) for key in self.data]])]

    def load(self):
        [(print(''), self.cprint('Enter number of user to load its data (ENTER to finish): ', 'm', 0, 1)) 
         if self.options == 'input_locaload' else self.cprint('Loaded successfully', 'g') 
         if self.options == 'locaload_ok' else self.cprint('\nError while loading file. Type error or data file is corrupted', 'r')
         if self.options == 'locaload_error' else (self.cprint(' _                 _      _                 _ \n| |               | |    | |               | |\n| | ___   ___ __ _| |    | | ___   __ _  __| |\n| |/ _ \\ / __/ _` | |    | |/ _ \\ / _` |/ _` |\n| | (_) | (_| (_| | |    | | (_) | (_| | (_| |\n|_|\\___/ \\___\\__,_|_|    |_|\\___/ \\__,_|\\__,_|', 'y'), self.cprint('\n\nList of all files found: \n', 'b'), self.cprint(list(chain.from_iterable(self.locaload_list())), 'g', 1))
         if self.options == 'locaload_list' else None]
    # / Local load printing

    # Save printing
    def save(self):
        self.cprint(self.options + ' list has been saved successfully', 'g')

    def save_no_list(self):
        [print('') for n in range(math.floor((self.terminal.size.y - 6) / 2) - 1)]
        self.cprint("  _   _                                             _     _          _ \n | \\ | |                                           | |   | |        | |\n |  \\| | ___    _   _ ___  ___ _ __ ___    __ _  __| | __| | ___  __| |\n | . ` |/ _ \\  | | | / __|/ _ \\ '__/ __|  / _` |/ _` |/ _` |/ _ \\/ _` |\n | |\\  | (_) | | |_| \\__ \\  __/ |  \\__ \\ | (_| | (_| | (_| |  __/ (_| |\n |_| \\_|\\___/   \\__,_|___/\\___|_|  |___/  \\__,_|\\__,_|\\__,_|\\___|\\__,_|", 'r')
        time.sleep(2)

    def header_save(self):
        self.cprint("   _____             _                     _       _        \n  / ____|           (_)                   | |     | |       \n | (___   __ ___   ___ _ __   __ _      __| | __ _| |_ __ _ \n  \\___ \\ / _` \\ \\ / / | '_ \\ / _` |    / _` |/ _` | __/ _` |\n  ____) | (_| |\\ V /| | | | | (_| |   | (_| | (_| | || (_| |\n |_____/ \\__,_| \\_/ |_|_| |_|\\__, |    \\__,_|\\__,_|\\__\\__,_|\n                              __/ |                         \n                             |___/                          \n\n", 'y')
    
    def no_files_found(self):
        [print('') for n in range(math.floor((self.terminal.size.y - 6) / 2) - 1)]
        self.cprint('  _   _           __ _ _                        _     _       \n | \\ | |         / _(_) |                      (_)   | |      \n |  \\| | ___    | |_ _| | ___  ___     _____  ___ ___| |_ ___ \n | . ` |/ _ \\   |  _| | |/ _ \\/ __|   / _ \\ \\/ / / __| __/ __|\n | |\\  | (_) |  | | | | |  __/\\__ \\  |  __/>  <| \\__ \\ |_\\__ \\\n |_| \\_|\\___/   |_| |_|_|\\___||___/   \\___/_/\\_\\_|___/\\__|___/', 'r')
        time.sleep(2)
    # / Save printing

    # Manage List
    def manage_header(self):
        self.cprint("  __  __                                     _ _     _       \n |  \\/  |                                   | (_)   | |      \n | \\  / | __ _ _ __   __ _  __ _  ___       | |_ ___| |_ ___ \n | |\\/| |/ _` | '_ \\ / _` |/ _` |/ _ \\      | | / __| __/ __|\n | |  | | (_| | | | | (_| | (_| |  __/      | | \\__ \\ |_\\__ \\\n |_|  |_|\\__,_|_| |_|\\__,_|\\__, |\\___|      |_|_|___/\\__|___/\n                            __/ |                            \n                           |___/                             ", 'y')

    def remove_users_header(self):
        self.cprint("  _____                                                          \n |  __ \\                                                         \n | |__) |___ _ __ ___   _____   _____    _   _ ___  ___ _ __ ___ \n |  _  // _ \\ '_ ` _ \\ / _ \\ \\ / / _ \\  | | | / __|/ _ \\ '__/ __|\n | | \\ \\  __/ | | | | | (_) \\ V /  __/  | |_| \\__ \\  __/ |  \\__ \\\n |_|  \\_\\___|_| |_| |_|\\___/ \\_/ \\___|   \\__,_|___/\\___|_|  |___/", 'y')
    
    def manage_menu(self):
        self.cprint('\n----------------------------------', 'r')
        self.cprint('List of options:\n\n1. View animes in list\n2. Remove selected users\n3. Remove all users\n4. Remove loaded files', 'c')
        self.cprint('----------------------------------', 'r')
    
    def manage_input(self):
        self.cprint('Enter number of user to load its data (ENTER to finish): ', 'm', 0, 1)

    def manage_delete_input(self):
        print('')
        self.cprint('Enter number of user to delete its data (ENTER to finish): ', 'm', 0, 1)

    def manage_error(self):
        print('Unable to find user')
    
    def manage_empty_list_error(self):
        [print('') for n in range(math.floor((self.terminal.size.y - 6) / 2) - 1)]
        self.cprint("  _   _                                      __                      _ \n | \\ | |                                    / _|                    | |\n |  \\| | ___     _   _ ___  ___ _ __ ___   | |_ ___  _   _ _ __   __| |\n | . ` |/ _ \\   | | | / __|/ _ \\ '__/ __|  |  _/ _ \\| | | | '_ \\ / _` |\n | |\\  | (_) |  | |_| \\__ \\  __/ |  \\__ \\  | || (_) | |_| | | | | (_| |\n |_| \\_|\\___/    \\__,_|___/\\___|_|  |___/  |_| \\___/ \\__,_|_| |_|\\__,_|", 'r')
    
    def manage_list_header(self):
        self.cprint('\n\nList of all users found\n', 'y')

    def view_anime_list_header(self):
        self.cprint(" __      ___                              _                   _ _     _   \n \\ \\    / (_)                            (_)                 | (_)   | |  \n  \\ \\  / / _  _____      __    __ _ _ __  _ _ __ ___   ___   | |_ ___| |_ \n   \\ \\/ / | |/ _ \\ \\ /\\ / /   / _` | '_ \\| | '_ ` _ \\ / _ \\  | | / __| __|\n    \\  /  | |  __/\\ V  V /   | (_| | | | | | | | | | |  __/  | | \\__ \\ |_ \n     \\/   |_|\\___| \\_/\\_/     \\__,_|_| |_|_|_| |_| |_|\\___|  |_|_|___/\\__|", 'y')

    def view_anime_list_input(self):
        print('')
        self.cprint('Enter number of user to view its data (ENTER to exit): ', 'm', 0, 1)

    def remove_files_header(self):
        self.cprint("  _____                                     __ _ _           \n |  __ \\                                   / _(_) |          \n | |__) |___ _ __ ___   _____   _____     | |_ _| | ___  ___ \n |  _  // _ \\ '_ ` _ \\ / _ \\ \\ / / _ \\    |  _| | |/ _ \\/ __|\n | | \\ \\  __/ | | | | | (_) \\ V /  __/    | | | | |  __/\\__ \\\n |_|  \\_\\___|_| |_| |_|\\___/ \\_/ \\___|    |_| |_|_|\\___||___/", 'y')

    def remove_files_input(self):
        print('')
        self.cprint('Enter number of user to delete its FILE! (ENTER to finish): ', 'm', 0, 1)

    def remove_files_list(self):
        self.cprint('\n\nList of all files found: \n', 'b')
        self.cprint(list(chain.from_iterable(self.locaload_list())), 'g', 1)
    # / Manage List

    # Create custom lists
    def custom_header(self):
        self.cprint("   _____                _            _ _     _       \n  / ____|              | |          | (_)   | |      \n | |     _ __ ___  __ _| |_ ___     | |_ ___| |_ ___ \n | |    | '__/ _ \\/ _` | __/ _ \\    | | / __| __/ __|\n | |____| | |  __/ (_| | ||  __/    | | \\__ \\ |_\\__ \\\n  \\_____|_|  \\___|\\__,_|\\__\\___|    |_|_|___/\\__|___/", 'y')
        
    def custom_list_header(self):
        self.cprint('\nList of all users\n', 'b')

    def custom_currently_loaded(self):
        self.cprint('\nCurrently loaded\n', 'b')

    def custom_input(self):
        print('')
        self.cprint('Enter a number of user to add his list (or "a" to add all users or ENTER to exit): ', 'm', 0, 1)

    def custom_input_error(self):
        self.cprint('List no found. Type error', 'r')

    def custom_ok(self):
        self.cprint(self.options + ' list has been added')

    def custom_already_in_list(self):
        self.cprint('This user is already in list!', 'r')

    def custom_modify_header(self):
        self.cprint('  __  __           _ _  __          _ _     _       \n |  \\/  |         | (_)/ _|        | (_)   | |      \n | \\  / | ___   __| |_| |_ _   _   | |_ ___| |_ ___ \n | |\\/| |/ _ \\ / _` | |  _| | | |  | | / __| __/ __|\n | |  | | (_) | (_| | | | | |_| |  | | \\__ \\ |_\\__ \\\n |_|  |_|\\___/ \\__,_|_|_|  \\__, |  |_|_|___/\\__|___/\n                            __/ |                   \n                           |___/                    ', 'y')
    
    def custom_modify_menu(self):
        self.cprint('\n\n----------------------------------', 'r')
        self.cprint('\nList of options: \n1. Choose options to include\n2. Choose options to exclude\n3. Include categories for each list separately\n4. Exclude categories for each list separately\nAny key to leave lists unmodified', 'c')
        self.cprint('\n----------------------------------', 'r')
    
    def custom_modify_input_modes(self):
        self.cprint('Enter a mode number: ', 'm', 0, 1)

    def custom_transfer_header(self):
        self.cprint("  _____                               _                \n |  __ \\                             | |               \n | |__) |_ _ _ __ __ _ _ __ ___   ___| |_ ___ _ __ ___ \n |  ___/ _` | '__/ _` | '_ ` _ \\ / _ \\ __/ _ \\ '__/ __|\n | |  | (_| | | | (_| | | | | | |  __/ ||  __/ |  \\__ \\\n |_|   \\__,_|_|  \\__,_|_| |_| |_|\\___|\\__\\___|_|  |___/", 'y')

    def custom_transfer_menu(self):
        if self.options == 0:
            self.cprint('\n\nCategories to add to lists\n', 'b')
        else:
            self.cprint('\n\nCategories to remove from lists\n', 'b')
            
        self.cprint('1. Completed\n2. Dropped\n3. On hold\n4. Planned\n5. Rewatching\n6. Watching\n7. Released\n8. Ongoing\n9. Anons', 'c')

    def custom_transfer_loaded(self):
        if self.options == 0:
            self.cprint('\n\nCategories ADDED\n', 'b')
        else:
            self.cprint('\n\nCategories REMOVED\n', 'b')

        dictionary = {'c' : 'Completed', 'd' : 'Dropped', 'o' : 'On hold', 'p' : 'Planned',
                      'r' : 'Rewatching', 'w' : 'Watching', 'b' : 'Released', 'n' : 'Ongoing',
                      'm' : 'Anons'}

        string = ''

        for item in self.data:
            string = string + dictionary[item] + '\n'

        self.cprint(string, 'g')

    def custom_for_user(self):
        if self.options == None:
            None
        else:
            self.cprint('\nCategories for user: ' + self.options, 'c')

    def custom_transfer_input(self):
        print('')
        self.cprint('Enter option number from list: ', 'm', 0, 1)

    # / Create custom lists

    # Merges
    def merges_header(self):
        self.cprint("    _____                     _        __           \n   / ____|                   | |      / _|          \n  | (___   ___  __ _ _ __ ___| |__   | |_ ___  _ __ \n   \\___ \\ / _ \\/ _` | '__/ __| '_ \\  |  _/ _ \\| '__|\n   ____) |  __/ (_| | | | (__| | | | | || (_) | |   \n  |_____/ \\___|\\__,_|_|  \\___|_| |_| |_| \\___/|_|   \n     | (_)/ _|/ _|                                  \n   __| |_| |_| |_ ___ _ __ ___ _ __   ___ ___  ___  \n  / _` | |  _|  _/ _ \\ '__/ _ \\ '_ \\ / __/ _ \\/ __| \n | (_| | | | | ||  __/ | |  __/ | | | (_|  __/\\__ \\ \n  \\__,_|_|_| |_| \\___|_|  \\___|_| |_|\\___\\___||___/ ", 'y')
    
    def merges_list_header(self):
        self.cprint('\n\nList of all users', 'b')

    def merges_reference_user_input(self):
        print('')
        self.cprint('Enter to skip reference user or enter a user number to make it a reference user: ', 'm', 0, 1)

    def merges_reference_user_input_error(self):
        self.cprint('User not found. Type error', 'r')

    def merges_reference_user_name(self):
        self.cprint('Animes from ' + self.options + ' will not be included in final list', 'g')

    def merges_list_input(self):
        self.cprint('Choose an option: ', 'm', 0, 1)

    def merges_list_print(self):
        self.cprint('\n\nList of all comparison\n', 'b')
        
        self.cprint([(str(n) + '. ' + ((len(str(len(self.options))) - len(str(n))) * ' ') + 'Show animes that appear in ' + 
                    ((len(str(len(self.options))) - len(str(n))) * ' ' + str(n)) + ' lists' + ' | Total junctions: ' + 
                    str(int(math.factorial(len(self.options)) / (math.factorial(n) * math.factorial((len(self.options)) - n))))) 
                    if n < len(self.options) else (str(n) + '. ' + ((len(str(len(self.options))) - len(str(n))) * ' ') + 
                    'Show animes that appear in all lists') for n in range(1, len(self.options) + 1)], 'g', 1)
    
    def merges_list_type_error(self):
        self.cprint('User not found. Type error', 'r')

    # / Merges

    # Main Output
    def main_output_header(self):
        self.cprint('           _   _ _____ __  __ ______       _      _____  _____ _______ \n     /\\   | \\ | |_   _|  \\/  |  ____|     | |    |_   _|/ ____|__   __|\n    /  \\  |  \\| | | | | \\  / | |__        | |      | | | (___    | |   \n   / /\\ \\ | . ` | | | | |\\/| |  __|       | |      | |  \\___ \\   | |   \n  / ____ \\| |\\  |_| |_| |  | | |____      | |____ _| |_ ____) |  | |   \n /_/    \\_\\_| \\_|_____|_|  |_|______|     |______|_____|_____/   |_|   ', 'y')
        print('\n')
    
    def main_output_menu(self):
        print('')
        self.cprint('Enter a anime number to see more info (0 to print the list again or enter to exit): ', 'm', 0, 1)

    def print_animelist(self):
        [print(item) for item in [str(key) + '. ' + ((len(str(len(self.options))) - len(str(key))) * ' ') + self.options[key].russian for key in self.options]]
    
    def main_empty_list(self):
        self.cprint("  _   _                      _                         __                      _ \n | \\ | |                    (_)                       / _|                    | |\n |  \\| | ___      __ _ _ __  _ _ __ ___   ___  ___   | |_ ___  _   _ _ __   __| |\n | . ` |/ _ \\    / _` | '_ \\| | '_ ` _ \\ / _ \\/ __|  |  _/ _ \\| | | | '_ \\ / _` |\n | |\\  | (_) |  | (_| | | | | | | | | | |  __/\\__ \\  | || (_) | |_| | | | | (_| |\n |_| \\_|\\___/    \\__,_|_| |_|_|_| |_| |_|\\___||___/  |_| \\___/ \\__,_|_| |_|\\__,_|", 'r')

class Main_Output():
    def __init__(self, animelist):
        self.animelist = animelist
        self.animedict = Convertation(animelist).convert_to_anime_dictionary()

    def print_list(self):
        Print(self.animedict).print_animelist()

    def ui(self):
        os.system('clear')
        Print().main_output_header()
        print(Fore.CYAN, end = '')
        self.print_list()
        Print().reset()

        while True:

            if self.animelist == []:
                Print().main_empty_list()
                time.sleep(1)
                break

            Print().main_output_menu()

            inp = input()
            
            if inp == '0':
                os.system('clear')
                Print().main_output_header()
                print(Fore.CYAN, end = '')
                self.print_list()
                Print().reset()

            elif inp == '':
                return 0

            else:
                try:
                    Print_Info(self.animedict[inp]).start()
                except:
                    None

class Print_Info():
    large_figures = {'0' : '  ___   \n / _ \\  \n| | | | \n| | | | \n| |_| | \n \\___/  ',
                     '1' : ' __  \n/_ | \n | | \n | | \n | | \n |_| ',
                     '2' : ' ___   \n|__ \\  \n   ) | \n  / /  \n / /_  \n|____| ',
                     '3' : ' ____   \n|___ \\  \n  __) | \n |__ <  \n ___) | \n|____/  ',
                     '4' : ' _  _    \n| || |   \n| || |_  \n|__   _| \n   | |   \n   |_|   ',
                     '5' : ' _____  \n| ____| \n| |__   \n|___ \\  \n ___) | \n|____/  ',
                     '6' : "   __   \n  / /   \n / /_   \n| '_ \\  \n| (_) | \n \\___/  ",
                     '7' : ' ______  \n|____  | \n    / /  \n   / /   \n  / /    \n /_/     ',
                     '8' : '  ___   \n / _ \\  \n| (_) | \n > _ <  \n| (_) | \n \\___/  ',
                     '9' : '  ___   \n / _ \\  \n| (_) | \n \\__, | \n   / /  \n  /_/   ',
                     '.' : '   \n   \n   \n   \n _ \n(_)'}

    info_logo = ['  ___ _  _ ___ ___  ',
                 ' |_ _| \\| | __/ _ \\ ',
                 '  | || .` | _| (_) |',
                 ' |___|_|\\_|_| \\___/ ']

    def __init__(self, anime):
        self.anime = anime
        self.terminal = Terminal()

    def print_logo(self):
        Print().cprint(self.info_logo, 'y', 1)

    def generate_q1(self):
        block = []

        try:
            block.append('Title: ' + self.anime.name + ' / ' + self.anime.russian)
        except:
            block.append('Title: Unable to display title')
        try:
            block.append('Type: ' + self.anime.kind)
        except:
            block.append('Type: Unable to display type')
        try:
            block.append('Status: ' + self.anime.status)
        except:
            block.append('Status: Unable to display status')
        try:
            block.append('Total episodes: ' + str(self.anime.episodes))
        except:
            block.append('Total episodes: Unable to display episodes')
        try:
            block.append('Episodes aired: ' + str(self.anime.episodes_aired))
        except:
            block.append('Episodes aired: Unable to display episodes aired')
        try:
            block.append('Premiere: ' + self.anime.aired_on)
        except:
            block.append('Premiere: Unable to display premiere')
        try:
            block.append('Released: ' + self.anime.released_on)
        except:
            block.append('Released: Unable to display release date')
        try:
            block.append('Duration: ' + str(self.anime.duration) + ' min')
        except:
            block.append('Duration: unable to display duration')
        try:
            block.append('URL link: ' + 'https:shikimori.one' + str(self.anime.url.split('-')[0]))
        except:
            block.append('URL link: Unable to display link')

        return block

    def generate_q2(self):
        score_list = list()

        for item in [[item[n] for item in [self.large_figures[item].split('\n') for item in self.anime.score]] for n in range(6)]:
            row_string = ''
            
            for row in item:
                row_string += row
            
            score_list.append(row_string)

        return score_list

    def generate_q3(self, q4):

        size = self.terminal.size.x - max([len(item) for item in q4])
        description = [math.floor((size - 18) / 2) * ' ' + 'Описание', '']
        final_list = []

        if self.anime.description == 'Нет описания':
            padded_list = ['', '', '', '', '', ' ' * math.floor((size - 22) / 2) + 'Нет описания', '', '', '', '', '', '']

        else:
            try:
                padded_list = self.anime.pad_text(size - 10)
                padded_list = padded_list.split('\n')
            except:
                padded_list = ['', '', '', '', '', ' ' * math.floor((size - 22) / 2) + 'Нет описания', '', '', '', '', '', '']

        while len(q4) > len(padded_list):
            padded_list.append('')

        [description.append(item) for item in padded_list]

        for item in description:
            while len(item) != size - 1:
                item += ' '
            final_list.append(item)

        return final_list, q4
    
    def generate_q4(self):

        sys_dictionary = {item['name'] : item['value'] for item in self.anime.rates_scores_stats}
        frames = [0 + max(list({item['name'] : item['value'] for item in self.anime.rates_scores_stats}.values()))/40 * i for i in range(41)]
        temp_list = [(str(key) + ' ' * (2 - len(str(key))) + ' : ' + '█' * {key : i + 1 for key in sys_dictionary for i in range(40) if frames[i] <= sys_dictionary[key] <= frames[i + 1]}[key] + ' (' + str(sys_dictionary[key]) + ')') for key in sys_dictionary]
        score_list = [math.floor((max([len(item) for item in temp_list]) - 16) / 2) * ' ' + 'Shikimori rating', '']
        [score_list.append(item) for item in temp_list]

        return score_list
    
    def print_q1_q2(self, q1, q2):
        [Print().print_color(q1.pop(0) + '\n', 'g') for i in range(len(q1) - 6)]
        [(Print().print_color(q1[i], 'g'), print((self.terminal.size.x - len(q1[i]) - len(q2[i]) - 11) * ' ', end = ''), Print().print_color(q2[i] + '\n', 'r')) for i in range(5)]
        [(Print().print_color(q1[5], 'g'), print((self.terminal.size.x - len(q1[5]) - len(q2[5]) - 11) * ' ', end = ''), Print().print_color(q2[5], 'r'), print(' User score'))]
        print('')

    def print_q3_q4(self, q4):
        q3, q4 = self.generate_q3(q4)

        [(Print().print_color(q3[i]), Print().print_color(q4[i] + '\n', 'c')) for i in range(len(q4))]
        [Print().print_color(item + '\n') for item in q3[12 : len(q3)] if len(q3) > 12]

    def start(self):

        self.print_logo()
        print('')
        
        try:

            self.print_q1_q2(self.generate_q1(), self.generate_q2())
            self.print_q3_q4(self.generate_q4())
        
        except:

            None

def progress_bar(iteration, total, prefix = '', suffix = '', decimals = 2, length = 100, fill = '█', printEnd = "\r"):
    
    length = Terminal().size.x - len(prefix) - len(suffix) - 12
    
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    
    Print().cprint_progress('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), 'r')
    
    if iteration == total: 
        print('\r%s |%s| %s%% %s' % (prefix, bar, ("{0:." + str(decimals) + "f}").format(100 * (total / float(total))), suffix), end = printEnd)

def create_custom_lists(users_list, mode = 0):

    def transfer(options, user = None):
        dictionary = {'1' : 'c', '2' : 'd', '3' : 'o', '4' : 'p', '5' : 'r', '6' : 'w', '7' : 'b', '8' : 'n', '9' : 'm'}
        params_list = []

        while True:

            os.system('clear')
            Print().custom_transfer_header()
            Print(user).custom_for_user()

            if params_list != []:
                Print(options, params_list).custom_transfer_loaded()

            Print(options).custom_transfer_menu()

            Print().custom_transfer_input()
            inp = sinp()

            if inp == '\r':
                if options == 0:
                    return params_list

                else:
                    letters = ['c', 'd', 'o', 'p', 'r', 'w', 'b', 'n', 'm']
                    [letters.remove(item) for item in params_list]

                    return letters

            try:
                [params_list.append(dictionary[inp]) if dictionary[inp] not in params_list else None]

            except:
                None

    os.system('clear')

    if users_list == []:
        Print().manage_empty_list_error()
        time.sleep(2)
        return 0

    if mode == 0:

        custom_dict = Convertation(users_list).convert_to_dictionary()
        custom_list = []

        while True:
            os.system('clear')
            Print().custom_header()

            if custom_list != []:
                Print().custom_currently_loaded()
                Print().cprint(Print(custom_list).print_users_list(), 'c', 1)

            Print().custom_list_header()
            Print().cprint(Print(users_list).print_users_list(), 'g', 1)

            Print().custom_input()
            inp = input()

            if inp == 'a':
                custom_list = users_list

                os.system('clear')
                Print().custom_header()
                Print().custom_currently_loaded()
                Print().cprint(Print(custom_list).print_users_list(), 'c', 1)
                time.sleep(2)

                return users_list

            try:

                [custom_list.append(custom_dict[inp]) if custom_dict[inp] not in custom_list else (Print().custom_already_in_list(), time.sleep(0.5))]
            
            except:

                if inp == '':
                    return custom_list

                else:
                    Print().custom_input_error()
                    time.sleep(0.5)

    if mode == 1:

        custom_dict = Convertation(users_list).convert_to_dictionary()
        custom_list = []

        while True:
            os.system('clear')
            Print().custom_header()

            if custom_list != []:
                Print().custom_currently_loaded()
                Print().cprint(Print(custom_list).print_users_list(), 'c', 1)

            Print().custom_list_header()
            Print().cprint(Print(users_list).print_users_list(), 'g', 1)

            Print().custom_input()
            inp = input()

            if inp == 'a':
                custom_list = users_list

                os.system('clear')
                Print().custom_header()
                Print().custom_currently_loaded()
                Print().cprint(Print(custom_list).print_users_list(), 'c', 1)
                time.sleep(2)

                break

            try:

                [custom_list.append(custom_dict[inp]) if custom_dict[inp] not in custom_list else (Print().custom_already_in_list(), time.sleep(0.5))]
            
            except:

                if inp == '':
                    break

                else:
                    Print().custom_input_error()
                    time.sleep(0.5)

        os.system('clear')

        Print().custom_modify_header()
        Print().custom_modify_menu()
        Print().custom_modify_input_modes()

        inp = sinp()
        
        if inp == '1':
            letters = ''

            for item in list(chain.from_iterable(transfer(0))):
                letters += item

            [item.custom_list(letters) for item in custom_list]
            return custom_list


        elif inp == '2':
            letters = ''

            for item in list(chain.from_iterable(transfer(1))):
                letters += item

            [item.custom_list(letters) for item in custom_list]
            return custom_list


        elif inp == '3':
            for item in custom_list:
                letters = ''

                for letter in list(chain.from_iterable(transfer(0, item.nickname))):
                    letters += letter

                item.custom_list(letters)
            
            return custom_list

        elif inp == '4':
            for item in custom_list:
                letters = ''

                for letter in list(chain.from_iterable(transfer(1, item.nickname))):
                    letters += letter

                item.custom_list(letters)
            
            return custom_list
        
        else:
            [item.custom_list('cdoprwbnm') for item in custom_list]
            return custom_list

def users(mode, options = None):
    
    if mode == 0:
        os.system('clear')
        Print().header_webload()
        Print().input_webload()
        inp = 'defaults'

        users_to_load = [(Print(count + 1).webload_list(), inp := input()) for count in range(1000000) if inp != '']
        Print().webload_start()
        return [item for item in [AnimeList(item[1], 'webload') for item in users_to_load if item[1] != ''] if item.animelist != 'Error: Download_error']
    
    if mode == 1:
        users_to_load = list()
        os.system('clear')

        if [f for f in Path(os.getcwd()).glob('**/*.smf') if f.is_file()] == []:
            Print().no_files_found()
            return []

        classlist = {str(n + 1) : sorted(sorted([Load(item) for item in [f for f in Path(os.getcwd()).glob('**/*.smf') if f.is_file()]], key=operator.attrgetter('date'), reverse = True), key=operator.attrgetter('name'))[n] for n in range(len([f for f in Path(os.getcwd()).glob('**/*.smf') if f.is_file()]))}

        Print('locaload_list', classlist).load()

        inp = 'defaults'
        
        try:
            [(Print('input_locaload').load(), inp := input(), users_to_load.append(AnimeList(classlist[inp].name, 'locaload', classlist[inp].path)), Print('locaload_ok').load()) for n in range(1000000)]
    
        except:
            [Print('locaload_error').load() if inp != '' else None for n in range(1)]
        
        return users_to_load

    if mode == 2:
        lists_to_save = create_custom_lists(options)
        
        if lists_to_save == 0:
            return 0

        os.system('clear')

        if lists_to_save == []:
            Print().save_no_list()

        Print().header_save()
        [(item.save(), Print(item.nickname).save(), time.sleep(1)) if options != [] else Print().save_no_list() for item in lists_to_save]

def menu():

    working_list = []

    while True:
        os.system('clear')
        Print().menu()
        Print(working_list).input_menu()

        inp = sinp()
        
        if inp == '0':
            None

        elif inp == '1':
            working_list = Convertation(users(0) + working_list).resort()

        elif inp == '2':
            working_list = Convertation(users(1) + working_list).resort()

        elif inp == '3':
            users(2, working_list)

        elif inp == '4':
            working_list = Manage(working_list).ui()

        elif inp == '5':
            custom_list = create_custom_lists(working_list, 1)
            if custom_list == 0:
                None
            else:
                Main_Output(Merges(custom_list).search_for_merges()).ui()

        elif inp == '6':
            custom_list = create_custom_lists(working_list, 1)
            if custom_list == 0:
                None
            else:
                Main_Output(Merges(custom_list).search_for_differences()).ui()

        elif inp == 'NA':
            [print(item.description) for item in working_list[0].animelist]

        elif inp == 'NA':
            create_custom_lists(working_list, 1)

        elif inp == '\r':
            Print().cprint('Press ENTER again to exit: ', 'y', 0, 1)
            if sinp() == '\r':
                sys.exit()

def start():
    author_logo(Terminal().size.x)
    on_start_up()
    menu()

def main():
    if __name__ == '__main__':
        start()

main()   
