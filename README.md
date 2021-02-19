# publication-API
API per ricavare le pubblicazioni dall'archivio istituzionale dell' Università degli studi di Udine.

## Come installare l'API?
Per utilizzare l'API si consiglia innanzitutto di creare un nuovo ambiente virtuale.</br>
Tramite conda: https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html#managing-environments </br>
Tramite venv: https://docs.python.org/3/tutorial/venv.html

Una volta creato l'ambiente virtuale sarà possibile installare il package contenente l'API:

```bash
pip install uniudpubapi
```

Dopo aver installato il package si può iniziare ad utilizzare il codice per l'importazione delle pubblicazioni.</br>

## Esempio di utilizzo dell'API
Di seguito si mostra come si può utilizzare l'API per esportare le pubblicazioni dei membri di un dipartimento in formato markdown e in formato bibtex
Innanzitutto bisogna importare le classi che servono per importare e scrivere le pubblicazioni:
```python
from uniudpubapi.dep_pubs import DepartmentPublications
from uniudpubapi.writers import BibtexPublicationWriter, MarkdownPublicationWriter
```
Poi sarà necessario definire i membri del dipartimento (o il gruppo di ricercatori) tramite un dizionario che ne specifica il nome e il codice:

```python
# Sostiturire nome e codice con quelli dei membri di cui si vuole ottenere le pubblicazioni
department = {
    "nome cognome": "rp1234"
}
```
Quindi definire le informazioni che si vuole ricavare, sia per quando riguarda gli elementi che andranno a essere visualizzati all'interno di un file markdown che per gli elementi che andranno inseritit all'interno del bibtex della pubblicazione.

```python
bibtex_elements = ["authors", "title", "year", "journal", "handle",
                   "publication type", "publisher", "volume", "book_title",
                   "doi", "pages", "series"]

markdown_elements = ["title", "authors", "year", "doi", "publication type",
                     "abstract"]
```
Gli elementi disponibili si possono trovare alla fine del file uniudpubepi/elements.py di questo repository, in cui si vedrà una successione di comandi di questo tipo:

```python
factory.register_type_of_element("title", Title)
factory.register_type_of_element("handle", Handle)
factory.register_type_of_element("publication type", PubType)
factory.register_type_of_element("authors", Authors)
factory.register_type_of_element("year", Year)
# ....
# ....
```
Gli elementi che si vedono all'interno del file sono tutti quelli che si possono importare (In nuove versioni tale lista può essere aggiornata con nuovi elementi).
Quindi si può procedere alla creazione di un oggetto di tipo DepartmentPublications, al cui costruttore si passa il dizionario con i membri del dipartimento e le liste delgi elementi (bibtex e markdown).
**N.B. gli argomenti devono essere nell'ordine mostrato nell'esempio.**
```python
d = DepartmentPublications(department, bibtex_elements, markdown_elements)
```
Quando si vuole popolare l'oggetto con tutte le informazioni basta eseguire il seguente comando:
```python
d.find_department_publications() # Dove d è l'oggetto creato in precedenza
```
Si noti che l'esecuzione di questa funzione richiederà una certa quantità di tempo, in quanto devono essere scaricate tutte le pubblicazioni.











