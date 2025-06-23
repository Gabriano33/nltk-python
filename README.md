Obie%vo
Realizzazione di due programmi scri. in Python o su Notebook (Jupyter, Colab, ...) che u>lizzino i
moduli di NLTK per analizzare linguis>camente due corpora di testo inglese, confrontarli sulla base
di alcuni indici sta>s>ci, ed estrarre da essi informazioni.
Creazione dei corpora
I due corpora devono essere crea> rispondendo alle seguen> caraGeris>che:
1. Devono essere in lingua inglese
2. Devono contenere almeno 5000 parole
3. Ciascuno deve essere rappresenta>vo di uno specifico genere testuale (ad es. Testo
giornalis>co, prosa leGeraria, blog, social media, ar>coli scien>fici, ecc.)
4. Devono essere salva> in un file ciascuno di testo semplice con codifica UTF-8
Programmi da sviluppare
Ciascuno dei due programmi deve anzituGo leggere i file e analizzarne il contenuto
linguis>camente almeno fino al Part-of-Speech Tagging.
Se si sceglie di sviluppare il codice come un file Python, il programma deve prendere in input da riga
di comando i file da analizzare.
Se si sceglie di sviluppare il codice come Notebook, è acceGabile che il/i file sia/siano specifica>
all’interno del codice u>lizzando un path rela)vo.
Programma 1
Il codice sviluppato deve prendere in input i due corpora, effeGuare le operazioni di annotazione
linguis>ca richieste (sentence spli.ng, tokenizzazione, PoS tagging, lemma>zzazione), e produrre
un confronto dei corpora rispeGo a:
1. Numero di frasi e token;
2. Lunghezza media delle frasi in token e lunghezza media dei token, a eccezione della
punteggiatura, in caraGeri;
3. Numero di Hapax tra i primi 500, 1000, 3000 token, e nell’intero corpus;
4. Dimensione del vocabolario e ricchezza lessicale (Type-Token Ra>o, TTR), calcolata per
porzioni incrementali di 200 token fino ad arrivare a tuGo il testo
• i.e., i primi 200, i primi 400, i primi 600, ..., per tu. i token;
5. Numero di lemmi disGnG (i.e., la dimensione del vocabolario dei lemmi).
6. Distribuzione di frasi con polarità posi>va e nega>va
• Per classificare le frasi in POS e NEG è possibile u>lizzare il classificatore di polarità
visto a lezione (Notebook) o un classificatore costruito ad hoc.
