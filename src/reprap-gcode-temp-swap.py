import argparse

def parse_arguments():
    """
    Parses the command-line arguments provided to the script.
    
    Returns:
        argparse.Namespace: Parsed command-line arguments including:
            - gcode_file: Path to the input G-code file.
            - gcode_flavor: The flavor of the G-code (e.g., 'Marlin', 'Marlin2', 'Repetier', 'UltiGCode').
            - new_bed_temp: New bed temperature.
            - new_nozzle_temp: New nozzle temperature.
            - output_file: Path to the output G-code file.
    """
    # Create the parser
    parser = argparse.ArgumentParser(description="Modify temperature settings in a G-code file.")
    
    # Add arguments
    parser.add_argument("gcode_file", type=str, help="Path to the input G-code file.")
    parser.add_argument("gcode_flavor", type=str, choices=['Marlin', 'Marlin2', 'Repetier', 'UltiGCode'], help="G-code flavor (e.g., 'Marlin', 'Marlin2', 'Repetier', 'UltiGCode').")
    parser.add_argument("new_bed_temp", type=int, help="New bed temperature.")
    parser.add_argument("new_nozzle_temp", type=int, help="New nozzle temperature.")
    parser.add_argument("output_file", type=str, help="Path to the output G-code file.")
    
    # Parse the arguments and return
    return parser.parse_args()

def modify_gcode(gcode_file, gcode_flavor, new_bed_temp, new_nozzle_temp, output_file):
    """
    Modifies the temperature settings in the given G-code file based on the specified G-code flavor.

    Args:
        gcode_file (str): Path to the input G-code file.
        gcode_flavor (str): The flavor of the G-code (e.g., 'Marlin', 'Marlin2', 'Repetier', 'UltiGCode').
        new_bed_temp (int): New bed temperature to set.
        new_nozzle_temp (int): New nozzle temperature to set.
        output_file (str): Path to the output G-code file.
    """
    # Open the input G-code file in read mode
    with open(gcode_file, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

    # Initialize a list to hold the modified lines
    modified_lines = []

    # Loop through each line in the original G-code file
    for line in lines:
        # Check the flavor of G-code to determine how to modify the temperature settings
        if gcode_flavor == "Marlin" or gcode_flavor == "Marlin2" or gcode_flavor == "Repetier":
            # Marlin, Marlin2, and Repetier firmware use the following commands for temperature control:
            # M104: Set nozzle temperature
            # M109: Wait for nozzle temperature to reach target
            # M140: Set bed temperature
            # M190: Wait for bed temperature to reach target
            if line.startswith("M104"):  # Set nozzle temperature
                line = f"M104 S{new_nozzle_temp}\n"
            elif line.startswith("M109"):  # Wait for nozzle temperature
                line = f"M109 S{new_nozzle_temp}\n"
            elif line.startswith("M140"):  # Set bed temperature
                line = f"M140 S{new_bed_temp}\n"
            elif line.startswith("M190"):  # Wait for bed temperature
                line = f"M190 S{new_bed_temp}\n"
        elif gcode_flavor == "UltiGCode":
            # UltiGCode uses comments for setting temperatures:
            # ;TYPE:START
            # ;BED:TEMP=<temperature>
            # ;NOZZLE:TEMP=<temperature>
            if ";BED:TEMP=" in line:
                line = f";BED:TEMP={new_bed_temp}\n"
            elif ";NOZZLE:TEMP=" in line:
                line = f";NOZZLE:TEMP={new_nozzle_temp}\n"

        # Append the (potentially modified) line to the list of modified lines
        modified_lines.append(line)

    # Open the output file in write mode
    with open(output_file, 'w') as file:
        # Write all the modified lines to the output file
        file.writelines(modified_lines)

def main():
    """
    Main function to parse arguments and call the modify_gcode function with those arguments.
    """
    # Parse the command-line arguments
    args = parse_arguments()
    
    # Call the modify_gcode function with the parsed arguments
    modify_gcode(args.gcode_file, args.gcode_flavor, args.new_bed_temp, args.new_nozzle_temp, args.output_file)

# This is the entry point of the script
if __name__ == "__main__":
    main()
