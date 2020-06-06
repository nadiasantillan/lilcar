def reward_function(params):
    '''
    Calculates the reward value (0, 1] based on params

    "all_wheels_on_track": Boolean,        # flag to indicate if the agent is on the track
    "x": float,                            # agent's x-coordinate in meters
    "y": float,                            # agent's y-coordinate in meters
    "closest_objects": [int, int],         # zero-based indices of the two closest objects to the agent's current position of (x, y).
    "closest_waypoints": [int, int],       # indices of the two nearest waypoints.
    "distance_from_center": float,         # distance in meters from the track center 
    "is_crashed": Boolean,                 # Boolean flag to indicate whether the agent has crashed.
    "is_left_of_center": Boolean,          # Flag to indicate if the agent is on the left side to the track center or not. 
    "is_offtrack": Boolean,                # Boolean flag to indicate whether the agent has gone off track.
    "is_reversed": Boolean,                # flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
    "heading": float,                      # agent's yaw in degrees
    "objects_distance": [float, ],         # list of the objects' distances in meters between 0 and track_length in relation to the starting line.
    "objects_heading": [float, ],          # list of the objects' headings in degrees between -180 and 180.
    "objects_left_of_center": [Boolean, ], # list of Boolean flags indicating whether elements' objects are left of the center (True) or not (False).
    "objects_location": [(float, float),], # list of object locations [(x,y), ...].
    "objects_speed": [float, ],            # list of the objects' speeds in meters per second.
    "progress": float,                     # percentage of track completed
    "speed": float,                        # agent's speed in meters per second (m/s)
    "steering_angle": float,               # agent's steering angle in degrees
    "steps": int,                          # number steps completed
    "track_length": float,                 # track length in meters.
    "track_width": float,                  # width of the track
    "waypoints": [(float, float), ]        # list of (x,y) as milestones along the track center

    '''
    print(params)
    allWheelsOnTrack = params['all_wheels_on_track']
    x = params['x']
    y = params['y']
    closestObjects = params['closest_objects']
    closestWaypoints = params['closest_waypoints']
    distanceFromCenter = params['distance_from_center']
    isCrashed = params['is_crashed']
    isLeftOfCenter = params['is_left_of_center']
    isOffTrack = params['is_offtrack']
    isReversed = params['is_reversed']
    heading = params['heading']
    objectsDistance = params['objects_distance']    
    objectsHeading = params['objects_heading']
    objectsLeftOfCenter = params['objects_left_of_center']
    objectsLocation = params['objects_location']
    objectsSpeed = params['objects_speed']
    progress = params['progress']
    speed = params['speed']
    steeringAngle = params['steering_angle']
    steps = params['steps']
    trackLenght = params['track_length']
    trackWidth = params['track_width']
    waypoints = params['waypoints']    

    reward = 0

    return float(reward)
