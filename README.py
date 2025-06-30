#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `tranlate-sheel` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar/desinstalar o `translate-sheel` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _In this document are contained the main commands and settings to set up/install/use/uninstalll the `translate-shell` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `translate-shell`
# 
# O `translate-shell` é uma ferramenta de linha de comando de código aberto que oferece a capacidade de traduzir texto e palavras entre vários idiomas diretamente do `Terminal Emulator`. Ele utiliza serviços de tradução _online_, como o `Google Translate`, para fornecer traduções rápidas e precisas. O `translate-shell` suporta uma ampla variedade de idiomas e pode ser usado tanto para traduções simples de palavras e frases quanto para traduções mais complexas de texto completo. Além disso, ele oferece opções avançadas, como tradução de áudio, detecção automática de idioma e pronúncia de palavras, tornando-se uma ferramenta útil para estudantes, viajantes e qualquer pessoa que precise de traduções instantâneas e convenientes diretamente do `Terminal Emulator`.
# 
# ### `pdftotext`
# 
# O `pdftotext` é uma ferramenta de linha de comando, geralmente parte do pacote `Poppler` ou `Xpdf`, que converte o conteúdo de arquivos PDF em texto simples. Ele extrai o texto mantendo a ordem de leitura e pode preservar ou não a formatação de colunas e quebras de linha, conforme opções configuráveis. É muito útil para automatizar a extração de texto de documentos PDF em _scripts_ e fluxos de trabalho de análise de dados ou indexação.
# 
# ### `pdfimages`
# 
# O `pdfimages` é uma ferramenta para extrair imagens de arquivos PDF. Caso seu PDF contenha imagens e você queira extraí-las, pode ser útil antes de uma conversão com OCR, como no caso de um PDF digitalizado.
# 
# ### `qpdf`
# 
# O `qpdf` é uma ferramenta para manipular arquivos PDF de maneira avançada. Você pode usá-lo para fazer operações como quebra de PDFs, mesclagem, e até mesmo para manipular metadados.
# 
# ### `pdfunite`
# 
# O `pdfunite` é uma ferramenta de linha de comando, integrante do pacote Poppler, que permite mesclar vários arquivos PDF em um único documento. Basta informar na chamada os arquivos de entrada e o nome do PDF de saída. É ideal para scripts e fluxos de trabalho automatizados de organização e consolidação de documentos.

# ## 1. Como configurar/instalar/usar o `translate-shell` no `Linux Ubuntu` [1]
# 
# Para instalar o `translate-shell` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
#     
#     ```bash
#     sudo apt clean
#     ``` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do `cache` local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando:
#     
#     ```bash
#     sudo apt autoclean
#     ```
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando:
#     
#     ```bash
#     sudo apt autoremove -y
#     ```
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: 
#     
#     ```bash
#     sudo apt update
#     ```
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes:
#     
#     ```bash
#     sudo apt --fix-broken install
#     ```
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
#     
#     ```bash
#     sudo apt clean
#     ``` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  
#     
#     ```bash
#     sudo apt list --upgradable
#     ```
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`:
#     
#     ```bash
#     sudo apt full-upgrade -y
#     ```

# 3. Para instalar o `Google Translate` para ser usado a partir do terminal no `Linux Ubuntu`, você pode usar uma ferramenta chamada `translate-shell`. Ela é um aplicativo de linha de comando que permite usar o Google Translate, Bing Translator, Yandex. Translate e outros serviços de tradução diretamente do terminal. Aqui estão os passos para instalá-lo:
# 
# 4. **Instale o `Translate-Shell`:** Após atualizar os pacotes, instale o `translate-shell` usando o seguinte comando: `sudo apt install translate-shell -y`
# 
# 5. **Verifique a Instalação:** Depois de instalar, você pode verificar se a instalação foi bem-sucedida executando o comando `trans`: `trans -V`
# 
# 6. **Como Usar:** Para usar o `translate-shell`, você pode simplesmente digitar `trans` seguido pelo texto que deseja traduzir. Por exemplo, para traduzir `"Hello World"` do inglês (`en`) para português (`pt-BR`), você usaria: `trans en:pt-BR "Hello World"`
# 
# Lembre-se de que o `translate-shell` usa APIs de tradução online, então você precisará de uma conexão com a internet para usar essa ferramenta.

