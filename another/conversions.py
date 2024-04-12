class Constants:
    CharMapSize = 30
    MpsToMph = 2.237
    MpsToKph = 3.6
    MetersToMiles = 0.000621371
    MetersToKm = 0.001
    WorldSize = 200.0

class Conversions:
    @staticmethod
    def wc_point_to_cc_point(val):
        return int(val * (Constants.CharMapSize / Constants.WorldSize) + (Constants.CharMapSize / 2))

    @staticmethod
    def wc_length_to_cc_length(val):
        return int(val * (Constants.CharMapSize / Constants.WorldSize))

class Heading:
    North = 'North'
    East = 'East'
    South = 'South'
    West = 'West'


