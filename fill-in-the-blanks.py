def fill_in_the_blanks():
    """ INPUTS: NONE
    OUTPUTS:
    1. The user is asked for a level of difficulty.
    2. The user is presented with the full script and asked for the word that would fit the blank
    2.1 If incorrect, the user will get up to 5 tries per word
    2.2 If correct, the user moves on to the next blank
    3. Once all blanks are complete > Success :)"""
    
    ### SCRIPTS ###
    scripts = [
    '''
One of the greatest pleasures of life is ___1___ . 
Listening to a beautiful ___2___ can cause a wide range of positive reactions. Your teeth peek out as you ___3___. You can feel the pendulum swing in your ___4___.  And sometimes, you'll even get chills!

Whithout ___1___, our human experience would be severely handicaped. Imagine how many ___2___s we won't get a chance to listen to. How many ___3___ you'll forgo. How your ___4___ won't dance.

If you've had a tough day, remember that at least we have ___1___.
    ''',
        
    ''' 
Chipotle is an amazing place to grab someting to ___1___, regardless of the bad press. 
On an almost daily basis I order a ___2___ bowl with white rice. One of the main features of Chipotle is it's handmade ___3___ made from fresh avocados. 
Finally, don't forget to grab some ___4___. They're homemade, sparkled with salt and lemon - pure goodness.
    ''',
        
    '''
Imagine we could build the time-travel ___1___, but was really hard to use. 

Some ___2___ would be hidding; plus activating them wouldn't give you ___3___ to know that the command has been received. 
Also, a few of these ___2___ can do several actions depending on the mode. Causing you to do something you didn't intend to do. 
Most importantly, the ___1___ makes errors irreversible...

Would we want to create this ___1____ after all?
    
The principles of good ___4___ are just as important (if not more) than the potential usefulness of a device
    ''']
    
    ### SOLUTIONS ###
    sol = [
        ['music', 'song', 'smile', 'body'],
        ['eat','burrito','guacamole','chips'],
        ['machine','buttons','feedback','design']
    ]
    
    blanks = [
        '___1___',
        '___2___',
        '___3___',
        '___4___'
        ]

    diff = ""

    possible_diff = ['easy','medium','hard']
    
    ### Dictionary for difficulty:script pairs ###
    diff_dict = {}
    for item in range(len(possible_diff)):
        diff_dict[possible_diff[item]] = scripts[item]
    
    ### Dictionary for all difficulty + blanks:solution pairs ###
    sol_dict = {}
    for item in range(len(possible_diff)):
        sol_dict[possible_diff[item]] = {}
        for pos in range(len(blanks)):
            sol_dict[possible_diff[item]][blanks[pos]] = sol[item][pos]
    
    while diff not in possible_diff:
        diff = raw_input("please enter a difficulty level: 'easy', 'medium' or 'hard'").lower()
    
    print ""
    print "-" *100
    print diff_dict[diff]
    
    
    for pos in range(len(blanks)):
        number_of_tries = 5
        guess = ""
        print"number of tries left: " + str(number_of_tries)
        while guess != sol_dict[diff][blanks[pos]]:
            guess = raw_input("what is " + blanks[pos] + "?  ").lower()
            if guess == sol_dict[diff][blanks[pos]]:
                diff_dict[diff] = diff_dict[diff].replace(blanks[pos],sol_dict[diff][blanks[pos]])
                print "CORRECT!"
                print ""
                print "-" *100
                print diff_dict[diff]
                break
            else:
                number_of_tries -= 1
                print "number of tries left: " + str(number_of_tries)
                if number_of_tries < 1:
                    return "GAME OVER - Try Again."
    return "YOU WON!!!"

fill_in_the_blanks()