import argparse
from bibtex_generator import generate_bibtex_file

def main():
    parser = argparse.ArgumentParser(description="Generate BibTeX file from LaTeX citations")
    parser.add_argument("input_file", help="Path to the input LaTeX file")
    parser.add_argument("-o", "--output", default="references.bib", help="Path to the output BibTeX file (default: references.bib)")
    args = parser.parse_args()

    try:
        generate_bibtex_file(args.input_file, args.output)
        print(f"BibTeX file generated successfully: {args.output}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
