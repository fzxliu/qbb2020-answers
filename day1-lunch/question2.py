import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
bed_columns=["chr","start","end"]
df_k4=pd.read_table("../../qbb2020/data/K4me3.bed", 
	names=bed_columns)
df_k9=pd.read_table("../../qbb2020/data/K9me3.bed", 
	names=bed_columns)
df_k27=pd.read_table("../../qbb2020/data/K27me3.bed", 
	names=bed_columns)

# finding unique chromosomes in K4, K9, and K27 dataset
chr_k4 = df_k4.loc[:,"chr"]
chr_k4 = chr_k4.value_counts()
print(chr_k4)

chr_k9 = df_k9.loc[:,"chr"]
chr_k9 = chr_k9.value_counts()
print(chr_k9)

chr_k27 = df_k27.loc[:,"chr"]
chr_k27 = chr_k27.value_counts()
print("K27 modifications are in", chr_k27)

# sort chromosome orders for each modification type
sorted_k4chr=['X','4','2L','2R','3L','3R']
sorted_k9chr=['X','4','2L','2R','3L','3R']
sorted_k27chr=['X','4','2L','3L','3R',]


chr_k4.loc[ sorted_k4chr ]
chr_k4.index

chr_k9.loc[ sorted_k9chr ]
chr_k9.index

chr_k27.loc[ sorted_k27chr ]
chr_k27.index

fig, ax = plt.subplots(nrows=3)
ax[0].bar( chr_k4.index, chr_k4 )
ax[1].bar( chr_k9.index, chr_k9 )
ax[2].bar( chr_k27.index, chr_k27 )


ax[0].set_title('K4me3 Chr distribution')
for axes in ax:
	axes.set_xlabel('Chr index')
	axes.set_ylabel('Mod numbers')

fig.savefig('question2.png')
plt.close('fig')


# assign chromosome index to variables for k4 mods
# k4chr_ind=(df_k4.loc[:,"chr"])


# ax.bar(chr_k4.index, chr_k4)

# k9chr_ind=sort(df_k9.loc[:,"chr"])
# k27chr_ind=sort(df_k27.loc[:,"chr"])


