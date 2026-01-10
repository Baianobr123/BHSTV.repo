import os

def gerar_index():
    repo_name = "Meu Repositório Kodi"
    zips_path = "zips"
    
    if not os.path.exists(zips_path):
        print("Pasta 'zips' não encontrada.")
        return

    # Lista as pastas de addons dentro de zips
    addons = [d for d in os.listdir(zips_path) if os.path.isdir(os.path.join(zips_path, d))]
    
    html_content = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{repo_name}</title>
        <style>
            body {{ font-family: sans-serif; background: #121212; color: white; text-align: center; padding: 50px; }}
            .container {{ max-width: 800px; margin: auto; background: #1e1e1e; padding: 20px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }}
            h1 {{ color: #00d2ff; }}
            ul {{ list-style: none; padding: 0; }}
            li {{ background: #2a2a2a; margin: 10px 0; padding: 15px; border-radius: 5px; display: flex; justify-content: space-between; align-items: center; }}
            a {{ color: #00d2ff; text-decoration: none; font-weight: bold; }}
            a:hover {{ text-decoration: underline; }}
            .footer {{ margin-top: 30px; font-size: 0.8em; color: #666; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{repo_name}</h1>
            <p>Para instalar, adicione esta URL no Gestor de Arquivos do Kodi.</p>
            <hr>
            <h3>Addons Disponíveis:</h3>
            <ul>
    """

    for addon in addons:
        html_content += f'<li><span>{addon}</span> <a href="zips/{addon}/">Ver Arquivos</a></li>\n'

    html_content += """
            </ul>
            <div class="footer">Gerado automaticamente para o seu Repositório Kodi</div>
        </div>
    </body>
    </html>
    """

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print("[SUCESSO] index.html gerado com sucesso!")

if __name__ == "__main__":
    gerar_index()