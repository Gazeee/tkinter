import csv

tsv_file = open("coordenadas_tabela - dados.tsv")
read_tsv = csv.reader(tsv_file, delimiter="\t")


if __name__ == '__main__':
    for r in read_tsv:
        print(r)

