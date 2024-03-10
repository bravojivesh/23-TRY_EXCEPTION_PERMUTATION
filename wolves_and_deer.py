# Parameters
deer_o = 1.5
wolves_o = 1.5
deer_growth = 2/3
deer_predation = 4/3
wolves_predation = 1
wolves_decay = 1
dt = 0.01  # time step

# Initial populations
deer_n = deer_o
wolves_n = wolves_o

# Simulation loop
num_steps = 10  # Number of time steps
for step in range(num_steps):
    # Update populations
    wolves_n_plus_1 = wolves_n + dt * (wolves_predation * wolves_n * deer_n - wolves_decay * wolves_n)
    deer_n_plus_1 = deer_n + dt * (deer_growth * deer_n - deer_predation * wolves_n * deer_n)

    # Update for next time step
    wolves_n = wolves_n_plus_1
    deer_n = deer_n_plus_1

    # Output population at current time step
    print(f"Step {step + 1}: Wolves = {wolves_n:.2f}, Deer = {deer_n:.2f}")
