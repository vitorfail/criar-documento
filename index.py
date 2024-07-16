from base64 import encodebytes
from statistics import mode
from flask import Flask, request, send_file, jsonify
from PIL import Image, ImageFont, ImageDraw
from flask_cors import CORS
import os
import random

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
def criar():
  if request.json == None or request.json == False:
    return 'Não há nehum parâmetro. Por favor envie a descriçaõ da imagem'
  else:
    t =29
    tipo1 = {
      "font_nome": r"font/auto.otf",
      "font_size_nome": t,
      "font_assinaturas": r"font/fran.ttf",
      "font_size_assinaturas": t,
      "assinatura": r"font/fran.ttf",
      "font_size_assinatura": t,
      "coord_nome": (759, 455),
      "coord_sex": (759, 680),
      "coord_data_nasci": (759, 790),
      "coord_data_expi": (759, 902),
      "coor_assinatura": (279, 802),
      "posicao": (191, 285),
      "tamanho":(294, 422),
      "imagem": r'moc1.jpg'
    }
    tipo2 = {
      "font_nome": r"font/auto.otf",
      "font_size_nome": t,
      "font_assinaturas": r"font/fran.ttf",
      "font_size_assinaturas": t,
      "assinatura": r"font/fran.ttf",
      "font_size_assinatura": t,
      "coord_nome": (760, 423),
      "coord_sex": (760, 640),
      "coord_data_nasci": (760, 740),
      "coord_data_expi": (760, 843),
      "coor_assinatura": (254, 756),
      "posicao": (196, 267),
      "tamanho":(294, 394),
      "imagem": r'moc2.jpg'
    }
    tipo3 = {
      "font_nome": r"font/auto.otf",
      "font_size_nome": t,
      "font_assinaturas": r"font/fran.ttf",
      "font_size_assinaturas": t,
      "assinatura": r"font/fran.ttf",
      "font_size_assinatura": t,
      "coord_nome": (723, 416),
      "coord_sex": (723, 633),
      "coord_data_nasci": (723, 729),
      "coord_data_expi": (723, 828),
      "coor_assinatura": (229, 736),
      "posicao": (181, 261),
      "tamanho":(281, 391),
      "imagem": r'moc3.jpg'
    }
    tipo4 = {
      "font_nome": r"font/auto.otf",
      "font_size_nome": t,
      "font_assinaturas": r"font/fran.ttf",
      "font_size_assinaturas": t,
      "assinatura": r"font/fran.ttf",
      "font_size_assinatura": t,
      "coord_nome": (761, 432),
      "coord_sex": (761, 650),
      "coord_data_nasci": (761, 752),
      "coord_data_expi": (761, 857),
      "coor_assinatura": (231, 750),
      "posicao": (192, 265),
      "tamanho":(298, 401),
      "imagem": r'moc4.jpg'
    }
    tipo5 = {
      "font_nome": r"font/auto.otf",
      "font_size_nome": t,
      "font_assinaturas": r"font/fran.ttf",
      "font_size_assinaturas": t,
      "assinatura": r"font/fran.ttf",
      "font_size_assinatura": t,
      "coord_nome": (752, 434),
      "coord_sex": (752, 668),
      "coord_data_nasci": (752, 767),
      "coord_data_expi": (752, 874),
      "coor_assinatura": (231, 757),
      "posicao": (190, 274),
      "tamanho":(295, 410),
      "imagem": r'moc5.jpg'
    }
    tipo6 = {
      "font_nome": r"font/auto.otf",
      "font_size_nome": t,
      "font_assinaturas": r"font/fran.ttf",
      "font_size_assinaturas": t,
      "assinatura": r"font/fran.ttf",
      "font_size_assinatura": t,
      "coord_nome": (752, 432),
      "coord_sex": (752, 656),
      "coord_data_nasci": (752, 756),
      "coord_data_expi": (752, 858),
      "coor_assinatura": (237, 756),
      "posicao": (189, 267),
      "tamanho":(299, 400),
      "imagem": r'moc6.jpg'
    }
    tipo7 = {
      "font_nome": r"font/auto.otf",
      "font_size_nome": t,
      "font_assinaturas": r"font/fran.ttf",
      "font_size_assinaturas": t,
      "assinatura": r"font/fran.ttf",
      "font_size_assinatura": t,
      "coord_nome": (765, 421),
      "coord_sex": (765, 648),
      "coord_data_nasci": (765, 744),
      "coord_data_expi": (765, 847),
      "coor_assinatura": (273, 743),
      "posicao": (192, 264),
      "tamanho":(298, 399),
      "imagem": r'moc7.jpg'
    }
    tipo8 = {
      "font_nome": r"font/auto.otf",
      "font_size_nome": t,
      "font_assinaturas": r"font/fran.ttf",
      "font_size_assinaturas": t,
      "assinatura": r"font/fran.ttf",
      "font_size_assinatura": t,
      "coord_nome": (764, 430),
      "coord_sex": (764, 667),
      "coord_data_nasci": (764, 765),
      "coord_data_expi": (764, 864),
      "coor_assinatura": (234, 762),
      "posicao": (192, 271),
      "tamanho":(297, 407),
      "imagem": r'moc8.jpg'
    }
    tipo9 = {
      "font_nome": r"font/auto.otf",
      "font_size_nome": t,
      "font_assinaturas": r"font/fran.ttf",
      "font_size_assinaturas": t,
      "assinatura": r"font/auto.otf",
      "font_size_assinatura": t,
      "coord_nome": (728, 436),
      "coord_sex": (728, 669),
      "coord_data_nasci": (728, 770),
      "coord_data_expi": (728, 872),
      "coor_assinatura": (228, 761),
      "posicao": (183, 272),
      "tamanho":(284, 409),
      "imagem": r'moc9.jpg'
    }
    
    def tipo(t):
      if t == "tipo1":
        return tipo1
      if t == "tipo2":
        return tipo2
      if t == "tipo3":
        return tipo3
      if t == "tipo4":
        return tipo4
      if t == "tipo5":
        return tipo5
      if t == "tipo6":
        return tipo6
      if t == "tipo7":
        return tipo7
      if t == "tipo8":
        return tipo8
      if t == "tipo9":
        return tipo9
    dados = request.json
    result = tipo(dados['tipo'])
    coord_nome = result["coord_nome"]
    coord_sex = result["coord_sex"]
    coord_data_nasci = result["coord_data_nasci"]
    coord_data_expi = result["coord_data_expi"]
    coor_assinatura = result["coor_assinatura"]
    posicao = result['posicao']
    tamanho = result['tamanho']


    imagem = Image.open(result["imagem"])
    font_nome = ImageFont.truetype(result["font_nome"], result["font_size_nome"])
    font_assinatura = ImageFont.truetype(result["font_assinaturas"], result["font_size_assinaturas"])

    nome = dados['nome']
    data_nasci = dados['data_nasci']
    data_expi = dados['data_expi']
    sex = dados['sex']
    assinatura = dados['assinatura']

    if sex == "WOMAN":
      diretorio = 'woman'

      # Lista todos os arquivos no diretório
      arquivos = os.listdir(diretorio)

      # Escolhe um arquivo aleatório da lista
      arquivo_aleatorio = random.choice(arquivos)
      imagem_sobreposta = Image.open(diretorio+'/'+arquivo_aleatorio)
      imagem_sobreposta = imagem_sobreposta.resize(tamanho, Image.Resampling.LANCZOS)
      imagem.paste(imagem_sobreposta, posicao)
    if sex == "MAN":
      diretorio = 'man'

      # Lista todos os arquivos no diretório
      arquivos = os.listdir(diretorio)

      # Escolhe um arquivo aleatório da lista
      arquivo_aleatorio = random.choice(arquivos)
      imagem_sobreposta = Image.open(diretorio+'/'+arquivo_aleatorio)
      imagem_sobreposta = imagem_sobreposta.resize(tamanho,Image.Resampling.LANCZOS)
      imagem.paste(imagem_sobreposta, posicao)

    rgb_azul = (4, 4, 4)
    desenho = ImageDraw.Draw(imagem)
    w1, h1 = font_nome.getsize(nome)
    W1, H1 = coord_nome
    W2, H2 = font_assinatura.getsize(dados['data_nasci'])
    w2, h2 = coord_data_nasci
    w3, h3 = coord_data_expi
    w5, h5 = coor_assinatura
    w, h = desenho.textsize(nome)
    desenho.text(coord_nome, nome, font=font_assinatura, fill=rgb_azul)
    desenho.text(coord_data_nasci, data_nasci, font=font_assinatura, fill=rgb_azul)
    desenho.text(coord_data_expi, data_expi, font=font_assinatura, fill=rgb_azul)
    desenho.text((w5 - w, h5 - h), assinatura, font=font_nome, fill=rgb_azul)
    desenho.text(coord_sex, sex, font=font_assinatura, fill=rgb_azul)

    imagem.save(f'{nome}.jpg')
    filename = nome + '.jpg'
    return send_file(filename, mimetype='image/jpg')      
     

@app.route('/', methods=['GET'])
def responder():
  return 'Não usamos esse método'

if __name__ == '__main__': 
  app.run()
