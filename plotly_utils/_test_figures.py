import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

def get_test_fig_hor_bar():
    df2 = px.data.tips()
    test_fig = px.bar(df2, x="total_bill", y="sex", color='day', orientation='h',
                 hover_data=["tip", "size"],
                 height=400,
                 title='Restaurant bills')
    return test_fig



def test_figure_conf_matr():

    z = [[0.1, 0.3, 0.5],
         [1.0, 0.8, 0.6],
         [0.1, 0.3, 0.6]]

    x = ['Scoot', 'Responsive', 'Actuated']
    y = ['Actuated', 'Responsive', 'Scoot']

    # change each element of z to type string for annotations
    z_text = [[str(y) for y in x] for x in z]

    # set up figure
    fig = ff.create_annotated_heatmap(z, x=x, y=y, annotation_text=z_text, colorscale='Viridis')

    # add title
    fig.update_layout(title_text='<i><b>Overlapping matrix</b></i>',
                      # xaxis = dict(title='x'),
                      # yaxis = dict(title='x')
                      )

    # add custom xaxis title
    fig.add_annotation(dict(font=dict(color="black", size=14),
                            x=0.5,
                            y=-0.15,
                            showarrow=False,
                            text="A&P proposed ToC",
                            xref="paper",
                            yref="paper"))

    # add custom yaxis title
    fig.add_annotation(dict(font=dict(color="black", size=14),
                            x=-0.15,
                            y=0.5,
                            showarrow=False,
                            text="Siemens proposed ToC",
                            textangle=-90,
                            xref="paper",
                            yref="paper"))

    # adjust margins to make room for yaxis title
    fig.update_layout(margin=dict(t=100, l=10))

    # add colorbar
    fig['data'][0]['showscale'] = True
    return fig

def test_fig_scatterbox():
    df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

    fig = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)
    return fig