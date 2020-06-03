## Loading Libraries

import matplotlib.pyplot as plt 

def plot_simulation_output(Graphsize,data,module=['Infected','Rt','Died']):

    lng = Graphsize

    time = list(range(len(data['Level'])))
  
    DATA ={'Normal':[x/lng for x in list(data['Level'].Normal)],'Infected':[x/lng for x in list(data['Level'].Infected)],'Died':[x/lng for x in list(data['Level'].Died)],'Rt':data['R0_time_list']}
    colors ={'Normal':'green','Infected':'blue','Died':'red','Rt':'black'}
    Ls ={'Normal':'solid','Infected':'solid','Died':'dashed','Rt':'dashed'}

    fig, ax1 = plt.subplots(1,1,figsize=(6,3), dpi= 120)
    for plot in module:
        if plot !='Rt':
            ax1.plot(time, DATA[plot] ,color=colors[plot],lw=1,label=plot,ls=Ls[plot])
        else:
            ax2 = ax1.twinx()
            ax2.plot(time, DATA[plot],color=colors[plot],lw=1,label=plot,ls=Ls[plot])
            ax2.set_ylabel('Rt', fontsize=5)
            ax2.tick_params(axis='y', rotation=0,labelsize=5 )
      
    

    if 'Rt' in module:
        ax2.grid(alpha=.4)
    else:
        ax1.grid(alpha=.4,axis='y')

    ax1.tick_params(axis='x', labelsize=5)
    ax1.set_ylabel('Percentage', fontsize=5)
    ax1.tick_params(axis='y', rotation=0,labelsize=5 )
    tick = int(len(time)/10)
    if tick==0:
        tick=1
    ax1.set_xticks(time[::tick])
    ax1.set_xticklabels(time[::tick])
    ax1.grid(alpha=.4,axis='x')

    fig.tight_layout()

    plt.title('Dynamic of Cascade in th Graph',fontsize=10)

    handles,labels = [],[]
    for ax in fig.axes:
        for h,l in zip(*ax.get_legend_handles_labels()):
            handles.append(h)
            labels.append(l)

    plt.legend(handles,labels,fontsize=7,loc='best')
    plt.show()
    return()