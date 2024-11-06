#!/bin/bash -l
#
#SBATCH --nodes=1 --ntasks=8 --cpus-per-task=1
#
#
#SBATCH --mem=72G
# SBATCH --mem-per-cpu=32000M
#
# SBATCH --tmp=24G
#
#SBATCH --job-name=test_param_id
#
#
#SBATCH --partition=idle
#
#          d-hh:mm:ss
#SBATCH --time=0-10:40:00
#
#
#
# SBATCH --output=%x-%j.out
# SBATCH --error=%x-%j.out
#
# [EDIT] Slurm can send emails to you when a job transitions through various
#        states: NONE, BEGIN, END, FAIL, REQUEUE, ALL, TIME_LIMIT,
#        TIME_LIMIT_50, TIME_LIMIT_80, TIME_LIMIT_90, ARRAY_TASKS.  One or more
#        of these flags (separated by commas) are permissible for the
#        --mail-type flag.  You MUST set your mail address using --mail-user
#        for messages to get off the cluster.
#
#SBATCH --mail-user='mmgee@udel.edu'
#SBATCH --mail-type=ALL
#
#
#SBATCH --export=NONE
#
#
#UD_QUIET_JOB_SETUP=YES
#
#job_exit_handler() {
#  # Copy all our output files back to the original job directory:
#  cp * "$SLURM_SUBMIT_DIR"
#
#  # Don't call again on EXIT signal, please:
#  trap - EXIT
#  exit 0
#}
#export UD_JOB_EXIT_FN=job_exit_handler
#
#export UD_JOB_EXIT_FN_SIGNALS="SIGTERM EXIT"

#UD_PREFER_MEM_PER_CPU=YES
#
#        Uncomment the following variable if the job mandates a per-CPU memory
#        limit to be present or calculable when UD_PREFER_MEM_PER_CPU is set:
#UD_REQUIRE_MEM_PER_CPU=YES

#
# If you have VALET packages to load into the job environment,
# uncomment and edit the following line:
#
#vpkg_require intel/2019


# vpkg_require anaconda
# old one: conda activate /home/2420/.conda/neuron/20230515
# vpkg_require neuron
# nrnivmodl mod
# vpkg_require neuron
vpkg_rollback
vpkg_require opencor-2022-05-23
vpkg_require openmpi

#
# Do general job environment setup:
#
. /opt/shared/slurm/templates/libexec/common.sh

#
./run_param_id.sh 8

