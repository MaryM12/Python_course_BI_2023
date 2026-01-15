import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt  
### Task 1
# functions to read files

def read_gff(path):
    liste = ["chromosome","source","type","start","end","score","strand","phase","attributes"]
    df_gff = pd.read_csv(path, comment='"',sep='\t',header=None,names=liste, skiprows=1)
    df_gff['score'] = df_gff['score'].map(lambda a: "{:.6e}".format(a))
    return df_gff
df_gff = read_gff("/content/rrna_annotation.gff")
df_gff

def read_bed6(path):
    liste=["chromosome","start","end","name","score","strand"]
    df_bed6=pd.read_csv(path, comment='"',sep='\t',header=None,names=liste)
    return df_bed6
df_bed = read_bed6("/content/alignment.bed")
df_bed
# Task 1.2: Колонка с атрибутами несёт слишком много избыточной информации и ей не удобно пользоваться,
# оставьте в ней только данные о типе рРНК одной короткой строкой (16S, 23S, 5S).

df_gff['attributes'] = df_gff['attributes'].str.split('_rRNA;product').str[0].str.split('Name=').str[1]
df_gff
# Task 1.3: barplot
rRNA = df_gff.groupby(['chromosome', 'attributes'])['attributes'].size().reset_index(name='count')
rRNA.head(10)
plt.subplots(figsize=(20, 10))
ax = sns.barplot(x="chromosome", y="count", hue="attributes", data=rRNA)
plt.xticks(rotation=90)
ax.set(xlabel='Sequence', ylabel='Count')
plt.show();

# Task 1.4: 'bedtools intersect' in pandas
merged = pd.merge(df_gff,df_bed, on="chromosome", how="outer")
intersect = merged.query('start_x >= start_y and end_x <= end_y')
intersect


### Task 2: Plot Customization
de = pd.read_csv("/content/diffexpr_data.tsv.gz", sep='\t')
de

#Additional column to make 4 groups from our data
# create a list of our conditions
conditions = [
    (de['pval_corr']< 0.05) & (de['logFC']>= 0),
    (de['pval_corr']< 0.05) & (de['logFC']< 0),
    (de['pval_corr']>= 0.05) & (de['logFC']>= 0),
    (de['pval_corr']>= 0.05) & (de['logFC']< 0)
    ]

# create a list of the values we want to assign for each condition
values = ['Significantly upregulated', 'Significantly downregulated', 'Non-significantly upregulated', 'Non-significantly downregulated']

# create a new column and use np.select to assign values to it using our lists as arguments
de['DE'] = np.select(conditions, values)

# logFC limits
min_logFC = de.logFC.min()
max_logFC = de.logFC.max()
min_logFC
max_logFC
# top up- and downregulated genes
top_up = de.query('DE == "Significantly upregulated"').sort_values(by = "logFC", ascending = False).head(2)
top_up
top_down = de.query('DE == "Significantly downregulated"').sort_values(by = "logFC").head(2)
top_down
top = pd.concat([top_up, top_down])
top

#main parameters
plt.rcParams["legend.markerscale"] = 2
plt.rcParams['mathtext.bf'] = 'Arial:italic:bold'
plt.subplots(figsize=(17, 10))

pal = ('tab:red','tab:orange','tab:green','tab:blue')
# palette=pal,
ax = sns.scatterplot(x='logFC', y='log_pval', data=de, hue="DE", palette=pal, s=20, linewidth=0)

# lines
plt.axhline(y=-np.log10(0.05), color='tab:gray', linestyle='--', lw=2)
plt.axvline(x=0, color='tab:gray', linestyle='--', lw=2)
plt.text(8, -np.log10(0.05)+1, "p_value = 0.05", size=18, c='tab:gray',fontweight='demi')

# axes and labels
plt.xlabel(r"$\mathbf{log_2(fold\ change)}$", size=20, style='italic')
plt.ylabel(r"$\mathbf{-log_{10}(p\ value\ corrected}$", size=20, style='italic')
plt.title(r"$\mathbf{Volcano\ plot}$", style='italic', fontsize=30)

# ticks and tricks

ax.set_xticks(np.linspace(-12, 11, 36),minor=True)
ax.set_yticks(np.linspace(-2, 115, 20),minor=True)
ax.tick_params(which='minor', length=4, width=1.2)
ax.tick_params(which='major', length=4, width=2)
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(1.8)

#limits of X axis
plt.xlim([-11, 11])

# legend
plt.legend(prop={'size': 13, 'weight':'bold'}, title=None, shadow=True)

# annotate top genes with arrows
for i in range(4): 
    ax.annotate(top.iloc[i, 0], 
                  xy=(top.iloc[i, 1], 
                      top.iloc[i, 4]),
                  xytext=(top.iloc[i, 1]+ 0.1, 
                          top.iloc[i, 4] + 8),
                  weight='bold', 
                  arrowprops=dict(facecolor = 'red', headlength=7, headwidth=8,
                                  linewidth=0.5, connectionstyle="arc3", shrink=0.1, width=2))

# save this damn piece of art
plt.savefig('volcano_plot.png', dpi=300)
plt.show()













