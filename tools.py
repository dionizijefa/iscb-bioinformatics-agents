from smolagents import tool
from typing import Dict, Union
import subprocess
from pathlib import Path


@tool
def fastqc_tool(input_file: str, output_dir: str) -> Dict[str, Union[str, int]]:
    """
    Perform quality control using FastQC on FASTQ files.

    Args:
        input_file: Path to the FASTQ file
        output_dir: Directory where FastQC results will be stored

    Returns:
        Dictionary containing stdout, stderr, and return code
    """
    result = subprocess.run(
        ["fastqc", input_file, "-o", output_dir], capture_output=True, text=True
    )

    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode,
    }


@tool
def salmon_index_tool(
    transcript_fasta: str, index_dir: str
) -> Dict[str, Union[str, int]]:
    """
    Create a Salmon index from a transcript FASTA file

    Args:
        transcript_fasta: Path to the transcript FASTA file
        index_dir: Directory where the Salmon index will be created

    Returns:
        Dictionary containing stdout, stderr, and return code
    """
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


@tool
def salmon_quantify_tool(
    index_dir: str, reads: str, output_dir: str
) -> Dict[str, Union[str, int]]:
    """
    Quantify transcript abundances using Salmon

    Args:
        index_dir: Path to the Salmon index directory
        reads: Path to the FASTQ reads file
        output_dir: Directory where the quantification results will be stored

    Returns:
        Dictionary containing stdout, stderr, and return code
    """
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


@tool
def read_directory_tool(directory_path: str) -> str:
    """
    List files and directories within a specified directory path.

    Args:
        directory_path: Path to the directory to read

    Returns:
        String representation of the files in the directory with paths relative to working directory
    """
    try:
        path = Path(directory_path)
        contents = list(path.iterdir())

        prefix = (
            f"/{directory_path}"
            if not directory_path.startswith("/")
            else directory_path
        )
        prefix = prefix.rstrip("/")

        files = [f"{prefix}/{item.name}" for item in contents if item.is_file()]
        directories = [f"{prefix}/{item.name}/" for item in contents if item.is_dir()]

        return str(files + directories)
    except Exception as e:
        return str(e)


# list all the tools to be able to export them
bioinformatics_tools = [
    fastqc_tool,
    salmon_index_tool,
    salmon_quantify_tool,
    read_directory_tool,
]
