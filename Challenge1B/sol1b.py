"""
Aiden Lab Computational Challenge 1B
Auther: Kevin Lin
"""

import sys
import pyglet

# store appropriate path and note of each sound file
NOTE_0 = ("C40.wav", "C")
NOTE_1 = ("D42.wav", "D")
NOTE_2 = ("E44.wav", "E")
NOTE_3 = ("F45.wav", "F")
NOTE_4 = ("G47.wav", "G")
NOTE_5 = ("A49.wav", "A")
NOTE_6 = ("B51.wav", "B")
NOTE_7 = ("C52.wav", "C2")
NOTE_8 = ("D54.wav", "D2")
NOTE_9 = ("E56.wav", "E2")

# map each digit, 0-9, to a corresponding musical note
# starts with 0 as middle C
sound_map = {0:NOTE_0, 1:NOTE_1, 2:NOTE_2, 3:NOTE_3, 4:NOTE_4, 5:NOTE_5, 6:NOTE_6, 7:NOTE_7, 8:NOTE_8, 9:NOTE_9}
# calculate the total duration of all sounds to be played
duration = pyglet.resource.media(sound_map[0][0]).duration * len(sys.argv[1])
# create a list of numbers with the input
seq = [int(char) for char in sys.argv[1]]
notes = []

player = pyglet.media.Player()

# fill notes with the musical note that corresponds to the number
# queue the corresponding sound file to be played
for num in seq:
	notes.append(sound_map[num][-1])
	player.queue(pyglet.resource.media(sound_map[num][0], streaming=False))
	
player.play()

def exit_callback(duration):
	"""
	Given a duration (passed by clock_schedule), exit the pyglet event loop
	and continue execution of the program.
	"""
	pyglet.app.exit()

# exit pyglet event loop after the length of time that it takes to play all queued sounds
pyglet.clock.schedule_once(exit_callback , duration)
pyglet.app.run()

# print the sequence numbers, and the mapped musical notes
print "Numbers: ", seq
print "Notes:" , notes

