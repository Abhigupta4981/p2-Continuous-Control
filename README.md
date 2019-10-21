### Udacity Deep Reinforcement Learning Nanodegree Project 2

# Continuous Control

## Use an agent that teaches an arm to move to a target

### Introduction
<div>
    <img src="https://user-images.githubusercontent.com/10624937/43851024-320ba930-9aff-11e8-8493-ee547c6af349.gif" width="70%" align="top-left" alt="" title="Banana Agent" />
</div>

The project uses Unity [Reacher](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Examples.md#reacher) environment. 

In this environment, a double-jointed arm can move to target locations. A reward of +0.1 is provided for each step that the agent's hand is in the goal location. Thus, the goal of the agent is to maintain its position at the target location for as many time steps as possible.

The observation space consists of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm. Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between -1 and 1.

### Distributed Training

For this project, Udacity provides us with two separate versions of the Unity environment:
- The first version contains a single agent.
- The second version contains 20 identical agents, each with its own copy of the environment.  

However, the Unity environment has dependencies which must also exist in order for it to run - see _Getting Started_ below ...

### Solving the Environment

Note that the project submission needs only solve one of the two versions of the environment, this project solves the second version. 

#### Option 1: Solve the First Version

The task is episodic, and in order to solve the environment,  the agent must get an average score of +30 over 100 consecutive episodes.

#### Option 2: Solve the Second Version

The barrier for solving the second version of the environment is slightly different, to take into account the presence of many agents.  In particular, the agents must get an average score of +30 (over 100 consecutive episodes, and over all agents).  Specifically,
- After each episode, we add up the rewards that each agent received (without discounting), to get a score for each agent.  This yields 20 (potentially different) scores.  We then take the average of these 20 scores. 
- This yields an **average score** for each episode (where the average is over all 20 agents).

The environment is considered solved, when the average (over 100 episodes) of those average scores is at least +30. 

### Getting Started

1. Depending somewhat on your operating system, the biggest challenge to getting this going will be that you need to have the [Unity ML-Agents](https://github.com/Unity-Technologies/ml-agents) libraries and [dependencies](https://github.com/udacity/deep-reinforcement-learning#dependencies) installed. To support the Udacity Deep Reinforcement Learning Unity envirnonments the specific version 0.40 of Unity ML-Agent is required.
 
2. There is a [guide](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Installation.md) for installation under Linux and Mac, and a separate guide for [Windows](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Installation-Windows.md) users. I am a Windows user, and I found that I needed to do a lot of work to get this going to support my GPU - as a supporting [detailed guide](https://medium.com/@ThoughtCaster/detailed-instructions-for-setting-up-unity-machine-learning-agents-8e2091e09d09) points out with great emphasis, it has dependencies on specific versions of Tensorflow, CUDA toolkit and CUDNN. It is highly recommended that this be done in a separate conda environment as the dependencies are likely to be older than current library versions. 

3. After installing Unity ML-Agents, download the environment from one of the links below.  You need only select the environment that matches your operating system:

    - **_Version 1: One (1) Agent_**
        - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Linux.zip)
        - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher.app.zip)
        - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Windows_x86.zip)
        - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Windows_x86_64.zip)

    - **_Version 2: Twenty (20) Agents_**
        - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux.zip)
        - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher.app.zip)
        - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86.zip)
        - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86_64.zip)
    
    (_For Windows users_) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

    (_For AWS_) If you'd like to train the agent on AWS (and have not [enabled a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md)), then please use [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Linux_NoVis.zip) (version 1) or [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux_NoVis.zip) (version 2) to obtain the "headless" version of the environment.  You will **not** be able to watch the agent without enabling a virtual screen, but you will be able to train the agent.  (_To watch the agent, you should follow the instructions to [enable a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md), and then download the environment for the **Linux** operating system above._)

4. Place the file in a working directory such as `p2_continuous-control/`, and unzip (or decompress) the file. 


## Instructions

The Jupyter Notebook `Continuous_Control.ipynb` must be followed to reproduce the training performed. It calls Agent and Model code in the files `ddpg_agent.py` and `model.py`. These must also be located in the working directory.

One thing that needs changing is the `reacherpath` definition early in the notebook - it must contain the path to wherever you have extracted the Reacher environment, as described in the _Getting Started_ section above. 

## Report

Please see the [`report.md`](report.md) for a discussion of the algorithm and model, and results of running the experiment.
