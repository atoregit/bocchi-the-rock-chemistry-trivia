# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define bocchi = Character("Hitori Gotoh")

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg pisay
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "..."

    "Sitting on the steps of the quadrangle, I take a deep breath."

    "Me" "It's been a week, huh?"

    "Probably from the exhaustion, my eyes start to gaze at the sky."

    "I sit there in silence for a while."

    "However, as if to disturb my quick meditation session, something appears behind my back."

    "???" "Huh? O-oh!"

    "???" "H-Hey...you over there!"

    scene bg pisay 2
    show bocchi3

    "Hitori" "M-my name's H-Hitori..."

    "Me" "Hey.. who are yo-"

    bocchi "Hitori Gotoh! If you want... you can also call me Bocchi!"

    hide bocchi3
    show bocchi2
    
    bocchi "Um...W-would you like to p-participate in this q-quick Chemistry quiz?"

    menu: 

        "No thanks.":
            jump wrong0
        
        "Sure thing! :))))))))))))":
            jump correct0


label wrong0:

    bocchi "Oh. Okay then! *gunshot*"

    with vpunch

    e "YOU DIED"

    return

label correct0:
    

    bocchi "Yay! I promise it'll be worth your time!"

    bocchi "Here we go, question number 1!"

    "Me" "Wait, we're starting no-" 

    hide bocchi2
    show bocchi1

    bocchi "What are the parts of an atom?"

    menu:

        "Mitochrondria, Nucleus, Stratum Basale":
            jump wrong1

        "Proton, Neutron, Electron":
            jump correct1 

label wrong1:

    bocchi "Wrong! Report to Sir Gian tomorrow."

    e "crash game hehe"

    return


label correct1:

    bocchi "R-Right! Let's move on to the next question!"

    bocchi "What is the third element of the periodic table?"

    menu:

        "Lithium":
            jump correct2

        "Diamond":
            jump wrong1
        
label correct2: 
    bocchi "Nice one! Let's go to question number 3."
 
    bocchi "What is the charge of an electron?"

    menu:
        "+1":
            jump wrong1

        "-1":
            jump correct3

label correct3:

    hide bocchi1
    show bocchi2

    bocchi "Sugoi! Let's go the next question!"

    hide bocchi2
    show bocchi1

    bocchi "How many electrons do atoms want in their valence shell, according to the Octet Rule?"

    menu:
        "69e-2":
            jump wrong1

        "Dyll Marc Valdez":
            jump wrong2

        "Eight":
            jump correct4

label wrong2:

    bocchi "What? That doesn't even make sense."

    e "Who the hell is Dyll Marc Valdez?"

    return

label correct4:
    
    bocchi "OMGGGGGGGGGGG! WHAT A PRO!"

    hide bocchi1
    show bocchi2

    bocchi "Next one! I think you're getting the hand of this!"

    hide bocchi2
    show bocchi1



    bocchi "Consider the hypothetical chemical compound polyhexamethylenebiguanide hydrochloride (PHMB), which is used as a disinfectant and has a molecular formula of C₃H₁₂N₄Cl₃."
    bocchi "Assuming PHMB exists as a complex mixture of oligomers and monomers in solution, with an average molecular weight of 40,000 g/mol, and a degree of polymerization of approximately 200, calculate the concentration of PHMB in a solution that has a pH of 7.5 and a molarity of 0.1. Additionally, assume that the PHMB molecules form positively charged quaternary ammonium groups in solution, which can undergo electrostatic interactions with negatively charged surfaces."
    bocchi "Using the Henderson-Hasselbalch equation and the Nernst equation, calculate the fraction of PHMB monomers and oligomers that are present in the solution at pH 7.5, and the electrostatic potential of the PHMB molecule at the surface of a negatively charged silica particle (with a zeta potential of -30 mV) in the same solution, assuming a temperature of 25°C and an ionic strength of 0.1 M."
    

    menu:
        "At least 1":
            jump correct5
        "Huh?":
            jump wrong3
        "Huh?":
            jump wrong3
        "Huh?":
            jump wrong3

label wrong3:

    bocchi "Too bad! Try answering the question next time :-)"

    e "I actually dk the answer of the question"

    return

label correct5:
    
    bocchi "You're really a chemistry genius! I can't believe someone answered it correctly!"

    "Me" "Y-yeah.."

    bocchi "Let's answer some chem history now!"

    bocchi "What famous chemist is known for developing the periodic table of elements?"

    menu:
        "Dmitri Mendeleev":
            jump correct6
        "Niels Bohr":
            jump wrong3
        "Werner Heisenberg":
            jump wrong1

label correct6:
    
    bocchi "W-Well done!"

    bocchi "What type of bonding involves a sea of electrons?"

    menu:
        "Ionic":
            jump wrong4
        "Metallic":
            jump correct7
        "Covalent":
            jump wrong4

label correct7:
    
    bocchi "Nice."

    bocchi "Who created the atomic bomb?"

    menu:
        "Orsic Paman":
            jump wrong4
        "Oppenheimer":
            jump correct8
        "Opiso":
            jump wrong4

