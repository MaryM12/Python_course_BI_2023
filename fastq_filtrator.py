#################################################################################################################
# Fastq_filtrator
#################################################################################################################

# Return a Boolean indicator whether the read falls within the allowable range of GC content
def filter_gc_bounds(gc_bounds, read):
  c = read.count("C")
  g = read.count("G")
  gc_total = g+c
  gc_content = (gc_total/float(len(read)))*100
  if isinstance(gc_bounds, int):
     gc_bounds = (0, gc_bounds)
  start, end = gc_bounds[0], gc_bounds[1]
  return (gc_content >= start) and (gc_content <= end)

# Return a Boolean indicator whether the read falls within the allowable range of length        
def filter_length(length_bounds, read):
  if isinstance(length_bounds, int):
      length_bounds = (0, length_bounds)
  start, end = length_bounds[0], length_bounds[1]
  return (len(read) >= start) and (len(read) <= end)

# Return a Boolean indicator whether the read falls within the allowable range of quality 
def filter_quality_threshold(quality_threshold, read_quality):
  sum_q = sum(ord(letter)-33 for letter in read_quality)
  mean_quality = sum_q/float(len(read_quality))
  return mean_quality >= quality_threshold

def main(input_fastq, output_file_prefix, gc_bounds = (0, 100), length_bounds = (0, 2**32), quality_threshold = 0, save_filtered = False):
    """
    Read from .fastq file and filter the reads by GC content, length and quality.
    The reads which passed filtering are saved into {output_file_prefix}_passed.fastq 
    file. If the parameter save_filtered = T is indicated, the filtered out reads are 
    saved into {output_file_prefix}_failed.fastq file
    :param input_fastq: (Required.) Path to input .fastq file (a string). 
    :param output_file_prefix: (Required.) Output file name prefix. 
    :param gc_bounds: (Optional). Default (0, 100). Allowable range of GC content. Either max and
    min values (inclusive) as a tuple or only the max value as int. 
    :param length_bounds:  (Optional). Default (0, 2**32). Allowable range of read length (indicated 
    in a similarway as gc_bounds).
    :param quality_threshold: (Optional). Default 0. Minimal allowable value of average
    Q-score (phred33 scale) for a read.
    """
# open the input and the 2 output files. Read and process each 4 lines from the input file at once. 
    with open(input_fastq, "r") as file, open(f'{output_file_prefix}_passed.fastq', "w") as file_out, open(f'{output_file_prefix}_failed.fastq', "w") as filtered_file:
        lines = []
        for line in file:
            lines.append(line.strip())
            if len(lines) == 4: #4 lines corresponding to one read are read and added to the list
                read = lines[1].upper() 
                read_quality = lines[3].upper()
                #process the read
                if filter_gc_bounds(gc_bounds, read) == True and filter_length(length_bounds, read) == True and filter_quality_threshold(quality_threshold, read_quality) == True:
                  #save the reads which passed the filtering
                    file_out.write('\n'.join(lines)) 
                    file_out.write('\n')
                else:
                  #save the filtered out reads if required
                    if save_filtered == True:
                        filtered_file.write('\n'.join(lines))
                        filtered_file.write('\n')
                lines = [] #empty the list to proceed to the next read
