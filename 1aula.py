while True:
    meme_dict = {
                "CRINGE": "Algo vergonhoso ou constrangedor",
                "STALKEAR": "Investigar a vida de alguém online",
                "VDD": "abreviação da palavrav verdade",
                "BISCOITAR": "postar algo apenas para chamar a atenção",
                "HATER": "pessoa que está constantemente criticando os outros",
                "VLW":  "abreviação da palavra valeu",
                "67": "é apenas 67, nao tem um sentido"
                }
    
    word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")
    
    if word in meme_dict.keys():
        print("Significado de " + word + ": " + meme_dict[word])
    else:
        print("palavra nao encontrada")
