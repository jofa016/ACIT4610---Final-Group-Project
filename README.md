# ACIT4610---Final-Group-Project

## Implementing Optimization and Learning Algorithms for Applied Problems
### Group 3

This repository contains four implemented problems from the **Final Group Project 2025**.  
Each problem applies an algorithm studied in **ACIT 4610 -Evolutionary artificial intelligence and robotics** to a practical or benchmark scenario.

---

## **Problem 1 – One-Dimensional Bin Packing Using Ant Colony Optimization (ACO)**

This module applies **Ant Colony Optimization (ACO)** to the **One-Dimensional Bin Packing Problem**.  
The objective is to minimize the number of boxes required to pack items without exceeding capacity.

Each “ant” constructs a packing solution guided by pheromone trails and heuristic desirability (tight fit).  
Performance is measured by the number of boxes used, total unused space, and runtime.

### **Data Source**
[OR-Library Bin Packing Instances](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/binpackinfo.html)
Files in use:
* binpack1–8

### **Implementation Details**
* ACO formulation with pheromone updates and heuristic weights.
* Evaluation metrics: number of boxes, unused space, and runtime.
* Convergence and load distribution plots.

### **Run Instructions**

* Open the notebook:
ACO notebook

Run all cells from top to bottom.  
Benchmark instances (binpack1–8) must be placed inside the `/data` folder.

* Then run all cells.


### Parameter sets:

1. **Balanced:**
* n = 80
* nb = 20
* ne = 5
* nre = 15
* nrb = 7
* ngh = 3
* stlim = 25
* max_iter = 500


2. **Exploration:**
* n = 100
* nb = 20
* ne = 5
* nre = 15
* nrb = 15
* ngh = 8
* stlim = 25
* max_iter = 500


3. **Exploitation:**
* n = 60
* nb = 20
* ne = 5
* nre = 25
* nrb = 7
* ngh = 3
* stlim = 25
* max_iter = 500


---

## Problem 3 – 0–1 Knapsack Problem Using Bees Algorithm (BA)

Implements the Bees Algorithm (BA) to solve the 0–1 Knapsack Problem, maximizing total value within a given weight limit.
Neighborhood search is guided by elite sites and recruited bees.

### Objectives:
* Maximize total item value.
* Maintain feasibility (total weight ≤ W).

### **Data Source**
[OR-Library Knapsack Instances](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/mknapinfo.html)
Files in use:
* mknapcb1
* mknapcb2
* mknapcb4
* mknapcb5
* mknapcb8
* mknapcb9

### **Implementation Details**
* Search agents represent candidate knapsack solutions.
* Feasibility repair mechanism.
* Convergence plots and multi-run statistics.

### **Run Instructions**
Open the notebook:
Knapsack notebook

Run all cells from top to bottom.  
Benchmark instances (mknapcb*) must be placed inside the `/data` folder.

### **Parameter Sets**

1. **Balanced**
* alpha = 1.2
* beta = 3.0
* rho = 0.10
* Q = 1200
* ants = 20
* iters = 150



2. **Exploration**
* alpha = 0.8
* beta = 3.5
* rho = 0.20
* Q = 800
* ants = 30
* iters = 200


3. **Exploitation**
* alpha = 1.5
* beta = 2.0
* rho = 0.05
* Q = 2000
* ants = 15
* iters = 250


--- 

## Problem 4 – Spam Detection Using Artificial Immune Systems (AIS: Negative Selection Algorithm)













## Problem 5 – Reinforcement Learning (Q-Learning) for Warehouse Robot Navigation

















## Repository

├── Problem1_ACO_BinPacking/
│   ├── data
│   └── aco notebook

├── Problem3_Bees_Knapsack/
│   ├── data
│   └── bees knapsack notebook

├── Problem4_AIS_SpamDetection/
│   ├── data
│   └── nsa notebook

├── Problem5_RL_WarehouseRobot/
│   ├── data
│   └── q learning notebook
└── README.md











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