# Problem 5 – Reinforcement Learning: FrozenLake-v1

## **Overview**



## Environment
- Gymnasium `FrozenLake-v1`, 6x6 map, `is_slippery=True`.

## Repository:
Project_5 <br/>
    ├── notebook <br/>
    │   └──feature_engineering <br/>
    ├── src <br/>
    │   ├── \__init__ <br/>
    │   ├── qlearning_agent <br/>
    │   └── utils <br/>
    ├── README <br/>
    ├── report_reference <br/>
    └── requirements <br/>

## Libraries
Gymnasium, NumPy, Matplotlib


## Implementation Details
* Environment:
  * Gymnasium `FrozenLake-v1` with `is_slippery=True`.
  * Experiments on both 4×4 and 8×8 maps, with increased `max_episode_steps` to avoid very early termination.

* Q-learning:
  * Tabular Q-table of shape `[n_states × n_actions]`, initialized to zeros.
  * ε-greedy action selection with multiple decay strategies (normal, linear, inverse, cosine, step).
  * Standard Q-learning update rule with tunable learning rate α and discount factor γ.
  * Optional reward shaping: step penalty, increased goal reward, and hole penalty (mainly for 8×8).

* Training setup:
  * Multiple independent runs (up to 20) to assess robustness.
  * Long training horizons (up to 100k episodes in some tests) to study convergence behaviour.
  * Post-convergence analysis by measuring success rate only after an initial burn-in period.

* Evaluation and analysis:
  * Success rate and average steps per episode, compared to random and heuristic baselines.
  * Moving-average success plots for different ε-decay methods and hyperparameter settings.
  * Heatmaps of max Q-values with overlaid policies for visualizing learned paths.
  * Additional runs with SARSA and Double Q-learning for algorithmic comparison.


## **Quick Start**
1. Open the notebook: `frozenlake_qlearning.ipynb`
    * To reproduce the main experiments:
        - For the 4×4 map: run the Q-learning sections with map_name="4x4".
        - For the 8×8 map: run the Q-learning sections with map_name="8x8".
2. All cells can be executed sequentially from top to bottom.



## **Parameter Sets**
* **Q-Learning (4×4 map, final setup)**
    * Environment:
        * env_name        = "FrozenLake-v1"
        * map_name        = "4x4"
        * is_slippery     = True
        * max_episode_steps = 100

    * Training:
        * num_episodes    = 20 000
        * alpha (α)       = 0.05
        * gamma (γ)       = 0.99
        * epsilon_start   = 1.0
        * epsilon_min     = 0.01
        * epsilon_schedule= step decay
        * step_size       = 1000
        * decay_factor    = 0.5
        * reward_scheme   = original Gym reward
                        (0 on F/H, 1 on G)

* **Q-Learning (8×8 map, final setup)**
    * **Environment:**
        * env_name        = "FrozenLake-v1"
        * map_name        = "8x8"
        * is_slippery     = True
        * max_episode_steps = 500

    * **Training:**
        * num_episodes    = 20 000
        * alpha (α)       = 0.10
        * gamma (γ)       = 0.99
        * epsilon_start   = 1.0
        * epsilon_min     = 0.01
        * epsilon_schedule= step decay
        * step_size       = 1000
        * decay_factor    = 0.5

    * **Reward shaping (used for 8×8 experiments):**
        * step_penalty        ≈ 0.01
        * goal_reward_bonus   ≈ 10.0
        * hole_penalty        ≈ -100.0

* **SARSA & Double Q-Learning (for comparison)**
    * **4×4 map (SARSA & Double Q-Learning):**
        * alpha (α)       = 0.05
        * gamma (γ)       = 0.99
        * epsilon_start   = 1.0
        * epsilon_min     = 0.01
        * epsilon_schedule= step decay
        * reward_scheme   = original Gym reward

    * **8×8 map (SARSA & Double Q-Learning):**
        * alpha (α)       = 0.10
        * gamma (γ)       = 0.99
        * epsilon_start   = 1.0
        * epsilon_min     = 0.01
        * epsilon_schedule= step decay
        * step_penalty    = 0.01
        * goal_reward_bonus = 10.0
        * hole_penalty    = -100.0


