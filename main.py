import aspose.words as aw
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Convert ODT document to pdf"
    )

    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required = True)

    args = parser.parse_args()

    inputfile = args.input
    outputfile = args.output

    doc = aw.Document(inputfile)
    doc.save(outputfile)


if __name__ == "__main__":
    main()