'''
This module contains the Telescope class. This class is used to contain all variables relating to the telescope
and its functions. It also contains the functions to calculate the telescope's position and the telescope's
position in the sky.
'''

class Telescope(object):
    '''
    This class contains all variables and functions relating to the telescope.

    Attributes:
        name (str): The telescope's name.
        latitude (float): The telescope's latitude.
        longitude (float): The telescope's longitude.
        altitude (float): The telescope's altitude.
        azimuth (float): The telescope's azimuth.
        elevation (float): The telescope's elevation.
        focal_length (float): The telescope's focal length.
        aperture (float): The telescope's aperture.
        slew_speed (float): The telescope's Maximum slew speed.

    Written: David J. Law, 2022
    '''
    def __init__(self, name, latitude, longitude, altitude, azimuth, elevation,
                 focal_length, aperture, slew_speed, slew_step_azimuth, slew_step_altitude):
        '''
        This function initalises the telescope class.
        '''
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.azimuth = azimuth
        self.elevation = elevation
        self.focal_length = focal_length
        self.aperture = aperture
        self.slew_speed = slew_speed
        self.slew_step_azimuth = slew_step_azimuth
        self.slew_step_altitude = slew_step_altitude


    def set_name(self, name):
        '''
        This function sets the telescope's name.
        '''
        self.name = name

    def get_name(self):
        '''
        This function returns the telescope's name.
        '''
        return self.name

    def set_latitude(self, latitude):
        '''
        This function sets the telescope's latitude.
        '''
        self.latitude = latitude

    def get_latitude(self):
        '''
        This function returns the telescope's latitude.
        '''
        return self.latitude
    
    def set_longitude(self, longitude):
        '''
        This function sets the telescope's longitude.
        '''
        self.longitude = longitude
    
    def get_longitude(self):
        '''
        This function returns the telescope's longitude.
        '''
        return self.longitude
    
    def set_altitude(self, altitude):
        '''
        This function sets the telescope's altitude.
        '''
        self.altitude = altitude
    
    def get_altitude(self):
        '''
        This function returns the telescope's altitude.
        '''
        return self.altitude
    
    def set_azimuth(self, azimuth):
        '''
        This function sets the telescope's azimuth.
        '''
        self.azimuth = azimuth
    
    def get_azimuth(self):
        '''
        This function returns the telescope's azimuth.
        '''
        return self.azimuth
    
    def set_elevation(self, elevation):
        '''
        This function sets the telescope's elevation.
        '''
        self.elevation = elevation

    def get_elevation(self):
        '''
        This function returns the telescope's elevation.
        '''
        return self.elevation

    def set_focal_length(self, focal_length):
        '''
        This function sets the telescope's focal length.
        '''
        self.focal_length = focal_length

    def get_focal_length(self):
        '''
        This function returns the telescope's focal length.
        '''
        return self.focal_length

    def set_aperture(self, aperture):
        '''
        This function sets the telescope's aperture.
        '''
        self.aperture = aperture

    def get_aperture(self):
        '''
        This function returns the telescope's aperture.
        '''
        return self.aperture

    def set_slew_speed(self, slew_speed):
        '''
        This function sets the telescope's slew speed.
        '''
        self.slew_speed = slew_speed

    def get_slew_speed(self):
        '''
        This function returns the telescope's slew speed.
        '''
        return self.slew_speed

    def set_slew_step_azimuth(self, slew_step_azimuth):
        '''
        This function sets the telescope's slew step azimuth.
        '''
        self.slew_step_azimuth = slew_step_azimuth

    def get_slew_step_azimuth(self):
        '''
        This function returns the telescope's slew step azimuth.
        '''
        return self.slew_step_azimuth

    def get_slew_step_altitude(self):
        '''
        This function returns the telescope's slew step altitude.
        '''
        return self.slew_step_altitude

    def set_slew_step_altitude(self, slew_step_altitude):
        '''
        This function sets the telescope's slew step altitude.
        '''
        self.slew_step_altitude = slew_step_altitude   
    


    def get_pointing_coordinates(self):
        ''' 
        This function returns the telescope's position in altitude and azimuth.
        Returns: (altitude, azimuth) 
        '''
        return (self.altitude, self.azimuth)

    def set_target(altitude, azimuth):
        '''
        This function sets the telescope's target position in altitude and azimuth.
        '''
        target_altitude = altitude
        target_azimuth = azimuth

    def slew_to_target(self, target_altitude, target_azimuth):
        '''
        This function slews the telescope to a new target.
        Args:
            target_altitude (float): The telescope's target altitude.
            target_azimuth (float): The telescope's target azimuth.
        Attributes: 
            slew_steps_altitude (int): The number of steps the telescope will take to slew to the target altitude.
            slew_steps_azimuth (int): The number of steps the telescope will take to slew to the target azimuth.
        Returns: 
            slew_time (float): The number of seconds the telescope will take to slew to the target.
        '''

        #calculate the slew steps
        slew_steps_altitude = int(abs((target_altitude - self.altitude) / self.slew_step_altitude))
        slew_steps_azimuth = int(abs((target_azimuth - self.azimuth) / self.slew_step_azimuth))
        #calculate the slew time
        slew_time = self.slew_speed * slew_steps_azimuth * slew_steps_altitude
        #set telescope position to target position
        self.altitude = target_altitude
        self.azimuth = target_azimuth
        #return slew time
        return slew_time




