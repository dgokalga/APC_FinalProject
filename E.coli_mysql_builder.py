#!/usr/bin/env python3

import mysql.connector

conn = mysql.connector.connect(user='dgokalg1', password='Admin4807', host='localhost', database='dgokalg1')
curs = conn.cursor()
for line in open("E.coli_genome/Ecoli.gff"):
    cols = line.split('\t') # splits gff3 portion into 9 columns
    if len(cols) == 9:
        seq_name = cols[0] # name of location of the sequence
        source = cols[1] # source of annotation
        feature = cols[2] # type of sequence
        start = int(cols[3]) # start position
        end = int(cols[4]) # stop position
        score = cols[5]
        strand = cols[6] # plus or minus strand
        phase = cols[7] 
        attributes = cols[8].strip() # unique value for the sequence
        
        qry = "INSERT INTO E_coli(seq_name, source, feature, start, end, score, strand, phase, attributes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        curs.execute(qry, (seq_name, source, feature, start, end, score, strand, phase, attributes))
        conn.commit()
        conn.rollback()
conn.close()

