import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import datetime
from prophet import Prophet

st.set_page_config(layout='wide')
st.title('O Preço do Petróleo 🛢️📈 ')
st.header('Análise da influência geopolítica e demanda global')

st.write('O preço é influenciado por uma série de fatores complexos e inter-relacionados. Em primeiro lugar, a :red[oferta] e :red[demanda] desempenham um papel crucial. Eventos que afetam a produção, como decisões da [Organização dos Países Exportadores de Petróleo (OPEP)](https://pt.wikipedia.org/wiki/Organiza%C3%A7%C3%A3o_dos_Pa%C3%ADses_Exportadores_de_Petr%C3%B3leo) ou interrupções nas operações de grandes produtores, podem impactar significativamente a oferta global. Por outro lado, a demanda por petróleo está intimamente ligada às condições econômicas globais, com flutuações na atividade industrial e no consumo de energia tendo um impacto direto.')
st.write('Além disso, fatores geopolíticos podem desempenhar um papel significativo na volatilidade dos preços do petróleo. Tensões em regiões-chave de produção, eventos políticos e instabilidades em grandes países exportadores podem gerar incerteza nos mercados e influenciar os preços. Além disso, considerações ambientais, avanços tecnológicos em energias renováveis e políticas governamentais relacionadas à transição para fontes de energia mais limpas também podem afetar as perspectivas de longo prazo do mercado de petróleo, impactando os preços de forma mais sustentada.')

st.divider()

url = 'http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view'
table_id = 'grd_DXMainTable'
df = pd.read_html(url, attrs={'id': table_id}, encoding='utf-8', header=0)[0]
df.rename(columns={'Data': 'data', 'Preço - petróleo bruto - Brent (FOB)': 'preco'}, inplace=True)
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
df['preco'] = pd.to_numeric(df['preco'].astype(str).str.replace(',', '.'), errors='coerce') / 100

col1, col2 = st.columns(2)

with col1:
    st.subheader("Dados de referência")
    st.dataframe(df)

with col2:
    max_price_row = df.loc[df['preco'].idxmax()]
    st.subheader("Valor Máximo do Preço e Ano Correspondente:")
    st.write(f"Data: {max_price_row['data'].strftime('%d/%m/%Y')}, Preço Máximo: {max_price_row['preco']}")

    st.divider()

    min_price_row = df.loc[df['preco'].idxmin()]
    st.subheader("Valor Mínimo do Preço e Ano Correspondente:")
    st.write(f"Data: {min_price_row['data'].strftime('%d/%m/%Y')}, Preço Mínimo: {min_price_row['preco']}")

st.divider()

st.subheader("Média Anual do Preço do Petróleo")  
df_mean_by_year = df.groupby(df['data'].dt.year).mean(numeric_only=False)
fig_mean_by_year = px.line(df_mean_by_year, x=df_mean_by_year.index, y=df_mean_by_year.columns[1:],
                                    labels={'value': 'Média do Preço do Petróleo (USD)', 
                                    'index': 'Ano'})
st.plotly_chart(fig_mean_by_year, use_container_width=True)
st.caption('A linha representa a média anual do preço do barril de petróleo ao longo do tempo. Variações notáveis podem ser resultado de eventos geopolíticos, flutuações na oferta e demanda, ou fatores econômicos globais.')

