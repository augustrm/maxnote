from datetime import datetime
from textwrap import fill
from os import system, SEEK_END, SEEK_SET
from hashlib import blake2b
loop = True
fl = input("Note filename?\n>>> ")
notelog = open(fl+".txt", "a+")
HTML_nl = open(fl+".HTML", "a+")
if HTML_nl.readline()!="<!DOCTYPE html>\n<html>":
    HTML_nl.write("<!DOCTYPE html>\n<html>")
else:
    # Move the pointer (similar to a cursor in a text editor) to the end of the file
    HTML_nl.seek(0, SEEK_END)

    # This code means the following code skips the very last character in the file -
    # i.e. in the case the last line is null we delete the last line
    # and the penultimate one
    pos = HTML_nl.tell() - 1

    # Read each character in the file one at a time from the penultimate
    # character going backwards, searching for a newline character
    # If we find a new line, exit the search
    while pos > 0 and HTML_nl.read(1) != "\n":
        pos -= 1
        HTML_nl.seek(pos, SEEK_SET)

    # So long as we're not at the start of the file, delete all the characters ahead
    # of this position
    if pos > 0:
        HTML_nl.seek(pos, SEEK_SET)
        HTML_nl.truncate()
note_number=0
lineline = "\n"+ "-"*80 +"\n"
poundline = "\n"+"#"*80 +"\n"
tildeline = "\n"+"~"*80 +"\n"
HTML_lineline = "<br><hr>"
notelog.write("#"*80+"\n"+"::-BEGIN SESSION-::\n")
HTML_nl.write("<body><h2>NOTELOG SESSION</h2>")
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
	HTML_note_text = "<h2 style=\"color:red\">Note #"+str(note_number)+"</h2>"+"TimeStamp::"+ "["+str(datetime.now())+"]"+HTML_lineline+ "<h3>"+_who +"</h3>" + _when+"<br><b>" + _contact_info+"</b><br><br>" + _what +"<br><br>"
	notelog.write(note_text)
	HTML_nl.write(HTML_note_text)
	hashstamp = blake2b()
	hashstamp.update(bytes(note_text, 'utf-8'))
	notelog.write("HashStamp::["+hashstamp.hexdigest()+"]"+tildeline)
	HTML_nl.write("HashStamp::["+hashstamp.hexdigest()+"]"+HTML_lineline)
	hashstamp=None
	stop_condition = input("\nAnother Note? [Y/n]\n>>> ")
	system('cls||clear')
	if stop_condition == 'n' or stop_condition == 'N':
		loop = False
session_hashstamp = blake2b()
session_hashstamp.update(bytes(notelog.read(), 'utf-8')) #This ensures the WHOLE of the notelog, not just a single session is verified as integral by hash 
notelog.write("||-END SESSION-||"+"\nSESSION HASHSTAMP::["+session_hashstamp.hexdigest()+"]" + poundline+"\n")
HTML_nl.write("<h2>END SESSION</h2>"+"\nSESSION HASHSTAMP::["+session_hashstamp.hexdigest()+"]" + "\n<hr><br></body></html>")
notelog.close()
HTML_nl.close()
