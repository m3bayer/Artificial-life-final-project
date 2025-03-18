# Differentiable MPM Simulation

This repository contains a differentiable Material Point Method (MPM) simulation implemented using Taichi. The code enables the simulation of soft-body materials with actuators, allowing for optimization using gradient-based techniques.

## Features
- Implements a differentiable MPM simulation.
- Supports soft-body physics with actuation.
- Uses Taichi for high-performance parallel computing.
- Allows for procedural generation and mutation of robot structures.
- Includes a script to automate multiple runs.

## Requirements
Before running the code, install the necessary dependencies:
```bash
pip install taichi numpy matplotlib
```

## Files
- **diffmpm.py**: The main script containing the MPM simulation logic.
- **subprocess_runner.py**: A helper script to run the simulation multiple times.

## Usage
### Running the Simulation
To run the simulation, execute:
```bash
python diffmpm.py --iters 50
```
This will perform 50 optimization iterations and save the results.

### Running Multiple Iterations
To automate multiple runs, use:
```bash
python subprocess_runner.py
```
This will execute `diffmpm.py` 10 times sequentially.

## Configuration
### Simulation Parameters
Key parameters can be adjusted in `diffmpm.py`:
- `n_particles`: Number of particles in the simulation.
- `n_grid`: Grid resolution.
- `dt`: Time step.
- `gravity`: Gravity strength.
- `act_strength`: Actuation strength.
- `max_steps`: Maximum simulation steps.

### Robot Structure
The robot's structure is generated using a procedural method with an actuator-based design. The seed matrix can be customized in the `robot` function.

## Output
- The simulation outputs images visualizing the particle positions.
- A loss value is printed to monitor optimization progress.
- The final structure seed is saved to `output.txt`.

## License
This project is released under the MIT License.

