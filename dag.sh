mkdir results
mkdir results/summary
snakemake --forceall --rulegraph | dot -Tpng > results/summary/rulegraph.png
snakemake --forceall --dag | dot -Tpng > results/summary/dag.png
snakemake --forceall --filegraph | dot -Tpng > results/summary/filegraph.png

