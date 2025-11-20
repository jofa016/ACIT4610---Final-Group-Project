import numpy as np
from .utils import epsilon_step_decay


class RewardShapedQLearning:
    """
    Final Q-learning agent with reward shaping + step-based epsilon decay.

    Works for both 4×4 and 8×8 maps depending on hyperparameters.
    """

    def __init__(
        self,
        env,
        alpha: float = 0.1,
        gamma: float = 0.99,
        epsilon: float = 1.0,
        epsilon_min: float = 0.01,
        epsilon_decay_stepsize: int = 1000,
        step_penalty: float = 0.0,
        hole_penalty: float = 0.0,
        goal_bonus: float = 1.0
    ):
        # Environment
        self.env = env
        self.n_states = env.observation_space.n
        self.n_actions = env.action_space.n

        # Q-table
        self.Q = np.zeros((self.n_states, self.n_actions))

        # Learning parameters
        self.alpha = alpha
        self.gamma = gamma

        # Exploration parameters
        self.epsilon = epsilon
        self.epsilon_initial = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay_stepsize = epsilon_decay_stepsize

        # Reward shaping
        self.step_penalty = step_penalty
        self.hole_penalty = hole_penalty
        self.goal_bonus = goal_bonus

    # ----------------------------------------------------------

    def choose_action(self, state: int) -> int:
        """ε-greedy action selection."""
        if np.random.rand() < self.epsilon:
            return self.env.action_space.sample()
        return np.argmax(self.Q[state])

    # ----------------------------------------------------------

    def compute_shaped_reward(self, real_reward: int, done: bool) -> float:
        """
        Reward shaping logic:

        - If not done: apply per-step penalty
        - If reached goal: goal bonus
        - If fell in hole: hole penalty
        """
        if not done:
            return self.step_penalty
        if real_reward > 0:     # reached goal
            return self.goal_bonus
        return self.hole_penalty  # hole or fail

    # ----------------------------------------------------------

    def train(self, episodes: int = 20000):
        """
        Trains the agent and returns success flags + steps per episode.
        """

        success_flags = []
        steps_per_episode = []

        for ep in range(episodes):
            state, info = self.env.reset()
            done = False
            steps = 0

            while not done:
                action = self.choose_action(state)
                next_state, real_reward, done, truncated, info = self.env.step(action)

                # Determine shaped reward
                reward = self.compute_shaped_reward(real_reward, done)

                # Q-learning update
                target = reward + self.gamma * np.max(self.Q[next_state]) * (not done)
                self.Q[state, action] += self.alpha * (target - self.Q[state, action])

                state = next_state
                steps += 1
                done = done or truncated

            # Episode records
            success_flags.append(1 if real_reward > 0 else 0)
            steps_per_episode.append(steps)

            # Epsilon decay
            self.epsilon = epsilon_step_decay(
                ep,
                self.epsilon_decay_stepsize,
                self.epsilon_initial,
                self.epsilon_min
            )

        return success_flags, steps_per_episode
