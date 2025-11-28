import json
import sys

def validar_json(caminho_arquivo):
    try:
        file = open(caminho_arquivo, "rt", encoding='utf-8')
        json_data = file.read()
        file.close()

        if not json_data.strip():
            raise Exception("Erro: Ficheiro Vazio!")

        dados = json.loads(json_data)

        if isinstance(dados, dict) and all(key in dados for key in ['nome', 'idade', 'localização']):
            print(dados)
        else:
            print("Erro: Campos Obrigatórios em Falta!")

    except FileNotFoundError:
        print("Erro: Ficheiro Não Encontrado!")
    
    except json.JSONDecodeError:
        print("Erro: Ficheiro Não Contém JSON Válido!")
    
    except Exception as e:
        print("Erro: Ficheiro Vazio!")
    
    finally:
        print("Processo Concluído!")

if __name__ == "__main__":
    caminho = input()
    validar_json(caminho)