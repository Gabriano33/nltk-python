# Linguistic Corpus Analysis with NLTK

## 🎯 Obiettivo

Realizzazione di due programmi scritti in Python (o tramite Jupyter/Colab Notebook) che utilizzano i moduli di **NLTK** per analizzare linguisticamente due **corpora di testo in lingua inglese**, confrontarli sulla base di alcuni indici statistici ed estrarre informazioni rilevanti.

---

## 📚 Creazione dei Corpora

Ogni corpus deve rispettare le seguenti caratteristiche:

- Essere in **lingua inglese**
- Contenere **almeno 5000 parole**
- Rappresentare un **genere testuale specifico**  
  *(es. giornalismo, narrativa, blog, social media, articoli scientifici, ecc.)*
- Essere salvato in un **file di testo semplice** (`.txt`) con codifica **UTF-8**

---

## 🛠️ Programmi da Sviluppare

Ogni programma deve:

- Leggere i file dei due corpora
- Effettuare **annotazione linguistica** (almeno fino al *Part-of-Speech Tagging*)

### 📥 Modalità di Input

- Se sviluppato in **Python** (`.py`): i file devono essere passati da **riga di comando**
- Se sviluppato come **Notebook** (Jupyter/Colab): è accettabile specificare il/i file nel codice, utilizzando un **percorso relativo**

---

## 📊 Programma 1 – Analisi e Confronto

Il programma deve eseguire le seguenti operazioni:

- Sentence splitting  
- Tokenizzazione  
- POS tagging  
- Lemmatizzazione  

### ⚖️ Confronto tra i due corpora rispetto a:

1. **Numero totale di frasi e token**
2. **Lunghezza media delle frasi** (in token)
3. **Lunghezza media dei token**, escludendo la punteggiatura (in caratteri)
4. **Numero di hapax** (parole che compaiono una sola volta):
   - Nei primi 500 token  
   - Nei primi 1000 token  
   - Nei primi 3000 token  
   - Nell’intero corpus
5. **Dimensione del vocabolario** e **ricchezza lessicale** (Type-Token Ratio, *TTR*) calcolata su porzioni incrementali di 200 token:  
   *200, 400, 600, ..., fino all’intero testo*
6. **Numero di lemmi distinti** (*dimensione del vocabolario lemmatizzato*)
7. **Distribuzione delle frasi per polarità**:
   - Utilizzando un **classificatore di polarità** fornito a lezione  
   - Oppure un **classificatore personalizzato**

---

## 🧠 Programma 2 – Estrazione Statistiche e Pattern Linguistici

Il secondo programma prende in input **un singolo corpus** e, dopo aver effettuato le operazioni di annotazione linguistica (sentence splitting, tokenizzazione, POS tagging), deve **estrarre le seguenti informazioni**:

### 1. 📌 Frequenze lessicali
- I **top-50 sostantivi**, **avverbi** e **aggettivi** più frequenti  
  > Visualizzare frequenza assoluta e relativa, ordinate per frequenza decrescente

### 2. 🔢 N-grammi più frequenti
- I **top-20 n-grammi di token** (con frequenza relativa) per:  
  - **n = 1, 2, 3, 4, 5**

### 3. ✍️ N-grammi di PoS più frequenti
- I **top-20 n-grammi di Part-of-Speech (PoS)** per:  
  - **n = 1, 2, 3**  
  > Anche qui con frequenza relativa e ordinati per frequenza decrescente

### 4. 🔗 Bigranmi Aggettivo–Sostantivo
I **top-10 bigrammi composti da aggettivo + sostantivo**, ordinati secondo:

a. Frequenza decrescente  
b. **Massima probabilità condizionata**, con valore associato  
c. **Massima probabilità congiunta**, con valore associato  
d. **Mutual Information (MI)** massima, con valore associato  
e. **Local Mutual Information (LMI)** massima, con valore associato  
f. Calcolo e stampa del **numero di elementi comuni** tra i top-10 per MI e LMI

### 5. 🧩 Analisi di Frasi Selezionate

Analizzare **le frasi comprese tra 10 e 20 token**, in cui almeno la **metà dei token (parte intera)** ricorre **almeno 2 volte nel corpus**. Per tali frasi identificare:

- a. La frase con la **media più alta** della distribuzione di frequenza dei token  
- b. La frase con la **media più bassa**  
- c. La frase con la **probabilità più alta secondo un modello di Markov** di **ordine 2**

> 📌 La media della distribuzione di frequenza dei token si ottiene sommando le frequenze dei token nella frase e dividendo per il numero di token.

### 6. 🏷️ Named Entity Recognition (NER)
- Estrazione delle **Entità Nominate (Named Entities)** del corpus
- Per ogni **classe di entità**, individuare i **15 elementi più frequenti**, ordinati per frequenza decrescente (con frequenza relativa)

---

## 📦 Requisiti per la Consegna

Perché il progetto sia considerato **idoneo**, devono essere consegnati i seguenti materiali **in una cartella compressa**:

1. I **due corpora**, come file `.txt` in UTF-8  
2. I **due programmi o notebook**, **ben commentati**

### 🖥️ Se il codice è sviluppato in `.py` (Python script)

- Salvare i **risultati dell’esecuzione** in un **file di testo formattato**
- Totale: **3 file di output**  
  - 1 per il **primo programma**  
  - 2 per il **secondo programma** (uno per ciascun corpus)

### 📓 Se il codice è sviluppato in Jupyter/Colab Notebook

- Consegnare i notebook **già eseguiti** (`.ipynb`)
- Totale: **3 notebook**  
  - 1 per il **primo programma**  
  - 2 copie del notebook del **secondo programma**: una per ogni corpus

⚠️ **Il codice deve essere eseguibile**, con attenzione ai *path* utilizzati (preferibilmente relativi), e deve replicare i risultati consegnati.

---
