from components.powerups.Power_ups import PowerUp
from utils.constants import SHIELD, SHIELD_TYPE,HAMMER,HAMMER_TYPE

class Shield(PowerUp):
    def __init__(self):
        self.image = SHIELD
        super(Shield, self).__init__(self.image, SHIELD_TYPE)
class Hammer(PowerUp):
    def __init__(self):
        self.image = HAMMER
        super(Hammer, self).__init__(self.image, HAMMER_TYPE)