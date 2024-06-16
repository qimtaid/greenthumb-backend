
### ENERGY USAGE TRACKER
```
energy-usage-tracker/
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   └── energy_usage.py
    ├── cli.py
    ├── debug.py
    ├── helpers.py
    └── seed.py
```

### `Pipfile`
```toml
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]
pylint = "*"

[packages]
```

### `README.md`
```markdown
# Energy Usage Tracker

## Project Structure

```
energy-usage-tracker/
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   └── energy_usage.py
    ├── cli.py
    ├── debug.py
    ├── helpers.py
    └── seed.py
```

## Description

The Energy Usage Tracker is a command-line interface (CLI) application designed to help users log and monitor their energy usage for different devices. It allows users to log energy usage, generate reports, and keep track of the energy consumption of various devices over time.

## Features

- Log energy usage for different devices.
- Generate reports summarizing total energy usage by device.
- Simple and easy-to-use command-line interface.

## Installation

### Prerequisites

- Python 3.6 or higher
- Pipenv for dependency management

### Steps

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/energy-usage-tracker.git
   cd energy-usage-tracker
   ```

2. Install dependencies using Pipenv:

   ```sh
   pipenv install
   ```

## Usage

### Logging Energy Usage

To log the energy usage of a device, use the `log` command:

```sh
pipenv run python lib/cli.py log --device "DeviceName" --usage UsageAmount --unit UsageUnit
```

Example:

```sh
pipenv run python lib/cli.py log --device "Washing Machine" --usage 1.2 --unit kWh
```

### Generating a Report

To generate a report summarizing the total energy usage by device, use the `report` command:

```sh
pipenv run python lib/cli.py report
```

Example:

```sh
pipenv run python lib/cli.py report
```

### Debugging

For debugging purposes, the application uses logging. You can configure the logging level and view debug messages as needed.

## Project Structure

- **Pipfile**: Pipenv file specifying project dependencies.
- **Pipfile.lock**: Pipenv lock file ensuring reproducible builds.
- **README.md**: Project documentation and usage instructions.
- **lib**: Contains the main application code.
  - **models**: Contains data models for the application.
    - **\_\_init\_\_.py**: Package initialization file.
    - **energy_usage.py**: Defines the `EnergyUsage` and `EnergyUsageTracker` classes.
  - **cli.py**: Command-line interface implementation.
  - **debug.py**: Debugging and logging setup.
  - **helpers.py**: Helper functions (if needed).
  - **seed.py**: Script to seed initial data.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.



## Contact

For any inquiries or support, please contact dan.koskei@student.moringaschool.com 

### How to Run the Application

1. **Clone the Repository and Install Dependencies:**
   ```sh
   git clone https://github.com/yourusername/energy-usage-tracker.git
   cd energy-usage-tracker
   pipenv install
   ```

2. **Seed Initial Data:**
   ```sh
   pipenv run python lib/seed.py
   ```

3. **Log Energy Usage:**
   ```sh
   pipenv run python lib/cli.py log --device "DeviceName" --usage UsageAmount --unit UsageUnit
   ```

   Example:
   ```sh
   pipenv run python lib/cli.py log --device "Washing Machine" --usage 1.2 --unit kWh
   ```

4. **Generate Report:**
   ```sh
   pipenv run python lib/cli.py report
   ```

