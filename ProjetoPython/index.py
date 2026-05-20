from templates.mantercategoria import ManterCategoriaUI
from templates.mantercliente import ManterClienteUI
from templates.manterproduto import ManterProdutoUI
from templates.reajustarproduto import ReajustarProdutoUI
from views import View
import streamlit as st

class IndexUI:

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", [
            "Entrar no Sistema",
            "Abrir Conta"])
        if op == "Entrar no Sistema": pass
        if op == "Abrir Conta": pass

    def menu_admin():            
        op = st.sidebar.selectbox("Menu", [
            "Cadastro de Categorias",
            "Cadastro de Clientes",
            "Cadastro de Produtos",
            "Reajustar Produtos"])
        if op == "Cadastro de Categorias": ManterCategoriaUI.main()
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Produtos": ManterProdutoUI.main()
        if op == "Reajustar Produtos": ReajustarProdutoUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", [
            "Listar produtos",
            "Inserir produto no carrinho",
            "Visualizar carrinho",
            "Comprar carrinho",
            "Listar minhas compras"])
        if op == "Listar produtos": pass
        if op == "Inserir produto no carrinho": pass
        if op == "Visualizar carrinho": pass
        if op == "Comprar carrinho": pass
        if op == "Listar minhas compras": pass

    def sidebar():
        IndexUI.menu_admin()

    def sair_do_sistema():
        pass

    def main():
        # verifica a existe o usuário admin
        View.cliente_criar_admin()
        # mostrar o menu lateral
        IndexUI.sidebar()

IndexUI.main()