import random

def play_monty_hall(switch = True, num_doors = 3, opp_given = 1) -> bool:
    '''
        Play the Monty Hall game show once.
        
        Parameters
        ----------
        switch: bool
            A boolean that affects the choice of the contestant
            when given the option to switch.
            
        num_doors: int
            The number of doors there is.
            
        opp_given: int
            The number of opportunity given by the host to switch to
            any other door.
            
        Returns
        -------
        bool
            A boolean that shows whether the contestant
            win or lose the game.
            
    '''
    
    # Check if the number of opportunity given must be less than num_doors - 1 (to avoid always getting the prize)
    if opp_given + 1 >= num_doors:
        raise ValueError('Number of opportunity to switch must be less than the number of doors')
    
    # Simulate the game by putting the car in a random place
    doors = ['goat'] * num_doors
    doors[random.randint(0, num_doors - 1)] = 'car'
    
    # Initial Position / initial choice (randomised)
    pos_ = random.randint(0, num_doors - 1)
    
    # If you are not allowed to switch, then immidiately return the outcome
    if not switch: return doors[pos_] == 'car'
    
    for i in range(opp_given):
        # Opening the other door
        door_open_pos_        = random.randint(0, num_doors - 1)
        while(door_open_pos_ == pos_ or doors[door_open_pos_] == 'car' or doors[door_open_pos_] == 'open'): door_open_pos_ = random.randint(0, num_doors - 1)
        doors[door_open_pos_] = 'open'
        
        # Give opportunity to switch to other
        pos_switch_ = random.randint(0, num_doors - 1)
        while(pos_switch_ == pos_ or doors[pos_switch_] == 'open'): pos_switch_ = random.randint(0, num_doors - 1)
        pos_ = pos_switch_
                   
    return 1 if doors[pos_] == 'car' else 0