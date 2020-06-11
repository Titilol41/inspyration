import PySimpleGUI as sg
from random import choice, randint

qualities = [
"honest", "loyal", "respectful", "responsible", "passionate", "fair",
"forgiving", "authentic", "brave", "generous", "persevering", "polite", "kind",
"loving", "optimistic", "disciplined", "ambitious", "encouraging", "calm", "adventurous",
"cheerful", "affectionate", "bright", "creative", "dynamic", "friendly", "funny"
"gentle", "genuine", "helpful", "humble" "insightful", "mature", "patient",
"persuasive", "powerful", "relaxed", "romantic", "sociable", "tolerant", "wise"
]

flaws = [
"obsessed", "cruel", "manipulative", "selfish", "jealous", "abusive",
"dishonest", "envious", "erratic", "flirty", "gluttonous", "humourless",
"hypocritical", "idealist", "immature", "impatient", "indecisive", "judgemental",
"lewd", "naïve", "overemotional", "overambitious", "perfectionist", "reckless",
"remorseless", "timid", "untrustworthy", "lustful", "agressive",
"lazy", "arrogant", "boring", "careless", "cold", "desperate", "forgetful",
"greedy", "guillible", "harsh", "hateful", "hostile", "killjoy", "mean",
"nasty", "narrow-minded", "paranoid", "pessimistic", "procrastinating",
"rigid", "rude", "stupid", "uncaring", "withdrawn", "shameless"
]

colors = [
"yellow", "green", "blue", "purple", "brown", "red", "pink", "orange",
"cherry", "banana", "coconut", "lime", "pumpkin", "space", "strawberry",
"peach", "sunset", "pastel", "rainbow", "lemonade", "turquoise",
"teal", "crimson", "blood", "nature", "mint"
]

def traits_list():
    if randint(0, 1) == 0:
        return [choice(qualities), choice(flaws)]
    else:
        return[choice(flaws), choice(qualities)]

def character_popup(theme_specific, colors, generated):
    sg.popup("Your generated character concept is...",
        "{}, with a(n) {} theme, most of the times {}, but sometimes {}!".format(
            choice(theme_specific), choice(colors), generated[0], generated[1])
            )


sg.theme('Dark Teal 4')

layout = [[sg.Text('Choose what to generate...')],
          [sg.Text("Actions:")],
          [sg.Button("Action", size=(10, 2)), sg.Button("Interaction", size=(10,2))],
          [sg.Text("Characters:")],
          [sg.Button("Modern", size=(10, 1)), sg.Button("Fantasy", size=(10,1))],
          [sg.Button("Superhero", size=(10, 1)), sg.Button("Furry", size=(10,1))],
          [sg.Text("by beltza~")],
          [sg.Text("original prompts list on https://salison.tumblr.com/")]]

