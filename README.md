# ShokiMore
Comparing anime lists from shikimori.one (BETA)
# Loading lists from shikimore.one
Anime lists can be loaded directly from the website, user data will be loaded as json file, common data will be loaded from API using links from json file.
Enter a nickname of the user to start data loading.<br />
! Data will not be loaded if lists are marked as private on user's account !<br />
A nickname of the user will be used as the name of the list later on.
# Loading lists from local files
There is an option to store loaded lists locally.<br />
They will be located in the folder named ShokiMore in the same directory as where the program is stored.<br />
Local lists get the nickname of the user as a name, if there are more than 1 user with simmilar name, then figures 1 - amount of files will be used after a nickname.<br />
However, date and time when the file was created will be stored in the file itself, they will appear as: 'nickname Created at date' in the programm afterwards<br />
# Comparing lists
Local lists can not be compared with lists loaded from the website.<br />
There is two options to compare:<br />
1. Merges search<br />
Script will search all identical items (using IDs) in the lists loaded to search function.<br /><br />
2. Difference search<br />
To search titles, that appear in list A but don't appear in list B, use difference search for lists A B, then pick user B (To find an area of Not B)<br />
Difference search for lists A B, then pick user A (To find an area of Not A)<br />
Or pick the last avaliable option, then it will work as an opposite to Merges search (Not A and Not B)<br />
Similarly it can be used for 3 or more users.
# Windows & Linux
File storage functions will work only on windows, however everything else works on linux as well.
# requirements.txt
Beautiful Soup is required
# .exe
There is a compiled version of this program.

 
