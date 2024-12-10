# import opencor as oc
import numpy as np
from opencor_helper import SimulationHelper
import csv
from matplotlib import pyplot as plt

# TODO Finbar
# TODO Make this a simple example of running a cellml model that has been generated.

file_path = "/lustre/ogunnaike/users/2420/matlab_example/circulatory_autogen/circulatory_autogen_devel_nolibcellml/generated_models/control_parasymp/control_parasymp.cellml"
#file_path = "/home/ash252/UoA/RA/Friberg.cellml"
Outputfile_address = "/lustre/ogunnaike/users/2420/matlab_example/circulatory_autogen/circulatory_autogen_devel_nolibcellml/generated_models/control_parasymp_control_parasymp_obs_data/"
plot_var_names_path = "/lustre/ogunnaike/users/2420/matlab_example/circulatory_autogen/circulatory_autogen_devel_nolibcellml/generated_models/control_parasymp_control_parasymp_obs_data/"


"""
names=[]

with open(plot_var_names_path + "Plot_var_names.csv") as file_name:
    file_read = csv.reader(file_name)

    array = list(file_read)

names=[]

for word in array:
    names.append(str(word))

for i in range(len(names)):
    names[i]=re.sub("_T/R_T", " ", names[i])
    names[i] = re.sub("\['", "", names[i])
    names[i] = re.sub("']", "", names[i])
"""

# See slurm-5350335.out in user_run_files/ for list of possible variables
names = ['arterial_chemoreceptor/S_O2_a', 'heart/T_wCont','respiratory_gt/F_O2_A','arterial_chemoreceptor/phi_apc','NTS/f_NTS_ch','NTS/f_NTS_cp','NA/f_NA', 'heart_period_effector/Delta_Tv', 'NTS/f_NTS_ls', 'NTS/f_NTS_br','cardiopulm_receptor/P_pv_P_thor','arm_leg_resistance_effector/Delta_theta','venous_ub/q_us_wCont', 'external_carotid_R_LC/C_O2_a','brachial_L82/u','arterial_chemoreceptor/f_apc','venous_us_volume_effector/f_s'] # 'respiratory_gt/P_O2_A', , 

#x = SimulationHelper(file_path, 0.001, 200, maximumNumberofSteps=1000, pre_time=0) # gives TypeError: __init__() got an unexpected keyword argument 'maximumNumberofSteps'

x = SimulationHelper(file_path, 0.001, 200,solver_info = {'MaximumNumberOfSteps': 5000, 'MaximumStep': 0.0001}, pre_time=0)

x.run()



"""
import matplotlib.pyplot as plt

print(dir(x))
help(x)
print(dir(x.data))
print(names)


# Loop through input_variable and plot the results
for entry in names:
    variable_name = names[0]  
    value = x[1]         

    # Extract the original name from the variable name
    original_name = variable_name.replace("R_T_", "")

    # Plot the result
    plt.figure(figsize=(6, 4))
    plt.bar(variable_name, value, color='blue')
    plt.title(f"Results for {original_name}")
    plt.xlabel("Variable")
    plt.ylabel("Value")
    plt.tight_layout()

    
    # Create the directory if it doesn't exist
    os.makedirs(Outputfile_address, exist_ok=True)

    # Save the figure with a filename based on the name
    filename = os.path.join(Outputfile_address, f"{original_name}_results.png")
    plt.savefig(filename, format='png', bbox_inches='tight')
    plt.close()  # Close the figure to avoid memory issues


"""


input_variable=[]

# plot
pre_time = 30.6
sim_time = 6.0
dt = 0.01
max_step = 0.0001


tSim = x.tSim - pre_time

result = x.get_results(names) # x.get_results(array[i])  # Get the result
print(result)

filenames = ['arterial_chemoreceptor-S_O2_a21', 'heart-T_wCont21','respiratoryGT-FO2_A21','arterial_chemoreceptor-phi_apc21', 'NTS-f_NTS_ch21','NTS-f_NTS_cp21','NA-f_NA21','heart_period_effector-Delta_Tv21', 'NTS-f_NTS_ls21', 'NTS-f_NTS_br21','cardiopulm_receptor-P_pv_P_thor21', 'arm_leg_resistance_effector-Delta_theta21','venous_ub-q_us_wCont21', 'external_carotid_R_LC-C_O2_21','brachial_L82-u21','chemoreceptor-f_apc21','venous_us_volume_effector-f_s21']
# 'arm_R_T-u', 'respiratoryGT-PO2_A',
for i in range(len(names)):
    #print(names[i])
    #result = np.array(x.get_results(array[i]))
    #input_variable.append(["R_T_" + names[i], x.get_results(array[i])[0, -1]])
    print(f"Processing: {names[i]}")


    # Access the last element of the first array in the first sublist
    value = np.array(result[i][0])
    print(value)
    # find where t > 0 (after simulation has reached steady state)
    sim_indices = np.where(tSim > 0)
    
    """
    if i == 0:
      value = value/133.32 # convert J/m3 to mm Hg
      print('Mean arm BP:')
      BP_ss = value[sim_indices]
      print(np.mean(BP_ss))
      print('SBP (max BP):')
      print(np.max(BP_ss))
      """
    if i == 0:
      print('Mean S_O2_a: ')
      S_O2_a_ss = value[sim_indices]
      print(np.mean(S_O2_a_ss))
    elif i == 1:
      meanRR = np.mean(value[sim_indices])
      print('Mean RR:')
      print(meanRR)
      print('Mean HR:')
      print(60/meanRR)
      """
    elif i == 3:
      meanPO2_A = np.mean(value[sim_indices])
      print('Mean PO2_A')
      print(meanPO2_A)
      """
    
    plt.plot(tSim[sim_indices],value[sim_indices])
    plt.xlabel('Time (s)')
    plt.ylabel(names[i])
    filename = os.path.join(Outputfile_address, f"{filenames[i]}_results.png")
    plt.savefig(filename, format='png', bbox_inches='tight')
    plt.close()  # Close the figure to avoid memory issues
    print("saving figure")
    
    # Calculate mean SpO2(%), HR (bpm) at 9.6% O2 over 5 min after steady-state
    # Calculate mean SBP (mm Hg) at 12% O2, no protocol specified by Fox 2006 
    
    input_variable.append([names[i], value])
    
    

print(input_variable)


with open (Outputfile_address+'elic_results.csv','w',newline = '') as csvfile:
    my_writer = csv.writer(csvfile, delimiter = ' ');
    my_writer.writerows(input_variable)





#y = x.get_results(['medial_occipital_occipitotemporal_branch_T52_L190_T/R_T'])[0, -1]
#print(y)




