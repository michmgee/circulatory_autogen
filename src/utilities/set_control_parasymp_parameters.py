import numpy as np
import os

# This script sets parameters from assumptions

# model and path
file_prefix = 'control_parasymp'
resources_path = '/lustre/ogunnaike/users/2420/matlab_example/circulatory_autogen/circulatory_autogen_devel_nolibcellml/resources/' #'/home/farg967/Documents/git_projects/CA_user/control_parasymp/resources'

# paths
param_path = os.path.join(resources_path, file_prefix + '_parameters.csv')
param_path_temp = os.path.join(resources_path, file_prefix + '_parameters_temp.csv')

## Define data dictionary

data_dict = {}
data_dict['trunk_C'] = {}
data_dict['arm_L'] = {}
data_dict['arm_R'] = {}
data_dict['leg_L'] = {}
data_dict['leg_R'] = {}
data_dict['anterior_cerebral_L'] = {}
data_dict['anterior_cerebral_R'] = {}
data_dict['middle_cerebral_L'] = {}
data_dict['middle_cerebral_R'] = {}
data_dict['posterior_cerebral_L'] = {}
data_dict['posterior_cerebral_R'] = {}
data_dict['external_carotid_L'] = {}
data_dict['external_carotid_R'] = {}
data_dict['par'] = {}

data_dict['trunk_C']['type'] = 'terminal'
data_dict['arm_L']['type'] = 'terminal'
data_dict['arm_R']['type'] = 'terminal'
data_dict['leg_L']['type'] = 'terminal'
data_dict['leg_R']['type'] = 'terminal'
data_dict['anterior_cerebral_L']['type'] = 'terminal'
data_dict['anterior_cerebral_R']['type'] = 'terminal'
data_dict['middle_cerebral_L']['type'] = 'terminal'
data_dict['middle_cerebral_R']['type'] = 'terminal'
data_dict['posterior_cerebral_L']['type'] = 'terminal'
data_dict['posterior_cerebral_R']['type'] = 'terminal'
data_dict['external_carotid_L']['type'] = 'terminal'
data_dict['external_carotid_R']['type'] = 'terminal'
data_dict['par']['type'] = 'vessel'

## assumptions

# pressures
P_arterial = 1.3e4 # Pa
P_venous = 1.0e3 # Pa
P_pulm = 1.866e3
P_atrial = 0.5e3
P_drop_art_ven = P_arterial - P_venous # Pa TODO make this specific for each vessel
P_drop_pulm = P_pulm - P_atrial

data_dict['trunk_C']['P_drop'] = P_drop_art_ven
data_dict['arm_L']['P_drop'] = P_drop_art_ven
data_dict['arm_R']['P_drop'] = P_drop_art_ven
data_dict['leg_L']['P_drop'] = P_drop_art_ven
data_dict['leg_R']['P_drop'] = P_drop_art_ven
data_dict['anterior_cerebral_L']['P_drop'] = P_drop_art_ven
data_dict['anterior_cerebral_R']['P_drop'] = P_drop_art_ven
data_dict['middle_cerebral_L']['P_drop'] = P_drop_art_ven
data_dict['middle_cerebral_R']['P_drop'] = P_drop_art_ven
data_dict['posterior_cerebral_L']['P_drop'] = P_drop_art_ven
data_dict['posterior_cerebral_R']['P_drop'] = P_drop_art_ven
data_dict['external_carotid_L']['P_drop'] = P_drop_art_ven
data_dict['external_carotid_R']['P_drop'] = P_drop_art_ven
data_dict['par']['P_drop'] = P_drop_pulm

# cardiac output
T = 1.0 # s

# volumes
q_lv_max = 1.5e-4
q_lv_min = 0.5e-4
q_rv_max = 1.5e-4
q_rv_min = 0.5e-4

P_lv_max = 16e3
P_lv_min = 1.5e3
P_rv_max = 3.3e3
P_rv_min = 0.5e4

SV = 1e-4 # m^3
CO = SV/T # m^3/s

# metabolism
C_O2_arterial = 0.2
M_CO2_over_M_O2 = -0.8

# flow fractions

data_dict['trunk_C']['flow_frac'] = 0.46
data_dict['arm_L']['flow_frac'] = 0.06
data_dict['arm_R']['flow_frac'] = 0.06
data_dict['leg_L']['flow_frac'] = 0.12
data_dict['leg_R']['flow_frac'] = 0.12
data_dict['anterior_cerebral_L']['flow_frac'] = 0.02
data_dict['anterior_cerebral_R']['flow_frac'] = 0.02
data_dict['middle_cerebral_L']['flow_frac'] = 0.03
data_dict['middle_cerebral_R']['flow_frac'] = 0.03
data_dict['posterior_cerebral_L']['flow_frac'] = 0.01
data_dict['posterior_cerebral_R']['flow_frac'] = 0.01
data_dict['external_carotid_L']['flow_frac'] = 0.03
data_dict['external_carotid_R']['flow_frac'] = 0.03
data_dict['par']['flow_frac'] = 1.0

print('Total flow percentage: ', np.sum([data_dict[key]['flow_frac'] for key in data_dict.keys()]))
if np.sum([data_dict[key]['flow_frac'] for key in data_dict.keys()]) != 2:
    print('Flow fractions do not sum to 2 (1 for systemic, 1 for pulmonary), exiting')
    exit()


# venous Oxygen concentrations

