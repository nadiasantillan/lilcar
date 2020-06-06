from pytest import fixture
from reward import reward_function

ALL_WHEELS_ON_TRACK = 'all_wheels_on_track'
X = 'x'
Y = 'y'
CLOSEST_OBJECTS = 'closest_objects'
CLOSEST_WAYPOINTS = 'closest_waypoints'
DISTANCE_FROM_CENTER = 'distance_from_center'
IS_CRASHED = 'is_crashed'
IS_LEFT_OF_CENTER = 'is_left_of_center'
IS_OFFTRACK = 'is_offtrack'
IS_REVERSED = 'is_reversed'
HEADING = 'heading'
OBJECTS_DISTANCE = 'objects_distance'
OBJECTS_HEADING = 'objects_heading'
OBJECTS_LEFT_OF_CENTER = 'objects_left_of_center'
OBJECTS_LOCATION = 'objects_location'
OBJECTS_SPEED = 'objects_speed'
PROGRESS = 'progress'
SPEED = 'speed'
STEERING_ANGLE = 'steering_angle'
STEPS = 'steps'
TRACK_LENGTH = 'track_length'
TRACK_WIDTH = 'track_width'
WAYPOINTS = 'waypoints'      

@fixture
def params():
    return {
        ALL_WHEELS_ON_TRACK: False, 
        X: 0.0,
        Y: 0.0,
        CLOSEST_OBJECTS: [ 0, 0 ],
        CLOSEST_WAYPOINTS: [ 0, 0],
        DISTANCE_FROM_CENTER: 0.0,
        IS_CRASHED: False, 
        IS_LEFT_OF_CENTER: False, 
        IS_OFFTRACK: False, 
        IS_REVERSED: False, 
        HEADING: 0.0, 
        OBJECTS_DISTANCE: [], 
        OBJECTS_HEADING: [], 
        OBJECTS_LEFT_OF_CENTER: [], 
        OBJECTS_LOCATION: [], 
        OBJECTS_SPEED: [],  
        PROGRESS: 0.0, 
        SPEED: 0.0, 
        STEERING_ANGLE: 0.0, 
        STEPS: 0, 
        TRACK_LENGTH: 0, 
        TRACK_WIDTH: 0, 
        WAYPOINTS: [], 
    }

def test_reward( params ):
    reward = reward_function( params )
    assert reward == 0.0
