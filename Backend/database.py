import sqlite3

pft = 7
frequencia_letras = {"a":14.63,"á":0.55,"à":0.05,"â":0.10,"ã":0.35,"b":1.04,"c":3.88,"ç":0.47,"d":4.99,"e":12.57,"é":1.10,"ê":0.40,"f":1.02,"g":1.30,"h":1.28,"i":6.18,"í":0.35,"j":0.40,"k":0.02,"l":2.78,"m":4.74,"n":5.05,"o":10.73,"ó":0.60,"ô":0.15,"õ":0.15,"p":2.52,"q":1.20,"r":6.53,"s":7.81,"t":4.34,"u":4.63,"ú":0.25,"v":1.67,"w":0.01,"x":0.21,"y":0.01,"z":0.47}

conn = sqlite3.connect("/home/martim/Documents/Hackathon/overcomplicated-hangman/Backend/hangman.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS base_de_dados(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               palavra TEXT NOT NULL,
               tamanho INTEGER NOT NULL,
               dificuldade REAL NOT NULL,
               complexidade REAL NOT NULL)
""")


def insere_palavra_database(palavra):
    complexidade, dificuldade = 0, 0
    for letra in palavra.lower():
        dificuldade += frequencia_letras[letra]
    
    tamanho = len(palavra)
    complexidade = tamanho*(1-pft) + dificuldade*pft
    cursor.execute("INSERT INTO base_de_dados (palavra, tamanho, dificuldade, complexidade) VALUES (?, ? ,?, ?)", (palavra, len(palavra), dificuldade, complexidade))

with open("/home/martim/Documents/Hackathon/overcomplicated-hangman/Backend/palavras.txt", "r") as file:
    palavras = file.readlines()

for palavra in palavras:
    insere_palavra_database(palavra.rstrip())

cursor.execute("SELECT id, palavra, tamanho, dificuldade, complexidade FROM base_de_dados ORDER BY complexidade DESC")
for coluna in cursor.fetchall():
    print(coluna)

conn.commit()
conn.close()
print("Funcionou")

