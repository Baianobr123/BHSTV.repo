import os
import hashlib

class GeradorDeRepositorio:
    """
    Classe para gerar os arquivos addons.xml e addons.xml.md5
    necessários para um repositório Kodi.
    """
    
    def __init__(self):
        # Define onde estão os addons. Padrão é a pasta 'zips' no mesmo diretório deste script
        self.zips_path = 'zips'
        
        # Arquivos de saída
        self.addons_xml = os.path.join(self.zips_path, 'addons.xml')
        self.addons_xml_md5 = os.path.join(self.zips_path, 'addons.xml.md5')

    def gerar(self):
        # Verifica se a pasta zips existe
        if not os.path.exists(self.zips_path):
            print(f"[ERRO] A pasta '{self.zips_path}' não foi encontrada.")
            print("Certifique-se de criar a pasta 'zips' e colocar seus addons lá dentro.")
            return

        print("Iniciando gerador de repositório...")
        
        # Cria a lista de XMLs
        xmls = []
        
        # Caminha pelas pastas dentro de 'zips'
        for pasta in os.listdir(self.zips_path):
            pasta_path = os.path.join(self.zips_path, pasta)
            
            # Pula se não for diretório (ex: arquivos soltos)
            if not os.path.isdir(pasta_path):
                continue
                
            # Procura o arquivo addon.xml dentro da pasta do addon
            arquivo_xml = os.path.join(pasta_path, 'addon.xml')
            
            if os.path.exists(arquivo_xml):
                try:
                    # Lê o conteúdo do xml do addon
                    with open(arquivo_xml, 'r', encoding='utf-8') as f:
                        xml_content = f.read()
                        
                        # Remove a primeira linha (declaração <?xml ...?>) para não duplicar
                        # e limpa espaços extras
                        if xml_content.startswith('<?xml'):
                            xml_content = xml_content.split('\n', 1)[1]
                        
                        xmls.append(xml_content.strip())
                        print(f"[OK] Lido: {pasta}")
                except Exception as e:
                    print(f"[ERRO] Falha ao ler {pasta}: {e}")
            else:
                print(f"[AVISO] addon.xml não encontrado em: {pasta}")

        # Monta o XML final
        xml_mestre = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
        xml_mestre += '<addons>\n\n'
        xml_mestre += '\n\n'.join(xmls)
        xml_mestre += '\n\n</addons>'

        # 1. Salva o arquivo addons.xml
        try:
            with open(self.addons_xml, 'w', encoding='utf-8') as f:
                f.write(xml_mestre)
            print(f"\n[SUCESSO] Arquivo 'addons.xml' criado em {self.addons_xml}")
        except Exception as e:
            print(f"[ERRO] Falha ao salvar addons.xml: {e}")
            return

        # 2. Gera e salva o arquivo MD5
        try:
            # Calcula o MD5 do conteúdo gerado
            md5_hash = hashlib.md5(xml_mestre.encode('utf-8')).hexdigest()
            
            with open(self.addons_xml_md5, 'w', encoding='utf-8') as f:
                f.write(md5_hash)
            print(f"[SUCESSO] Arquivo 'addons.xml.md5' criado em {self.addons_xml_md5}")
        except Exception as e:
            print(f"[ERRO] Falha ao gerar MD5: {e}")

if __name__ == "__main__":
    gerador = GeradorDeRepositorio()
    gerador.gerar()