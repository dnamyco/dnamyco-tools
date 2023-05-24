# DNAMA-Tools Docker Image

This Docker image is specifically crafted to enable smooth operation of the DNAMA-Tools suite. The suite includes ITSx for identifying and extracting Internal Transcribed Spacer (ITS) sequences from genomic data, HMMER for biosequence analysis, and Guppy, an Oxford Nanopore basecaller tool for reading sequencing data. These tools are encased in a robust, containerized environment based on Fedora Linux, allowing seamless bioinformatics workflow.

## System Requirements

- Docker: Docker software must be installed and running on your system. For a comprehensive guide on installation, please refer to the Docker documentation: [Get Docker](https://docs.docker.com/get-docker/)
- Graphics Processing Unit (GPU): If you have a GPU and wish to leverage it for computations, especially when running Guppy, ensure that the appropriate Nvidia drivers and Nvidia Docker are installed. For instructions, visit the official Nvidia Docker GitHub page: [Nvidia Docker](https://github.com/NVIDIA/nvidia-docker)

Note: If you do not have a GPU or do not wish to use one, or if you're running Docker on a non-Linux system, you can simply skip the GPU-related steps and commands.

## Instructions for Use

### Download the Docker Image

To fetch the DNAMA-Tools Docker image from the image registry, open your terminal and execute the following command:

```bash
docker pull dnama-tools:latest
```

### Executing Commands

The DNAMA-Tools Docker image supports a range of commands for different tools included in the suite:

## Subcommands

The DNAMA-Tools Docker image supports a range of subcommands corresponding to different tools included in the suite. Here's a list of the current supported subcommands:

### ITSx
- `ITSx`: Command for ITSx tool for identifying and extracting Internal Transcribed Spacer (ITS) sequences from genomic data.

### HMMER
- `alimask`
- `hmmbuild`
- `hmmemit`
- `hmmlogo`
- `hmmpgmd_shard`
- `hmmscan`
- `hmmsim`
- `jackhmmer`
- `nhmmer`
- `phmmer`
- `hmmalign`
- `hmmconvert`
- `hmmfetch`
- `hmmpgmd`
- `hmmpress`
- `hmmsearch`
- `hmmstat`
- `makehmmerdb`
- `nhmmscan`

### Guppy
- `guppy_aligner`
- `guppy_barcoder`
- `guppy_basecall_client`
- `guppy_basecaller`
- `guppy_basecaller_duplex`
- `guppy_basecaller_supervisor`
- `guppy_basecall_server`

### Others
- `bam_convert`
- `minimap2`

You can pass any of these subcommands after `dnama-tools:latest` in the `docker run` command, followed by the appropriate arguments for the subcommand. For example:

```bash
docker run -v /path/to/input:/data -v /path/to/output:/output dnama-tools:latest hmmscan <arguments>
```

In the command above, `hmmscan` is a subcommand for running the HMMER tool. Replace `<arguments>` with the arguments you want to pass to the `hmmscan` command.

## Contribution Guide

If you'd like to contribute to the development of this Docker image, please follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your/repo.git
```

2. Apply necessary modifications to the Dockerfile or other relevant files.

3. Build the Docker image using the Dockerfile:

```bash
docker build -t dnama-tools:latest .
```

4. Test the image locally to ensure it operates as expected:

```bash
docker run dnama-tools:latest itsx --help
```

5. If everything functions correctly, commit your changes and push them to your repository.

6. Submit a pull request with your changes to the original repository.