# ### 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `translate-sheel` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean
#     sudo apt autoclean
#     sudo apt autoremove -y
#     sudo apt update
#     sudo apt --fix-broken install
#     sudo apt clean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     sudo apt install translate-shell -y
#     trans -V
#     trans en:pt-BR "Hello World"
#     ```
# 

# ## 2. Como usar o `translate-shell` [3]
# 
# Esta ferramenta pode identificar o idioma do texto fonte automaticamente. **Por padrão, ele traduz o texto original para o inglês.**

# ### 2.1 Traduzir para o inglês [3]
# 
# 1. Vou traduzir `"saudável"` para inglês. Para isso só teremos que escrever no terminal (`Ctrl + Alt + T`):
# 
#     ```
#     trans saúde
#     saúde
# 
#     health
# 
#     Definitions of saúde
#     [ Português Brasileiro -> English ]
# 
#     noun
#         health
#             saúde, sanidade, brinde
#         welfare
#             bem, prosperidade, saúde, felicidade, bem-estar
# 
#     saúde
#         health, Cheers, Healthcare
#     ```
#     

# ### 2.2 Selecione o idioma para traduzir [3]
# 
# 1. Podemos traduzir uma palavra (neste caso a mesma do exemplo anterior) para russo (por exemplo) usando o seguinte comando:
# 
#     ```
#     trans :ru saúde
#     saúde
# 
#     здоровье
#     (zdorov'ye)
# 
#     Translations of saúde
#     [ Português Brasileiro -> Русский ]
# 
#     saúde
#         здоровье
#     ```
# 

# ### 2.3 Traduzir para mais de um idioma [3]
# 
# 1. Para traduzir uma palavra para mais de um idioma, poderemos utilizar o seguinte comando (Neste exemplo, vou traduzir a palavra saúde para inglês e russo):
# 
#     ```
#     trans :en+ru saúde
#     saúde
# 
#     health
# 
#     Definitions of saúde
#     [ Português Brasileiro -> English ]
# 
#     noun
#         health
#             saúde, sanidade, brinde
#         welfare
#             bem, prosperidade, saúde, felicidade, bem-estar
# 
#     saúde
#         health, Cheers, Healthcare
# 
#     saúde
# 
#     здоровье
#     (zdorov'ye)
# 
#     Translations of saúde
#     [ Português Brasileiro -> Русский ]
# 
#     saúde
#         здоровье
#     ```
# 

# ### 2.4 Traduzir frases inteiras [3]
# 
# 1. Para traduzir uma frase, basta usar a frase entre aspas, como você pode ver abaixo. O exemplo a seguir será traduzido do inglês para o português brasileiro:
# 
#     ```
#     trans :pt-BR "What is going on your life"
#     What is going on your life
# 
#     O que está acontecendo em sua vida
# 
#     Translations of What is going on your life
#     [ English -> Português Brasileiro ]
# 
#     What is going on your life
#         O que está acontecendo em sua vida, O que está acontecendo na sua vida
#     ```
# 

# ### 2.5 Traduzir no modo dicionário [3]
# 
# 1. Modo dicionário. Para usar esta ferramenta como dicionário, basta **adicionar a opção `-d`** ao comando:
# 
#     ```
#     trans -d :pt-BR Thanks
#     Thanks
# 
#     (♂) Obrigado
#     (♀) Obrigada
# 
#     Definitions of Thanks
#     [ English -> Português Brasileiro ]
# 
#     noun
#         an expression of gratitude.
#             - "festivals were held to give thanks for the harvest"
#         Synonyms: gratitude, gratefulness, appreciation, acknowledgment, recognition, credit, hat tip
# 
#     Synonyms
#         noun
#             - gratitude, gratefulness, appreciation, acknowledgment, recognition, credit, hat tip
# 
#         verb
#             - express (one's) gratitude to, express one's thanks to, offer/extend thanks to, say thank you to, show appreciation to
#             - blame, hold responsible
# 
#     See also
#         thank
#     ```
# 