label wrong4:
    
    bocchi "Too bad!"

    bocchi "lol"

    e "CRASHHH"

    return

label correct8:
    
    bocchi "Stupendous!"

    bocchi "Which of the following has the most basic structure among the choices?"

    menu:
        "Titin":
            jump wrong4
        "Electron":
            jump correct9

label correct9:
    
    bocchi "Impressive.."

    bocchi "This is the 10th question! Good luck.."

    label correct95:
        bocchi "If I had a rough night out and wanted to forget everything the day after, what medicine should I take?"
        menu:
            "Exelon":
                jump wrong5
            "Aricept":
                jump wrong5
            "Benzodiazepines":
                jump correct10

label wrong5: 
    bocchi "Let's give you another chance! I think you just mispressed the answer or something, haha"

    jump correct95

label correct10:

    bocchi "You've now advanced to the Hard Level!"

    bocchi "Moving on.."

    bocchi "The Avogadro Constant is..."

    menu:
        "6.02214076 × 10^23 mol^-1":
            jump correct11
        "3.14":
            jump wrong1
        "0":
            jump wrong1

label correct11:
    bocchi "I can't believe this..."

    bocchi "Let's go to the next question! You're like the Albert Einstein of Chemistry!"

    bocchi "What does the R mean in PV = nRT?"

    menu:
        "Rizz Constant":
            jump wrong1
        "Rhyss Constant":
            jump wrong1
        "Natural Gas Constant":
            jump wrong1
        "Revyel Constant":
            jump wrong1
        "Ideal Gas Constant":
            jump correct12
        "The Rodriguez Constant":
            jump wrong1
        "Rodriguez's Gas Constant":
            jump wrong1
        "Rodolfo Crizz Constant":
            jump wrong1
        "Real Gas Constant":
            jump wrong1
        "Ramer the Gamer Constant":
            jump wrong1

label correct12:
    bocchi "You somehow managed to answer that! Well done!"

    bocchi "Next question... I think you need a periodic table for this one!~"

    bocchi "The isotope Cr–53 is produced by the beta decay of which of the following:"

    menu:
        "53Mn":
            jump wrong6
        "54V":
            jump wrong6
        "52Cr":
            jump wrong6
        "53V":
            jump correct13
        "54Cr":
            jump wrong6
            
label wrong6:
    bocchi "Oops! Let's give that another try!"

    jump correct135

label correct13:
    bocchi "Very good! I wish I was that smart..."

    bocchi "Let's go to the next question!"

    label correct135:

        bocchi "When a voltaic cell reaches equilibrium, what happens?"

        menu:
            "E= 0":
                jump wrong6
            "Ecell = 0":
                jump correct14
            "Ecell = K":
                jump wrong6
            "E= K":
                jump wrong6
            "Ecell = Q":
                jump wrong6


label correct14:
    bocchi "Great! By now it's obvious that you're passionate about chemistry!"

    bocchi "Next question..."

    label correct145:

        bocchi "Which of the following is a double-ring nitrogenous base?"

        menu:
            "Thymine":
                jump wrong6
            "Cytosine":
                jump wrong6
            "Guanine":
                jump correct15
            "Ribose":
                jump wrong6
            "Adenine":
                jump wrong6

label wrong7:
    bocchi "Oops! Let's give that another try!"

    jump correct145

label correct15:
    bocchi "Amazing!"

    bocchi "Keep up the good work! We're nearing the end of the quiz!"
    
    bocchi "What is the electron domain geometry of sulfur hexafluoride?"

    menu:
        "Circle":
            jump wrong6
        "Octahedral":
            jump correct16
        "Popeye's Chicken Sandwich":
            jump wrong6

label correct16:
    bocchi "Good job!"

    bocchi "This is the final question in my super amazing Chemistry Trivia Game."

    bocchi "Let's end this quiz with my most difficult question... heheheh"

    bocchi "I wonder how a mere PSHS student can answer this impossible question."

    bocchi "Are you ready?????"

    menu:
        "Okay, I guess?":
            jump preend
        "nah not rlly":
            e "Okay"

label preend:
    bocchi "What is the boiling point of water?"

    menu:
        "100 C":
            jump ending
        "212 F":
            bocchi "{cps=20}AMERICAN DETECTED. ELIMINATION STARTS IN {/cps}{cps=4}3...2...1...e{/cps}{nw}"
            e "dreaded e. you pizza eating mcdonalds grubbing patriot"

label ending: 
    bocchi "Now this ends the chemistry trivia!"

    hide bocchi1
    show bocchi2
    bocchi "T-thank you so much for participating!"
    hide bocchi2
    show bocchi1

    bocchi "See you! Bocchi's gonna go back to the cardboard box in the closet and play guitar. Bye, bye~"

    "I lay myself on the quadrangle stairs again, as the girl slowly disappears from my sight."

    "Maybe I really was.. the rock of her Bocchi."

    return

