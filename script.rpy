# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define bocchi = Character("Hitori Gotoh")


# The game starts here.

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

    "???" "Huh? O-oh!"

    "???" "H-Hey...you over there!"

    show bocchi3
    with fade

    bocchi "M-my name's H-Hitori... Hitori Gotoh!"

    bocchi "Um...W-would you like to p-participate in this q-quick Chemistry quiz?"

    "Me" "What do I get?"

    bocchi "I-I-I promise I'll give you a reward if you get it all right! <3 ;)"

    bocchi "...S-So...Whaddya say?"

    menu: 

        "No thanks.":
            jump wrong0
        
        "Sure thing! :))))))))))))":
            jump correct0

    return

label wrong0:

    bocchi "Oh. Okay then! *gunshot*"

    with vpunch

    e "YOU DIED"

    return

label correct0:

    bocchi "Yay! I promise it'll be worth your time! ;)"

    bocchi "Here we go, question number 1!"

    "Me" "Wait, we're starting no-" 

    hide bocchi3

    show bocchi1


    bocchi "What are the parts of an atom?"

    menu:

        "Mitochrondria, Nucleus, Stratum Basale":
            jump wrong1

        "Proton, Neutron, Electron":
            jump correct1


    # This ends the game.

    return

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

    bocchi "Wow!"

    hide bocchi2
    show bocchi1

    bocchi "How many electrons do atoms want in their valence shell?"

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

    bocchi "I bet you have a Chem grade of 2.50 :)"

    e "CRASHHH"

    return

label correct8:
    
    bocchi "Stupendous!"

    bocchi "I think you need a periodic table for this one."

    bocchi "If 4 neutrons are released during the combination of Iodine-127 and Uranium-235, what atom is created?"

    menu:
        "Unquadquadium-358":
            jump wrong4
        "Unquadpentium-358":
            jump correct9
        "Unquadhexium-358":
            jump wrong4

label correct9:
    
    bocchi "Impressive.."

    bocchi "This is the 10th question! Good luck"

    label correct95:
        bocchi "If I had a rough night out and wanted to forget everything the day after, what drug would I cook?"
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

    bocchi "Let's start with my most difficult question, leaving famous scientists such as Quandale Dingle confused and dazed."

    bocchi "Let's see how a mere PSHS student can answer this impossible question."

    bocchi "What is the boiling point of water?"

    menu:
        "100 C":
            jump correct11
        "212 F":
            bocchi "{cps=20}AMERICAN DETECTED. ELIMINATION STARTS IN {/cps}{cps=4}3...2...1...e{/cps}{nw}"
            e "dreaded e. you pizza eating mcdonalds grubbing patriot"
        "373.15 K":
            jump correct11

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

    bocchi "Next question..."

    bocchi "Which of the following has the most basic structure among the choices?"

    menu:
        "Methane":
            jump wrong6
        "Carbon":
            jump wrong6
        "Titin":
            jump wrong6
        "Electron":
            jump correct13
        "Proton":
            jump wrong6
            
label wrong6:
    bocchi "Wrong! Report to Sir Kier tomorrow."

    e "hii"

label correct13:
    bocchi "-"

    bocchi "Next question..."

    bocchi "Which of the following structures have                    ?"

    menu:
        "Methane":
            jump wrong6
        "Carbon":
            jump wrong6
        "Titin":
            jump wrong6
        "Electron":
            jump correct14
        "Proton":
            jump wrong6

label correct14:
    bocchi "You somehow managed to answer that! Well done!"

    bocchi "Next question..."

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


label correct15:
    bocchi "Amazing!"

    bocchi "Keep up the good work! We're nearing the end of the quiz!"
    
    bocchi "What is the electron domain geometry of sulfur hexafluoride?"

    menu:
        "Square pyramidal":
            jump wrong6
        "Octahedral":
            jump correct15
        "Linear":
            jump wrong6

