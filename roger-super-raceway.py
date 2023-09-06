class Reward:
    def __init__(self):
        self.prevPosition = 0.0

    def rewardFunction(self, params):
        # Read input parameters
        all_wheels_on_track = params['all_wheels_on_track']
        distance_from_center = params['distance_from_center']
        track_width = params['track_width']
        track_length = params['track_length']
        abs_steering = abs(params['steering_angle'])
        speed = params['speed']
        progress = params['progress']

        # Give a very low reward by default
        reward = 1e-3

        # Rewards calculation
        # 1. On-Track reward (Max = 15)
        if all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.1:
            reward += 15
        else:
            reward *= 0.5

        # 2. Distance from center line reward (Max = 20)
        reward += (1 - distance_from_center / (track_width / 2)) * 20

        # 3. Steering angle reward (Max = 15)
        reward += (1 - abs_steering / 15) * 15

        # 4. Speed reward (Max = 20)
        reward += (speed / 5) * 20

        # 5. Progress reward (Max = 30)
        reward += (progress / 100) * 30

        return float(reward)

reward = Reward()

def reward_function(params):
    return reward.rewardFunction(params)