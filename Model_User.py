#Importing Libraries#

import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import csv
import tkinter
import requests
import bs4 #This is beautiful soup 4


#This pulls data from a webpage. This is used to create the inital cooridinates#

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser') #Adapted from the Beautiful Soup website
td_ys = soup.find_all(attrs={"class": "y"}) #using the table attributes in a search: 'y' is the value you are looking for within 'class'
td_xs = soup.find_all(attrs={"class": "x"}) #you are using the 100 x and y values generated on this webpage as your x and y values


#Creating the environment#

environment = []    #Creating the environment container

#The following imports a csv file which contains values in a grid format. Each value defines a pixel within the environment
with open('in.txt.csv', newline='') as f:                   
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = [] 
        for value in row:
            rowlist.append(value)   
        environment.append(rowlist)

#Setting the initial agent parameters#

maxd = 3                    #Setting maximum distance
num_of_agents = 20          #Setting initial number of agents
num_of_movesbeforeanim = 4  #Setting the number of moves that happen before each animation refresh
neighbourhood = 20          #Setting the neighbourhood value
agents = []                 #Creates a new container for agent coordinates


#Using seeds to test#

#seed = time.time() * 100000
#seed = 157114417707807.88      #Seed 1
#seed = 157114440355559.38      #Seed 2, this is a second different seed to test against
#random.seed(seed)              #Generate seed


#Setup the slider so the information can be passed back into the model#
def sel():

    global num_of_agents
    num_of_agents = agentslider.get()   #This allows the number of agents to be defined by the slider on the GUI interface

#Creating agent loop#
    for i in range(num_of_agents):
        y = int(td_ys[i].text)
        x = int(td_xs[i].text)
        agents.append(agentframework.Agent(environment, agents, y, x))
        #This now calls the agentframewok.py to generate coordinates
        
     
carry_on = True	            #Model runs until stopping conidtion is met or it is manually stopped

#Animation of the agents#

def update(frame_number):   #Updates the animation
    
    fig.clear()             
    global carry_on
    global num_of_interations
    global num_of_movesbeforeanim
    
    #Sets the environment within the animation#           
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    #Set the colour of the agents#
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y, c='white') #Sets colour of all agents to white

    #Move the agents and complete actions#    
    for j in range(num_of_movesbeforeanim):
        for i in range(num_of_agents):
            maxd = 3
            distmoved = agents[i].move(maxd)                #'distmoved' is the amount moved by an agent
            #print("distmoved",distmoved)                   #Can print the distance moved to check model is working correctly
            agents[i].eat(distmoved)
            agents[i].share_with_neighbours(neighbourhood)  #Share store with other agents that are within the neighbourhood
        
    
    #Create a stoping condition# 
    count = 0
    for i in range(num_of_agents):        
        if (agents[i].store > 500):     #When the total minimum store of all agents is 500, then stop the animation
            count = count + 1           #Count how many agents have reached the total store
            
    if (count == num_of_agents):        #If the count reaches the total number of agents, stop
        carry_on = False
        #print("stopping condition")
                       
def gen_function(b = [0]):
    a = 0
    global carry_on                     #Not actually needed as we're not assigning, but clearer
    while (a < 500) & (carry_on) :
        yield a			                #Returns control and waits next call.
        a = a + 1

#Building the GUI#

#The GUI is built using tkinter#
#Run the model#        
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
#Close the model#    
def close():
    root.destroy()

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
    
#root builds the main GUI window
root = tkinter.Tk() #main window
root.wm_title("Model")

#Create a button to close the model
btn = tkinter.Button(root, text = 'Close Model', bd = '5', 
                          command = close)  
# Set the position of button on the bottom of the window
btn.pack(side = 'bottom')

#Create a button to run the model
btn = tkinter.Button(root, text = 'Run Model', bd = '5', 
                          command = run)  
# Set the position of button on the bottom of the window
btn.pack(side = 'bottom')
  
# Creating s slider for scale adjustment of agents
agentslider = tkinter.Scale(root, from_=1, to=100,length=200, orient=tkinter.HORIZONTAL, label = "Number of Sheep:")
agentslider.pack()

#Create a button to set the number of agents once the slider has been moved
btn = tkinter.Button(root, text = 'Set number', bd = '5', command = sel)
btn.pack()

#Embedding a canvas within the window#
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

tkinter.mainloop()


###END###