# ### 2.6 Traduzir um arquivo [3]
# 
# #### 2.6.1 Primeiro método
# 
# 1. Para traduzir um arquivo precisaremos indicar o caminho do arquivo a ser traduzido. Use o seguinte formato no terminal (`Ctrl + Alt + T`):
# 
#     ```
#     trans -t pt-BR < /home/edendenis/Documents/Downloads/linux_unix/ubuntu/translate_shell/text.txt
# 
#     To translate a file we will need to indicate the path of the file to be translated. Use the following format in the terminal (Ctrl + Alt + T):
# 
#     Para traduzir um arquivo precisaremos indicar o caminho do arquivo a ser traduzido. Use o seguinte formato no terminal (Ctrl + Alt + T):
# 
#     Translations of To translate a file we will need to indicate the path of the file to be translated. Use the following format in the terminal (Ctrl + Alt + T):
#     [ English -> Português Brasileiro ]
# 
#     To translate a file we will need to indicate the path of the file to be translated.
#         Para traduzir um arquivo precisaremos indicar o caminho do arquivo a ser traduzido., Para traduzir um arquivo será necessário indicar o caminho do arquivo a ser traduzido.
#     Use the following format in the terminal (Ctrl + Alt + T):
#         Use o seguinte formato no terminal (Ctrl + Alt + T):, Utilize o seguinte formato no terminal (Ctrl+Alt+T):
#     ```
# 
# #### 2.6.2 Segundo método
# 
# 1. Para traduzir um arquivo de legendas (`legendas.srt`) do inglês para o português e salvar o resultado em um novo arquivo sem substituir o arquivo original. Você pode fazer isso especificando um novo nome de arquivo de saída. Aqui está como você pode modificar o código:
# 
#     ```
#     # Define o caminho do arquivo de entrada
#     input_file="/home/edendenis/Documents/Downloads/linux_unix/ubuntu/translate_shell/text.txt"
# 
#     # Define o nome do arquivo de saída (novo arquivo)
#     output_file="/home/edendenis/Documents/Downloads/linux_unix/ubuntu/translate_shell/translated_text.txt"
# 
#     # Executa a tradução e salva o resultado no novo arquivo
#     trans :en -t pt-BR -i "$input_file" -o "$output_file"
#     ```
# 
#     Certifique-se de substituir `/home/edendenis/Documents/Downloads/linux_unix/ubuntu/translate_shell.txt` pelo caminho e nome de arquivo desejados para o novo arquivo de legendas traduzidas. Isso garantirá que o arquivo original (`text.srt`) não seja substituído e que a tradução seja salva em um novo arquivo com o nome especificado.

# ### 2.7 Use o modo interativo [1][3]
# 
# O método iterativo do `shell`, no contexto do `Translate Shell`, refere-se ao uso do `shell` interativo do `Translate Shell` para traduzir palavras ou frases diretamente na linha de comando. Em vez de usar um único comando para tradução, você inicia o `shell` interativo com o comando `trans -shell` e, em seguida, pode inserir várias palavras ou frases para tradução sem a necessidade de iniciar um novo comando para cada uma delas.
# 
# ### 2.7.1 Aqui está como funciona
# 
# Após iniciar o `shell` interativo, ele aguarda sua entrada.
# 
# Você pode digitar palavras ou frases que deseja traduzir e pressionar Enter. O `shell` interativo traduzirá a entrada e exibirá as traduções.
# 
# Você pode continuar inserindo palavras ou frases adicionais sem a necessidade de reiniciar o comando. O `shell` interativo permanecerá aberto até você decidir sair, geralmente pressionando `:q`.
# 
# Isso é útil quando você precisa traduzir várias palavras ou frases em sequência, economizando tempo e tornando o processo mais interativo. No exemplo que você forneceu, a palavra `"thanks"` foi traduzida para `"obrigado"` no contexto do `shell` interativo do `Translate Shell`.
# 
# 1. Para abrir o `shell` interativo do Translate, teremos que nos certificar de que especificamos o idioma de origem e o idioma de destino antes de iniciar um shell interativo . Neste exemplo, vou traduzir a palavra obrigado do inglês para o português brasileiro:
# 
#     ``` 
#     trans -shell en:pt-BR thanks
#     Translate Shell
#     (:q to quit)
#     thanks
#     /THaNGks/
# 
#     (♂) obrigado
#     (♀) obrigada
# 
#     Definitions of thanks
#     [ English -> Português Brasileiro ]
# 
#     interjection
#         Obrigado!
#             Thank you!, Thanks!, Ta!
# 
#     thanks
#         obrigado, graças
#     ```
# 
# - Você inicia o `shell` interativo com o comando `trans -shell`, seguido das configurações de idioma de origem e destino, por exemplo, `en:pt-BR` para traduzir do inglês para o português brasileiro.
# 
# - Após iniciar o `shell` interativo, ele aguarda sua entrada.
# 
# - Você pode digitar palavras ou frases que deseja traduzir e pressionar `Enter`. O `shell` interativo traduzirá a entrada e exibirá as traduções.
# 
# - Você pode continuar inserindo palavras ou frases adicionais sem a necessidade de reiniciar o comando. O `shell` interativo permanecerá aberto até você decidir sair, geralmente pressionando `:q`.
# 
# Isso é útil quando você precisa traduzir várias palavras ou frases em sequência, economizando tempo e tornando o processo mais interativo. No exemplo que você forneceu, a palavra "thanks" foi traduzida para "obrigado" no contexto do `shell` interativo do `Translate Shell`.

