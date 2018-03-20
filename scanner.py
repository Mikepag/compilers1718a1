#http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python



#opening external file to save LOG
logfile = open("log_file.txt", "w")


def getchar(words,pos):
	""" returns char at pos of words, or None if out of bounds """

	if pos<0 or pos>=len(words): return None

	return words[pos]
	

def scan(text,transition_table,accept_states):
	""" Scans `text` while transitions exist in 'transition_table'.
	After that, if in a state belonging to `accept_states`,
	returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	pos = 0
	state = 'q0'
	
	while True:
		
		c = getchar(text,pos)	# get next char
		
		if state in transition_table and c in transition_table[state]:
		
			state = transition_table[state][c]	# set new state
			pos += 1	# advance to next char
			
		else:	# no transition found

			# check if current state is accepting
			if state in accept_states:
				return accept_states[state],pos

			# current state is not accepting
			return 'ERROR_TOKEN',pos
			
	
# the transition table, as a dictionary

# Αντικαταστήστε με το δικό σας λεξικό μεταβάσεων...
td = { 'q0':{ '0':'q1', '1':'q1', '2':'q6', '3':'q2', '4':'q2', '5':'q2', '6':'q2', '7':'q2', '8':'q2', '9':'q2' },
       'q1':{ '0':'q2', '1':'q2', '2':'q2', '3':'q2', '4':'q2', '5':'q2', '6':'q2', '7':'q2', '8':'q2', '.':'q3', ':':'q3' },
       'q2':{ '.':'q3', ':':'q3' },
       'q3':{ '0':'q4', '1':'q4', '2':'q4', '3':'q4', '4':'q4', '5':'q4'},
       'q4':{ '0':'q5', '1':'q5', '2':'q5', '3':'q5', '4':'q5', '5':'q5', '6':'q5', '7':'q5', '8':'q5', '9':'q5' },
       'q6':{ '0':'q2', '1':'q2', '2':'q2', '3':'q2', '.':'q3', ':':'q3' }
     } 

# the dictionary of accepting states and their
# corresponding token

# Αντικαταστήστε με το δικό σας λεξικό καταστάσεων αποδοχής...
ad = { 'q5':'TIME_TOKEN' }


# get a string from input
text = input('give some input>')
logfile.write(text + "\n")


# scan text until no more input
while text:	# that is, while len(text)>0
	
	# get next token and position after last char recognized
	token,position = scan(text,td,ad)
	
	if token=='ERROR_TOKEN':
		print('unrecognized input at pos',position+1,'of',text)
		logfile.write('unrecognized input at pos ' + position+1 + 'of ' + text)

		break
	

	print("token:",token,"string:",text[:position])
	logfile.write("token: " + token + " string: " + text[:position] + "\n")

	# remaining text for next scan
	text = text[position:]


logfile.close()
	
