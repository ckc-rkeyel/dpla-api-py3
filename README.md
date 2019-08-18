## Center for Knit and Crochet DPLA extraction

This code was originally designed to export DPLA extracts to RDF. For the Center for Knit and Crochet, the code has been modified to produce TSV (tab-separated values) output suitable for conversion to CSV (comma-separated values) and import into Omeka. **Please see the original README on the parent repository for more general instructions on how to use this code to extract data from DPLA.**

In order for this code to work, you'll need a DPLA [API-Key](http://dp.la/info/developers/codex/policies/#get-a-key). Copy the `default_EXAMPLE.cfg` file to `default.cfg` and add your API key to the `default.cfg` file.

From the command line, type `python ckc.py`.

Output:

    Query: 'crochet* OR knit*' returned 7000 results
    ----Accessing results page 2
    ----Accessing results page 3
    ----Accessing results page 4
    ----Accessing results page 5
    ----Accessing results page 6
    ----Accessing results page 7
    ----Accessing results page 8
    ----Accessing results page 9
    ----Accessing results page 10
    ----Accessing results page 11
    ----Accessing results page 12
    ----Accessing results page 13
    ----Accessing results page 14
    ----Check: 7000 records transferred
    Completed writing data/ckc.txt

Download the `data/ckc.txt` file to your computer, and open it in Microsoft Excel.

This can be a tricky process to make sure special characters are preserved. Open Excel first, use the Open, Browse option, then find the text file. In the Text Import Wizard, use the following options:

    Start import at row: 1
    File origin: 65001: Unicode (UTF-8)
    My data has headers: checked
    (next)

    Delimiters: Tab
    Text qualifier: "
    (next)

    All columns as "General"
    (next)

Save the file as `ckc.csv` with a file type of CSV UTF-8.

Login to the CKC Omeka site, and go to the Admin page. 

Click on the CSV Import+ entry on the left menu.

Attach the csv file to the form.

Use the following settings for a new import:

    Column delimiter: comma
    Enclosure: " (double quote)
    Element delimiter: pipe
    Tag delimiter: pipe
    File delimiter: pipe

    Default item type: Still Image
    Default collection: Library and Museum Collections
    Make records public: checked

    Identifier field: Identifer
    Action: Update the record if it exists, else create one
    Contains extra data: Perhaps, so the mapping should be done manually.

Click Next.

Map the following element fields:

    omeka_link -> Relation
    omeka_thumb -> Relation
    description -> Description
    language -> Language
    creator -> Creator
    id -> Identifier
    title -> Title
    source -> Source
    subjects -> Subject
    omeka_full -> Relation
    date -> Date
    type -> Type
    seeAlso -> References

In the special values column, set the following:

    identifier -> Identifier

Perform the import.

Note that there is a bug that puts everything in an [Untitled] collection. You have to move them to the Library & Museum Collections collection.


