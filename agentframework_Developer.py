import random 
 
class Agent(): #This creates the Agent class
    
    def __init__(self, environment, agents, wolves, y, x):
        if (x == None):                 #If no coordinates are found, create a random value
            self.x = random.randint(0,99)
        else:
            self.x = x                  #Use preassigned coordinate
        if (y == None):                 #If no coordinates are found, create a random value
            self.y = random.randint(0,99)
        else:
            self.y = y                  #Use preassigned coordinate
        self.environment = environment  #feeding the environment into the agent
        self.agents = agents                #feeding the agent list to all the agents
        #self.wolves = wolves
        self.store = 0                  #setting the store start value
       

    def move(self, dist):                #Causes movement in a random direction
        dx = random.randint(0,dist)     #Creating a random number between 0 and the value of 'dist'
        dy = random.randint(0,dist)     #Creating a random number between 0 and the value of 'dist'
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

    def eat(self, distmoved):           #Eating the environment and calculating metabolism cost
        ce = 10 - distmoved             #Can eat = 10-the number of pixels moved. This is restricting the maximum amount that can be eaten, so if the agent moves more it eats less
        ae = random.randint(0, ce)      #Amount eaten = this is determining the amount eaten by picking a random number between 0 and the maximum number, as set by the 'can eat' above
        #print("amount eaten", ae)      #This is being printed to check the calculations are working correctly
        metab = int(round(distmoved/2)) #The metabolism changes depending on distance moved, in this case half the distance moved is being defined as the amound of 'energy' burnt off whilst moving
        #print("metabolism", metab)     #This is being printed to check the calculations are working correctly
        total_add = ae - metab          #The total food is the amount eaten (ae) minus the metabolism (metab)
        #print("Total",total_add)       #This is being printed to check the calculations are working correctly
        #The following set how the sheep eat the terrain
        if self.environment[self.y][self.x] > total_add:
            self.environment[self.y][self.x] -= total_add
            self.store += total_add     #This adds the total to the cumulative store, in the main model once this reaches 300 the stop codition activates
            #print("Store", self.store) #This is being printed to check the calculations are working correctly
            
    def share_with_neighbours(self, neighbourhood): #The sheep share their food store when they come into contact with each other
        for i in range(0, len(self.agents)):
            distance = self.distance_between(self.agents[i])
            if distance <= neighbourhood:                   #If the distance between agents is less than or equal to the value of the neighbourhood, then;
                 sum = self.store + self.agents[i].store
                 average = sum /2                           #Divide the store between agents
                 self.store = average
                 self.agents[i].store = average
                 #print("sharing " + str(dist_) + " " + str(average))
               
    def distance_between(self, agent):  #Calculate the distance between agents
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
                   
    
class Wolf():
    
    def __init__(self, environment, agents, wolves, y, x):
        self.x = random.randint(0,99)       #Creating a random number between 0 and 99
        self.y = random.randint(0,99)       #Creating a random number between 0 and 99
#        self.wolves = wolves                #Feeding the agent list to all the agents
        self.agents = agents
        self.store = 0
        
        
    def move(self):
        #Near_sheep = []
        
        if random.random() < 0.5:
            self.y = (self.y + 2) % 100 
        else:
            self.y = (self.y - 2) % 100
            
        if random.random() < 0.5:
            self.x = (self.x + 2) % 100 
        else:
            self.x = (self.x - 2) % 100
            
              
    def distance_wolves(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 # find out the distance between the sheep and the wolf
    
    
    def eat(self, agent):
         self.agents.remove(agent)
         self.store += 5
         