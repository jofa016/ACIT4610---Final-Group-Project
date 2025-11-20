# Problem 3 – 0–1 Knapsack Problem Using Bees Algorithm (BA)

## **Overview**
This project implements the Bees Algorithm (BA) to solve the 0–1 Knapsack Problem, aiming to maximise total value while respecting a weight constraint.The algorithm explores the search space using scout bees, neighbourhood search around selected sites, and deeper exploitation at elite sites, progressively refining candidate item selections.

## Objectives:
* Maximize total item value.
* Maintain feasibility (total weight ≤ W).

## **Data Source**
OR-Library Knapsack Instances:<br/>
[https://people.brunel.ac.uk/~mastjjb/jeb/orlib/mknapinfo.html](https://people.brunel.ac.uk/~mastjjb/jeb/orlib/mknapinfo.html) <br/>
Files in use:
* mknapcb1
* mknapcb2
* mknapcb4
* mknapcb5
* mknapcb8
* mknapcb9

## Repository:
```
Project_3_Knapsack
│
├── data/
│   ├── mknapcb1.txt 
│   ├── mknapcb2.txt
│   ├── mknapcb4.txt
│   ├── mknapcb5.txt
│   ├── mknapcb8.txt
│   └── mknapcb9.txt
│
├── notebook/
│   └── BA_Knapsack
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

Install(local):
```sh
pip install requirements.txt
```

## **Implementation Details**
1. Dataset Parsing (Beasley OR-Library)
    * Use first instance from: mknapcb1, 2, 4, 5, 8, 9
    * Extract:
        * profits → values
        * weight matrix → W
        * capacities → b
    * Store as pandas.DataFrame with attributes (n, m, capacities).

2. Problem Setup (MKP)
    * Binary decision vector x ∈ {0,1}^n
    * Objective: maximize values @ x
    * Constraints: W @ x <= b (multi-constraint knapsack)

3. Bees Algorithm (BA)
    * Initial population: n random binary solutions
    * Evaluate via profit; repair infeasible solutions
    * Best sites:
        * nb best, ne elite
        * Explore neighbours by flipping ≤ ngh bits
        * Keep best neighbour per site
    * Scouts refill remaining population
    * Early stop when no improvement for stlim iterations

4. Repair Strategy
    * If W @ x > b:
    * compute profit_per_density = profit / normalized_weight
    * iteratively drop items with lowest ratio
    * stop when feasible

5. Parameter Sets
    * Balanced: moderate scouts + neighbourhood size
    * Exploration: larger neighbourhood + more recruits
    * Exploitation: more elite recruits, smaller neighbourhood

6. Experiments
    * Instances: 6 datasets × 3 parameter sets
    * Seeds: 10 runs each
    * Logged metrics:
        * Baseline_Best, Best_Value, Improvement
        * Deviation_% vs known optimum
        * Runtime_s, Iterations, Iter_of_Best
        * Convergence curves (Hist_Best, Hist_Avg)

7. Evaluation
    * Aggregated summary tables
    * Heatmaps (improvement, deviation)
    * Convergence plots
    * Runtime analysis & runtime–quality scatterplots



## **Quick start**
1. Ensure the OR-library knapsack files (mknapcb*) are placed in: `Project_3/data/`
2. Open the notebook: `BA_Knapsack.ipynb`
3. Run all cells from top to bottom.  <br/>



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

