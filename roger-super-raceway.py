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
        current_position = progress * 0.01 * track_length
        distance_travelled = current_position - self.prevPosition

        # Give a very low reward by default
        reward = 1e-3

        # Rewards calculation
        # 1. On-Track reward (Max = 25)
        if all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.34:
            reward += 25
        else:
            reward *= 0.2

        # 2. Distance from center line reward (Max = 25)
        if distance_from_center <= 0.1 * track_width:
            reward += 25
        elif distance_from_center <= 0.25 * track_width:
            reward += 15
        elif distance_from_center <= 0.5 * track_width:
            reward += 5
        else:
            reward *= 0.4

        # 3. Steering angle reward (Max = 15)
        if abs_steering > 15:
            reward *= 0.8

        # 4. Speed reward (Max = 20)
        if speed < 0.95:
            reward *= 0.5
        elif speed >= 0.95:
            reward += (speed / 5) * 100

        # 5. Progress reward (Max = 15)
        reward += (distance_travelled / track_length) * 15

        self.prevPosition = current_position
        return float(reward)

reward = Reward()

def reward_function(params):
    return reward.rewardFunction(params)