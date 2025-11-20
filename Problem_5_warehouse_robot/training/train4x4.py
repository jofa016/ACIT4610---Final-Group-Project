from pathlib import Path
import numpy as np

from Problem_5_warehouse_robot.src.utils import make_env
from Problem_5_warehouse_robot.src.qlearning_agent import RewardShapedQLearning


RESULTS_DIR = Path(__file__).resolve().parent.parent / "results"


def main():

    # Create environment
    env = make_env(
        map_name="4x4",
        slippery=True,
        max_steps=200,
        render_mode=None
    )

    # Best-performing hyperparameters for 4x4
    agent = RewardShapedQLearning(
        env,
        alpha=0.1,
        gamma=0.99,
        step_penalty=0.0,
        hole_penalty=0.0,
        goal_bonus=1.0,
        epsilon=1.0,
        epsilon_min=0.01,
        epsilon_decay_stepsize=1000
    )

    # Train agent
    success, steps = agent.train(episodes=20000)
    success_rate = sum(success) / len(success)
    print(f"Final 4x4 success rate: {success_rate:.4f}")

    # Save Q-table
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    qtable_path = RESULTS_DIR / "qtable_4x4.npy"
    np.save(qtable_path, agent.Q)
    print(f"Saved Q-table to {qtable_path}")


if __name__ == "__main__":
    main()
