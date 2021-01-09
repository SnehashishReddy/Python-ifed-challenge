# Importing the time module for timing each match function
import time
import pandas as pd
# Importing Numpy for making use of its highly optimized arrays and functions
import numpy as np

# This comparision function will be making use of numpy
def numpy_match(subsetlist, mainlist):
    '''Summary of the numpy_match() function
    
    Parameters:
    subsetlist (list): The list from which you want to check for common elements
    mainlist (list): The main list with which you want to compare the elements from the subsetlist
    
    Returns:
    NoneType: Print statements are used to get the required output
    
    '''
    start = time.time() # Starting the timer
    subsetarr = np.array(subsetlist)
    mainarr = np.array(mainlist)
    i = np.in1d(mainarr,subsetarr) # The in1d function of np will check and return the indices of every element in subsetarr that is present in mainarr
    verified_elements = np.where(i)[0] # This statement will bring out the matching indices
    print("The Results of the Numpy VectorOps Match are: ")
    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start)) # Ending the timer
    print()

# This comparision function will be making use of the set datastructure in Python
def set_match(subsetlist, mainlist):
    '''Summary of the set_match() function
    
    Parameters:
    subsetlist (list): The list from which you want to check for common elements
    mainlist (list): The main list with which you want to compare the elements from the subsetlist
    
    Returns:
    NoneType: Print statements are used to get the required output
    
    '''
    start = time.time() # Starting the timer
    mainSet = set(mainlist)
    subsetSet = set(subsetlist)
    verified_elements = subsetSet.intersection(mainSet) # This operation makes use of the intersection method of the sets to return the common elements
    print("The Results of the Set Datastructure Match are: ")
    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start)) # Ending the timer

def main():
    with open('subset_elemets.txt') as f:
        subset_elements = f.read().split('\n')
    with open('all_elements.txt') as f:
        all_elements = f.read().split('\n')    
    numpy_match(subset_elements,all_elements)
    set_match(subset_elements, all_elements)

if __name__ == "__main__":
    main()