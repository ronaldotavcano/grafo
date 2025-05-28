import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

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
    ["Victor Freire", "Manoel Gomes", "Kanye West", "Childish Gambino"]
]

lista_pesquisa = []
for linha in matriz_artistas:
    pessoa = linha[0]
    artistas = linha[1:]
    for artista in artistas:
        lista_pesquisa.append((pessoa, artista))

df_long = pd.DataFrame(lista_pesquisa, columns=["Pessoa", "Artistas"])


G = nx.Graph()
pessoas = list(set(df_long["Pessoa"]))
artistas = list(set(df_long["Artistas"]))

G.add_nodes_from(pessoas, bipartite=0)
G.add_nodes_from(artistas, bipartite=1)

for _, row in df_long.iterrows():
    G.add_edge(row["Pessoa"], row["Artistas"])

popularidade = df_long["Artistas"].value_counts().to_dict()


pos = nx.spring_layout(G, seed=42, k=0.7)


node_sizes = [500 if node in pessoas else 300 + popularidade.get(node, 1) * 100 for node in G.nodes()]


edge_colors = []
for u, v in G.edges():
    artista = v if v in popularidade else u
    pop = popularidade.get(artista, 1)
    if pop >= 5:
        edge_colors.append("red")
    elif pop >= 3:
        edge_colors.append("orange")
    else:
        edge_colors.append("gray")


plt.figure(figsize=(20, 14))
nx.draw_networkx_nodes(G, pos, nodelist=pessoas, node_color='skyblue', node_size=600, label='Pessoas')
nx.draw_networkx_nodes(G, pos, nodelist=artistas,
                       node_color='lightgreen',
                       node_size=[node_sizes[list(G.nodes()).index(n)] for n in artistas],
                       label='Artistas')
nx.draw_networkx_edges(G, pos, edge_color=edge_colors)
nx.draw_networkx_labels(G, pos, font_size=8)

plt.title("Grafo Bipartido com Popularidade dos Artistas", fontsize=18)
plt.axis('off')
plt.tight_layout()
plt.show()