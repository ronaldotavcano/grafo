import matplotlib.pyplot as plt #Visualização do grafo
import networkx as nx # Criação do grafo
import pandas as pd # leitura e organização dos dados

matriz_artistas = [
    ["Rafael Generoso Ponzetto", "Mili", "Charlie Brown", "AC/DC", "O Rappa", "Metallica"],
    ["Nicolas Emanuel Pinheiro", "Matue", "Alee", "Central Cee"],
    ["Miguel Aparecido Guimarães Santos", "Alex Turner", "Paul McCartney", "Elvis Presley", "John Lennon", "Damon Albarn"],
    ["Miguel Vinícius de Oliveira Ferreira", "Alee", "Tim Maia", "MC IGU", "Laufey"],
    ["João Pedro Barbosa Scaquette", "Kevin", "Mc PP da VS", "Racionais"],
    ["Matheus Silva Carneiro", "Matue", "Wiu", "Kevin"],
    ["Vinícius Silva Mita Mayer", "Negão Original", "Kevin", "Daleste"],
    ["Ronaldo", "Bruno e Marrone", "Jorge e Matheus", "Cristiano Araújo"],
    ["Matheus Kreski", "Yun Li", "Hugovhb", "Yoasobi", "EF", "Chrono Rapper", "Seu Jorge"],
    ["Vitor Mapelli", "Michael Jackson", "Eminem", "Exalta Samba", "Zeca Pagodinho", "Seu Jorge"],
    ["Miguel Venâncio", "Limp Bizkit", "Korn", "Rage Against the Machine"],
    ["Stella", "LiSA", "Yoasobi", "Mitski"],
    ["Vitoria Gonçalves Colombo", "Stray Kids", "Aespa", "LiSA"],
    ["Nicolas Marques Vilela", "Ice Cube", "Dr. Dre", "Nas"],
    ["Eduardo Girão", "Tame Impala", "Gorillaz", "Tribalistas"],
    ["Pedro Gabriel Aiello", "Scorpions", "Home", "Edu Falaschi"],
    ["Vitor Guilherme", "Ryan Gosling", "Kevin Hart", "Ice Cube"],
    ["Iago Gabriel", "Michael Jackson", "Sabrina Carpenter", "Eminem", "Evanescence", "Knocked Loose",
     "Arctic Monkeys", "Gorillaz", "BABYMETAL", "LiSA", "Haruka Tomatsu", "ASCA",
     "Necry Talkie", "Yoasobi", "Morning Musume", "MYTH & ROID"],
    ["Victor Freire", "Manoel Gomes", "Kanye West", "Childish Gambino"],
    ["Pedro Henrique Vieira Carvalho", "Phil Anselmo" , "Charlie Brown Jr", "Sepultura"],
    ["Felipe Chiaramonte De Souza ", "Mc pipoquinha", "Os Barões da pisadinha", "Marília Mendonça", "Mc Dalete"],
    ["Victor Hugo brahim affonso ", "Michael Jackson", "Pablo citar", "oruam"],
    ["Murilo Pericini", "Vin diesel", "the rock", "Paul walker"],
    ["Leonardo Aguiar", "Jorge e Matheus", "Charles Do Bronxs", "Neymar"],
    ["giovanna da guarda lopes", "selena gomes", "caio castro", "sabrina carpenter"],
    ["Tiago Konishi", "Cristiano Ronaldo", "Messi", "Neymar"],
    ["Enzo Takaku Gonçalves", "Guri", "Zero", "Duzz"],
    ["Maria Fernanda", "Rosa de saron", "henrique e juliano", "chase atlantic"],
    ["Sergio Rodrigues Zuicker", "Cristiano Ronaldo", "Abel Ferreira", "Jayson Tatum"],
    ["Vinicius Pedro Menezes", "Mano Brown", "Djonga", "Yago Oproprio"],
    ["Yohan", "Damon Albarn", "bbno$", "Chris Christodoulou"],
    ["João Bosco Adão da Silva André", "Alee", "Travis Scott", "Kanye West"],
    ["Miguel Felizardo dos Reis", "Travis scott", "A$AP Rocky", "pop smoke"],
    ["Murilo Santos Teixeira", "Drake", "Eminem", "50cent"],
    ["Gabriel Roncon", "Alee", "WS da igrejinha", "DJ Arana", "The Weeknd"],
    ["Otávio Sá", "Mc Paiva", "Mc IG", "Cbjr"]
]

lista_pesquisa = []
for linha in matriz_artistas:
    pessoa = linha[0]
    artistas = linha[1:]
    for artista in artistas:
        lista_pesquisa.append((pessoa, artista))

# Cria uma tabela com 2 colunas                    0           1
df_long = pd.DataFrame(lista_pesquisa, columns=["Pessoa", "Artistas"])

# cria um grafo vazio
Grafo = nx.Graph()

pessoas = list(set(df_long["Pessoa"])) # cria uma lista com o nome das pessoas
artistas = list(set(df_long["Artistas"]))# cria uma lista com o nome dos artistas

# Adiciona nós no grafos
Grafo.add_nodes_from(pessoas, bipartite=0)  # nó de pessoa
Grafo.add_nodes_from(artistas, bipartite=1) # nó de coluna

# Cria uma aresta que liga pessoa aos artistas
for aresta, row in df_long.iterrows():
    Grafo.add_edge(row["Pessoa"], row["Artistas"])

# Calcula a popularidade            quantidade      dicionario -> {Artista : Qtd}
popularidade = df_long["Artistas"].value_counts().to_dict()

#calcula a posição de cada nó
pos = nx.spring_layout(Grafo, seed=42, k=1.2)


tamanho_no = [600 if node in pessoas else 200 + popularidade.get(node, 1) * 100 for node in Grafo.nodes()]


cor_arestas = []
# Um nó de uma ponta e o da outra ponta da mesma aresta(u e v)
for u, v in Grafo.edges():
    artista = v if v in popularidade else u
    pop = popularidade.get(artista, 1)
    if pop >= 5:
        cor_arestas.append("red")
    elif pop >= 3:
        cor_arestas.append("orange")
    else:
        cor_arestas.append("gray")

# Define o tamanho da figura
plt.figure(figsize=(20, 14))
#Desenho dos nós
nx.draw_networkx_nodes(Grafo, pos, nodelist=pessoas, node_color='skyblue', node_size=700, label='Pessoas')
nx.draw_networkx_nodes(Grafo, pos, nodelist=artistas,node_color='lightgreen', node_size=[tamanho_no[list(Grafo.nodes()).index(n)] for n in artistas], label='Artistas')
#Desenho das arestas
nx.draw_networkx_edges(Grafo, pos, edge_color=cor_arestas)
#fonte dos nós
nx.draw_networkx_labels(Grafo, pos, font_size=10)

plt.title("Grafo Bipartido com Popularidade dos Artistas", fontsize=20)
plt.axis('off')
plt.tight_layout()
plt.show()