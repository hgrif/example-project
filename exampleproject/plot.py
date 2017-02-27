def profit(df):
    ax = df.plot(x='time', y='profit')
    ax.set_title('Profit keeps increasing!')
    ax.set_xlabel('Time')
    ax.set_ylabel('Profit')
    return ax
