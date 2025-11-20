# Problem 5 – Reinforcement Learning: FrozenLake-v1

This project implements and evaluates Q-learning on the FrozenLake-v1 environment from Gymnasium. A warehouse robot must navigate a slippery grid world, avoid holes, and reach the goal tile.

## Highlights
- Full experimental notebook documenting exploration, tuning, and comparisons
- Production-ready reward-shaped Q-learning implementation
- Training scripts for both 4×4 and 8×8 maps
- Command-line visualization tool
- Command-line evaluation tool (success rate, steps, plots)
- Detailed analysis of convergence, hyperparameters, and alternative algorithms

## Repository Structure
```
Problem_5_warehouse_robot/
│
├── notebook/
│   └── feature_engineering.ipynb        # Full experiments and analysis
│
├── src/
│   ├── __init__.py
│   ├── utils.py                         # Environment factory + epsilon decay
│   ├── qlearning_agent.py               # Final reward-shaped Q-learning agent
│   ├── visualize.py                     # CLI visualization/animation tool
│   └── evaluate.py                      # Evaluation + plotting script
│
├── training/
│   ├── __init__.py
│   ├── train4x4.py                      # Train 4×4 agent → saves Q-table
│   └── train8x8.py                      # Train 8×8 agent → saves Q-table
│
├── results/
│   ├── qtable_4x4.npy                    # Saved 4×4 Q-table
│   └── qtable_8x8.npy                    # Saved 8×8 Q-table
│
├── README.md
└── requirements.txt
```

## Environment
- Gymnasium FrozenLake-v1 with `is_slippery=True`
- Two maps:
  - 4×4 (baseline environment)
  - 8×8 (significantly harder)
- Extended horizons:
  - 4×4 → `max_episode_steps=200`
  - 8×8 → `max_episode_steps=500`

## Final Algorithm: Reward-Shaped Q-learning
- Tabular Q-learning
- ε-greedy exploration
- Step-based epsilon decay (`step_size=1000`, `decay_factor=0.5`)
- Tunable learning rate α and discount factor γ
- Optional reward shaping (used only in the 8×8 final model)
- Update rule:

  \[
  Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]
  \]

- SARSA and Double Q-learning were explored only in the notebook for comparison. The production code ships with the final Q-learning agent.

## Final Hyperparameters
**✔ 4×4 Q-learning (final setup)**
- Episodes: 20 000
- α = 0.10
- γ = 0.99
- ε: 1.0 → 0.01 using step decay
- Reward shaping: none (default FrozenLake rewards)

**✔ 8×8 Q-learning (reward-shaped)**
- Episodes: 20 000
- α = 0.10
- γ = 0.99
- ε: 1.0 → 0.01 using step decay
- Reward shaping:
  - `step_penalty = +0.01`
  - `hole_penalty = −100`
  - `goal_bonus = +10`

## Training Scripts
4×4 training:
```pwsh
python -m Problem_5_warehouse_robot.training.train4x4
```
Output: `Problem_5_warehouse_robot/results/qtable_4x4.npy`

8×8 training:
```pwsh
python -m Problem_5_warehouse_robot.training.train8x8
```
Output: `Problem_5_warehouse_robot/results/qtable_8x8.npy`

## Visualization Tool
Animate a trained agent step-by-step:
```pwsh
python -m Problem_5_warehouse_robot.src.visualize `
    --qtable Problem_5_warehouse_robot/results/qtable_4x4.npy `
    --map 4x4 `
    --delay 0.2

python -m Problem_5_warehouse_robot.src.visualize `
    --qtable Problem_5_warehouse_robot/results/qtable_8x8.npy `
    --map 8x8 `
    --delay 0.3
```

## Evaluation & Metrics (`evaluate.py`)
This tool runs batches of episodes and produces plots:
- Success rate curve
- Steps per episode
- Steps histogram
- Success/fail pie chart

Example:
```pwsh
python -m Problem_5_warehouse_robot.src.evaluate `
    --qtable Problem_5_warehouse_robot/results/qtable_4x4.npy `
    --map 4x4 `
    --episodes 500

python -m Problem_5_warehouse_robot.src.evaluate `
    --qtable Problem_5_warehouse_robot/results/qtable_8x8.npy `
    --map 8x8 `
    --episodes 500
```

## Experiments Notebook
All exploration, testing, and analysis are inside `notebook/feature_engineering.ipynb`, covering:
- Epsilon decay comparisons
- SARSA and Double Q-learning tests
- α/γ hyperparameter sweeps
- Reward shaping experiments
- Convergence curves
- Random and heuristic baselines
- Q-value heatmaps

## Installation
```pwsh
pip install -r Problem_5_warehouse_robot/requirements.txt
```


