import numpy as np
import matplotlib.pyplot as plt
from Problem_5_warehouse_robot.src.utils import make_env


def run_evaluation(
    qtable_path: str,
    map_name: str = "4x4",
    episodes: int = 500
):
    """
    Evaluate a trained Q-table on FrozenLake.

    Returns:
        success_flags  : list[int]
        steps_per_ep   : list[int]
        rewards        : list[int]
    """

    # Load Q-table
    Q = np.load(qtable_path)

    # Create evaluation environment (no rendering)
    env = make_env(
        map_name=map_name,
        slippery=True,
        max_steps=500,
        render_mode=None
    )

    success_flags = []
    steps_per_ep = []
    episode_rewards = []

    for _ in range(episodes):
        state, info = env.reset()
        done = False
        steps = 0
        total_reward = 0

        while not done:
            # always greedy
            action = int(np.argmax(Q[state]))
            next_state, reward, done, truncated, info = env.step(action)
            done = done or truncated
            total_reward += reward
            steps += 1
            state = next_state

        success_flags.append(1 if reward > 0 else 0)
        steps_per_ep.append(steps)
        episode_rewards.append(total_reward)

    return success_flags, steps_per_ep, episode_rewards


# -------------------------------------------------
# PLOTTING SECTION
# -------------------------------------------------

def plot_results(success_flags, steps, title_prefix="Policy Evaluation"):
    episodes = len(success_flags)

    # Moving average success
    window = min(50, episodes)
    moving_avg = np.convolve(success_flags, np.ones(window) / window, mode="valid")

    # ---- Plot 1: Success Rate ----
    plt.figure(figsize=(10, 4))
    plt.plot(moving_avg, label="Success Rate (moving avg)")
    plt.title(f"{title_prefix} – Success Rate")
    plt.xlabel("Episode")
    plt.ylabel("Success Rate")
    plt.grid(True)
    plt.legend()
    plt.show()

    # ---- Plot 2: Steps per episode ----
    plt.figure(figsize=(10, 4))
    plt.plot(steps)
    plt.title(f"{title_prefix} – Steps Per Episode")
    plt.xlabel("Episode")
    plt.ylabel("Steps")
    plt.grid(True)
    plt.show()

    # ---- Plot 3: Steps histogram ----
    plt.figure(figsize=(8, 4))
    plt.hist(steps, bins=20, edgecolor="black")
    plt.title(f"{title_prefix} – Steps Distribution")
    plt.xlabel("Steps")
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.show()

    # ---- Plot 4: Success ratio pie ----
    success_count = sum(success_flags)
    fail_count = episodes - success_count

    plt.figure(figsize=(4, 4))
    plt.pie(
        [success_count, fail_count],
        labels=["Success", "Fail"],
        autopct="%1.1f%%",
        colors=["#4CAF50", "#F44336"]
    )
    plt.title(f"{title_prefix} – Success/Fail Ratio")
    plt.show()


# -------------------------------------------------
# CLI ENTRYPOINT
# -------------------------------------------------

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Evaluate Q-learning agent on FrozenLake")

    parser.add_argument("--qtable", required=True, type=str, help="Path to Q-table (.npy)")
    parser.add_argument("--map", default="4x4", choices=["4x4", "8x8"], help="FrozenLake map size")
    parser.add_argument("--episodes", default=500, type=int, help="Number of evaluation episodes")

    args = parser.parse_args()

    success, steps, rewards = run_evaluation(
        qtable_path=args.qtable,
        map_name=args.map,
        episodes=args.episodes
    )

    print(f"\nEvaluation over {args.episodes} episodes:")
    print(f"- Success Rate: {sum(success)/len(success):.3f}")
    print(f"- Avg Steps:   {np.mean(steps):.2f}")

    plot_results(success, steps, title_prefix=f"Policy Evaluation ({args.map})")
