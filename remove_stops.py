from Bio import SeqIO
import sys


stop_codons = { "UAA":" stop", "UAG":" stop", "UGA":" stop"}

def chunk_string(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))


def remove_stops(input_data):
    output_data = ""
    for chunk in chunk_string(input_data, 3):
        try:
            stop_codons[chunk] == " stop"
            output_data += "---"
        except KeyError as e:
            output_data += chunk
    return output_data

def main(input_file, output_file):
    with open(output_file, "w") as file:
        with open(input_file, "rU") as handle:
            for record in SeqIO.parse(handle, "fasta"):
                file.write(f">{record.id}\n")
                file.write(str(remove_stops(str(record.seq))))

    

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Usage: python3 {sys.argv[0]} <input file> <output file>")
        exit(1)

    main(sys.argv[1], sys.argv[2])