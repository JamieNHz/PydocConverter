import aspose.words as aw
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
        description="Covert documents to and from 'odt, ' pdf', 'html', or 'docx'"
    )

    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()
    
    inputfile = args.input
    outputfile = args.output

    types = ['.odt', '.pdf', '.html', '.docx']

    infile = Path(inputfile)
    outfile = Path(outputfile)
    
    if infile.exists():
        if infile.suffix.lower() not in types:
            raise ValueError("Invalid input file type detected, please use either odt, pdf, html, or docx")
        elif outfile.suffix.lower() not in types:
            raise ValueError("Invalid output file type detected, please use either odt, pdf, html, or docx")
    elif not infile.exists():
        raise FileNotFoundError("Input file not found, please check entries and try again")
    else:
        raise FileNotFoundError("Output file not found, please check entries and try again")

    doc = aw.Document(inputfile)
    doc.save(outputfile)


if __name__ == "__main__":
    main()