bad_choose = 'Wrong answer, choose the words provided'

print('Interactive Stories')
print()
print('''Choose your history:\n
A. Exit in the forest\n
B. The donkey and the lion''')
print()

lista = ['A. Exit in the forest', 'B. The donkey and the lion']
history = input('Choose your story A or B: ')

if history == 'A' or history == 'a':
    print('The chosen story is: ')
    print(lista [0])
    print()
    print("Let's go!")

    print('You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT.')
    tool = input('Which one do you want to pick up? ')
    tool = tool.lower()
    if tool == 'match':
        print()
        print('''You pick up the match and strike it, and for an instant, the forest around you is illuminated.
You see a large grizzly bear, and then the match burns out.''')

        action1 = input('Do you want to RUN, or HIDE behind a tree? ')
        action1 = action1.lower()
        if action1 == 'hide':
            print()
            print('''The longest minutes of your life ran, you felt the sounds of the bear getting closer and closer but
after a few minutes you began to feel that it was moving away, after a couple of minutes you continued
on your way without any further problems while you decide whether to go to TOWN or you come HOME.''')
            action2 = input('Do you want to go to TOWN or return HOME? ')
            action2 = action2.lower()
            if action2 == 'town':
                print("You arrive at the town without trouble and you go to your friend Joe's house to have a good time.")
                exit()
        
            elif action2 == 'home':
                print('You return home to find your family almost ready for dinner.')
                exit()
            else:
                print(bad_choose)
        if action1 == 'run':
            print('''You start to run but unfortunately the bear hears you and begins to run after you, soon you begin to
feel that the bear is getting closer and you are aware of the inevitable, the bear catches up with you
and despite your efforts to free yourself from it you die.''')
            exit()
        else:
            print(bad_choose)
            
    if tool == 'flashlight':
        print('''You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought
you also heard something off to the side.''')

        action3 = input('Do you want to FOLLOW the path, take your PHONE and ask for help or LOOK in the trees for what made the noise? ')
        action3 = action3.lower()
        if action3 == 'follow':
            print('''Without making much noise, you take the path that is in front of you and you turn on the flashlight
in some sections of the route to make sure that there are no dangers.''')
        
        elif action3 == 'phone':
            print('''You take your phone and call 911, they immediately contact the forest ranger service
and after a while they come for you.''')

        elif action3 == 'look':
            print('''You pick up the flashlight and turn it on, and for an instant, the forest around you lights up.
You see a large grizzly bear starting to see you.''')
            action4 = input('What do you do? Do you FACE the bear or THINK what to do? ')
            action4 = action4.lower()
            if action4 == 'face':
                print('''You start to raise your hands and scream desperately while you move the flashlight.
Surprisingly the bear gets scared and runs away.''')
            elif action4 == 'think':
                print('''You quickly remember a TV show where they talked about bear attacks.
You remember that you should not make sudden movements, or do anything that the animal feels threatened.
Very slowly you immediately begin to back away from danger.''')
            else:
                print(bad_choose)
        else:
                print(bad_choose)
    else:
        print(bad_choose)

elif history == 'B' or history == 'b':
    print('The chosen story is: ')
    print(lista[1])
    print()
    print("Let's go!")

    print('Once upon a time there was a very angry donkey, who did not know who to ask for wise advice.')
    action5 = input('Do you want to ask the KING of the Jungle or the old ELEFHANT for advice? ')
    action5 = action5.lower()
    if action5 == 'king':
        print('''The donkey in the presence of the king told him: no one respects me or fears me (the donkey cried).
Teach me to Roar like you. He would thus make men and beasts flee.''')
        print('''Listening to him carefully and having much more important matters in the kingdom, I didn't know
whether to spend more TIME on him or just KICK him out.''')
        action6 = input('Do you think the king should listen to him and spend more TIME on him or KICK him out? ')
        if action6 == 'time':
            action6 = action6.lower()
        print('''The king of the jungle with patience and love finished listening, looked compassionately at the
deluded donkey and gave him the following advice:
"Though he will roar most terribly, my friend, you could not impress even the most timid rabbit." The one who mocks
you today would only tremble if you had claws and fangs as huge as mine. The voice, when it is not accompanied by
drive and strength, is useless to impose itself.''')
        if action6 == 'Kick':
            print('''The king, surprised by the problem that the donkey was telling him, began to get angry since he
considered it nonsense. He immediately asked the guards to throw the donkey away. Although when the donkey was going
to his house he met the old and wise elephant who promised to give him great advice.''')
        else:
            print(bad_choose)
    elif action5 == 'elephant':
        print('''The donkey went out in search of the wise old elephant but could not find it since it was already on
its way to its great migratory journey.''')
    else:
        print(bad_choose)
else:
    print('Error: choose one of the provided options')