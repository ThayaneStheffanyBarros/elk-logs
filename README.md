# Centralização de Logs com ELK Stack

Projeto desenvolvido para a disciplina de Administração de Sistemas – UFCG.

Este projeto demonstra a centralização de logs utilizando o **ELK Stack** (Elasticsearch, Logstash/Kibana) e **Filebeat**, coletando logs de um servidor Nginx e permitindo sua visualização através do Kibana.

## Integrantes

- Ailton José de Araújo Júnior
- Nome 2
- Nome 3
- Thayane Stheffany Silva Barros

## Professor

Giovanni Farias

---

# Sobre o Projeto

Em ambientes modernos de software, aplicações e serviços geram grandes volumes de logs. Esses logs são essenciais para:

- identificar erros
- monitorar aplicações
- realizar auditorias
- analisar desempenho

Porém, quando os logs ficam espalhados em diferentes servidores, torna-se difícil analisá-los.

Este projeto demonstra uma solução de **centralização de logs**, utilizando o **ELK Stack**, permitindo:

- coleta automática de logs
- armazenamento centralizado
- busca e análise em tempo real
- visualização em dashboards

---

# Arquitetura da Solução

A arquitetura utilizada neste projeto é composta pelos seguintes componentes:

Aplicação (Nginx)  
↓  
Filebeat  
↓  
Elasticsearch  
↓  
Kibana

### Componentes

**Nginx**

Servidor web utilizado para gerar logs de acesso.

**Filebeat**

Responsável por coletar os logs do Nginx e enviá-los para o Elasticsearch.

**Elasticsearch**

Banco de dados utilizado para armazenar e indexar os logs.

**Kibana**

Interface gráfica utilizada para visualizar e pesquisar os logs.

---

# Estrutura do Projeto

```

elk-logs
├ docker-compose.yml
├ filebeat.yml
├ nginx
│  └ Dockerfile
└ README.md

````

---

# Requisitos

Antes de executar o projeto é necessário ter instalado:

- Docker
- Docker Compose

Verifique se estão instalados:

```bash
docker --version
docker compose version
````

---

# Instalação

Clone o repositório:

```bash
git clone https://github.com/ThayaneStheffanyBarros/elk-logs.git
```

Entre na pasta do projeto:

```bash
cd elk-logs
```

---

# Execução do Projeto

Para iniciar todos os serviços execute:

```bash
docker compose up -d
```

Este comando irá iniciar os seguintes containers:

* Elasticsearch
* Kibana
* Nginx
* Filebeat

Verifique se os containers estão rodando:

```bash
docker ps
```

Você deverá ver algo semelhante a:

```
elasticsearch
kibana
nginx
filebeat
```

---

# Acessando os Serviços

Nginx (gerador de logs)

```
http://localhost:8080
```

Kibana

```
http://localhost:5601
```

Elasticsearch API

```
http://localhost:9200
```

---

# Criando o Data View no Kibana

1. Acesse o Kibana:

```
http://localhost:5601
```

2. Vá em:

Stack Management → Data Views

3. Clique em:

Create Data View

4. Configure:

```
Index pattern: filebeat-*
Time field: @timestamp
```

5. Clique em **Create Data View**

---

# Testando o Sistema

## 1 Gerar logs

Acesse o servidor Nginx:

```
http://localhost:8080
```

Atualize a página algumas vezes para gerar requisições.

Cada requisição irá gerar um log.

---

## 2 Verificar se os logs chegaram no Elasticsearch

Execute:

```bash
curl http://localhost:9200/_cat/indices?v
```

Deve aparecer um índice semelhante a:

```
filebeat-8.x.x-2026.03.07
```

---

## 3 Visualizar logs no Kibana

No Kibana:

1. Vá em **Discover**
2. Selecione o Data View `filebeat-*`
3. Os logs coletados aparecerão na tela.

Agora é possível:

* pesquisar logs
* aplicar filtros
* analisar eventos em tempo real

---

# Parando o Ambiente

Para parar os containers execute:

```bash
docker compose down
```
