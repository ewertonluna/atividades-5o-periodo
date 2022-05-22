# Grupo: Carolina Vasconcelos, Ewerton Luna e Mariana Coutinho

## Atividade sobre Docker Containers
### Instruções
1.  Dentro do diretório `demo` faça o build da imagem da aplicação spring boot com `docker build -t spring-boot-app .`
2. Rode a aplicação spring boot com `docker run -p 8080:8080 spring-boot-app`
3. Dentro do diretório `my-angular-app` faça o build da imagem da aplicação angular com `docker build -t nginx-angular-app .`
4. Rode a aplicação nginx/angular com `docker run -p 80:80 nginx-angular-app`.
5. Dentro do diretório `nginx-docker` faça o build da imagem do reverse proxy server com `docker build -t nginx-reverse-proxy .`
6. Rode o servidor com `docker run -p 8000:80 nginx-reverse-proxy`.
