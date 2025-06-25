import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Import data
data = pd.read_csv('stock.csv')

st.title('Stock Analysis')
st.write('In this project we will analyze the amount of products in stock, by category, of a supermarket product database')


def show_number_lines(dataframe):
    number_lines = st.sidebar.slider('Select the quantity of lines you would like to show in the table', min_value=1, max_value=len(dataframe), step=1)
    st.write(dataframe.head(number_lines).style.format(subset=['Valor'], formatter="{:.2f}"))

def plot_stock(dataframe, category):
    data_plot = dataframe.query('Categoria == @category')

    fig, ax = plt.subplots(figsize=(8, 6))
    ax = sns.barplot(x='Produto', y='Quantidade', data=data_plot)
    ax.set_title(f'Quantity of the product {category} in stock', fontsize=16)
    ax.set_xlabel('Products', fontsize=12)
    ax.tick_params(rotation=20, axis='x')
    ax.set_ylabel('Quantity', fontsize=12)

    return fig


# Filter for the table
show_table = st.sidebar.checkbox('Show table')
if show_table:
    st.sidebar.markdown('## Table filters')
    categories = list(data['Categoria'].unique())
    categories.append('All')

    category = st.sidebar.selectbox('Select a category to show the table', options = categories)

    if category != 'All':
        df_category = data.query('Categoria == @category')
        show_number_lines(df_category)
    else:
        show_number_lines(data)


st.sidebar.markdown('## Graph filter')
category_graph = st.sidebar.selectbox('Select the category to show in the graph', options=data['Categoria'].unique())
figure = plot_stock(data, category_graph)
st.pyplot(figure)