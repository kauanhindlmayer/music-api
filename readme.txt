#para voces lerem rapaziada

preparando o ambiente

    #para criar a imagem docker basta executar esse comando "docker build -t docker-mysql . "

    #para rodar a imagem docker  em um container utilize o seguinte comando "docker run -p 3306:3306 --name mysql-container -e MYSQL_ROOT_PASSWORD=1234 -d docker-mysql"

    #para criar o banco musicas basta rodar o seguinte comando, "docker exec -it mysql-container mysql -uroot -p1234 " , para acessar o banco de dados

    #depois execute a seguinte query para criar o banco create " CREATE DATABASE musicas ";

rodando o código

    #pra rodar o código python tem que importar o requiremnts.txt, padrão só dar pip install requirements.txt, caso de algum erro por falta de módulo, será necessário realizar o pip install dele separado, caso seja o caso, fique a vontado para atualizar os requirements

    #para rodar o código pode usar o python main.py ou afins

Testando o código

    #coleção postman para testes, basta importar isso no postman, se precisar de ajuda me chama, a coleção é atulizada de forma automática, https://api.postman.com/collections/23428387-411e9ac6-fb5e-4e5c-9ff9-eb5fa4141d40?access_key=PMAT-01H2RQS5P6JKTT1VSX2N6T7CHF

Agora fiquem livres para fazerem outras tabelas e se divirtam 