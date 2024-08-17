import re

def parse_latex_file(file_path):
    """
    Parse a LaTeX file and extract citation keys.
    
    Args:
    file_path (str): Path to the LaTeX file.
    
    Returns:
    list: A list of unique citation keys found in the file.
    """
    citation_pattern = r'\\cite(?:\[.*?\])?{(.*?)}'
    citation_keys = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Find all citations
        matches = re.findall(citation_pattern, content)
        
        # Extract and clean citation keys
        for match in matches:
            keys = [key.strip() for key in match.split(',')]
            citation_keys.extend(keys)
        
        # Remove duplicates and return
        return list(set(citation_keys))
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred while parsing the file: {str(e)}")
        return []

def main():
    # Example usage
    latex_file = 'path/to/your/latex/file.tex'
    citations = parse_latex_file(latex_file)
    
    if citations:
        print("Found citations:")
        for citation in citations:
            print(f"- {citation}")
    else:
        print("No citations found or an error occurred.")

if __name__ == "__main__":
    main()