col1, col2, col3 = st.columns(3)
with col1:

    st.markdown(":red[2008]")
    st.write('No ano de 2008, o preço do petróleo atingiu seu maior patamar, marcando uma significativa alta que nunca havia sido alcançada até então.')
    st.write('Este aumento expressivo pode ser contextualizado no cenário global da economia, onde eventos econômicos complexos e dinâmicas geopolíticas desempenharam papéis cruciais.')
    st.write('Além disso, este ano também marcou a crise econômica mundial mais séria desde a Segunda Guerra Mundial')
    st.write('Por causa da crise financeira e da recessão que freou a demanda por petróleo, o barril desabou até os US$ 33,36 em 24 de dezembro.')
    st.write(' ')
    subcol1, subcol2 = st.columns(2)
    with subcol1:
        df_2008 = df[df['data'].dt.year == 2008]
        max_price_2008 = df_2008.loc[df_2008['preco'].idxmax()]
        st.write("Valor Máximo em 2008")
        st.caption(f"Data: {max_price_2008['data'].strftime('%d/%m/%Y')}") 
        st.caption(f"Preço Máximo: {max_price_2008['preco']}")
    with subcol2:
        min_price_2008 = df_2008.loc[df_2008['preco'].idxmin()]
        st.write("Valor Mínimo em 2008:")
        st.caption(f"Data: {min_price_2008['data'].strftime('%d/%m/%Y')}")
        st.caption(f"Preço Mínimo: {min_price_2008['preco']}")
    
with col2:
    st.markdown(":red[2016]")
    st.write('A demanda por petróleo caiu por causa do ritmo mais lento de crescimento das economias dos países grandes consumidores, como Estados Unidos, China, Japão e os países ricos da Europa.')
    st.write('Os Estados Unidos, o segundo maior importador global, conseguiram reduzir sua dependência do Oriente Médio e aumentar seus estoques de petróleo por meio de uma abordagem diversificada. ')
    st.write('Aumentando sua produção de petróleo de 10 para 14 milhões de barris por dia, tornaram-se o maior produtor mundial, ultrapassando a Rússia e a Arábia Saudita.')
    st.caption(' \n')
    st.write(' ')
    st.write(' ')
    subcol1, subcol2 = st.columns(2)
    with subcol1:
        df_2016 = df[df['data'].dt.year == 2016]
        max_price_2016 = df_2016.loc[df_2016['preco'].idxmax()]
        st.write("Valor Máximo em 2016")
        st.caption(f"Data: {max_price_2016['data'].strftime('%d/%m/%Y')}") 
        st.caption(f"Preço Máximo: {max_price_2016['preco']}")
    with subcol2:
        min_price_2016 = df_2016.loc[df_2016['preco'].idxmin()]
        st.write("Valor Mínimo em 2016")
        st.caption(f"Data: {min_price_2016['data'].strftime('%d/%m/%Y')}")
        st.caption(f"Preço Mínimo: {min_price_2016['preco']}")

with col3:
    st.markdown(":red[2022]")
    st.write('A disseminação do COVID-19 provocou quedas sucessivas no preço do petróleo. Na base de qualquer atividade produtiva, o setor de energia é sensível aos efeitos da pandemia na economia.')
    st.write('Apesar dos ganhos, preços ficaram longe dos mais de US$ 120 por barril registrados durante o pico da crise da guerra da Ucrânia')
    st.write('As reservas globais de petróleo subiram ao seu maior nível histórico em 2022, a 1.564,44 bilhões de barris, informou a Organização dos Países Exportadores de Petróleo (Opep), em seu Boletim Estatístico Anual de 2023.')
    st.caption(' \n')
    st.caption(' \n')
    st.write(' ')
    subcol1, subcol2 = st.columns(2)
    with subcol1:
        df_2022 = df[df['data'].dt.year == 2016]
        max_price_2022 = df_2022.loc[df_2022['preco'].idxmax()]
        st.write("Valor Máximo em 2022")
        st.caption(f"Data: {max_price_2022['data'].strftime('%d/%m/%Y')}") 
        st.caption(f"Preço Máximo: {max_price_2022['preco']}")
    with subcol2:
        min_price_2022 = df_2022.loc[df_2022['preco'].idxmin()]
        st.write("Valor Mínimo em 2016")
        st.caption(f"Data: {min_price_2022['data'].strftime('%d/%m/%Y')}")
        st.caption(f"Preço Mínimo: {min_price_2022['preco']}")

st.divider()

