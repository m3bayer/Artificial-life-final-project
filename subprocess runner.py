import subprocess

# Number of times to run the script
num_runs = 10

# Path to the script to run
script_name = "diffmpm.py"

for i in range(num_runs):
    print(f"Running {script_name}, iteration {i + 1}/{num_runs}")
    subprocess.run(["python", script_name])  # Runs the script