window = sg.Window('inspyration', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == "Action":
        generated = choice([
            "Jumping", "Falling", "Sitting", "Talking", "Walking",
            "Eating", "Drinking", "Thinking", "Singing", "Crying",
            "Searching", "Reaching", "Climbing", "Searching", "Reaching",
            "Climbing", "Sleeping", "Shopping", "Swimming", "Carrying",
            "Cheering", "Hugging", "High-fiving", "Fighting", "Hula hooping",
            "Lecturing", "Whispering", "Shouting", "Laughing", "Throwing",
            "Catching", "Cooking", "Cleaning", "Examining", "Giving", "Taking",
            "Calling (to someone, on the phone", "Listening to music",
            "Playing a musical instrument", "Petting an animal", "Shooting"
            "Putting on clothes", "Reading", "Watching (people, tv, movies)",
            "Knitting", "Blocking (someone, something)", "Dancing",
            "Bumping (into someone, something)", "Hanging (upside down, on a cliff)",
            "Posing", "Bowing", "Waiting", "Clapping", "Kicking", "Punching",
            "Doing Yoga", "Gathering", "Fishing", "Gardening", "Cycling",
            "Piggyback riding", "Bug catching", "Ghost hunting", "Yo-yoing",
            "Swinging on swings", "Snowball fighting", "Juggling", "Playing ping pong",
            "Raking leaves", "Ice skating", "Playing video games", "Horseback riding",
            "Kissing", "Vomiting", "Web surfing", "Taking pictures", "Handstanding",
            "Kite flying", "Running", "Showing", "Pushing", "Pulling", "Sewing",
            "Writing", "Sneaking", "Holding (flowers, hands)", "Balancing",
            "Fingernail painting", "Tying (tie, bandage, bow)", "Pointing",
            "Crawling", "Playing poker", "Stabbing", "Driving", "Brushing teeth"
            "Stacking (books, cards)", "Drawing", "Dropping something",
            "Picking something up", "Fixing something", "Exercising", "Streching",
            "Stargazing"
        ])
        sg.popup("Your generated prompt is to draw your character...",
        generated + "!")
    if event == "Interaction":
        generated = choice([
            "Racing each other", "Arguing with each other", "Walking together",
            "Hugging each other", "Eating together", "Taking a photo together",
            "Shopping together", "Laughing together", "High-fiving each other",
            "Dancing together", "Watching a movie together", "Singing together",
            "Playing charades together", "Reading together", "Waiting together",
            "Staring at each other", "Exercising together", "Napping together",
            "Texting each other", "Playing catch together", "Baking a cake together",
            "Cleaning together", "Playing leapfrog together", "Sharing an umbrella",
            "Playing rock-paper-scissors", "Comparing heights with each other",
            "Playing tug-of-war with each other", "Shaking hands with each other",
            "Playing a sport together", "Panicking together", "Studying together",
            "Playing video games together", "Cooking together",
            "Putting a jigsaw puzzle together", "Playing hide-and-seek together",
            "Playing tag with each other", "Wrestling each other", "Rowing a boat together",
            "Pushing something together", "Pulling something together",
            "Lifting something together", "Building something together", "Crying together",
            "One laughing at the other", "One comforting the other", "One bandaging the other",
            "One carryig the other", "One supporting the other", "One begging the other",
            "One helping the other", "One pouring the other a drink",
            "One feeding the other", "One throwing something at the other",
            "One pushing the other", "One pulling the other", "One dragging the other",
            "One watching the other", "One sitting on the other",
            "One giving a piggy back ride to the other", "One putting makeup on the other",
            "One dumping water on the other", "One taking a photo of the other",
            "One leaning on the other", "One holding the other up", "One holding the other back",
            "One helping the other up", "One washing dishes, other drying",
            "One on a swing, other pushing them", "One scaring the other",
            "One falling, other catching them", "One jumping over the other",
            "One getting the other's attention", "One judging the other",
            "One fixing the other's appearance", "One hiding behind the other",
            "One teaching the other", "One surprising the other", "One pranking the other",
            "One blocking the other", "One clinging to the other", "One lecturing the other",
            "One driving, other passenger", "One drawing the other", "One slapping the other",
            "One giving a gift to the other", "One chasing the other", "One punching the other",
            "One kicking the other", "One listening to the other", "One holding the other",
            "One singing to the other", "One sharing with the other", "One stealing from the other",
            "One whispering to the other", "One tackling the other", "One ignoring the other",
            "One poking the other", "One kissing the other", "One protecting the other",
            "One mimicking the other"
        ])
        sg.popup("Your generated prompt is to draw two characters...",
        generated + "!")
    if event == "Modern":
        theme_specific = [
            "A highschool girl", "A student", "A kindergarten teacher", "A teenager", "A gamer", "A scientist",
            "A doctor", "A reporter", "A priest", "An electrician", "A clown", "A gardener",
            "A housekeeper", "A builder", "A waiter", "An engineer", "A sportsman", "A cameraman",
            "A barman", "A postman", "A policeman", "A highschool student", "An aspiring singer",
            "An artist", "An edgy kid", "A writer" "A weeb", "A middle-school student", "An aspiring magician",
            "A dancer"
        ]
        generated = traits_list()
        character_popup(theme_specific, colors, generated)
    if event == "Fantasy":
        theme_specific = [
            "A barbarian", "A bard", "A cleric", "A druid", "A fighter",
            "A monk", "A paladin", "A ranger", "A rogue", "A sorcerer",
            "A warlock", "A wizard"
        ]
        generated = traits_list()
        character_popup(theme_specific, colors, generated)
    if event == "Superhero":
        break
    if event == "Furry":
        break

window.close()