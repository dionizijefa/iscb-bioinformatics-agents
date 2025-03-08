TOOLS = {
    "fastqc": {
        "description": "Perform quality control using FastQC on FASTQ files",
        "command": ["fastqc", "{input_file}", "-o", "{output_dir}"],
        "inputs": {
            "input_file": {
                "type": "string",
                "description": "Path to the FASTQ file",
                "required": True,
            },
            "output_dir": {
                "type": "string",
                "description": "Directory where FastQC results will be stored",
                "required": True,
            },
        },
    },
    "salmon_index": {
        "description": "Create a Salmon index from a transcript FASTA file",
        "command": ["salmon", "index", "-t", "{transcript_fasta}", "-i", "{index_dir}"],
        "inputs": {
            "transcript_fasta": {
                "type": "string",
                "description": "Path to the transcript FASTA file",
                "required": True,
            },
            "index_dir": {
                "type": "string",
                "description": "Directory where the Salmon index will be created",
                "required": True,
            },
        },
    },
    "salmon_quantify": {
        "description": "Quantify transcript abundances using Salmon",
        "command": [
            "salmon",
            "quant",
            "-i",
            "{index_dir}",
            "-l",
            "A",
            "-r",
            "{reads}",
            "-o",
            "{output_dir}",
        ],
        "inputs": {
            "index_dir": {
                "type": "string",
                "description": "Path to the Salmon index directory",
                "required": True,
            },
            "reads": {
                "type": "string",
                "description": "Path to the FASTQ reads file",
                "required": True,
            },
            "output_dir": {
                "type": "string",
                "description": "Directory where the quantification results will be stored",
                "required": True,
            },
        },
    },
}
