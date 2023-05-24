#!/usr/bin/env python3
import subprocess
import sys

def run_command(cmd_name):
    args = sys.argv[2:]  # Extract arguments after the subcommand
    command = [cmd_name, *args]

    # Print the generated command
    print(f"Executing command: {' '.join(command)}")

    # Run the command and capture the output
    completed_process = subprocess.run(command, capture_output=True, text=True)

    # Print the output of the command
    print(completed_process.stdout)
    if completed_process.stderr:
        print(completed_process.stderr)

def run_subcommand(subcommand):
    allowed_commands = ["alimask", "hmmbuild", "hmmemit", "hmmlogo", "hmmpgmd_shard", 
                        "hmmscan", "hmmsim", "jackhmmer", "nhmmer", "phmmer", 
                        "hmmalign", "hmmconvert", "hmmfetch", "hmmpgmd", "hmmpress", 
                        "hmmsearch", "hmmstat", "makehmmerdb", "nhmmscan",
                        "guppy_aligner", "guppy_barcoder", "guppy_basecall_client", 
                        "guppy_basecaller", "guppy_basecaller_duplex", 
                        "guppy_basecaller_supervisor", "guppy_basecall_server", 
                        "bam_convert", "minimap2", "ITSx"]

    if subcommand in allowed_commands:
        run_command(subcommand)
    else:
        print(f"Unknown subcommand: {subcommand}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a subcommand.")
        sys.exit(1)

    subcommand = sys.argv[1]
    print(f"Executing subcommand: {subcommand}")
    run_subcommand(subcommand)