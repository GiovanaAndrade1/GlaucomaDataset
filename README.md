vessel_Analysis

Pipeline de análise de segmentação de vasos retinianos para triagem de glaucoma.

Calcula a discrepância de pixels entre as máscaras de artéria e veia e sinaliza os casos que ultrapassam um limiar configurável como possível glaucoma.



Estrutura

Main.py - Roda a pipeline, chama todas as pastas (ponto de entrada)

config/Settings.py - Monta todos os caminhos e qualquer parâmetro de análise - se é possível indicativo de glaucoma ou não - é configurado nessa parte

readers/Readers.py - Abre as pastas - Dataset baixado localmente, código no support_Code- e monta os pares da artéria e veia utilizando o ip presente na frente de cada imagem.

analyzers/vessel_Analysis.py - o Coração principal da primeira parte do projeto, aqui que calcula a discrepância entre os pixels brancos do par artéria/veia.

reporters/Reporters.py - não feito ainda, mas a ideia é armazenar todos os resultados em CSV e/ou TXT.

utils/Utils.py - não feito ainda, mas a ideia é montar o caminho das pastas aqui.


Para Iniciar 

Precisa instalar todas as dependências

pip install pillow numpy pandas

precisa configurar o caminho do dataset dependendo da sua máquina 
Abra o config/Settings e em DATASET_ROOT ajuste de acordo com a sua pasta.

Para executar - python GlaucomaDataset/main.py


Destrinchando as configurações - 
DATASET_ROOT - Caminho das pastas de onde o DATASET está armazenado.

ARTERY_FOLDER_NAME - O nome da subpasta com as imagens da artéria (desconsidere se você baixou o dataset localmente-ja configurado)

VEIN_FOLDER_NAME - O nome da subpasta com as imagens da veia (Desconsidere se você baixou localmente - já configurado)

OUTPUT_DIR  - pasta executada automaticamente quando rodar o código - para armazenar os arquivos CSV e/ou TXT.

GLAUCOMA_DISCREPANCY_THRESHOLD_PCT - Porcentagem de discrepância para sinalizar de possivel glaucoma (ATENÇÃO -Desativado- conversar esse parametro com o Lucas)


Fluxo da pipeline - 


main
|
|
|--utils - quando for feito ele é o responsável por montar os caminhos da veia e artéria a partir do settings.py.
|
|
|-- GlaucomaBenchmarkReader.load_pairs() - no Readers.py
    -- Pareia as imagens da artéria e veia pelo seu nome
|
|
|-- VesselPairAnalyzer.analyze(pairs)
    --agora, depois de montar o pares essa função é responsável, em cada par: 
        --count_pixels() -abrir a imagem, jogar em um      array numpy e contar os pixels ( todos que não são pretos)  e calcular o ratio, abs_diff, disc_pct, predominance, glaucoma_flag
        esperado retornar um Dataframe com 22X8
CSV e txt ainda não feitos - não possui documentação ainda

formula usada para calcular a divisão é a
disc_pct = |vein_pixels - artery_pixels| / max(vein_pixels, artery_pixels) × 100

Na pratica,oque essa fórmula faz? 

1- ela pega a diferença de pixels não-pretos entre artéria e a veia (|vein_pixels - artery_pixels|)

2- pega o maior valor de pixels entre a artéria e veia ( max(vein_pixels, artery_pixels)) - porque? se pegassémos uma imagem só, ou artéria ou a veia, pode ser dividido por um numero muito pequeno em comparação, que aumentaria o resultado de uma forma que não é conveniente para a conta,por isso sempre dividimos pelo maior para ter uma porcentagem entre 0% e 100%

3- Divide a diferença entre a quantidade de pixels da diferença dividido pelo maior numero de pixels

4- multiplica por 100% para oferecer uma porcentagem de desbalanceamento.

5- Armazena no disc_pct que será sinalizado quando a sua porcentagem for > GLAUCOMA_DISCREPANCY_THRESHOLD_PCT


Para adicionar um Script futuro - razão do copo óptico e disco optico, analíse do full-fundus, etc.

se precisar de um novo cálculo, o nome da pasta deve ser imagem_analizada_Analysis (igual o vessel_Analysis)

se precisar abrir mais pastas (oque claramente vamos precisar), renomeie o Readers.py para o nome_da_pasta_Readers.py

caso precisemos de um novo ponto de entrada da pipeline nomeie os mains de acordo com a sua entrada de dados.

        

    "# GlaucomaDataset" 
"# GlaucomaDataset" 
