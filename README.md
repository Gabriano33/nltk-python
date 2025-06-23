Linguistic Corpus Analysis with NLTK
Obiettivo
Realizzazione di due programmi scritti in Python (o tramite Jupyter/Colab Notebook) che utilizzano i moduli di NLTK per analizzare linguisticamente due corpora di testo in lingua inglese, confrontarli sulla base di alcuni indici statistici ed estrarre informazioni rilevanti.

Creazione dei Corpora
Ogni corpus deve rispettare le seguenti caratteristiche:

Essere in lingua inglese

Contenere almeno 5000 parole

Rappresentare un genere testuale specifico (es. giornalismo, narrativa, blog, social media, articoli scientifici, ecc.)

Essere salvato in un file di testo semplice (.txt) codificato in UTF-8

Programmi da Sviluppare
Ogni programma deve:

Leggere i file dei due corpora

Effettuare l'annotazione linguistica (almeno fino al POS tagging)

Modalità di Input
Se sviluppato in Python (file .py): i file devono essere passati tramite riga di comando

Se sviluppato come Jupyter/Colab Notebook: è accettabile specificare il/i file nel codice, utilizzando un percorso relativo


Programma 1 – Analisi e Confronto
Il programma deve eseguire le seguenti operazioni:

Sentence splitting, tokenizzazione, POS tagging, lemmatizzazione

Calcolo e confronto tra i due corpora rispetto a:

Numero totale di frasi e token

Lunghezza media delle frasi (in token)

Lunghezza media dei token (escludendo la punteggiatura), in caratteri

Numero di hapax (parole che compaiono una sola volta) tra:

i primi 500 token

i primi 1000 token

i primi 3000 token

l'intero corpus

Dimensione del vocabolario e ricchezza lessicale (Type-Token Ratio, TTR) calcolata su porzioni incrementali di 200 token (i primi 200, 400, 600, ..., fino all’intero testo)

Numero di lemmi distinti (dimensione del vocabolario lemmatizzato)

Distribuzione delle frasi per polarità (positiva/negativa), utilizzando:

il classificatore di polarità fornito durante le lezioni

oppure un classificatore personalizzato
