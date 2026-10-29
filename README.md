# Public document formats

Public bodies print their records in a small number of layouts that repeat for decades: a civil service title specification, a notice of examination, an audit letter, a hearing testimony. A program that reads such a PDF can get the text right and still not know what the document says about itself: its title, its code, its agency, its date, where each section starts. This repository describes those layouts as data, with real public samples and the output a reader should produce for each, so that any tool can use them and any change to a reader can be tested against documents people rely on.

Each format is one folder under `formats/`. Its `README.md` describes the layout in plain words: how to recognise it, which fields it carries and where, and the traps a reader falls into. `samples/` holds public PDFs of that format, each with `<name>.expected.json`, the fields as printed, checked by a person against the scan. The samples also carry what one reader produced from them today, so the gap is visible.

`tools/check.py` scores a reader's text against the expected fields:

```sh
python3 tools/check.py formats/nyc-dcas-title-specification/samples \
  --reader-output formats/nyc-dcas-title-specification/samples/pdf-ocr-output.jsonl
```

The first format is the New York City civil service title specification, from the eleven scanned specifications in the set DCAS released under FOIL that had no text layer. The next is likely the DCAS notice of examination.

What is still open, and where to start:

- The syntax of a format's rules. The expected outputs are the contract; how a format states its rules (patterns, positions, section headings) should be settled with the first two formats in hand, not before.
- Field names. `title_code`, `agency_code`, `classification` and the rest come from these samples and are open to change.
- More samples, especially ones that break a reader.

Corrections and new formats are welcome as pull requests, and questions as issues. People and their agents are both welcome; an agent's pull request should say which samples it checked against the scans.

The descriptions, expected outputs, tools and the text read from the samples are dedicated to the public domain under [CC0 1.0](LICENSE). The sample PDFs are public records of the bodies that issued them. Maintained by [Symbiosis Lab](https://github.com/Symbiosis-Lab).
