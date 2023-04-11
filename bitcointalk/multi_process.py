import multiprocessing
import subprocess

# define a function to run each script
def run_script(script):
    subprocess.call(['python', script])

if __name__ == '__main__':
    # list of scripts to run
    scripts = ['bitcointalk/process_1.py', 'bitcointalk/process_2.py', 'bitcointalk/process_3.py', 'bitcointalk/process_4.py']

    # number of processes to create
    num_processes = 4

    # create a pool of processes
    with multiprocessing.Pool(num_processes) as pool:
        # run each script in a separate process
        pool.map(run_script, scripts)

