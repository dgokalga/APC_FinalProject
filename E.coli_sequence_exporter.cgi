#!/usr/local/bin/python3 

print("Content-Type: text/html")
print()

import operator
import mysql.connector
import cgitb
cgitb.enable(format = 'text')

import cgi

form = cgi.FieldStorage()
feat = form.getfirst('feature')
attrib = form.getfirst('attributes')

if feat == None:
    print("""<html style="word-wrap: break-word; background-color:lightblue">
                <head>
                        <h1 style="text-align: center; font-size: 300%; text-decoration: underline">Escherichia coli str. K-12 substr. MG1655</h1>
                                
                                <body>
        <p style = "font-size: 150%">Please enter a valid feature type</p>
                </body>

                </head>
        </html>                 """)

elif attrib == None:
     print("""<html style="word-wrap: break-word; background-color:lightblue">
                <head>
                        <h1 style="text-align: center; font-size: 300%; text-decoration: underline">Escherichia coli str. K-12 substr. MG1655</h1>
                                
                                <body>
        <p style = "font-size: 150%">Please enter a valid attribute value</p>
                </body>

                </head>
        </html>                 """)

elif feat==None and attrib==None:
     print("""<html style="word-wrap: break-word; background-color:lightblue">
                <head>
                        <h1 style="text-align: center; font-size: 300%; text-decoration: underline">Escherichia coli str. K-12 substr. MG1655</h1>
                                
                                <body>
        <p style = "font-size: 150%">Please enter a valid feature type and valid attribute value</p>
                </body>

                </head>
        </html>                 """)

else:
    conn = mysql.connector.connect(user='dgokalg1', password='Admin4807', host='localhost', database='dgokalg1')
    curs = conn.cursor()
    qry = "SELECT * FROM E_coli WHERE feature LIKE %s AND attributes LIKE %s"
    curs.execute(qry, ("%" + str(feat) + "%", "%" + str(attrib) + "%"))
    for gff_1, gff_2, gff_3, gff_4, gff_5, gff_6, gff_7, gff_8, gff_9 in curs:
        seq_name = gff_1
        source = gff_2
        feature = gff_3
        start = gff_4
        stop = gff_5
        score = gff_6
        strand = gff_7
        phase = gff_8
        attributes = gff_9
    curs.close()
    conn.close()
    try:
        genome = ""
        for line in open("E.coli_genome/Ecoli_fasta.fna"):
            if line.startswith(">"):
                header = line
            else:
                line = line.rstrip()
                genome += line

        if feat == "region":
            sequence = genome
            print("""<html style="word-wrap: break-word; background-color:lightblue">
                <head>
                        <h1 style="text-align: center; font-size: 300%; text-decoration: underline">Escherichia coli str. K-12 substr. MG1655</h1>
                                
                                <body>
                                        <h1 style = "font-size: 250%">Sequence Result:</h1>
                                        <p style="font-size: 150%">Escherichia coli str. K-12 substr. MG1655 Entire Genome:  </p>       
                        <p style= "font-size: 125%">{0}</p> 
 </body>

                </head>
        </html>                 """.format(sequence))
        else:

            sequence = genome[start - 1: stop]

            reverse_dict = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
            reverse_comp = ''

            if strand == '-': # if minus strand
                reverse_seq = sequence[::-1]
                for nuc in reverse_seq:
                    reverse_comp += reverse_dict[nuc]
                    sequence = reverse_comp

            for nuc in sequence:
                c = round(sequence.count("C")/len(sequence) * 100, 1)
                g = round(sequence.count("G")/len(sequence) * 100, 1)

            gc = g + c

            seq_length = len(sequence)

            table = {
                'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
                'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
                'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
                'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
                'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
                'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
                'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
                'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
                'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
                'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
                'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
                'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
                'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
                'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
                'TAC':'Y', 'TAT':'Y', 'TAA':'', 'TAG':'',
                'TGC':'C', 'TGT':'C', 'TGA':'', 'TGG':'W',
            }
            protein =""
            if len(sequence)%3 == 0:
                for i in range(0, len(sequence), 3):
                    codon = sequence[i:i + 3]
                    protein+= table[codon]

            protein_len = len(protein)


            aa_comp = {}

            for aa in protein:
                if aa in aa_comp:
                    aa_comp[aa] += 1
                else:
                    aa_comp[aa] = 1

            aa_list = []
            aa_perc = []
            for key, value in sorted(aa_comp.items(), key=operator.itemgetter(1), reverse = True):
                aa_list.append(key)
                aa_perc.append(str(round((value/len(protein))*100, 2)))

            prot = {}

            for line in open("E.coli_genome/Ecoli_protein.faa"):
                if line.startswith('>'):
                    key = line.rstrip()[1:]
                    prot[key] = ''
                else:
                    prot[key] += line.rstrip()

            prot_name = "Protein name not identified"
            for key, value in prot.items():
                if protein == value:
                    prot_name = key


            print("""<html style="word-wrap: break-word; background-color:lightblue">
                <head>
                        <h1 style="text-align: center; font-size: 300%; text-decoration: underline">Escherichia coli str. K-12 substr. MG1655</h1>
                                
                                <body>
                                        <h1 style = "font-size: 250%">Sequence Result:</h1>
                                        <p style = "text-align: center; font-size: 150%">Sequence name: {0}, Source: {1}, Feature: {2}</p>
                                        <p style="font-size: 120%">{3}</p>
                                        <p style="font-size: 150%">Sequence Length: {4}bp</p>
                                        <p style="font-size: 150%">G-C content: {5}%</p>
                                        <h2 style = "font-size: 250%">Protein Search Result:</h2>
                                        <p style = "text-align: center; font-size: 150%">{6}</p>
                                        <p style="font-size: 120%">{7}</p>
                                        <p style="font-size: 150%">Protein Length: {8} amino acids</p>
                                        <p style="font-size: 120%">Amino Acid Composition:</p>

                                """.format(seq_name, source, feat, sequence, seq_length, gc, prot_name, protein, protein_len))
            x = 0
            while x < len(aa_list):
                print("""<br>{0}: {1}%</br>""".format(aa_list[x], aa_perc[x]))
                x += 1
            print("""  </body>

                </head>
        </html>""")

    except NameError:
        print("""<html style="word-wrap: break-word; background-color:lightblue">
                <head>
                        <h1 style="text-align: center; font-size: 300%; text-decoration: underline">Escherichia coli str. K-12 substr. MG1655</h1>
                                
                                <body>
                                        <p>Sequence not found, please make sure feature type and/or attribute value is valid</p>
                                 </body>

                </head>
        </html>""")
