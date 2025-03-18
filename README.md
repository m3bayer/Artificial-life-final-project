# Evolutionary Differentiable MPM Simulation

This repository contains a differentiable Material Point Method (MPM) simulation implemented using Taichi. The code enables the simulation of soft-body materials with actuators, allowing for optimization using gradient-based techniques and evolution of robot form and movement.

## Features
- Implements a differentiable MPM simulation.
- Supports soft-body physics with actuation.
- Allows for procedural generation and mutation of robot structures.
- Uses an evolutionary algorithm to refine robot designs over multiple generations.
- Includes a script to automate evolutionary optimization.

## Requirements
Before running the code, install the necessary dependencies:
```bash
pip install taichi numpy matplotlib
```

## Files
- **diffmpm.py**: The main script containing the MPM simulation logic, along with the code for robot form generation, mutation, and evaluation.
- **subprocess_runner.py**: A helper script to run the simulation multiple times, enabling the evolutionary loop across generations.

## Evolutionary Algorithm
The system follows an evolutionary approach to optimize soft robots by refining their structure and actuation over multiple generations:

### 1. **Initialize Population**
   - A population of robots is created, each represented as a matrix-based design space.
   - Matrix values correspond to different robot components, including actuators and soft material.

### 2. **Simulation & Fitness Evaluation**
   - Each robot is simulated using the differentiable MPM method.
   - Gradient-based learning optimizes actuation patterns to improve movement.
   - The distance traveled by each robot is recorded as its fitness score.

### 3. **Selection & Mutation**
   - The best-performing robot is selected based on fitness evaluation.
   - A mutation process is applied to create a new generation of robots:
     - Each value in the robot’s matrix has a probability of mutating into an adjacent component type.
     - New variations of the best robot are generated, forming the next generation.

### 4. **Iteration**
   - The cycle repeats over multiple generations, progressively evolving robot forms and movement strategies.

## Configuration
### Simulation Parameters
Key parameters can be adjusted in `diffmpm.py` and `subprocess_runner.py`:
- `mutation_rate`: Controls the probability of changes in robot structure.
- `num_generations`: Determines the number of evolutionary iterations.
- `population_size`: Defines the number of robots per generation.
- `act_strength`: Modifies the intensity of actuation forces.

### Robot Structure
- The robot's structure is represented as a 2D matrix where each cell can hold different robot components.
- Procedural generation initializes these matrices randomly or based on predefined seed structures.
- Mutation enables gradual structural evolution by modifying matrix values.

## Running the Evolutionary Simulation
To run the full evolutionary loop:
```bash
python subprocess_runner.py
```
This will execute `diffmpm.py` multiple times sequentially, simulating the evolution of robot structures.

## Output
- The simulation outputs images visualizing the particle positions.
- A loss value (fitness score) is printed to monitor optimization progress.
- The best structure seed from each generation is saved to `output.txt`.

## Challenges & Considerations
- **Mutation Rate Balance:** Too high a mutation rate leads to instability, while too low a rate hinders evolution.
- **Actuation Optimization:** Learning how to best integrate differentiable MPM with evolutionary learning requires tuning.
- **Computation Costs:** Running multiple generations requires significant computational resources.

## License
This project is released under the MIT License.

