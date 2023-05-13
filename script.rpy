# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define bocchi = Character("Hitori Gotou")


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

    bocchi "M-my name's H-Hitori... Hitori Gotou!"

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

    "Wrong! Report to Sir Gian tomorrow."

    e "crash game hehe"

    return


label correct1:

    bocchi "R-Right! Let's m-m  ove on to the next question!"

    bocchi "What is the third element of the periodic table?"

    menu:

        "Lithium":
            jump correct2

        "Diamond":
            jump wrong1
        
label correct2: 
    bocchi "N-nice one! L-Let's go to question number 3."
 
    bocchi "What is the charge of an electron?"

    menu:
        "+1":
            jump wrong1

        "-1":
            jump correct3

        "At least 4":
            jump wrong1

label correct3:

    hide bocchi1
    show bocchi2

    bocchi "Wow! S-Sugoi!"

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
        "Huh?":
            return
        "Huh?":
            return
        "Huh?":
            return