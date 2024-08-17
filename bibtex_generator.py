import requests
from latex_parser import parse_latex_file

def fetch_bibtex_entry(citation_key):
    """
    Fetch BibTeX entry for a given citation key using CrossRef API.

    Args:
    citation_key (str): The citation key to fetch.

    Returns:
    str: BibTeX entry if found, None otherwise.
    """
    base_url = "https://api.crossref.org/works"
    params = {
        "query.bibliographic": citation_key,
        "format": "bibtex"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        if data["message"]["items"]:
            return data["message"]["items"][0]["bibtex"]
        else:
            return None
    except requests.RequestException as e:
        print(f"Error fetching BibTeX entry for {citation_key}: {str(e)}")
        return None

def generate_bibtex_file(latex_file_path, output_file_path):
    """
    Generate a BibTeX file from citations in a LaTeX file.

    Args:
    latex_file_path (str): Path to the LaTeX file.
    output_file_path (str): Path to save the generated BibTeX file.
    """
    citation_keys = parse_latex_file(latex_file_path)
    bibtex_entries = set()

    for key in citation_keys:
        entry = fetch_bibtex_entry(key)
        if entry:
            bibtex_entries.add(entry)

    with open(output_file_path, 'w', encoding='utf-8') as bib_file:
        for entry in bibtex_entries:
            bib_file.write(entry + "\n\n")

def main():
    latex_file = 'path/to/your/latex/file.tex'
    output_file = 'references.bib'
    generate_bibtex_file(latex_file, output_file)
    print(f"BibTeX file generated: {output_file}")

if __name__ == "__main__":
    main()