st.subheader("O Preço do Petróleo anual de 1987 até 2024")  
st.write('O gráfico interativo permite uma análise detalhada da variação diária do preço do petróleo ao longo dos anos. Utilizando o widget de seleção de ano, você pode escolher um ano específico para examinar sua série temporal correspondente. Isso é valioso para entender como o preço do petróleo flutuou em um determinado período, destacando potenciais padrões, tendências sazonais ou eventos específicos que afetaram os preços.')
st.write('Ao selecionar um ano de interesse, você pode visualizar como o mercado reagiu a eventos geopolíticos, mudanças na oferta e demanda, ou outros fatores econômicos. Por exemplo, durante anos de crises financeiras ou conflitos globais, é possível observar picos ou quedas acentuadas nos preços do petróleo. Essa análise granular proporciona insights valiosos para investidores, economistas e profissionais do setor, ajudando-os a tomar decisões informadas com base nos padrões históricos de preços do petróleo.')

selected_year = st.selectbox("Selecione um ano:", df['data'].dt.year.unique())
df_selected_year = df[df['data'].dt.year == selected_year]
fig = px.line(df_selected_year, x='data', y='preco', title=f"Preço do Petróleo em {selected_year}",
              labels={'Preco': 'Preço do Petróleo (USD)', 'data': 'data'})
fig.update_xaxes(title_text='Data')
fig.update_yaxes(title_text='Preço do Petróleo (USD)')
st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Eventos que afetam o preço do petróleo")  

st.write('As guerras frequentemente exercem uma influência significativa nos preços do petróleo devido à sua capacidade de perturbar a estabilidade do fornecimento global de energia. Conflitos armados em regiões-chave produtoras de petróleo podem resultar em interrupções na produção e no transporte, levando a uma redução na oferta. Essa incerteza no fornecimento, combinada com a dependência global do petróleo como fonte primária de energia, pode resultar em aumentos súbitos e acentuados nos preços do petróleo durante períodos de conflito.')
st.write('Além disso, a percepção de risco geopolítico pode levar os investidores a especularem sobre futuros aumentos nos preços do petróleo, exacerbando ainda mais a volatilidade do mercado. Portanto, as guerras têm o potencial de desempenhar um papel significativo na dinâmica dos preços do petróleo, impactando tanto a oferta quanto a demanda globais.')

col1, col2 = st.columns([2, 1])
with col1:
    df_guerra_golfo = df[(df['data'] >= '1990-08-01') & (df['data'] <= '1990-08-31')]
    fig = px.line(df_guerra_golfo, x='data', y='preco', title='Variação do Preço do Petróleo durante a Guerra do Golfo 📈',
              labels={'preco': 'Preço do Petróleo (USD)', 'data': 'Data'})
    fig.add_trace(go.Scatter(x=df_guerra_golfo['data'], y=df_guerra_golfo['preco'], showlegend=False))
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write('Em 1990, o Iraque invade o Kuwait – que participou na Guerra Irã-Iraque. Mais uma vez, uma das mais importantes regiões petrolíferas levanta preocupações no abastecimento do ocidente.')
    st.write('O preço do barril, que no início da Guerra do Golfo, em 2 de agosto de 1990, era cotado a US$ 22,25, teve um aumento de cerca de 25%.')

col1, col2 = st.columns([2, 1])
with col1: 
    df_setembro_2001 = df[(df['data'] >= '2001-09-01') & (df['data'] <= '2001-09-30')]
    fig_setembro_2001 = px.line(df_setembro_2001, x='data', y='preco', title='Variação do Preço do Petróleo em Setembro de 2001 📉',
                            labels={'preco': 'Preço do Petróleo (USD)', 'data': 'Data'})
    fig_setembro_2001.add_trace(go.Scatter(x=df_setembro_2001['data'], y=df_setembro_2001['preco'], showlegend=False))
    st.plotly_chart(fig_setembro_2001, use_container_width=True)
with col2:
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write('Em 11 setembro de 2001, o mundo assistia aos ataques contra o World Trade Center')
    st.write('No dia dos ataques, o barril Brent era cotado a 29,12 dólares, diminuindo a US$ 25,57 dólares uma semana depois. No final do mês de setembro registra uma queda de cerca de 25%.')

