# recording command lines used

# Part 1

bowtie2-build chr19.fa chr19

for sample in input_G1E input_ER4 CTCF_ER4 CTCF_G1E
do
    bowtie2 -x chr19 -U ${sample}.fastq -S ${sample}.sam -p 6
    samtools view -bSo ${sample}.bam ${sample}.sam
    samtools sort ${sample}.bam ${sample}.sorted
    samtools index ${sample}.sorted.bam
done

macs2 callpeak -t CTCF_G1E.bam -c input_G1E.bam --format=BAM --name=G1E --gsize=61420004
macs2 callpeak -t CTCF_ER4.bam -c input_ER4.bam --format=BAM --name=ER4 --gsize=61420004

bedtools intersect -a G1E_peaks.narrowPeak -b ER4_peaks.narrowPeak -v > lost.bed
wc -l lost.bed > diff_gain_loss.txt
bedtools intersect -a ER4_peaks.narrowPeak -b G1E_peaks.narrowPeak -v > gained.bed
wc -l gained.bed >> diff_gain_loss.txt

bedtools intersect -a Mus_musculus.GRCm38.94_features.bed -b G1E_peaks.narrowPeak > G1E_features.bed
bedtools intersect -a Mus_musculus.GRCm38.94_features.bed -b ER4_peaks.narrowPeak > ER4_features.bed

cut -f4 G1E_features.bed | sort | uniq -c > uniq_G1E_features.txt
cut -f4 ER4_features.bed | sort | uniq -c > uniq_ER4_features.txt


# Part 2

# sort the narrowPeak file using pvalue and extract the top 100 most significant sequences
sort -nk 8 ER4_peaks.narrowPeak | tail -100 > ER4_sorted_peaks.narrowPeak

# extract fasta file from the narrowPeak file as input for meme-chip
bedtools getfasta -fo ER4_sorted_peaks.fasta -fi chr19.fa -bed ER4_sorted_peaks.narrowPeak

meme-chip -db motif_databases/JASPAR/JASPAR_CORE_2016.meme -meme-maxw 20 ER4_sorted_peaks.fasta

# note that my PC does not have epstopdf, so I simply used Illustrator to convert the eps file to pdf
# the command line to use would have been:
# epstopdf memechip_out/meme_out/logo1.eps 