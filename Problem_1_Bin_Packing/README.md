# **Problem 1 – One-Dimensional Bin Packing Using Ant Colony Optimization (ACO)**

This module applies **Ant Colony Optimization (ACO)** to the **One-Dimensional Bin Packing Problem**.  
The objective is to minimize the number of boxes required to pack items without exceeding capacity.

Each “ant” constructs a packing solution guided by pheromone trails and heuristic desirability (tight fit).  
Performance is measured by the number of boxes used, total unused space, and runtime.

## **Data Source**
OR-Library Bin Packing Instances: <br/>
[https://people.brunel.ac.uk/~mastjjb/jeb/orlib/binpackinfo.html](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/binpackinfo.html) <br/>
Files in use:
* binpack1
* binpack2
* binpack3
* binpack4
* binpack5
* binpack6
* binpack7
* binpack8

These files should be placed in the local `data/` folder for Project 1.

## Content:
```
Project_1_Bin_Packing/
│
├── data/
│   ├── binpack1.txt
│   ├── binpack2.txt
│   ├── binpack3.txt
│   ├── binpack4.txt
│   ├── binpack5.txt
│   ├── binpack6.txt
│   ├── binpack7.txt
│   └── binpack8.txt
│
├── notebook/    
│   └── ACO_binpacking.ipynb
│
├── README.md
└── requirements.txt
```


## Requirements:
* Python 3.8+

Libraries to install:
```sh
pip install numpy pandas matplotlib seaborn ipython
```

## **Implementation Details**
* Ant Colony Optimization formulation:
    * Pheromone matrix over item–position choices.
    * Heuristic preference for tighter fits (minimising leftover space).
    * Probabilistic solution construction for each ant per iteration.
* Pheromone update:
    * Evaporation plus reinforcement from best solutions.
* Evaluation:
    * Number of bins used.
    * Total unused capacity across all bins.
    * Runtime per parameter set.
    * Optional plots of convergence and load distribution.



## **Quick start**
1. Ensure the OR-library bin-packing files (binpack1–binpack8) are placed in: `Project_1/data/`
2. Open the notebook: `ACO_BinPacking.ipynb`
3. Run all cells from top to bottom.


## Parameter sets:

1. **Balanced:**
* n = 80 (number of scout ants)
* nb = 20 (number of best sites)
* ne = 5 (number of elite sites)
* nre = 15 (recruited ants around elite sites)
* nrb = 7 (recruited ants around other best sites)
* ngh = 3 (neighbourhood size)
* stlim = 25 (stagnation limit)
* max_iter = 500 (maximum iterations)


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

