if [[ $# -eq 0 ]] ; then
    echo 'usage is ./run_param_id.sh num_processors'
    exit 1
fi
source opencor_pythonshell_path.sh
./run_autogeneration.sh
mpiexec -n $1 /lustre/ogunnaike/sw/opencor-2022-05-23/0.7.1/pythonshell ../src/scripts/param_id_run_script.py