data_dict['trunk_C']['C_O2_venous'] = 0.155
data_dict['arm_L']['C_O2_venous'] = 0.155
data_dict['arm_R']['C_O2_venous'] = 0.155
data_dict['leg_L']['C_O2_venous'] = 0.155
data_dict['leg_R']['C_O2_venous'] = 0.155
data_dict['anterior_cerebral_L']['C_O2_venous'] = 0.14
data_dict['anterior_cerebral_R']['C_O2_venous'] = 0.14
data_dict['middle_cerebral_L']['C_O2_venous'] = 0.14
data_dict['middle_cerebral_R']['C_O2_venous'] = 0.14
data_dict['posterior_cerebral_L']['C_O2_venous'] = 0.14
data_dict['posterior_cerebral_R']['C_O2_venous'] = 0.14
data_dict['external_carotid_L']['C_O2_venous'] = 0.14
data_dict['external_carotid_R']['C_O2_venous'] = 0.14

# TODO add other assumptions here
k_O2_pulmonary_GE = 1.8e-8
data_dict['pulmonary_GE']['k_O2'] = k_O2_pulmonary_GE

## calculations

# heart 
data_dict['heart'] = {}
data_dict['heart']['type'] = 'heart'

# These assumptions don't work very well at all
# data_dict['heart']['E_lv_B'] = P_lv_min/q_lv_max
# data_dict['heart']['E_lv_A'] = P_lv_max/q_lv_min - data_dict['heart']['E_lv_B'] This assumption doesn't work
# data_dict['heart']['E_rv_B'] = P_rv_min/q_rv_max
# data_dict['heart']['E_rv_A'] = P_rv_max/q_rv_min - data_dict['heart']['E_rv_B']

data_dict['heart']['param_names'] = [] # ['E_lv_B', 'E_lv_A', 'E_rv_B', 'E_rv_A']

# data_dict['heart']['E_lv_B_set'] = False
# data_dict['heart']['E_lv_A_set'] = False
# data_dict['heart']['E_rv_B_set'] = False
# data_dict['heart']['E_rv_A_set'] = False

# flow rates

for key in data_dict.keys():
    
    # Resistances
    if data_dict[key]['type'] in ['terminal', 'vessel']:
        data_dict[key]['flow'] = CO*data_dict[key]['flow_frac']

        data_dict[key]['R'] = data_dict[key]['P_drop']/data_dict[key]['flow']
        if data_dict[key]['type'] == 'vessel':
            data_dict[key]['R_name'] = 'R_' + key
        elif data_dict[key]['type'] == 'terminal':
            data_dict[key]['R_name'] = 'R_T_' + key + '_T'
        else:
            print('Type not recognized for ', key)
        data_dict[key]['R_set'] = False

    # Oxygen consumption rates
    if data_dict[key]['type'] == 'terminal':
        data_dict[key]['M_O2'] = -data_dict[key]['flow']*(C_O2_arterial - data_dict[key]['C_O2_venous'])
        data_dict[key]['M_O2_name'] = 'M_O2_' + key + '_GE'
        data_dict[key]['M_O2_set'] = False

    # CO2 production rates
    if data_dict[key]['type'] == 'terminal':
        data_dict[key]['M_CO2'] = data_dict[key]['M_O2']*M_CO2_over_M_O2
        data_dict[key]['M_CO2_name'] = 'M_CO2_' + key + '_GE'
        data_dict[key]['M_CO2_set'] = False

# TODO Add more calculations here

## Setting parameters in param file

# open file
with open(param_path_temp, 'w') as wf:
    with open(param_path, 'r') as rf:
        for line in rf:
            if line[0] == '#':
                wf.write(line)
            else:
                line_entries = line.split(',')
                param_name = line_entries[0]
                for key in data_dict.keys():
                    if data_dict[key]['type'] in ['heart']:
                        if param_name in data_dict[key]['param_names']:
                            line_entries[2] = str(data_dict[key][param_name])
                            line_entries[3] = 'calc_from_user_assumptions'
                            line = ','.join(line_entries) + '\n'
                            data_dict[key][param_name + '_set'] = True
                            break
                    if data_dict[key]['type'] in ['vessel', 'terminal']:
                        if param_name == data_dict[key]['R_name']:
                            line_entries[2] = str(data_dict[key]['R'])
                            line_entries[3] = 'calc_from_user_assumptions'
                            line = ','.join(line_entries) + '\n'
                            data_dict[key]['R_set'] = True
                            break
                    if data_dict[key]['type'] in ['terminal']:
                        if param_name == data_dict[key]['M_O2_name']:
                            line_entries[2] = str(data_dict[key]['M_O2'])
                            line_entries[3] = 'calc_from_user_assumptions'
                            line = ','.join(line_entries) + '\n'
                            data_dict[key]['M_O2_set'] = True
                            break
                        if param_name == data_dict[key]['M_CO2_name']:
                            line_entries[2] = str(data_dict[key]['M_CO2'])
                            line_entries[3] = 'calc_from_user_assumptions'
                            line = ','.join(line_entries) + '\n'
                            data_dict[key]['M_CO2_set'] = True
                            break
                    ## TODO add other additions here.
                    else:
                        pass
                wf.write(line)

# check if all parameters were set
for key in data_dict.keys():
    for key2 in data_dict[key].keys():
        if key2.endswith('_set'):
            if not data_dict[key][key2]:
                print(key2, ' is False for ', key, 'param has not been set')

# replace old file with new file

os.rename(param_path, param_path.split('.')[0] + '_old.csv')
os.rename(param_path_temp, param_path)


