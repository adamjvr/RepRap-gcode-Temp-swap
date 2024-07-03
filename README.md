# RepRap-gcode-Temp-swap

## Overview

This Python script allows you to modify the temperature settings in a G-code file used by 3D printers. It supports different G-code flavors including Marlin, Marlin2, Repetier, and UltiGCode. The script updates the nozzle and bed temperatures based on the values provided via command-line arguments.

## Features

- Modify nozzle and bed temperatures in G-code files.
- Support for multiple G-code flavors: Marlin, Marlin2, Repetier, and UltiGCode.
- Easy to use via command-line interface.

## Requirements

- Python 3.x

## Usage

### Command-Line Arguments

The script accepts the following command-line arguments:

1. `gcode_file`: Path to the input G-code file.
2. `gcode_flavor`: The flavor of the G-code (e.g., 'Marlin', 'Marlin2', 'Repetier', 'UltiGCode').
3. `new_bed_temp`: New bed temperature (in degrees Celsius).
4. `new_nozzle_temp`: New nozzle temperature (in degrees Celsius).
5. `output_file`: Path to the output G-code file.

### Example Commands

#### Marlin Flavor

```sh
python modify_gcode.py input.gcode Marlin 60 200 output.gcode
```

```sh
python modify_gcode.py input.gcode Marlin2 70 210 output.gcode
```

```sh
python modify_gcode.py input.gcode UltiGCode 55 195 output.gcode
```
## Script Explanation

### `parse_arguments`

This function parses the command-line arguments provided to the script. It returns the parsed arguments including the G-code file path, G-code flavor, new bed temperature, new nozzle temperature, and output file path.

### `modify_gcode`

This function modifies the temperature settings in the given G-code file based on the specified G-code flavor. It reads the input G-code file, modifies the relevant temperature commands, and writes the modified lines to the output file.

### `main`

The main function to parse arguments and call the `modify_gcode` function with those arguments.

### Script Entry Point

The `if __name__ == "__main__":` construct ensures that the `main` function is called only when the script is executed directly, not when imported as a module.

## How to Run the Script

1. Make sure you have Python 3 installed on your system.
2. Save the script as `modify_gcode.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the script.
5. Run the script using one of the example commands provided above, replacing the arguments with your desired values.

## License
GPL V3 License 