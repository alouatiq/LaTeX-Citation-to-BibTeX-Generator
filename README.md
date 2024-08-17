# LaTeX Citation to BibTeX Generator

This tool parses LaTeX files to extract citation keys, fetches corresponding BibTeX entries from the CrossRef API, and generates a BibTeX file.

## Installation

1. Ensure you have Python 3.6+ installed on your system.

2. Install the required dependencies:

```bash
sudo apt-get update
sudo apt-get install -y texlive-full python3-pip
pip3 install requests
```

3. Clone this repository or download the source files.

## Usage

Run the tool from the command line using the following syntax:

```bash
python3 cli_tool.py input_file [-o output_file]
```

Arguments:
- `input_file`: Path to the input LaTeX file (required)
- `-o`, `--output`: Path to the output BibTeX file (optional, default: references.bib)

## Examples

1. Generate a BibTeX file with the default name (references.bib):

```bash
python3 cli_tool.py path/to/your/latex_file.tex
```

2. Generate a BibTeX file with a custom name:

```bash
python3 cli_tool.py path/to/your/latex_file.tex -o custom_bibliography.bib
```

## Error Handling

The tool provides error messages for common issues such as:
- File not found
- API request failures
- General exceptions during execution

If you encounter any issues, please check the error messages for guidance.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
