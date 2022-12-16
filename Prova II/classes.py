import requests
from newsapi import NewsApiClient

class Noticias():
    def __init__ (self, titulo, data, assunto, categoria, conteudo, url, autor):
        self.titulo = titulo
        self.data = data
        self.assunto = assunto
        self.categoria = categoria
        self.conteudo = conteudo
        self.url = url
        self.autor = autor

    def get_titulo(self):
        return self.titulo
    def get_data(self):
        return self.data
    def get_assunto(self):
        return self.assunto
    def get_categoria(self):
        return self.categoria
    def get_conteudo(self):
        return self.conteudo
    def get_url(self):
        return self.url
    def get_autor(self):
        return self.autor

    def set_titulo(self, titulo):
        self.titulo = titulo
    def set_data(self, data):
        self.data = data
    def set_assunto(self, assunto):
        self.assunto = assunto
    def set_categoria(self, categoria):
        self.categoria = categoria
    def set_conteudo(self, conteudo):
        self.conteudo = conteudo
        