# ISCB-Africa ASBCB 2025 Tutorial IP5: Building Agentic workflows in bioinformatics
This repo contains materials for the tutorial session - Tutorial IP5: Building agentic 
workflows for bioinformatics. \
https://www.iscb.org/africa2025/home

## Tutorial description
Agentic workflow is a process of interacting with Large Language Models (LLMs) to complete complex tasks - allowing practitioners to build pipelines that integrate data retrieval, reasoning, and execution steps. This tutorial guides participants through the conceptual and practical foundations of setting up their own agentic workflows.

## Dataset
Dataset is taken from 
https://github.com/GoekeLab/bioinformatics-workflows
which contains RNA-Seq reads and a transcriptome reference file.

## Requirements
Either Docker or Conda/Mamba environment. You don't need both.
1. The tutorial can be run inside the Docker container. The easiest way to make sure it will work on your system is to have Docker setup on your machine.
2. Setup a Conda/Mamba environment. If you haven't done this you can follow the instruction and use miniforge to install it https://github.com/conda-forge/miniforge

### Clone this repository
```bash
git clone https://github.com/dionizijefa/iscb-bioinformatics-agents.git
cd iscb-bioinformatics-agents
```

### Conda/Mamba instruction
```bash
mamba env create -f environment.yml
mamba activate bio-agent
```

### Docker instructions
If running from command line
1. Build the image
```bash
docker build -t bio-agent .
```

2. Run the directory and mount a drive
```bash
docker run -it --volume $(pwd):/app bio-agent
```

3. Don't forget to activate the micromamba environment
```bash
micromamba activate bio-agent
```

## Running the tutorial code
The default setup requires you to use an Azure API key. To do that create a .key file in the root directory and paste the given key inside of it. After that you can create a results folder if you wish

```bash
mkdir results
```

Then you just run the agent with

```bash
python agent.py
```