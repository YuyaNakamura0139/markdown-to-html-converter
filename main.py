import sys
import markdown


def validate_args(args):
    if len(args) != 4:
        print("Usage: python3 main.py markdown <inputfile> <outputfile>")
        sys.exit(1)


if __name__ == "__main__":
    validate_args(sys.argv)
    _, _, input_file_path, output_file_path = sys.argv
    with open(input_file_path, "r", encoding="utf-8") as input_file:
        text = input_file.read()

    html = markdown.markdown(text)

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(html)
