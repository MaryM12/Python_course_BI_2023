# Python_BI_2022
# FastQ Filtrator
Reads from .fastq file and filters the reads by GC content, length and quality.
## Usage
Run main function from fastq_filtrator.py script with the necessary parameters
- exit — abort the program
- transcribe — create an mRNA transcript for a DNA seq
- complement — create a complement seq for DNA (default) or RNA
- reverse complement — create a reverse-complement seq for DNA (default) or RNA

## Parameters of the function main:

- input_fastq — (Required.) Path to input .fastq file (a string). 
output_file_prefix - (Required.) Output file name prefix.
- gc_bounds — (Optional). Default (0, 100). Allowable range of GC content. Either max and
min values (inclusive) as a tuple or only the max value as int.
- length_bounds — (Optional). Default (0, 2^32). Allowable range of read length (indicated 
in a similarway as gc_bounds).
- quality_threshold — (Optional). Default 0. Minimal allowable value of average Q-score (phred33 scale) for a read.
- save_filtered — (Optional). Default False. If save_filtered = T is indicated, the filtered out reads are 
saved into {output_file_prefix}_failed.fastq file

**Free Software, Hell Yeah!**
