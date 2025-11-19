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
└── Project_3 <br/>
    ├── README <br/>
    ├── data <br/>
    │   ├── mknapcb1 <br/>
    │   ├── mknapcb2 <br/>
    │   ├── mknapcb4 <br/>
    │   ├── mknapcb5 <br/>
    │   ├── mknapcb8 <br/>
    │   ├── mknapcb9 <br/>
    └── BA_Knapsack <br/>

## Requirements:
* Python 3.8+
* Libraries:
    * numpy
    * pandas
    * matplotlib
    * seaborn

Install(local):
```sh
pip install numpy pandas matplotlib seaborn
```

## **Implementation Details**
* Candidate solutions are encoded as binary vectors indicating item selection.
* Bees Algorithm components:
    * Scout bees explore new random solutions.
    * Elite and selected sites receive more recruited bees for local neighbourhood search.
    * Neighbourhood search flips item-selection bits to refine high-quality solutions.
* Feasibility repair is applied to ensure the total weight does not exceed capacity.
* Multiple runs and convergence plots are used to analyse stability and performance.


## **Quick start**
1. Ensure the OR-library knapsack files (mknapcb*) are placed in: `Project_3/data/Knapsack/`
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