col1, col2 = st.columns([2, 1])
with col1: 
    df_russia_ucrania = df[(df['data'] >= '2022-02-24') & (df['data'] <= '2022-03-03')]
    fig_russia_ucrania = px.line(df_russia_ucrania, x='data', y='preco', title='Variação do Preço do Petróleo no conflito Rússia-Ucrânia 📉',
                            labels={'preco': 'Preço do Petróleo (USD)', 'data': 'Data'})
    fig_russia_ucrania.add_trace(go.Scatter(x=df_russia_ucrania['data'], y=df_russia_ucrania['preco'], showlegend=False))
    st.plotly_chart(fig_russia_ucrania, use_container_width=True)

with col2:
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write(' ')
    st.write('Com guerra envolvendo a Rússia foi um pouco diferente, quando a cotação do barril Brent, referência internacional, subiu rapidamente.')
    st.write('No conflito com a Ucrânia, o crescimento do dia 24 de fevereiro a 3 de março de 2022 foi de 19,21%, com barris cotados em US$ 118,11.')
    st.write('Após cerca de 3 meses, os preços caíram. Isso porque, segundo Bassotto, as cadeias produtivas se realocam, e, quem antes comprava da Rússia, migrou para outro mercado ou conseguiu comprar mais barato do país, como Índia e China fizeram.')

st.divider()

st.subheader("Mas afinal, como uma conflito geopolítico influencia no valor do petróleo?")  

st.write("Antes de tudo, vale lembrar que as guerras são diferentes e ocorrem em cenários econômicos distintos.")
st.write("No entanto, de maneira geral, a instabilidade geopolítica em regiões produtoras de petróleo pode afetar o fornecimento global. Conflitos podem resultar em interrupções na produção, transporte e exportação de petróleo, gerando incertezas no mercado. Essa incerteza muitas vezes leva a aumentos nos preços do petróleo, pois os investidores buscam proteção diante dos riscos associados à oferta.")
st.write(' ')
st.write('Para auxiliar em previsões futuras, vamos destacar os 10 principais países exportadores de petróleo por região e por país')

dados = {
    "Região/Organização": ["OPEP", "América do Norte", "CEI", "Resto do Mundo", "Total"],
    "Produção de Petróleo em 2021 (barris por dia)": [31.7e6, 23.9e6, 13.8e6, 20.5e6, 89.9e6],
    "% do Total": [35, 27, 15, 23, 100]
}

df_producao_petroleo = pd.DataFrame(dados)
fig = px.bar(df_producao_petroleo, x="Região/Organização", y="Produção de Petróleo em 2021 (barris por dia)",
             color="% do Total", title="Produção de Petróleo por Região/Organização em 2021",
             labels={"Produção de Petróleo em 2021 (barris por dia)": "Produção de Petróleo (barris por dia)", "% do Total": "Percentual do Total"})
st.plotly_chart(fig, use_container_width=True)

st.divider()
st.subheader("10 países mais exportadores de petróleo do mundo")  

st.caption("O próximo gráfico mostra a produção de petróleo diária de alguns dos maiores produtores em 2021. "
           "Você pode selecionar os países na caixa de seleção e visualizar a contribuição de cada país para a produção total.")
dados_paises = {
    "País": ["EUA 🇺🇸", "Arábia Saudita 🇸🇦", "Federação Russa 🇷🇺", "Canadá 🇨🇦", "Iraque 🇮🇶", 
             "China 🇨🇳", "Emirados Árabes Unidos 🇦🇪", "Irã 🇮🇷", "Brasil 🇧🇷"],
    "Produção de Petróleo em 2021 (barris por dia)": [16.6e6, 11e6, 10.9e6, 5.4e6, 4.1e6, 4e6, 3.7e6, 3.6e6, 3e6],
    "% do Total": [18.5, 12.2, 12.2, 6.0, 4.6, 4.4, 4.1, 4.0, 3.3]
}

