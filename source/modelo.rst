Persistência do modelo
----------------------
O modelo é persistido usando a biblioteca `joblib`, que é eficiente para salvar objetos Python grandes, como modelos de machine learning. O modelo é salvo em um arquivo chamado `modelo.joblib` na pasta `modelo`.

Integração com o Dashboard
----------------------
O modelo é carregado no dashboard usando a função `joblib.load()`, que lê o

Visualização dos Resultados
----------------------
Os resultados das previsões do modelo são visualizados no dashboard usando gráficos e tabelas. O
dashboard é construído usando a biblioteca `Dash`, que permite criar interfaces web interativas. Os gráficos são criados usando a biblioteca `Plotly`, que é integrada ao Dash para visualização de dados.