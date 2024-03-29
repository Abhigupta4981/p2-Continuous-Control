import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F

def hidden_init(layer):
    fan_in = layer.weight.data.size()[0]
    lim = 1./np.sqrt(fan_in)
    return (-lim, lim)

class Actor(nn.Module):
    """Actor (Policy) Model"""
    
    def __init__(self, state_size, action_size, seed, fc1_units=400, fc2_units=300, leakiness=0.001):
        """
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed to use
            fc1_units (int): Number of nodes for first hidden layer
            fc2_units (int): Number of nodes for second hidden layer
        """
        
        super(Actor, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(state_size, fc1_units)
        self.bn1 = nn.BatchNorm1d(fc1_units)
        self.fc2 = nn.Linear(fc1_units, fc2_units)
        self.fc3 = nn.Linear(fc2_units, action_size)
        self.leakiness = leakiness
        self.reset_parameters()
    
    def reset_parameters(self):
        self.fc1.weight.data.uniform_(*hidden_init(self.fc1))
        self.fc2.weight.data.uniform_(*hidden_init(self.fc2))
        self.fc3.weight.data.uniform_(-3e-3, 3e-3)
    
    def forward(self, state):
        "Build an actor network that maps states to actions"
        if state.dim()==1: state = torch.unsqueeze(state, 0)
        x = F.leaky_relu(self.fc1(state), self.leakiness)
        x = self.bn1(x)
        x = F.leaky_relu(self.fc2(x), self.leakiness)
        return torch.tanh(self.fc3(x))
    
class Critic(nn.Module):
    """Critic (Value) Model"""
    
    def __init__(self, state_size, action_size, seed, fc1_units=400, fc2_units=300, leakiness=0.001):
        """
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed to use
            fc1_units (int): Number of nodes for first hidden layer
            fc2_units (int): Number of nodes for second hidden layer
        """
        
        super(Critic, self).__init__()
        self.seed = torch.manual_seed(seed)
        self.fc1 = nn.Linear(state_size, fc1_units)
        self.bn1 = nn.BatchNorm1d(fc1_units)
        self.fc2 = nn.Linear(fc1_units+action_size, fc2_units)
        self.fc3 = nn.Linear(fc2_units, 1)
        self.leakiness = leakiness
        self.reset_parameters()
    
    def reset_parameters(self):
        self.fc1.weight.data.uniform_(*hidden_init(self.fc1))
        self.fc2.weight.data.uniform_(*hidden_init(self.fc2))
        self.fc3.weight.data.uniform_(-3e-3, 3e-3)
    
    def forward(self, state, action):
        "Build an actor network that maps states to actions"
        if state.dim()==1: state = torch.unsqueeze(state, 0)
        x = F.leaky_relu(self.fc1(state), self.leakiness)
        x = self.bn1(x)
        x = torch.cat((x, action), dim=1)
        x = F.leaky_relu(self.fc2(x), self.leakiness)
        return self.fc3(x)