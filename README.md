# bcltools
![github version](https://img.shields.io/badge/Version-0.0.1-informational)

*NB* This code is *very* ugly and was developed to figure out the behavior of illumina's bcl2fastq program for barcodes that collide. 

bcltools are a set of tools for manipulating, reading, files associated with illumina short read sequencers.

## Installation
```
$ git clone https://github.com/sbooeshaghi/bcltools.git
$ cd bcltools
$ pip install .
```

## Usage - Reading
### BCL files
```
$ bcltools read -x nextseq --head examples/bcl.bcl     # read header only
$ bcltools read -x nextseq examples/bcl.bcl            # read all entries
$ bcltools read -x nextseq examples/bcl.bcl | head -8  # read 8 entries
```

### LOCS files
```
$ bcltools read -x nextseq -f locs --head examples/locs.locs      # read header only
$ bcltools read -x nextseq -f locs examples/locs.locs             # read all entries
$ bcltools read -x nextseq -f locs examples/locs.locs | head -15  # read 15 entries
```

### FILTER files
```
$ bcltools read -x nextseq -f filter --head examples/filter.filter      # read header only
$ bcltools read -x nextseq -f filter examples/filter.filter             # read all entries
$ bcltools read -x nextseq -f filter examples/filter.filter | head -12  # read 12 entries
```

## Usage - Writing
### BCL files
```
$ echo "G\t%" | bcltools write -x miseq -o ./out.bcl -  # write basepair and Qscore to bclfile
$ bcltools read -x miseq out.bcl                        # check that it worked
```

### LOCS files
```
$ echo "12223.44\t2.44334" | bcltools write -x miseq -f locs -o out.locs -  # write an x y value
$ bcltools read -x miseq -f locs out.locs                                   # check that it worked
```

### FILTER files
```
$ echo "Y\nY\nN\nY" | bcltools write -x nextseq -f filter -o out.filter -  # write a filter value 
$ bcltools read -x nextseq -f filter out.filter                            # check that it worked
```

## Usage - Piping
We can chain commands when reading and writing by passing through pipes
```
$ bcltools read -f filter -x nextseq examples/filter.filter | head -12 | bcltools write -f filter -x nextseq -o ./smaller.filter -
```