# ### 2.8 Ajuda [3]
# 
# Para saber mais opções podemos usar o help `man` com o comando: `man trans``
# 

# ### 2.8 Obtenha os códigos dos idiomas disponíveis
# 
# 1. Para descobrir os códigos de idioma que podemos usar, basta executar o seguinte comando: `trans -T`

# ### 2.9 Habilitar modo conciso
# 
# #### 2.9.1 Mode conciso
# 
# Para exibir o resultado conciso no `translate-shell`, você pode usar a opção `-brief` ou `-b`. Isso reduzirá a saída a uma única linha concisa, mostrando a tradução principal sem muitos detalhes adicionais.
# 
# 1. Aqui está um exemplo: `trans -brief en:pt-BR "Hello, how are you?"`
# 
#     Isso exibirá a tradução concisa da frase `"Hello, how are you?"` para o português brasileiro em uma única linha.
# 
#     Observe que a saída concisa geralmente é mais curta e direta, fornecendo a tradução principal sem informações adicionais, tornando-a útil quando você deseja uma resposta rápida e simples.
# 
# #### 2.9.2 Exibir apenas um dos resultados
# 
# É possível fazer com que o translate-shell exiba apenas um dos resultados da tradução. Você pode usar a opção `-brief` ou `-b` seguida pelo número do resultado que você deseja exibir. Aqui está como fazer isso: `trans -brief=2 en:pt-BR "Hello, how are you?"`
#         
# Neste exemplo, o `-brief=1` indica que você deseja exibir apenas o primeiro resultado da tradução. Você pode substituir `1` pelo número do resultado que deseja exibir.
# 
# Lembre-se de que os resultados da tradução são numerados a partir de `1`. Portanto, se você quiser exibir o segundo resultado, use `-brief=2`, e assim por diante.
# 
# Isso permitirá que você escolha qual resultado da tradução deseja exibir quando houver várias traduções possíveis.    

# ### 2.9 Consultar os mecanismos de tradução
# 
# 1. Para consultar os mecanismos de tradução disponíveis no `translate-shell`, você pode usar o seguinte comando: `trans -list-engines`
# 
#     Este comando lista os mecanismos de tradução suportados pelo `translate-shell` e exibe informações sobre cada um deles, incluindo seus nomes e descrições.
# 
#     Ao executar esse comando, você verá uma lista de mecanismos de tradução disponíveis, o que permitirá que você escolha qual mecanismo deseja usar ao realizar traduções com o `translate-shell`. Lembre-se de que os mecanismos podem variar em termos de qualidade e limitações, portanto, escolha o mais adequado para suas necessidades:
# 
#     ```
#     trans -list-engines
# 
#     aspell
#     * google
#     bing
#     spell
#     hunspell
#     apertium
#     yandex
#     ```
#     
# ### 2.9.1 Alterar o mecanismo de tradução
# 
# Para alterar o mecanismo de tradução padrão do Google para outro mecanismo, como o Bing ou Youdaozhiyun, você pode usar a opção -e seguida do nome do mecanismo desejado. Aqui estão alguns exemplos:
# 
# 1. Alterar para o mecanismo Bing Translator: `trans -e bing "Hello, how are you?"`
# 
# Certifique-se de ter os mecanismos de tradução desejados instalados e configurados corretamente no seu sistema antes de usá-los com o `translate-shell`. Você pode verificar a documentação do `translate-shell` ou a ajuda do comando `trans` para obter mais informações sobre os mecanismos de tradução disponíveis e como configurá-los.
# 
# 

