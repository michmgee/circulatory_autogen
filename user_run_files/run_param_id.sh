if [[ $# -eq 0 ]] ; then
    echo 'usage is ./run_param_id.sh num_processors'
    exit 1
fi
source opencor_pythonshell_path.sh
./run_autogeneration.sh
pyinstaller --onefile --copy-metadata pyproj "param_id_run_script.py"
/lustre/ogunnaike/sw/opencor/0.7.1/pythonshell ../src/scripts/param_id_run_script.py

