import aspose.words as aw
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Convert ODT document to pdf"
    )

    parser.add_argument("input_file")
    parser.add_argument("output_file")

    args = parser.parse_args()

    print(args.input_file)
    print(args.output_file)


if __name__ == "__main__":
    main()