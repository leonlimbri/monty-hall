from modules.play_monty_hall import play_monty_hall
import matplotlib.pyplot as plt
import numpy as np

def simulation(n = 1000, num_doors = 3, opp_given = 1):
    '''
        Simulate the Monty Hall game show n times.
        
        Parameters
        ----------
        n: int
            An integer to show number of times the game is simulated.
            
        num_doors: int
            The number of doors there is.
            
        opp_given: int
            The number of opportunity given by the host to switch to
            any other door.
            
        Returns
        -------
        average probability of winning
        plot that shows the probability of winning over simulation #
            
    '''
    
    simulated_games = [play_monty_hall(True, num_doors, opp_given) for i in range(n)]
    p_winning_switch = [win / tots * 100 for win, tots in zip(np.cumsum(simulated_games), np.arange(1, n + 1))]
    
    simulated_games = [play_monty_hall(False, num_doors, opp_given) for i in range(n)]
    p_winning_noswitch = [win / tots * 100 for win, tots in zip(np.cumsum(simulated_games), np.arange(1, n + 1))]
    
    print('Probability of switching: %.2f%% | Probability of not switching: %.2f%%' %(p_winning_switch[-1], p_winning_noswitch[-1]))
    
    f, ax = plt.subplots()
    ax.axis([1, n, 0, 100])
    ax.set_xlabel('# Simulated Trial')
    ax.set_ylabel('Winning Probability (%)')
    ax.set_title('Winning Probability as number of simulation increases')
    ax.plot(np.arange(1, n + 1), p_winning_switch, label = 'switch')
    ax.plot(np.arange(1, n + 1), p_winning_noswitch, label = 'not switch')
    ax.legend(loc = 'upper right')
    
    return {
        'p_winning_switch': p_winning_switch,
        'p_winning_noswitch': p_winning_noswitch
    }