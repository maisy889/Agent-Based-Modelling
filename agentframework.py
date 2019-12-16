import random 
 
#This creates the Agent class#
class Agent(): 
    
    def __init__(self, environment, agents, y, x):
        if (x == None):                         #If no coordinates are found, create a random value
            self.x = random.randint(0,99)
        else:
            self.x = x                          #Use preassigned coordinate
        if (y == None):                         #If no coordinates are found, create a random value
            self.y = random.randint(0,99)
        else:
            self.y = y                          #Use preassigned coordinate
        self.environment = environment          #Feeding the environment into the agent
        self.agents = agents                    #Feeding the agent list to all the agents
        self.store = 0                          #Setting the store start value
       
    #Makes the agents move in a random direction#
    def move(self, dist):                       
        dx = random.randint(0,dist)             #Creating a random number between 0 and the value of 'dist'
        dy = random.randint(0,dist)             #Creating a random number between 0 and the value of 'dist'
        if random.random() < 0.5:
            self.y = (self.y + dy) % 100 
        else:
            self.y = (self.y - dy) % 100
            
        if random.random() < 0.5:
            self.x = (self.x + dx) % 100 
        else:
            self.x = (self.x - dx) % 100
        return int(round((dx*dx + dy*dy)**0.5)) #This is giving the 'dist' 
                                                #int(round is allowing this to be converted to an interger and rounded to the nearest whole number
   
    #The agents eating their environment and calculating metabolism cost#
    def eat(self, distmoved):           
        ce = 10 - distmoved                 #Can eat = 10-the number of pixels moved. This is restricting the maximum amount that can be eaten, so if the agent moves more it eats less
        ae = random.randint(0, ce)          #Amount eaten = this is determining the amount eaten by picking a random number between 0 and the maximum number, as set by the 'can eat' above
        #print("amount eaten", ae)          #This is being printed to check the calculations are working correctly
        metab = int(round(distmoved/2))     #The metabolism changes depending on distance moved, in this case half the distance moved is being defined as the amound of 'energy' burnt off whilst moving
        #print("metabolism", metab)         #This is being printed to check the calculations are working correctly
        total_add = ae - metab              #The total food is the amount eaten (ae) minus the metabolism (metab)
        #print("Total",total_add)           #This is being printed to check the calculations are working correctly
        #The following sets how the sheep eat the terrain#
        if self.environment[self.y][self.x] > total_add:
            self.environment[self.y][self.x] -= total_add
            self.store += total_add     #This adds the total to the cumulative store, in the main model once this reaches 300 the stop codition activates
            #print("Store", self.store) #This is being printed to check the calculations are working correctly
            
    #The agents share their food store when they come into contact with each other#
    def share_with_neighbours(self, neighbourhood):         
        for i in range(0, len(self.agents)):
            distance = self.distance_between(self.agents[i])
            if distance <= neighbourhood:                                   #If the distance between agents is less than or equal to the value of the neighbourhood, then;
                 sum = self.store + self.agents[i].store
                 average = sum/2                                            #Divide the store between agents
                 self.store = average
                 self.agents[i].store = average
                 #print("sharing " + str(distance) + " " + str(average))    #Shows the distance between agents that are sharing their store
   
    #Calculate the distance between two agents#        
    def distance_between(self, agent):  
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
    #Gives string with x and y values#
    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)
