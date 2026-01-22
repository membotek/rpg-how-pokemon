BOB_QUEAST=False
curent_queat=None
quest_active=[]
complete_quest=[]
class Quest:
    def __init__(self,type,goal,from_who):
        self.type=type
        self.goal=goal
        self.from_who=from_who
        self.done=False
    def update(self,talk_with_who):
        if talk_with_who != self.from_who and talk_with_who != self.goal:
            return
        if self.type==1:
            self.goal_go_from_A_to_B(talk_with_who)
    def goal_go_from_A_to_B(self,who):
        if self.goal==who:
            self.done=True
        if who==self.from_who:
            pass