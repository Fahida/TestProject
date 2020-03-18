class fromhome():
    def __init__(self,status,Designation,interest):
        self.status= []
        self.Designation= None
        self.mentorStatus={}
        self.mentorTime={}
        self.ID=0

    def addStacks(self,status):
        self.ID=input("Enter your ID")
        self.Designation=input("Enter Your Designaton(mentor/learner)")
        currentStatus=input("Enter your interest(if you are a learner)/Expertise(if you are a mentor)")
        self.status=status.append(currentStatus)
        if(self.Designation=="mentor"):
             self.mentorStatus[ID]=currentStatus
        

    def setMentorOrLearner(self,Designation):
        
        self.Designation=input("Enter Your Designaton(mentor/learner)")
        
        

    def setAvailableTime(self,time):
        self.ID=input("Enter your ID")
        if(self.Designation=="mentor"):
            self.time=input("Enter your availability")
            self.mentorTime[ID]=time
            
    def getMentor(self):
        requiredTime=print("Enter your feasible time to study")
        stack=print("Enter your Interest")
        StackList=[]
        for key in self.mentorStatus:
            {
            
                if(stack==self.mentorstatus[ID]):
                    StackList=self.mentorStatus[ID]
        
            }

        TimeList=[]
        for key in self.mentorTime:
            {
            
                if(stack==self.mentorTime[ID]):
                    TimeList=self.mentorStatus[ID]
        
            }
        print("Mentors available for your stack"+str(StackList))
        print("Mentors available for your Time"+str(TimeList))




       









        






    
