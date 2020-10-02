import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# manhattan plots and qq plots for phenotypes
gwas = pd.read_csv(sys.argv[1], sep = "\s+")
print(sys.argv[1])
gwas['logP'] = -1 * np.log10(gwas['P'])
gwas['snp_index'] = range(len(gwas))


fig, ax = plt.subplots()

fig, ax = plt.subplots()
for chr in range(1, 16): 
    ax.scatter(gwas["snp_index"][gwas["CHR"] == chr][gwas["logP"] < 5], gwas["logP"][gwas["CHR"] == chr][gwas["logP"] < 5], marker = '.')
    ax.scatter(gwas["snp_index"][gwas["CHR"] == chr][gwas["logP"] > 5], gwas["logP"][gwas["CHR"] == chr][gwas["logP"] > 5], c='black', marker = '.')
plt.xlabel("SNPs")
plt.ylabel("-log10(p-value)")

plt.savefig("manhattan_{picname}.png".format(picname=sys.argv[1]))



# QQ plot

gwas_sorted = gwas.sort_values(by = "P")

gwas_sorted['uniform_points'] = range(0, len(gwas_sorted))
gwas_sorted['uniform_pval'] = (gwas_sorted['uniform_points'] + 1) / len(gwas_sorted)
gwas_sorted['uniform_logP'] = -1 * np.log10(gwas_sorted['uniform_pval'])

gwas['snp_index'] = range(len(gwas))

fig, ax = plt.subplots()
ax.scatter(gwas_sorted["uniform_logP"], gwas_sorted["logP"])
ax.plot([8,0], [8, 0], color = "black")

plt.xlim([0, 8])
plt.ylim([0, 10])
plt.xlabel("Expected -log10(p-value)")
plt.ylabel("Observed -log10(p-value)")
    
plt.savefig("qq_{picname}.png".format(picname=sys.argv[1]))