

def eat_ghost(power_pellet_active, touching_ghost):
   # return bool(power_pellet_active*touching_ghost)
    
    if (power_pellet_active and touching_ghost):
        return True
    elif(power_pellet_active or touching_ghost):
        return False

def score(touching_power_pellet,touching_dot):
     return bool(touching_power_pellet or touching_dot)
def lose(power_pellet_active, touching_ghost):
     will_lose = False
     if touching_ghost and not power_pellet_active:
        will_lose = True
     return will_lose

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
     will_lose = False
     if touching_ghost and not power_pellet_active:
        will_lose = True
     return has_eaten_all_dots and not will_lose

def eat_ghost(power_pellet_active, touching_ghost):
    '''
 
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    '''
    return power_pellet_active and touching_ghost
def score(touching_power_pellet, touching_dot):
    '''
 
    :param touching_power_pellet: bool - does the player have an active power pellet?
    :param touching_dot:  bool - is the player touching a dot?
    :return: bool
    '''
    return touching_power_pellet or touching_dot
def lose(power_pellet_active, touching_ghost):
    '''
 
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool
    '''
    return not power_pellet_active and touching_ghost
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    '''
 
    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost:  bool - is the player touching a ghost?
    :return: bool
    '''
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)