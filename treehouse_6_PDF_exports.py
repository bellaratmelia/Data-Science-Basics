from treehouse_5_charts import *
from matplotlib.backends.backend_pdf import PdfPages

def plot_minimal_graph(tally, columns, *args):
    plt.style.use('bmh')
    fig = plt.figure(dpi=200) 
    colors=plt.rcParams['axes.color_cycle']
        
    # --- White background to use less printer ink --- #
    ax = plt.subplot(111,axisbg='white')
        
    # Plot bars and create text labels for the table
    for priceBucket in tally:
        ax.bar(priceBucket, tally[priceBucket], color=colors[priceBucket%len(tally)])
        ax.annotate(r"%d" % (tally[priceBucket]),
                   (priceBucket+0.2, tally[priceBucket]), 
                   va="bottom", ha="center")


    # --- Include a legend  --- #
    ax.legend(columns)
      
    # --- Remove distracting lines on top, left, and right --- #
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # --- Remove distracting tick marks  --- #
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('none')


    # --- Add chart title and axes labels --- #          
    plt.xlabel('Tie Price', fontsize = 13)
    plt.ylabel('Number of Ties', fontsize = 13)
    plt.title('Chart #1')


    # --- Add labels to bars along x axes --- #
    x = range(1, len(tally)+1)
    plt.xticks(x, columns, rotation='horizontal', ha='left')
            
    return fig
    
def plot_graph_with_table(cell_text, row_text, columns):
    plt.style.use('ggplot') 
    fig = plt.figure() 

    # --- Include table --- #
    ax2 = fig.add_subplot(111)
    ax2.axis('off')

    the_table = ax2.table(cellText=cell_text, 
                        rowLabels=row_text, 
                        colLabels=columns, 
                        loc='center right')

def plot_bar_graphs_for_pdf(mypdf, data_sample, brand, conditions):
  for cond in conditions: 
    item_sample = filter_col_by_string(data_sample, brand, cond)
    y = [float(x[2]) for x in item_sample[1:]]
    price_groups = group_prices_by_range(y) 
    item_chart = plot_minimal_graph(price_groups, [], cond)
    mypdf.savefig(item_chart, bbox_inches='tight')

mypdf = PdfPages('reports.pdf')
plot_bar_graphs_for_pdf(mypdf, data_csv, "brandName", ["DKNY", "Gucci", "Kiton"])
mypdf.close()



