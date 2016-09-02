# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 12:26:49 2016

@author: Kai Zheng

standardized game element functions
complete search in all branches
"""

class NZeroBoardGame:
    def __init__(self, ini_state):
        self.ini_state = ini_state
        
    def primitive(self, stat):
        """
         no-available-move state loses 
         return value:
         -1: losing
         0: unknown
        """
        if(len(self.gen_move(stat)) == 0) :
            return -1
        else:
            return 0
        
    def initial_state(self):
        return self.ini_state
        
    def do_move(self, stat, flag):
        return stat - flag
    
    def gen_move(self, stat):
        """
         return value is the flag of moves:
          2 indicates a -2 move
          1 indicates a -1 move
        """
        if stat >= 2:
            return [2, 1]
        elif stat >= 1:
            return [1]
        else:
            return []
            
class Solver(NZeroBoardGame):
    def __init__(self, ini_state):
        NZeroBoardGame.__init__(self, ini_state)
        """
         __init__() must be called 
         with NZeroBoardGame instance as first argument
         So self here is super class instance not subclass instance?
         Confusing...
        """
        self.state_dict = {}
        res_dict = {1: "winning.", -1: "losing."}
        
        res = self._solve_dwlt(self.initial_state())
        print self.initial_state(), "is", res_dict[res]
        print self.state_dict
        
        
    def _solve_dwlt(self, cur_state):
        """
         This method takes an unknown state and solves its dwlt
         return value:
         1: winning
         -1: losing
        """
        cur_state_dwlt = self.primitive(cur_state) # 0 or -1 possible
        if(cur_state_dwlt == 0): # not directly losing, at least 1 child state
            for move_flag in self.gen_move(cur_state):
                next_state = self.do_move(cur_state, move_flag)
                if self.state_dict.has_key(next_state): # known next state
                    if(self.state_dict[next_state] == -1): # losing child found
                        cur_state_dwlt = 1
                else: # unknown next state
                    if(self._solve_dwlt(next_state) == -1):# losing child found
                        cur_state_dwlt = 1
        if(cur_state_dwlt == 0): # no losing child found
            cur_state_dwlt = -1
        self.state_dict[cur_state] = cur_state_dwlt
        return cur_state_dwlt
        
my_solver = Solver(8)
        

#def situationSearch(situ, situDict):
#    """
#     return value: 1 for winning situ, -1 for losing situ
#    """
#    steps = [2, 1]
#    for i in range(0, len(steps)):
#        if(situ - steps[i] >= 0): # if move available
#            if situDict.has_key(situ - steps[i]):
#                tmp = situDict[situ - steps[i]] # utilize previous knowledge
#            else:
#                tmp = situationSearch(situ - steps[i], situDict) # fail util.
#            if tmp == -1: # if next found situ loses
#                situDict[situ] = 1
#                return 1
#    situDict[situ] = -1
#    return -1 # no move available or all moves lead to winning situ
#
#iniSitu = 4
#situDict = {}
#res = situationSearch(iniSitu, situDict)
#if res == 1:
#    print iniSitu, "is winning."
#else:
#    print iniSitu,"is losing."
#print situDict