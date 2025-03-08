import smolagents
from typing import Dict, Union


class FastQCTool(smolagents.Tool):
    name = "fastqc"
    description = "Perform quality control using FastQC on FASTQ files."
    inputs = {
        "input_file": {"type": "string", "description": "Path to the FASTQ file"},
        "output_dir": {
            "type": "string",
            "description": "Directory where FastQC results will be stored",
        },
    }
    output_type = "string"

    def forward(self, input_file: str, output_dir: str) -> Dict[str, Union[str, int]]:
        import subprocess

        result = subprocess.run(
            ["fastqc", input_file, "-o", output_dir], capture_output=True, text=True
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
        }


class SalmonIndexTool(smolagents.Tool):
    name = "salmon_index"
    description = "Create a Salmon index from a transcript FASTA file"
    inputs = {
        "transcript_fasta": {
            "type": "string",
            "description": "Path to the transcript FASTA file",
        },
        "index_dir": {
            "type": "string",
            "description": "Directory where the Salmon index will be created",
        },
    }
    output_type = "string"

    def forward(
        self, transcript_fasta: str, index_dir: str
    ) -> Dict[str, Union[str, int]]:
        import subprocess

        result = subprocess.run(
            ["salmon", "index", "-t", transcript_fasta, "-i", index_dir],
            capture_output=True,
            text=True,
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
        }


class SalmonQuantifyTool(smolagents.Tool):
    name = "salmon_quantify"
    description = "Quantify transcript abundances using Salmon"
    inputs = {
        "index_dir": {
            "type": "string",
            "description": "Path to the Salmon index directory",
        },
        "reads": {"type": "string", "description": "Path to the FASTQ reads file"},
        "output_dir": {
            "type": "string",
            "description": "Directory where the quantification results will be stored",
        },
    }
    output_type = "string"

    def forward(
        self, index_dir: str, reads: str, output_dir: str
    ) -> Dict[str, Union[str, int]]:
        import subprocess

        result = subprocess.run(
            [
                "salmon",
                "quant",
                "-i",
                index_dir,
                "-l",
                "A",
                "-r",
                reads,
                "-o",
                output_dir,
            ],
            capture_output=True,
            text=True,
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
        }


fastqc_tool = FastQCTool()
salmon_index_tool = SalmonIndexTool()
salmon_quantify_tool = SalmonQuantifyTool()

bioinformatics_tools = [
    fastqc_tool,
    salmon_index_tool,
    salmon_quantify_tool,
]
