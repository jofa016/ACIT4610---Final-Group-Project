# ACIT4610---Final-Group-Project

## Implementing Optimization and Learning Algorithms for Applied Problems
### Group 3

This repository contains four implemented problems from the **Final Group Project 2025**.  
Each problem applies an algorithm studied in **ACIT 4610 -Evolutionary artificial intelligence and robotics** to a practical or benchmark scenario.


## Repository
```
├── Project_1_Bin_Packing/
│   ├── data/
│   │   ├── binpack1.txt
│   │   ├── binpack2.txt
│   │   ├── binpack3.txt
│   │   ├── binpack4.txt
│   │   ├── binpack5.txt
│   │   ├── binpack6.txt
│   │   ├── binpack7.txt
│   │   └── binpack8.txt
│   ├── notebook/
│   │   └──ACO_binpacking
│   │
│   ├── README
│   └── requirements
│
├── Project_3_Knapsack/ 
│   ├── data/
│   │   ├── mknapcb1.txt 
│   │   ├── mknapcb2.txt
│   │   ├── mknapcb4.txt
│   │   ├── mknapcb5.txt
│   │   ├── mknapcb8.txt
│   │   └── mknapcb9.txt
│   ├── notebook/
│   │   └──BA_Knapsack
│   │
│   ├── README
│   └── requirements
│
├── Project_4_spam_detection/
│   │
│   ├── data/
│   │   ├── readme
│   │   └── SMSSpamCollection
│   │   
│   ├── notebook/
│   │   └── BA_Knapsack
│   │
│   ├── README.md
│   └── requirements.txt
│
├── Project_5_warehouse_robot/
│   ├── notebook/
│   │   └──feature_engineering
│   │
│   ├── src>
│   │   ├── __init__ 
│   │   ├── qlearning_agent
│   │   └── utils
│   │
│   ├── README 
│   ├── report_reference 
│   └── requirements
│
├──Final Group Projct 2025
└──README.md
```

---
## Task descriptions:

### **Problem 1 – One-Dimensional Bin Packing Using Ant Colony Optimization (ACO)**

This problem applies Ant Colony Optimization to the 1-D bin packing challenge, where items must be assigned to bins without exceeding capacity. Ants create packing solutions using pheromone trails and a tight-fit heuristic. The objective is to reduce the number of boxes while maintaining feasibility, with OR-Library benchmark instances used for evaluation.


### Problem 3 – 0–1 Knapsack Problem Using Bees Algorithm (BA)

This problem uses the Bees Algorithm to optimise item selection under a weight constraint while maximising total value. The approach explores and improves solutions using scout bees, elite sites, neighbourhood searches, and recruited bees. Performance is evaluated using OR-Library knapsack instances of varied sizes.


### Problem 4 – Spam Detection Using Artificial Immune Systems (AIS) - Negative Selection Algorithm(NSA)
This problem applies the Negative Selection Algorithm to detect spam SMS messages. The model only learns from ham ("self") messages and creates detectors for "non-self" patterns (spam). On the SMS Spam Collection v1 dataset, messages are encoded in char-level TF-IDF, binarized, and assessed for accuracy, recall, and F1-score.


### Problem 5 – Reinforcement Learning (Q-Learning) for Warehouse Robot Navigation
This problem trains a Q-learning agent to navigate the FrozenLake-v1 environment, simulating a warehouse robot moving across a slippery floor. Experiments are conducted on 4×4 and 8×8 maps, testing multiple ε-decay strategies and hyperparameters, and results are compared against random and heuristic baselines.


---

## Contribution:
The group was divided into two sub-teams to work efficiently on the four assigned problems:
* **Team 1:** Focused on Problem 1 (ACO Bin Packing) and Problem 3 (Bees Algorithm for Knapsack) — implementing, tuning, and analyzing optimization-based methods.
* **Team 2:** Focused on Problem 4 (AIS Spam Detection) and Problem 5 (Q-Learning Robot Navigation) — handling machine learning and reinforcement learning components.

In the initial phase, the tasks were devided between the members of the pair, thereafter in each of the following sessions the codes were reviewed together and then worked on by coordinating via Discord and sharing files on GitHub. Each member contributed to the coding, testing and report written, as well as to the compilation and review of the code by the end of the project.

## Members:
* [Joanne T. Farstad](https://github.com/jofa016) 
* [Robel W. Ghebremedhin](https://github.com/rabrie10)
* [Susrita Khadka](https://github.com/susritak)
* [Karoline Nielsen](https://github.com/karroni)