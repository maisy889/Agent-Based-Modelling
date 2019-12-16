# Agent Based Model - Programming for Geographical Information Analysts: Core Skills

This is the first assessment for the module GEOG5990 as part of the MSc Geographic Information Systems course at the University of Leeds. 
More information about this can be found at: https://maisy889.github.io  

# Overview

The agent-based model has been created in Spyder (Anaconda 3) on Windows using Python coding language 3.7.
The aim of the assignment was to create an agent-based model that simulates ‘sheep’ (agents) grazing within an environment. 

# Files

The files needed to run the model are as follows:
•	Model_User (operational model)
•	Agentframework
•	In.text
•	Model_Developer (model with issues)
•	Agentframework_Developer 
This project is licensed under the GNU General Public License v.3.0 - see [here] (https://github.com/maisy889/Agent-Based-Modelling/blob/master/LICENSE)

# Setup

The environment was created by inputting a csv file with values between 0 to 255. By using MatPlotLib these values can be visualised as a graphic. The value of the square determines how much ‘food’ there is available at each pixel. 

The agents (aka ‘Sheep’) have been designed to interact with their environment and each other. This includes the following functions:

•	Move – The sheep are originally plotted from a set of coordinates scraped from a webpage. After this they are able to move in random directions.

•	Eat – The sheep are able to ‘eat’ their environment and put what they eat in a store. The amount the can eat and store is dependant of how much they move. The more that they move, the maximum amount they are able to eat is reduced. The total amount they then eat is impacted by their metabolism, which is also determined by the total distance moved by an sheep within one cycle of the animation. Once the total amount eaten is calculated is it added to the sheep’s total store. 

•	Share with neighbours – When sheep are within a certain distance of another sheep, their total stores are combined and then divided equally between the two sheep. 

A condition has been set so that when all sheep have a total store of 500, the animation will stop. 

The MatPlotLib animation function is used to create a moving animation of the graph.

The General User Interface (GUI) was created using tkinter. This allowed the addition of a slider bar to determine how many sheep the user would like to set for their animation. 

# Operation guide – User Model
It is recommended that you run this model in Spyder (Anaconda 3) and the following instructions are for this software. 
Firstly, download the above files (Model_Developer and Agentframework_Developer optional) from the GitHub repository. Ensure that all files are stored within the same folder. 
Open both the agentframework.py and Model_User.py within Python. To ensure that the animation runs correctly, you need to set the Graphics option to Tkinter. You can do this by selecting: Tools > Preferences > IPython Console > Graphics, and then from the drop-down select Tkinter.
Run the agentframework file first, and once this has completed run the model file. This will pop out a window in which your animation will run. 
To change and set the number of sheep, firstly set the slider to the desired number then press ‘Set number’. Then to run the model, click ‘Run Model’ below the animation screen. When the model has finished running or if you want to close the model early, click ‘Close Model’.

# Operation guide – Developer Model
If you have downloaded the developer files, you will see that is has an additional class within the agentframework_Developer – Wolves. Follow the first two steps of the Operation Guide (above) but then run the agentframework_Developer.py file, then the 
You will see that there is an additional slider to set the number of wolves for the simulation. Set both values before running the model, as per the above instructions. The model will then run in a pop out window and you will see the addition of black ‘wolves’ within the environment.
The aim was to have the wolves ‘eat’ and remove the sheep from the model, however in its current state this is unable to happen and the relevant bit of code within the model for the wolves ‘eat’ function is commented out. 

