from pydantic_settings import BaseSettings  # Importa BaseSettings do Pydantic Settings para gerenciamento de configurações

# Classe que gerencia as configurações do projeto
class Settings(BaseSettings):
    # Configura a URL do banco de dados, que será lida do arquivo .env
    DATABASE_URL: str  # Caminho para a conexão com o banco de dados (ex.: SQLite, PostgreSQL, etc.)

    # Configura a opção de depuração (debug), com valor padrão como False
    DEBUG: bool = False  # Indica se o modo de depuração está ativado ou não (útil para desenvolvimento)

    # Configuração adicional para o carregamento do arquivo .env
    class Config:
        env_file = ".env"  # Especifica o arquivo de ambiente (.env) de onde as configurações serão carregadas
        env_file_encoding = "utf-8"  # Define a codificação do arquivo .env como UTF-8
