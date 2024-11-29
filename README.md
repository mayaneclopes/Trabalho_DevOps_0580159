Trabalho_DevOps_0580159

Tecnologias utilizadas: 
-> Docker: administração dos containers da aplicação, banco de dados e demais;
-> MariaDB: banco de dados relacional;
-> Prometheus, para coletar e armazenar métricas da aplicação e do banco MariaDB;
-> Grafana: para visualização das métricas e criação de dashboards;
-> Git LFS: gerenciamento de arquivos grandes que não podem ser comitados no github.

Estrutura: 
-> docker-compose.yml: configuração da aplicação, mariaDB, Prometheus e Grafana;
-> prometheus.yml: configuração do Prometheus e seus alvos de monitoramento (webapp e MariaDB);
-> grafana_dashboard.json: configuração dos dashfboards grafana;
-> /app: pasta contendo arquivos de configuração MariaDB;
-> Jenkinsfile: configuração do Jenkins.

Pré-requisitos: 
Para rodar o projeto, será necessário ter instalado:
-> Docker;
-> Docker Compose;
-> Git LFS;
-> Prometheus;
-> Grafana.

Iniciando o projeto: 
1) Clonando o repositório:

git clone https://github.com/mayaneclopes/Trabalho_DevOps_0580159.git
cd Trabalho_DevOps_0580159

2) Configurando docker: 
-> Para iniciar MariaDB, webapp, Prometheus e Grafana, execute na pasta raíz o seguinte comando:

docker-compose up -d 

3) Acessando:
->Grafana:  http://localhost:3000 (usuário: admin, senha: mayane);
->Prometheus: http://localhost:9090;
->Webapp: http://localhost:5000.

Sobre Git LFS:
O projeto usa o Git LFS para armazenamento de arquivos grandes (binários Prometheus e Promtool),
se fazendo PRIMORDIAL tê-lo instalado ao clonar o repositório. Caso não tenha instalado, execute
o comando: 

git lfs install

Desta forma, garantimos que os arquivos grandes serão corretamente baixados.

Obrigada. 
