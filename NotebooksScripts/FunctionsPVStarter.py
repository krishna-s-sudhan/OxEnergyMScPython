"""
Functions, Classes and Modules Tutorial
This file demonstrates Python functions.

Learning objectives:
- Defining and using functions

Complete the script by filling in the missing code sections marked with <---.

@author: Krishna Skandha Sudhan
"""

# Import any necessary libraries
import math
import pandas as pd
import numpy as np
import os

# <--- Define a function to size a PV system based on building dimensions and panel specifications
def calculate_pv_size(building_length, building_width, roof_angle, panel_width, panel_height, panel_power): # <--- include parameters for building length, width, roof angle, panel width, panel height and panel power
    building_width = ((building_width/2)/math.cos(math.radians(roof_angle))) # m
    max_panels_length = math.floor(building_length/(panel_width/1000))
    max_panels_width = math.floor(building_width/(panel_height/1000))
    max_panels = max_panels_length*max_panels_width
    max_power = max_panels*panel_power/1000
    
    return max_power,max_panels
    



    # <--- return the total PV capacity in kW and number of panels

if __name__ == "__main__":
    # =============================================================================
    # This section is a common way to incorporate code that you want to run if the 
    # script is executed directly, but will be ignored if the script is 
    # imported as a module into another. 
    # 
    # It separates the executable part of the script from the part that defines
    # reusable components e.g. functions.
    # 
    # This is useful way of testing the code or providing examples of how to 
    # use the code.
    # =============================================================================
    
    pv_capacity_kw, num_panels = calculate_pv_size(30, 16, 22, 1690, 1046, 400)
    # <--- call the calculate_pv_size function with appropriate arguments

    print(str(num_panels) +' panels and '+ str(pv_capacity_kw)+' kW max capacity') # <--- Add a print statement to display the number of PV panels and the total PV capacity in kW
