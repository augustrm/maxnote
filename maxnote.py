from datetime import datetime
from textwrap import fill
from os import system
from hashlib import blake2b
loop = True
today = input("Note filename?\n>>> ")+".txt"
notelog = open(today, "a+")
note_number=0
lineline = "\n"+ "-"*80 +"\n"
poundline = "\n"+"#"*80 +"\n"
tildeline = "\n"+"~"*80 +"\n"
notelog.write("#"*80+"\n"+"::-BEGIN SESSION-::\n")
while loop == True:
	note_number+=1
	_who = input("\nWho?\n>>> ") +"\t"
	_when = input("\nWhen? (leave blank for current time)\n>>> ")
	if _when == "":
		_when = str(datetime.now())
	_when = _when+"\n"
	_contact_info = input("\nContact Information?\n>>> ")+"\n"
	_what = ">>> "+input("\nWhat?\n>>> ")
	_what = fill(_what, subsequent_indent="\t")
	note_text = "Note #"+str(note_number)+"\n"+"TimeStamp::"+ "["+str(datetime.now())+"]"+lineline+ _who + _when + _contact_info + _what +"\n\n"
	notelog.write(note_text)
	hashstamp = blake2b()
	hashstamp.update(bytes(note_text, 'utf-8'))
	notelog.write("HashStamp::["+hashstamp.hexdigest()+"]"+tildeline)
	hashstamp=None
	stop_condition = input("\nAnother Note? [Y/n]\n>>> ")
	system('cls||clear')
	if stop_condition == 'n' or stop_condition == 'N':
		loop = False
session_hashstamp = blake2b()
session_hashstamp.update(bytes(notelog.read(), 'utf-8')) #This ensures the WHOLE of the notelog, not just a single session is verified as integral by hash 
notelog.write("||-END SESSION-||"+"\nSESSION HASHSTAMP::["+session_hashstamp.hexdigest()+"]" + poundline+"\n")
notelog.close()