# ### 2.10 Reconhecer o idioma automaticamente
# 
# Para traduzir um texto, por exemplo, a partir do alfabeto cirílico, pois mesmo indicando o idioma como `ru` nem sempre o texto é traduzido, pode ser usando o comando `auto` conforme abaixo:
# 
# 1. Experimente usar a opção `auto` para especificar que o texto de entrada é do idioma detectado automaticamente. Aqui está o comando atualizado: `trans -brief auto:pt "Москва"`
# 
# Isso deve corrigir o problema e fornecer a tradução correta para o texto `"Москва"`.

# ## 3. Remover quebras
# 
# ### 3.1 Uma quebra de linha [1]
# 
# O `translate-shell` não possui uma opção integrada para ignorar possíveis quebras de linha (`Enter`'s) ao traduzir texto. No entanto, você pode pré-processar o texto para remover as quebras de linha antes de enviá-lo para tradução.
# 
# Você pode usar ferramentas de linha de comando como o `tr` para substituir as quebras de linha por espaços em branco ou remover completamente. Por exemplo, você pode fazer o seguinte:
# 
# 1. **Defina o texto com quebras de linha:**
# 
#     ```
#     texto_com_quebras="Este é um exemplo de
#     um texto com quebras
#     de linha."
#     ```
# 
# 2. **Remover completamente as quebras de linha:** `texto_sem_quebras=$(echo "$texto_com_quebras" | tr -d '\n')`
# 
#     - **`texto_com_quebras`:** Esta é uma variável que contém o texto original com quebras de linha.
# 
#     - **`echo "$texto_com_quebras"`:** O comando echo é usado para exibir o conteúdo da variável `texto_com_quebras`.
#     
#     - **`|`:** É o operador de tubulação (pipe) que redireciona a saída do comando `echo` para a entrada do próximo comando.
# 
#     - **`tr -d '\n'`:** Este é o comando `tr`, que é usado para traduzir ou excluir caracteres. `-d` é a opção para deletar, e `'\n'` é a sequência de caracteres de nova linha. 
#     
#     Portanto, `tr -d '\n'` remove todas as quebras de linha do texto.
# `
#     - **texto_sem_quebras`**: Esta é a variável que armazena o texto original sem quebras de linha, após a execução do comando.
# 
# 3. **Usar o `translate-shell` para traduzir o texto sem quebras de linha:** `trans -brief en:pt-BR "$texto_sem_quebras"`

# ### 3.2 Multíplas quebras de linha
# 
# Você pode usar uma abordagem semelhante à anterior, mas com uma ferramenta de linha de comando diferente, como o `sed`. Aqui está como você pode fazer isso:
# 
# Suponha que você tem o seguinte texto com múltiplas quebras de linha entre os parágrafos:
# 
# 1. **Defina o texto com multíplas quebras de linha:**
# 
#     ```
#     texto_com_quebras="Este é o primeiro parágrafo.
# 
#     Este é o segundo parágrafo.
# 
# 
#     Este é o terceiro parágrafo."
#     ```
# 
# 2. **Remover completamente as múltiplas quebras de linha emanter apenas uma:** `texto_sem_quebras=$(echo "$texto_com_quebras" | sed '/^$/N;/^\n$/D')`
# 
#     Agora, `$texto_sem_quebras` conterá o texto com apenas uma quebra de linha entre os parágrafos. Em seguida, você pode usar o `translate-shell` para traduzir o texto sem quebras de linha:
# 
# 3. **Usar o `translate-shell` para traduzir o texto sem quebras de linha:** `trans -brief en:pt-BR "$texto_sem_quebras"`
# 

