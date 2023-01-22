import argparse
from pandoc import Document

def convert_file(input_file, output_file):
    # Load the text file
    with open(input_file, 'r') as f:
        text = f.read()

    # Convert the text to Markdown
    doc = Document()
    doc.markdown = text
    markdown = doc.markdown

    # Write the Markdown to a file
    with open(output_file, 'w') as f:
        f.write(markdown)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert a text file to a Markdown file')
    parser.add_argument('input_file', help='The input text file')
    parser.add_argument('output_file', help='The output Markdown file')
    args = parser.parse_args()

    convert_file(args.input_file, args.output_file)
