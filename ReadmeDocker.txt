Aby zbudowac obraz docker: 

docker build -t myimage .

Aby uruchomić kontener z obrazu:

docker run -p 8000:8000 myimage

Aplikacja startowa django będzie znajdować się na http://localhost:8000