# ### 3.3 Uma quebra de linha e multíplas quebras de linha
# 
# #### 3.3.1 Uma quebra de linha
# 
# Você deseja remover tanto as quebras de linha individuais quanto as múltiplas quebras de linha entre os parágrafos. Você pode fazer isso em etapas separadas, primeiro removendo as quebras de linha individuais e depois removendo as múltiplas quebras de linha. Aqui está como você pode fazer isso:
# 
# 1. **Remover quebras de linha individuais:** Defina o texto com quebras de linha:
# 
#     ```
#     texto_com_quebras="Este é um exemplo de
#     um texto com quebras
#     de linha."
#     ```
# 
# 2. **Remova as quebras de linha individuais:** `texto_sem_quebras_individuais=$(echo "$texto_com_quebras" | tr -d '\n')`
# 

# #### 3.3.2 Multíplas quebras de linha
# 
# 1. **Remover múltiplas quebras de linha entre os parágrafos:** Defina o texto com múltiplas quebras de linha entre os parágrafos:
# 
#     ```
#     texto_com_mais_quebras="Este é o primeiro parágrafo.
# 
#     Este é o segundo parágrafo.
# 
# 
#     Este é o terceiro parágrafo."
#     ```
# 
# 2. **Remova múltiplas quebras de linha entre os parágrafos:** `texto_sem_mais_quebras=$(echo "$texto_com_mais_quebras" | sed '/^$/N;/^\n$/D')`
# 
# 3. **Usar o `translate-shell` para traduzir o texto sem quebras de linha:** `trans -brief en:pt-BR "$texto_sem_mais_quebras"`
# 
# Agora, você tem duas variáveis: `texto_sem_quebras_individuais` e `texto_sem_mais_quebras`, cada uma contendo o texto processado sem as quebras de linha desejadas. Você pode usar essas variáveis separadamente para tradução ou combiná-las de acordo com suas necessidades.

# #### 3.3.3 Remover quebras de linha e manter espaços entre parágrafos
# 
# 1. **Defina o texto com quebras de linha e múltiplas quebras de linha:** 
# 
#     ```bash
#     texto_com_quebras="Este é o primeiro parágrafo.
# 
#     Este é o segundo parágrafo.
# 
# 
#     Este é o terceiro parágrafo."
#     ```
# 
# 2. **Remover quebras de linha e manter espaços entre os parágrafos:** Você pode usar o seguinte comando para substituir as quebras de linha por espaços e remover múltiplos espaços resultantes:
# 
#     ```bash
#     texto_sem_mais_quebras=$(echo "$texto_com_quebras" | sed ':a;N;$!ba;s/\n/ /g;s/ \{2,\}/ /g;s/ \n/\n/g')
#     ```
# 
#    - **`sed ':a;N;$!ba;s/\n/ /g`**: Este comando une todas as linhas em uma única linha, substituindo quebras de linha (`\n`) por espaços.
# 
#    - **`s/ \{2,\}/ /g`**: Remove múltiplos espaços consecutivos, deixando apenas um espaço.
#    
#    - **`s/ \n/\n/g`**: Restaura a quebra de linha entre parágrafos ao final do texto.
# 
# 3. **Usar o `translate-shell` para traduzir o texto processado:** Após remover as quebras de linha indesejadas e ajustar os espaços, você pode traduzir o texto usando o comando abaixo:
# 
#     ```bash
#     trans -brief en:pt-BR "$texto_sem_mais_quebras"
#     ```
# 
# Agora você tem uma nova variável `texto_sem_mais_quebras`, que contém o texto processado sem quebras de linha internas e com a formatação desejada. Essa variável pode ser usada para tradução ou outras manipulações conforme necessário.
# 

# ### 

