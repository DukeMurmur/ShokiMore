# ShokiMore
Comparing anime lists from shikimori.one
# Loading lists from shikimore.one
Anime lists can be loaded directly from the website, user data will be loaded as json file, common data will be loaded from API using links from json file.
Enter a nickname of the user to start data loading.<br />
! Data will not be loaded if lists are marked as private on user's account !<br />
A nickname of the user will be used as the name of the list later on.
# Loading lists from local files
There is an option to store loaded lists locally.<br />
They will be located in the folder named ShokiMore_Data in the same directory as where the program is stored.<br />
# Comparing lists
There is two options to compare:<br />
Merges search<br />
Script will search all identical items (using IDs) in the lists loaded through search function.<br /><br />
Difference search<br />
There are several options to search differences in lists:<br />
(As an example, a list of 4 users A B C D will be used)<br /><br />
1. Search titles that are either in list A or B or C or D<br />
2. Search titles that are either in both lists AB or AC or AD or BC or BD or CD<br />
3. Search titles that are either in ABC or ABD or ACD or BCD<br />
4. Search titles that are in all 4 lists<br />
5. Search titles that are less than in 4 lists<br />
<br />
The last available option will always be less than total amount of lists.<br />
Number of lists junctions will be printed next to each option<br />
<br />
There also can be a reference user picked in the beginning, to exclude everything that is on his/her list<br />
<br />
# requirements.txt
Requirements are available in requirements.txt file
# .exe
There is a compiled version of this program.

 
