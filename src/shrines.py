import itertools
# Obtained from https://diablo2.diablowiki.net/Diablo_I_Shrines
shrines = {
    'Diablo': {
        'Abandoned': 'The hands of men may be guided by fate.',
        'Creepy': 'Strength is bolstered by heavenly faith.',
        'Cryptic': 'Arcane power brings destruction.',
        'Divine': 'Drink and be refreshed.',
        'Eerie': 'Knowledge and wisdom at the cost of self.',
        'Eldritch': 'Crimson and Azure become as the sun.',
        'Enchanted': 'Magic is not always what it seems to be.',
        'Fascinating': 'Intensity comes at the cost of wisdom.',
        'Glimmering': 'Mysteries are revealed in the light of reason.',
        'Gloomy': 'Those who defend seldom attack.',
        'Hidden': 'New strength is forged through destruction.',
        'Holy': 'Wherever you go, there you are.',
        'Imposing': 'A surge of blood interrupts your thoughts.',
        'Magical': 'While the spirit is vigilant the body thrives.',
        'Mysterious': 'Some are weakened as one grows strong.',
        'Ornate': 'Salvation comes at the cost of wisdom.',
        'Quiet': 'The essence of life flows from within.',
        'Religious': 'Time cannot diminish the power of steel.',
        'Sacred': 'Energy comes at the cost of wisdom.',
        'Secluded': 'The way is made clear when viewed from above.',
        'Spiritual': 'Riches abound when least expected.',
        'Spooky': 'Where avarice fails, patience gains rewards.',
        'Another Spooky': 'Blessed by a benevolent companion!',
        'Stone': 'The powers of mana refocused renews.',
        'Tainted': 'Those who are last may yet be first.',
        'Another Tainted': 'Generosity brings its own rewards.',
        'Thaumaturgic': 'What once was opened now is closed.',
        'Weird': 'The sword of justice is swift and sharp.',
    },
    'Hellfire': {
        'Glowing': 'Knowledge is power.',
        'Mendicant': 'Give and you shall receive.',
        "Murphy's": 'That which can break will.',
        'Oily': 'That which does not kill you...',
        'Shimmering': 'Spiritual energy is restored.',
        'Solar': 'You feel stronger.',
        'Another Solar': 'You feel wiser.',
        'Another Solar': 'You feel refreshed.',
        'Another Solar': 'You feel more agile.',
        'Sparkling': 'Some experience is gained by touch.',
        'Town': "There's no place like home.",
    },
    'Beta': {
        'Cryptic': 'Power comes from your disorientation...',
        'Eerie': 'You forget who you are!',
        'Enchanted': 'Did you forget something?',
        'Fascinating': 'You are the powerless master of fire!',
        'Hidden': 'Energy passes through your equipment.',
        'Imposing': 'A surge of blood interrupts your thoughts.',
        'Magical': 'Growling is heard throughout the dungeon.',
        'Mysterious': 'Odd sensations.',
        'Mystic': 'Your skills increase, but at a price.',
        'Spiritual': 'Untold wealth!',
        'Supernatural': 'You hear a strange cry from the distance.',
        'Thaumaturgic': 'You hear a series of creaks and thumps.',
    }
}

flat = [shrines.items() for game, shrines in shrines.items()]
shrines = list(itertools.chain(*flat))

if __name__ == "__main__":
    import random
    _, dictum = random.choice(shrines)
    print(dictum)