# ## 4. Traduzir a partir de um arquivo
# 
# ### 4.1 Traduzir e salvar um arquivo `.txt`
# 
# 1. **Defina o nome do arquivo de entrada**: `nome_arquivo_entrada="input.txt"`
# 
# 2. **Defina o nome do arquivo de saída**: `nome_arquivo_saida="output_$nome_arquivo_entrada"`
# 
# 3. **Defina o idioma de origem**: Código de idioma de origem, por exemplo, `en` para inglês: `idioma_origem="en"`
# 
# 4. **Defina o idioma de destino**: Código de idioma de destino, por exemplo, `pt-BR` para português brasileiro: `idioma_destino="pt-BR"`
# 
# 5. **Para traduzir o conteúdo de um arquivo `.txt` e salvá-lo em um novo arquivo `.txt`, você pode fazer isso em um sistema `Unix/Linux`:** `cat "$nome_arquivo_entrada" | trans -brief "$idioma_origem":"$idioma_destino" -no-ansi > "output_$nome_arquivo_saida_$idioma_destino"`
# 
#     Este comando irá ler o conteúdo do arquivo `input.txt`, traduzir o texto do inglês para o português brasileiro usando o `trans`, e salvar a tradução no arquivo `output.txt`.
# 
# 6. **# Exibir uma mensagem indicando que a tradução foi concluída**: `echo "A tradução do arquivo $nome_arquivo_entrada para $idioma_destino foi concluída e salva em output_$nome_arquivo_saida."`
# 
# 7. **(Opcional) Retornar o arquivo original para o texto inicial**: Se desejar substituir o texto traduzido de volta no arquivo original `.txt`, você pode usar comandos de edição de texto, como o `sed`. Por exemplo, se quiser adicionar o texto traduzido em uma nova linha após cada linha no arquivo original, você pode usar o seguinte comando: `cat output.txt > input.txt`
# 
#     Este comando irá substituir o conteúdo do arquivo `input.txt` pelo texto traduzido contido no arquivo `output.txt`.
# 
# Lembre-se de sempre fazer backup do arquivo original antes de realizar qualquer manipulação.
# 

# ### 4.1.1 Traduzir e sobreescrever o mesmo arquivo de origem `.txt`
# 
# Para sobrescrever o mesmo arquivo de entrada com o resultado da tradução, você pode redirecionar a saída do comando para o arquivo original. Aqui está um exemplo:
# 
# 1. **Defina o nome do arquivo de entrada**: `nome_arquivo_entrada="input.txt"`
# 
# 2. **Defina o nome do arquivo de saída**: `nome_arquivo_saida="output_$nome_arquivo_entrada"`
# 
# 3. **Defina o idioma de origem**: Código de idioma de origem, por exemplo, `en` para inglês: `idioma_origem="en"`
# 
# 4. **Defina o idioma de destino**: Código de idioma de destino, por exemplo, `pt-BR` para português brasileiro: `idioma_destino="pt-BR"`
# 
# 5. Suponha que você tenha um arquivo chamado `input.txt` que deseja traduzir e sobrescrever com a tradução: `trans -brief "$idioma_origem":"$idioma_destino" -no-ansi < "$nome_arquivo_entrada" > "output_$nome_arquivo_saida_$idioma_destino"`
# 
#     Neste comando, a tradução é realizada a partir do conteúdo de `input.txt` e o resultado é redirecionado para `output.txt`. Como a saída está sendo redirecionada para um novo arquivo, o arquivo original `input.txt` não é afetado.
# 
# 6. Se você deseja sobrescrever diretamente o arquivo original `input.txt` com a tradução, você pode usar o seguinte comando: `trans -brief "$idioma_origem":"$idioma_destino" -no-ansi < "$nome_arquivo_entrada" > temp.txt && mv temp.txt "$nome_arquivo_entrada"`
# 
#     Neste comando:
# 
#     - **`trans -brief "$idioma_origem":"$idioma_destino" -no-ansi`**: realiza a tradução do conteúdo do arquivo de entrada.
# 
#     - **`< "$nome_arquivo_entrada"`**: redireciona o conteúdo do arquivo de entrada para o comando de tradução.
#     
#     - **`> temp.txt`**: redireciona a saída da tradução para um novo arquivo temporário chamado temp.txt.
#     
#     - **`&& mv temp.txt "$nome_arquivo_entrada"`** renomeia o arquivo temporário para substituir o arquivo original de entrada, sobrescrevendo-o com a tradução.
# 
#     Este comando primeiro traduz o conteúdo de `input.txt` e redireciona a saída para um novo arquivo temporário chamado `temp.txt`. Em seguida, ele renomeia o arquivo temporário para substituir o arquivo original `input.txt`, sobrescrevendo-o com a tradução.
# 
# 7. **(Opcional) Remover o arquivo de backup gerado usando o comando:** `rm temp.txt`
# 
#     Removemos o arquivo de backup gerado para manter apenas o arquivo original com as traduções.
# 
# Certifique-se de fazer backup dos arquivos originais antes de realizar alterações, especialmente quando estiver sobrescrevendo-os com novos conteúdos.
# 

