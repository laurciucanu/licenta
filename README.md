# Managementul laboratoarelor la facultate

    Introducere

De-a lungul anilor petrecuți la facultate, profesorii aveau posibilitatea de a posta
tematica laboratoarelor doar pe site-ul lor personal sau prin e-mail. Consider că această
problemă se poate rezolva prin crearea unui site dedicat pentru postarea laboratoarelor și
asignarea acestor studenților.
În cadrul acestui site profesorul se poate loga și înregistra un nou laborator. Ulterior
această temă poate fi adaugată unor grupe sau unor studenți. O altă caracteristică este
adăugarea de note la anumite laboratoare și crearea de documente care arată progresul
fiecărui student pe parcursul unui anumit laborator.
Profesorul poate deasemenea adăuga o formulă personalizată de calculare a notei
finale la laborator. Aceasta are posibilitatea de a cuantifica fiecare notă și la sfârșit să
calculeze nota finală obținută.
Totodată profesorul poate adăuga studenții prezenți la laborator. Această prezență
putând fi folosită ulterior la calculul notei.
Managementul laboratoarelor va fi mult mai simplu din punct de vedere al timpului.
Profesorul va trebui doar să atașeze un document sau să introducă direct tematică pentru
laborator. Studenții vor avea posibilitatea de a vedea acest document și ulterior în funcție
de un deadline să adauge un fișier cu rezolvarea laboratorului.
Aceast site este scris folosind Python pe partea de backend și HTML, CSS, Javascript
pe partea de frontend. Pentru construirea lui este necesară o baza de date. Am ales
PostgreSQL. Totodată este utilizat microframework-ul Flask pentru Python.

    Descrierea soluției

Soluția propusă de mine rezolvă probleme de management al laboratoarelor fiind
ușor de folosit atât de profesori cât și de studenți existând posibilitatea de încărcare a
fișierelor(cod sursă, documente, etc.) de către studenți și adăugarea de conținut al
laboratoarelor de către profesori
