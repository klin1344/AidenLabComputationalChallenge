#Aiden Lab Computational Challenge: 1B


###Challenge:
Create a Number to Word converter. This is an open ended project - we want to see your creativity. Your input will be a 10-20 digit number. The output will be a mix of numbers and letters which help you remember the original number.

There are several approaches (visual, phonetic, dictionary, etc.) to this problem. A starting place for ideas:
http://phonespell.org/
http://www.word2number.com/
http://dialabc.com/

Document what you're doing. This should be fun. It may even be something to add to your github profile/portfolio. 

Your program can be submitted as a command line tool. Bonus points for a nice GUI or launching it as an app, but our primary criteria will be creativity of the solution, speed of execution, and sufficient documentation.


###Solution:
According to [scientific research](http://www.wsj.com/articles/SB10001424052702304483804579284682214451364), music tends to play a very important role in memorization for humans.  Thus, I created a tool that maps a sequence of digits into a sequence of musical notes.  It is much easier to remember a specific sound pattern than it is a string of numbers.  This tool maps every digit to a musical note in C-major, starting with 0 at middle-C.  When you enter a sequence of numbers, the tool will display the sequence of notes and play back the sound representation of that sequence of numbers.  

According to a small test study I conducted here at Rice University, those with a musical background or "perfect pitch" could easily identify the series of notes, and quickly map them back to the original numbers.  Those without a musical background were still able piece back the sequence of numbers better than without the musical (sound and notes) representation; they were able to roughly decipher the numbers using the relative pitch of the notes they see and hear.


###How To Use:
Run the solution using Python 2.7.  The program looks for one call-line argument `<sequence of numbers>`, e.g., `9854373289234`

####Examples:
#####Run
`python sol1b.py 704981234`
#####Output:
```Numbers:  [7, 0, 4, 9, 8, 1, 2, 3, 4]
Notes: ['C2', 'C', 'G', 'E2', 'D2', 'D', 'E', 'F', 'G']```

#####Run
`python sol1b.py 0123456789`
#####Output:
```Numbers:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Notes: ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C2', 'D2', 'E2']```