# ### 4.1.2 Reconhecer o idioma automaticamente a partir de um arquivo `.txt`
# 
# Para traduzir um texto, por exemplo, a partir do alfabeto cirílico, pois mesmo indicando o idioma como `ru` nem sempre o texto é traduzido, pode ser usando o comando `auto` conforme abaixo:
# 
# 1. **Defina o nome do arquivo de entrada**: `nome_arquivo_entrada="input.txt"`
# 
# 2. **Defina o nome do arquivo de saída**: `nome_arquivo_saida="output"`
# 
# 3. **Defina o idioma de origem**: Código de idioma de origem, por exemplo, `en` para inglês: `idioma_origem="auto"`
# 
# 4. **Defina o idioma de destino**: Código de idioma de destino, por exemplo, `pt-BR` para português brasileiro: `idioma_destino="pt-BR"`
# 
# 5. Para traduzir automaticamente o texto de entrada para o português brasileiro e depois salvar a saída em um arquivo de texto, você pode usar o seguinte comando: `cat "$nome_arquivo_entrada" | trans -brief "$idioma_origem":"$idioma_destino" -no-ansi > "$nome_arquivo_saida"`
# 
#     Isso irá traduzir o texto do idioma detectado automaticamente para o português brasileiro e salvará a tradução no arquivo de saída especificado (`output.txt`).
# 

# ### 4.1.3 Remover as quebras de linhas, traduzir e salvar em um arquivo `.txt`
# 
# Para remover as quebras de linhas, traduzir e salvar em um arquivo `.txt`, você deve seguir os passos abaixo:
# 
# 1. **Defina o nome do arquivo de entrada**: `nome_arquivo_entrada="input.txt"`
# 
# 2. **Defina o idioma de origem**: Código de idioma de origem, por exemplo, `en` para inglês: `idioma_origem="en"`
# 
# 3. **Defina o idioma de destino**: Código de idioma de destino, por exemplo, `pt-BR` para português brasileiro: `idioma_destino="pt-BR"`
# 
# 4. **Defina o nome do arquivo de saída**: `nome_arquivo_saida="output_$nome_arquivo_entrada"`
# 
# 5. É possível combinar esses dois comandos para remover as quebras de linhas dos parágrafos e depois traduzir o texto. Você pode usar pipes para encadear os comandos, como mostrado abaixo: `awk '{printf "%s", (NF ? (NR>1 ? (/^[[:upper:]]/ ? "\n" : " ") : "") : "\n") $0} END {print ""}' "$nome_arquivo_entrada" | trans -brief "$idioma_origem":"$idioma_destino" -no-ansi > "$nome_arquivo_saida"`
#     
#     Isso irá ler o conteúdo do arquivo `input.txt`, remover as quebras de linha dos parágrafos usando o comando `tr -d '\n'`, e em seguida traduzir o texto para o português brasileiro usando o comando trans com a opção `-brief`, e salvar o resultado no arquivo `output.txt`.
# 

# ## Referências
# 
# [1] OPENAI. ***Instalar translate-shell no ubuntu.*** Disponível em: <https://chat.openai.com/c/e2c5af6e-e05f-44e5-aea7-4836717cc18b> (texto adaptado). ChatGPT. Acessado em: 11/12/2023 08:51.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 11/12/2023 08:51.
# 
# [3] A., DAMIEN. ***Translate-shell, translate to any language from the command line.*** Disponível em: <https://ubunlog.com/en/translate-shell-traduce-terminal/>. Ubunlog. Acessado em: 30/01/2024 22:44.
