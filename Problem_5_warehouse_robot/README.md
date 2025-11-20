# Problem 5 – Reinforcement Learning: FrozenLake-v1

This project implements and evaluates Q-learning on the FrozenLake-v1 environment from Gymnasium. A warehouse robot must navigate a slippery grid world, avoid holes, and reach the goal tile.

## Highlights
- Full experimental notebook documenting exploration, tuning, and comparisons
- Production-ready reward-shaped Q-learning implementation
- Training scripts for both 4×4 and 8×8 maps
- Command-line visualization tool for trained agents
- Detailed analysis of convergence, hyperparameters, and alternative algorithms

## Repository Structure
```
Problem_5_warehouse_robot/
│
├── notebook/
│   └── feature_engineering.ipynb     # Full experiments and analysis
│
├── src/
│   ├── __init__.py
│   ├── utils.py                      # Environment creation + epsilon decay helpers
│   ├── qlearning_agent.py            # Reward-shaped Q-learning agent
│   └── visualize.py                  # CLI visualization tool
│
├── training/
│   ├── __init__.py
│   ├── train4x4.py                   # Train 4×4 agent → saves Q-table
│   └── train8x8.py                   # Train 8×8 agent → saves Q-table
│
├── results/
│   ├── qtable_4x4.npy                # Saved 4×4 Q-table
│   └── qtable_8x8.npy                # Saved 8×8 Q-table
│
├── README.md
└── requirements.txt
```

## Environment
- Gymnasium FrozenLake-v1 (`is_slippery=True`)
- Maps: 4×4 (baseline) and 8×8 (hard)
- Extended horizons: `max_episode_steps=200` for 4×4, `max_episode_steps=500` for 8×8

## Final Algorithm: Reward-Shaped Q-learning
- Tabular Q-table with ε-greedy exploration
- Step-based epsilon decay, configurable α and γ
- Optional reward shaping (used in 8×8 runs): step penalty, hole penalty, goal bonus
- Update rule:

  \[
  Q(s, a) \leftarrow Q(s, a) + \alpha \left[ r + \gamma \max_{a'} Q(s', a') - Q(s, a) \right]
  \]

- SARSA and Double Q-learning were explored in the notebook for comparison, but the final codebase ships only the tuned Q-learning agent

## Final Hyperparameters
**4×4 Q-learning**
- Episodes: 20 000
- α = 0.10, γ = 0.99
- ε: start 1.0 → min 0.01 with step decay (size 1000, factor 0.5)
- Reward shaping: none (Gym default rewards)

**8×8 Q-learning (reward-shaped)**
- Episodes: 20 000
- α = 0.10, γ = 0.99
- ε: start 1.0 → min 0.01 with step decay (size 1000, factor 0.5)
- Reward shaping: step_penalty = +0.01, hole_penalty = −100, goal_bonus = +10

## Training Scripts
Train the 4×4 agent and save its Q-table:
```pwsh
python -m Problem_5_warehouse_robot.training.train4x4
```
Output: `Problem_5_warehouse_robot/results/qtable_4x4.npy`

Train the 8×8 agent:
```pwsh
python -m Problem_5_warehouse_robot.training.train8x8
```
Output: `Problem_5_warehouse_robot/results/qtable_8x8.npy`

## Visualization Tool
Animate a trained policy run:
```pwsh
python -m Problem_5_warehouse_robot.src.visualize \
    --qtable Problem_5_warehouse_robot/results/qtable_4x4.npy \
    --map 4x4 \
    --delay 0.2

python -m Problem_5_warehouse_robot.src.visualize \
    --qtable Problem_5_warehouse_robot/results/qtable_8x8.npy \
    --map 8x8 \
    --delay 0.3
```

## Experiments Notebook
All exploratory work lives in `notebook/feature_engineering.ipynb`, covering:
- Multiple ε-decay strategies
- SARSA and Double Q-learning comparisons
- Hyperparameter sweeps for α and γ
- Reward shaping ablations
- Convergence curves and success-rate tracking
- Random vs heuristic policy baselines and Q-value heatmaps

## Installation
```pwsh
pip install -r Problem_5_warehouse_robot/requirements.txt
```


