* ABOUT *
Escherichia coli str. K12 subst. MG1655 sequence exporter.

Source code can be found at:
http://bfx.eng.jhu.edu/dgokalg1/adv_final_project

E.coli annotation data can be found at:
http://bfx.eng.jhu.edu/dgokalg1/adv_final_project/E.coli_genome/Ecoli.gff

mySQL builder source code can be found at:
http://bfx.eng.jhu.edu/dgokalg1/adv_final_project/E.coli_mysql_builder.py

Interface can be found at:
http://bfx.eng.jhu.edu/dgokalg1/adv_final_project/search_seq_E.coli.html

* REQUIREMENTS *
Storage not required. Recommended memory/cpu is 1gb. 

* DETAILED USAGE *

1. Enter a feature type typically found in annotation analysis data (gff file). This includes gene, CDS,
tRNA, region, etc. Autocomplete will provide options for user.

2. Enter valid attribute value provided by the gff annotation file for the respective sequence of interest.
For example, the user may want to view analysis of creA gene in E.coli. The user will enter 'gene' in the
feature text box, and creA in the attribute text box and click submit. 

The interface will display and output the nucleotide sequence, sequence length, GC content, 
protein full name, protein sequence, protein length, and amino-acid composition of creA. 

* References *
All data used, the genomic fasta file, genomic gff3 file and protein fasta file for Escherichia coli 
were provided by NCBI database


