# שמירה ונגינה של אירועי מקלדת
import keyboard

# multi-key, windows+d as example shows the desktop in Windows machines
# print all typed strings in the events;;
# record all keyboard clicks until esc is clicked
events = keyboard.record('esc')
# play these events
keyboard.play(events)
key = list(keyboard.get_typed_strings(events))
for k in key:
    for i in k:
        print(i)
# log all pressed keys
keyboard.on_release(lambda e: print(e.name))
keyboard.unhook_all()