df_producao_paises = pd.DataFrame(dados_paises)
selected_countries = st.multiselect("Selecione os países", df_producao_paises['País'].unique(), default=df_producao_paises['País'].unique())
df_selected_countries = df_producao_paises[df_producao_paises['País'].isin(selected_countries)]
fig_countries = px.bar(df_selected_countries, x="País", y="Produção de Petróleo em 2021 (barris por dia)",
                       color="% do Total", title="Os 10 maiores produtores de Petróleo em 2021",
                       labels={"Produção de Petróleo em 2021 (barris por dia)": "Produção de Petróleo (barris por dia)", "% do Total": "Percentual do Total"})
st.plotly_chart(fig_countries, use_container_width=True)


st.divider()
st.subheader("Breve análise dos top 5 países e as principais mudanças de 2021 em relação a 2022-2023")

st.write('Em 2022–23, o cenário global de exportação de petróleo sofreu uma mudança subtil. De acordo com os dados dos países exportadores de petróleo de 2023, as exportações aumentaram 0,8% em relação ao ano anterior, atrás da superfície agitou-se um mar de dinâmicas em mudança. Embora tenha registado uma expansão de 2,3%, a procura ficou aquém das expectativas originais, destacando factores adversos como o aumento da eficiência energética e a crescente adopção de veículos eléctricos. ')

st.write('Vejamos os 5 países que mais exportam de 2001 até hoje:')

conteudo_eua = """
**1. Estados Unidos:**
Com uma estimativa aproximada de 11.567.000 barris por dia, os Estados Unidos continuam a ser o principal produtor mundial de petróleo, como têm sido durante muitos anos.
"""

conteudo_arabia_saudita = """
**2. Arábia Saudita:**
A Arábia Saudita continua a ser o líder incontestado entre os gigantes exportadores de petróleo. Com enormes reservas de petróleo e tecnologias de extracção de ponta, a monarquia tem contribuído regularmente com a maior parte do mercado petrolífero global.
"""

conteudo_russia = """
**3. Rússia:**
Com base nos dados de 2023 dos países exportadores de petróleo, a Rússia é o maior país do mundo em área terrestre e também é um importante produtor de petróleo.
"""

conteudo_iraque = """
**4. Iraque:**
O Iraque, localizado no centro do Médio Oriente, é um exportador de petróleo resiliente. Apesar de problemas como a instabilidade política e a guerra regional, o Iraque continua a ser um dos 10 principais países exportadores de petróleo.
"""

conteudo_canada = """
**5. Canadá:**
Com as extensas paisagens do Canadá, o país solidificou a sua posição como um importante exportador de petróleo. As areias betuminosas e as reservas convencionais do Canadá contribuem principalmente para o mercado global de petróleo.
"""

st.markdown(conteudo_eua, unsafe_allow_html=True)
st.markdown(conteudo_arabia_saudita, unsafe_allow_html=True)
st.markdown(conteudo_russia, unsafe_allow_html=True)
st.markdown(conteudo_iraque, unsafe_allow_html=True)
st.markdown(conteudo_canada, unsafe_allow_html=True)

st.divider()

st.subheader("Fatores complexos e inter-relacionados")

st.write(':red[**Eventos geopolíticos nos países que mais exportam petróleo é crucial**] porque esses eventos têm o potencial de impactar significativamente o mercado global de petróleo e, por consequência, o preço por barril. Aqui estão algumas razões pelas quais é importante acompanhar esses eventos:')

st.write(':red[**Instabilidade no Fornecimento**]: Eventos geopolíticos, como conflitos armados, revoluções políticas ou tensões regionais, podem resultar em interrupções no fornecimento de petróleo. Se um país importante interrompe ou reduz sua produção de petróleo devido a instabilidades, isso pode afetar diretamente a oferta global.')

