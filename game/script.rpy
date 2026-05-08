
# Image definitions are here.
image bg start = "images/backgrounds/bg start.png"

# The game starts here.

label start:

    scene bg start
    with dissolve

    "In Club Room 215 of \[Insert School Name Here\], there is a group of super fans for {b}{i}Jack Griffin & The Coven Girls{/i}{/b} that were meeting for the final time of the school year."
    
    "Since classes were officially over for the year, and summer was just around the corner, they had all chipped in some funds to secure passes to a month long cruise!"

    "Little would they know that going on that cruise would be the most insane trip they'd take of their lives…"

    ls "Well everyone, looks like we made it JUST in time!"

    s "Did we? Are passes secured"

    "Lysanndra looks at the laptop screen she's been staring at for who knows how long at this point."

    "She double checked the receipt page on the cruise line's site, and checked her email to make sure she had gotten confirmation. She sighed when she saw said confirmation in her inbox."

    ls "Yup, we sure did! Cruise passes are confirmed!"

    "Everyone breathed a sigh of relief, including myself!"

    call choice_1
        
    pm "Well, the important thing is that they're secured. So when and where do we need to meet?"

    ls "The cruise ships on June 11th. That's Nigella Davenport's Birthday!"

    pm "You memorized her birthday?!"

    ls "Well, we all do. At least, I do."

    pm "Just promise me you don't do that thing where you call off your life to celebrate."

    ls "Uhhh... No? Who does that?"

    pm "I'll tell you later."

    return
# Option 1 labels
label choice_1:
    menu:
        "Choose a response..."
        "Oh, Thank God!":
            #block of code to run
            jump nice_response_1 
        "You Better Have gotten them,,,":
            #block of code to run
            jump rude_response_1

label nice_response_1:
    ls "I know! It was stressing me out!"
return

label rude_response_1:
    ls "Uuh, I know I did. I'm looking at my screen..."
return