# zadanie_stepik_5
# Treść
Wykonaj następujące zadania:

Napisz funkcje, które będą generować skróty dla każdej z trzech funkcji skrótów (MD5, SHA-256, SHA-3, SHA-1, BLAKE2S).
Napisz funkcje, które pozwolą na generowanie łańcuchów znaków o określonej długości i ilości prób, aby móc przeprowadzić pomiary czasu obliczeń dla każdej funkcji skrótów.
Przeprowadź następujący eksperyment:

Wygeneruj 10 000 unikalnych łańcuchów znaków o długości 1-10000 znaków (1,10,100,1000,10000)
Oblicz i zapisz skróty dla każdego z łańcuchów za pomocą każdej funkcji skrótu (MD5, SHA-256, SHA-3, SHA-1, BLAKE2S).
Zmierz czas obliczeń dla każdej funkcji skrótu.
Spróbuj znaleźć kolizje dla każdej funkcji skrótu poprzez sprawdzenie, czy dwa różne łańcuchy mają ten sam skrót.


# OUTPUT
```
String length: 10
MD5 - Time: 0.015625 seconds, Collisions:0
SHA-256 - Time: 0.0 seconds, Collisions:0
SHA3-256 - Time: 0.015625 seconds, Collisions:0
SHA1 - Time: 0.015625 seconds, Collisions:0
BLAKE2S - Time: 0.0 seconds, Collisions:0

String length: 100
MD5 - Time: 0.0 seconds, Collisions:0
SHA-256 - Time: 0.015625 seconds, Collisions:0
SHA3-256 - Time: 0.015625 seconds, Collisions:0
SHA1 - Time: 0.0 seconds, Collisions:0
BLAKE2S - Time: 0.015625 seconds, Collisions:0

String length: 1000
MD5 - Time: 0.015625 seconds, Collisions:0
SHA-256 - Time: 0.03125 seconds, Collisions:0
SHA3-256 - Time: 0.015625 seconds, Collisions:0
SHA1 - Time: 0.015625 seconds, Collisions:0
BLAKE2S - Time: 0.015625 seconds, Collisions:0

String length: 10000
MD5 - Time: 0.09375 seconds, Collisions:0
SHA-256 - Time: 0.15625 seconds, Collisions:0
SHA3-256 - Time: 0.203125 seconds, Collisions:0
SHA1 - Time: 0.078125 seconds, Collisions:0
BLAKE2S - Time: 0.21875 seconds, Collisions:0

String length: 1000000
MD5 - Time: 10.859375 seconds, Collisions:0
SHA-256 - Time: 16.1875 seconds, Collisions:0
SHA3-256 - Time: 20.390625 seconds, Collisions:0
SHA1 - Time: 8.0625 seconds, Collisions:0
BLAKE2S - Time: 20.9375 seconds, Collisions:0
```
