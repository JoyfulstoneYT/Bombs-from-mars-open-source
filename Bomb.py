phone = 'no'
game_start = 'yes'

while game_start == 'yes':
  print('TV: THE WORLD IS ABOUT TO END. THE LARGEST ATOMIC BOMB KNOWN TO MAN IS GOING TO BE LAUNCHED TO EARTH, NOW THAT THE MARTIANS HAVE FOUND US. FIND THE NEAREST BUNKER IMMIDIENTLY. MOVE FAST, BECAUSE THE BOMB WILL HIT IN 20 MINUTES! (Ok, so there is a bomb. I guess we should not have started a war against another planet, but that is the fault of some leader or something. You never have payed attention to the news latley, or at all... Anways here are your options:')
  answer_1 = input('Stay or Leave? ')
  if answer_1 == 'Stay':
    print('You stay put. Weird choice, you have 20 minutes to do something and decide to do nothing. The bomb comes and you die. You got the "Stupid" ending. RESTARTING SIMULATION:') 
  else:
    print('Ok, you decide to leave then.')
    print('You go to your Neighbors home and knock. Somebody, who is drunken, exits the door and yells at you. Maybe you should tell them what is going on?')
    answer_3 = input('Explain or Run')
    if answer_3 == 'Explain':
      print('You tell them about the Bomb, and show them the brodcast. You both escaped. You got the "Helpful" ending. RESTARTING SIMULATION:')
    if answer_3 == 'Run':
     print('You run away and leave your Neighbor for dead. You got the "Sole Survivor" ending. RESTARTING SIMULATION:')
  