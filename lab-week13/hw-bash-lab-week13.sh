# creating Krona chart

for i in $(ls week13_data/KRAKEN/SRR*.kraken | sort -V);
do cut -f2 "$i" | tr ';' '\t' > "$i".txt; 
done

for i in $(ls week13_data/KRAKEN/SRR*.kraken.txt | sort -V);
do perl bin/ktImportText -q "$i";
mv text.krona.html "$i".html;
done

# align reads to assembly
bwa index assembly.fasta

cd week13_data/READS/
for f in $(ls *.fastq | cut -f1 -d'_')
do
    bwa mem -p assembly.fasta ${f}_1.fastq ${f}_2.fastq > ${f}.aln.sam
    samtools sort -o ${f}.sorted.bam ${f}.aln.sam
    samtools index ${f}.sorted.bam
done
cd ../..

# binning

conda activate metabat2
cd week13_data/READS/
jgi_summarize_bam_contig_depths --outputDepth depth.txt week13_data/READS/*.sorted.bam
metabat2 -i week13_data/assembly.fasta -a depth.txt -o bins_dir/bin


# compute total bin size

cd bins_dir/
for f in $(ls bin.*.fa); do grep -v 'NODE' | wc -m; done;
cd ..

grep -v 'NODE' week13_data/assembly.fasta | wc -m


# find taxonomy of each bin
# used these files to answer Q4
cd bins

for f in $(ls bin.*.fa); do grep 'NODE' ${f} | cut -c2- > ${f}_NODE; done

for f in $(ls *_NODE)
do
    for l in $(cat ${f})
    do
        grep "$l" ../week13_data/KRAKEN/assembly.kraken >> ${f}_taxa.txt
    done
done


# extract taxonomy information from each bin
for f in $(ls *_taxa.txt | cut -f1 -d'_')
do
    cut -f2 ${f}_NODE_taxa.txt | tr ';' '\t' | cut -f9 | sort | uniq -c > ${f}_genera_quant.txt
done

for f in $(ls *_quant.txt)
do
    echo "bin starts"
    cat ${f}
    echo "bin ends"
done









