# Tamagotchi-GPT
I built a simple virtual pet in python using only prompts from ChatGPT3. 
I generate de code by several prompts using several prompt iteration. 
After getting parts of code i cleaned up and debug the code

The aim of this project is show developers how we can use ChatGPT in our daily job and the limitations of the AI

Now im gonna list some prompts i used to built it:

1. First i set the project and the rules:

    Hello, I want you to help me create a python program using PyCharm as an IDE, when I say let's go I mean that you are going to create the code.
    
2. I set the basic code i want to start with the structure:

   We are going to create a tamagotchi in python, I want to create an ASCII art version of a virtual pet that appears on the screen. The main thread of execution simply shows a simple animation of this pet without  doing anything on the screen. give me the code.
  
3. Now i add functions to the code like the stats:

    Ok, now I want to add stats to my tamagotchi. The stats are variables that contain information about: Hunger, boredom, sleep, hygiene. These indicators will rise over time, unevenly, that is, not all rise at the same time, but some rise faster than others. For example, hunger rises faster than sleep and hygiene slower than sleep and boredom a little slower than hunger. The idea would be to increase these numerical variables and when it reaches 100 a message appears indicating that this stat is too high and it is necessary to attend.
    
4. Improve the UI

    make it so that instead of showing the stats with a number it shows it with a loading bar 
 
5. I add more function to take care of the Tamagotchi where i can reset de stats 

    Now I want that by means of different keyboard keys, for example the initial of each stat, that stat can be attended to. Attending means that I'm going to launch a process that will lower the stat value a bit each time I press that key. While this is happening the animation will change to reflect the stat it is dropping, if my tamagochi is sleepy and I press s on the keyboard I want the animation of the tamagotchi to change to one where it is sleeping. Can you do this for all stats? For example, when it is hungry, the animation of the recovery state would be the tamahotchi eating and it is launched with h and so on.


## Requirements
- Python 3.6 or higher.
- `keyboard` library (you can install it using `pip install keyboard`).  

## Instructions for use
1. Clone this repository to your local machine.
2. Install the requirements mentioned above.
3. Open a terminal and navigate to the repository folder.
4. Run the following command to start the program:  
  
