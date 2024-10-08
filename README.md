# 📦 Project1-Telcom2300

This repository contains two Python scripts for simulating packet queues in network routers with both constant and variable arrival rates. 📊

## 📁 Folders and Files

### 1. Constant Input Rate Event Simulator

- **`eventSimulator_constantInput.py`**:  
   Simulates a packet queue system with constant input rates. It takes three arguments from the command line: the arrival rate, departure rate, and buffer size. The simulation runs for a specified number of events (default: 1,000,000) and tracks the number of packets in the queue and the number of packets dropped at each step.  
   After the simulation, it generates a plot showing the number of packets in the queue and the number of packets dropped over the simulation steps. It also saves the simulation results to a TXT file with the same name as the plot file but with a `.txt` extension.

- **Output**:  
   Includes a series of PNG files that visualize the simulation results and TXT files showing the number of packets in the queue, the number of packets dropped, and the steps.

### 2. Variable Input Rate Event Simulator

- **`eventSimulator_VariableInput.py`**:  
   Defines a simulation of variable arrival rate events in a packet queue system. It determines the arrival rate based on the current event number and simulates packet arrivals and departures according to the arrival and departure rates, respectively. The simulation tracks the number of packets in the queue and the number of packets dropped at each step, writing the results to a TXT file.

- **`plotForVariableInputSimulator.py`**:  
   Reads the simulation results from the specified file and generates a line plot using Seaborn and Matplotlib. It visualizes the queue length and the number of dropped packets over the simulation steps, providing insights into the system's behavior under variable arrival rates. The plot is saved as a PNG file with a filename based on the input file's name.


## 🚀 Usage

To run the simulations, simply execute the scripts with Python


### Constant Input Rate Simulator
```bash
python eventSimulator_constantInput.py 30 50 50
python eventSimulator_constantInput.py 30 50 100
python eventSimulator_constantInput.py 30 50 150

python eventSimulator_constantInput.py 30 100 50
python eventSimulator_constantInput.py 30 100 100
python eventSimulator_constantInput.py 30 100 150

python eventSimulator_constantInput.py 30 120 50
python eventSimulator_constantInput.py 30 120 100
python eventSimulator_constantInput.py 30 120 150

python eventSimulator_constantInput.py 80 50 50
python eventSimulator_constantInput.py 80 50 100
python eventSimulator_constantInput.py 80 50 150

python eventSimulator_constantInput.py 80 100 50
python eventSimulator_constantInput.py 80 100 100
python eventSimulator_constantInput.py 80 100 150

python eventSimulator_constantInput.py 80 120 50
python eventSimulator_constantInput.py 80 120 100
python eventSimulator_constantInput.py 80 120 150

python eventSimulator_constantInput.py 120 50 50
python eventSimulator_constantInput.py 120 50 100
python eventSimulator_constantInput.py 120 50 150

python eventSimulator_constantInput.py 120 100 50
python eventSimulator_constantInput.py 120 100 100
python eventSimulator_constantInput.py 120 100 150

python eventSimulator_constantInput.py 120 120 50
python eventSimulator_constantInput.py 120 120 100
python eventSimulator_constantInput.py 120 120 150

```

Variable Input Rate Simulator

- python eventSimulator_VariableInput.py
- python plotForVariableInputSimulator.py


  
📦 Requirements

- Python 3.x
- Pandas
- Seaborn
- Matplotlib
- 
Make sure to install the required libraries before running the scripts:

- pip install pandas seaborn matplotlib

- **Output**:  
   The simulation results are saved in a TXT file with step-wise packet queue and dropped packet counts. Additionally, a PNG plot visualizes queue length and dropped packets over steps, aiding in understanding system behavior under variable arrival rates.