st.write(':red[**Tensões no Estreito de Ormuz**]: O Estreito de Ormuz, localizado entre o Irã e Omã, é uma passagem estratégica para o transporte de petróleo. Tensões geopolíticas na região podem levar a restrições no tráfego de petroleiros, afetando o suprimento global.')

st.write(':red[**Sanções Econômicas**]: A imposição de sanções econômicas a países produtores de petróleo pode restringir suas capacidades de produção e exportação. Isso pode levar a uma redução na oferta global, impactando os preços.')

st.write(':red[**Relações entre Países Exportadores**]: Disputas diplomáticas entre países exportadores de petróleo podem influenciar as decisões de produção e exportação. Acordos bilaterais ou desentendimentos podem ter efeitos diretos na oferta global.')

st.write(':red[**Mercado de Futuros e Especulação**]: Os traders nos mercados financeiros frequentemente reagem a eventos geopolíticos, antecipando possíveis impactos na oferta e demanda de petróleo. Isso pode levar a movimentos significativos nos preços dos contratos futuros de petróleo.')

st.write(':red[**Risco de Investimento**]: Investidores em petróleo e commodities consideram os riscos geopolíticos ao tomar decisões de investimento. A incerteza associada a eventos geopolíticos pode aumentar a volatilidade nos mercados.')

st.divider()

st.subheader('Previsão')

df.rename(columns={'data': 'ds', 'preco': 'y'}, inplace=True)

data_atual = df['ds'].max()
data_futuro = data_atual + datetime.timedelta(days=365)
futuro = pd.date_range(start=data_atual, end=data_futuro, freq='D')
futuro = pd.DataFrame({'ds': futuro})
df_prophet = pd.concat([df, futuro], ignore_index=True)

train_data = df_prophet[df_prophet['ds'] < '2022-01-01']
test_data = df_prophet[df_prophet['ds'] >= '2022-01-01']

model = Prophet()
model.fit(train_data)

future = model.make_future_dataframe(periods=365)
forecast = model.predict(future)

fig = px.line(forecast, x='ds', y=['yhat', 'yhat_lower', 'yhat_upper'], title='Previsão do Preço do Petróleo (Brent) para os Próximos 365 Dias')
fig.add_scatter(x=df_prophet['ds'], y=df_prophet['y'], mode='lines', name='Observado')
fig.update_xaxes(title_text='Data')
fig.update_yaxes(title_text='Preço do Petróleo')

fig.for_each_trace(lambda t: t.update(name=t.name.replace('yhat', 'Previsão').replace('yhat_lower', 'Limite mínimo').replace('yhat_upper', 'Limite máximo')))
st.plotly_chart(fig, use_container_width=True)

comparison_data = pd.merge(test_data[['ds', 'y']], forecast[['ds', 'yhat']], on='ds', how='inner')
accuracy_percentage = (1 - (comparison_data['y'] - comparison_data['yhat']).abs().sum() / comparison_data['y'].sum()) * 100
st.write(f'Acurácia do teste de 2022: {accuracy_percentage:.2f}%')

st.divider()

st.subheader('Próximos 365 dias')

modelo_prophet = Prophet(interval_width=0.75) 
modelo_prophet.fit(df_prophet)
previsao = modelo_prophet.predict(futuro)

fig = go.Figure()
fig.add_trace(go.Scatter(x=previsao['ds'], y=previsao['yhat'], mode='lines', name='Preço Previsto'))

fig.add_trace(go.Scatter(x=previsao['ds'], y=previsao['yhat_lower'], fill='tonexty', mode='lines', line=dict(width=0), name='Intervalo de Confiança'))
fig.add_trace(go.Scatter(x=previsao['ds'], y=previsao['yhat_upper'], fill='tonexty', fillcolor='rgba(0,100,80,0.2)', mode='lines', line=dict(width=0), name=''))

fig.update_xaxes(title_text='Data')
fig.update_yaxes(title_text='Previsão do Preço do Petróleo')

st.plotly_chart(fig, use_container_width=True)
