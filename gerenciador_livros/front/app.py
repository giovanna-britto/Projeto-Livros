import streamlit as st
import requests

# Configurações da URL da API
API_URL = "http://127.0.0.1:8000/books"

# Título da Aplicação
st.title("Gerenciador de Livros 📚")

# Formulário para adicionar um novo livro
with st.form("Adicionar Livro"):
    title = st.text_input("Título")
    author = st.text_input("Autor")
    year = st.number_input("Ano", min_value=0, step=1)
    isbn = st.text_input("ISBN")
    category = st.text_input("Categoria")
    price = st.number_input("Preço", min_value=0.0, step=0.01)
    assessment = st.slider("Avaliação", min_value=1, max_value=5, step=1)

    # Botão de submissão
    submitted = st.form_submit_button("Adicionar Livro")

    if submitted:
        # Enviar dados para a API
        book_data = {
            "title": title,
            "author": author,
            "year": int(year),
            "isbn": isbn,
            "category": category,
            "price": float(price),
            "assessment": int(assessment),
        }
        response = requests.post(API_URL, json=book_data)

        if response.status_code == 201:
            st.success("Livro adicionado com sucesso!")
        else:
            st.error(f"Erro ao adicionar livro: {response.json()}")

# Listar todos os livros
st.header("Lista de Livros")
response = requests.get(API_URL)

if response.status_code == 200:
    books = response.json()

    if len(books) > 0:
        # Mostrar os livros em uma tabela
        for book in books:
            st.subheader(f"{book['title']} (ID: {book['id']})")
            st.write(f"**Autor:** {book['author']}")
            st.write(f"**Ano:** {book['year']}")
            st.write(f"**Categoria:** {book['category']}")
            st.write(f"**Preço:** R$ {book['price']:.2f}")
            st.write(f"**Avaliação:** {book['assessment']}/5")

            # Botão para deletar o livro
            if st.button(f"Excluir Livro {book['id']}", key=f"delete_{book['id']}"):
                delete_response = requests.delete(f"{API_URL}/{book['id']}")
                if delete_response.status_code == 204:
                    st.success(f"Livro ID {book['id']} excluído com sucesso!")
                else:
                    st.error(f"Erro ao excluir livro ID {book['id']}: {delete_response.json()}")

        # Formulário para atualizar livro
        st.subheader("Atualizar Livro")
        selected_book_id = st.selectbox("Selecione o ID do livro para atualizar", [book['id'] for book in books])

        if selected_book_id:
            # Recuperar o livro selecionado
            selected_book = next(book for book in books if book['id'] == selected_book_id)

            # Mostrar os campos para edição
            with st.form(f"Atualizar Livro {selected_book_id}"):
                new_title = st.text_input("Título", value=selected_book["title"])
                new_author = st.text_input("Autor", value=selected_book["author"])
                new_year = st.number_input("Ano", min_value=0, value=selected_book["year"], step=1)
                new_isbn = st.text_input("ISBN", value=selected_book["isbn"])
                new_category = st.text_input("Categoria", value=selected_book["category"])
                new_price = st.number_input("Preço", min_value=0.0, value=selected_book["price"], step=0.01)
                new_assessment = st.slider("Avaliação", min_value=1, max_value=5, value=selected_book["assessment"])

                # Botão de submissão para atualizar
                update_submitted = st.form_submit_button("Atualizar Livro")

                if update_submitted:
                    # Dados atualizados
                    updated_data = {
                        "title": new_title,
                        "author": new_author,
                        "year": int(new_year),
                        "isbn": new_isbn,
                        "category": new_category,
                        "price": float(new_price),
                        "assessment": int(new_assessment),
                    }

                    # Enviar atualização para a API
                    update_response = requests.put(f"{API_URL}/{selected_book_id}", json=updated_data)

                    if update_response.status_code == 200:
                        st.success(f"Livro ID {selected_book_id} atualizado com sucesso!")
                    else:
                        st.error(f"Erro ao atualizar livro ID {selected_book_id}: {update_response.json()}")

    else:
        st.info("Nenhum livro cadastrado.")
else:
    st.error("Erro ao buscar livros.")
