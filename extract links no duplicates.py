import re

def extract_links_from_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        content = input_file.read()

    # Regular expression pattern to match URLs
    url_pattern = re.compile(r'https?://\S+')

    # Find all matches of URLs in the file content
    links = re.findall(url_pattern, content)

    # Remove duplicates while preserving the order
    links = list(dict.fromkeys(links))

    with open(output_file_path, 'w') as output_file:
        for link in links:
            output_file.write(link + '\n')

    print("Links extracted and saved to", output_file_path)

# Example usage
input_file_path = 'input.txt'  # Replace with your input file path
output_file_path = 'output.txt'  # Replace with your desired output file path

extract_links_from_file(input_file_path, output_file_path)
