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
* Libraries:
    * numpy
    * pandas
    * matplotlib
    * seaborn

Libraries to install:
```sh
pip install requirements.txt
```

## **Implementation Details**
1. Dataset Parsing (Beasley OR-Library)
    * Use first instance from: binpack1, 2, 3, 4, 5, 6, 7, 8
    * Extract:
        * bin capacity → C
        * item sizes → w
        * known optimal bins → opt_bins
    * Store as pandas.DataFrame with attributes (n_items, capacity, opt_bins).

2. Problem Setup (1-D Bin Packing)
    * Items: integer sizes w_i.
    * Capacity: C.
    * Objective: minimize number of bins; tie-break by unused space.
    * Feasible solutions generated using a tight-fit decoder.

3. ACO Parameters
    * alpha, beta, rho, Q, ants, iters, seed, stlim
    * Parameter sets: balanced, exploration, exploitation.

4. ACO Algorithm (aco_binpack)
    * Pheromone matrix tau[n × n].
    * Heuristic: larger items favored (`eta = (w/C)^beta`).
    * Each ant builds a permutation using `P(j) ∝ tau[a,j]^alpha · eta[j]^beta.`
    * Decode with tight-fit → bins + loads → cost.
    * Adaptive evaporation + rank-based, normalized deposit.
    * Tracks history_best, history_mean, tau_std.
    * Early stopping on stagnation.

5. Experiment Runner (run_experiments)
    * Runs all instances × param sets × multiple seeds.
    * Logs:
        * best_cost, num_bins, unused_capacity, runtime_s, history_best, history_mean, tau_std.
    * Writes aggregated results to results.csv.

6. Post-Processing
    * Parse histories from CSV.
    * Add metadata + metrics:
        * opt_bins, gap_to_opt (%),
        * load_efficiency,
        * exploration_decay (pheromone-std drop).
    * Expand tau_std per iteration for exploration tracking.

7. Evaluation
    * Summary tables (mean across runs).
    * Convergence curves.
    * Load-distribution analysis.
    * Heatmaps of load_efficiency & gap_to_opt.
    * Exploration–exploitation dynamics (tau_std, smoothed curves).



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

