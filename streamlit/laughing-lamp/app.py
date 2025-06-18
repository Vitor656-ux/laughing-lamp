import streamlit as st

st.set_page_config(page_title="Projeto Streamlit", layout='wide')

st.markdown("# Testando o Streamlit")

def main():
    abas = st.tabs([
        'Clientes',
        'Cadastrar Cliente',
        'Editar', 
        'Deletar',
    ])

    with abas[0]:
        st.title('Clientes')

        with st.form (key= 'add_cliente', clear_on_submit=True):
            nome = st.text.input('Nome', placwholder='Nome')
            email = st.text.input('email', placwholder='email')
            idade = st.number_input('idade', placwholder='idade')
            telefone = st.number_input('telefone', placwholder='telefone')
            profissao = st.selectbox('Selecione a profissão', options=[
                'Desevolvedor Web',  'Analista de Infraestrutura',
                'DBA Senior', 'Tecnico de Informatica'
            ])
            btn_cadastrar = st.form_submit_button('Cadastrar Clientes')
            
            data_cliente = {
                    "nome": nome,
                    "email": email,
                    "idade": idade,
                    "telefone": telefone,
                    "profissao": profissao 
            }

            if btn_cadastrar:
                if not nome or not email or idade == 0:
                    st.error("Todos os campos precisam ser preechidos")
    
    with abas[1]:
        st.title('Cadastrar Cliente')

    with abas[2]:
        st.title('Editar')

    with abas[3]:
        st.title('Deletar')

main()