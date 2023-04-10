import multiprocessing
import subprocess

# define a function to run each script
def run_script(script):
    subprocess.call(['/usr/bin/python3', script])

if __name__ == '__main__':
    # list of scripts to run
    scripts = ['process_1_aws.py', 'process_2_aws.py', 'process_3_aws.py', 'process_4_aws.py']

    # number of processes to create
    num_processes = 4

    # create a pool of processes
    with multiprocessing.Pool(num_processes) as pool:
        # run each script in a separate process
        pool.map(run_script, scripts)

