
for f in $(ls A*.fastq)
do
    echo $f
    bwa mem -R "@RG\tID:${f}\tSM:${f}" sacCer3.fa ${f} > alignment/${f}.sam
    samtools sort -o alignment/${f}.bam alignment/${f}.sam
done

freebayes --genotype-qualities -f sacCer3.fa -p 1 alignment/*.bam > var.vcf

vcffilter -f "QUAL > 20" var.vcf | snpEff ann R64-1-1.86 > results.vcf

head -1000 results.vcf > results_subset.vcf