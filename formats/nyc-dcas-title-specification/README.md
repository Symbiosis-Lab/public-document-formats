# New York City civil service title specification

Issued by the Department of Citywide Administrative Services (DCAS) for each civil service title. A specification states what the title's holders do and what they need to qualify. DCAS released 941 of them under a FOIL request; [Databook](https://databook.nyc) shows them on its title pages. The samples here are the eleven of the 941 that are scans with no text layer.

## Layout

Every page starts with the same two or three header lines, and every page ends with the same footer. Page 1 then gives the title, underlined and centred, and the sections follow.

The header names the class of the title and its code, in one of three forms seen so far:

| Classification | Second line | Code | Samples |
|---|---|---|---|
| `C-X` | the service, `THE MANAGERIAL SERVICE [061]` | `CODE NO. M 10019`, top right | 10019, 82989 |
| `NC – X, PART I` | the agency and its three-digit code, `ADMINISTRATION FOR CHILDREN’S SERVICES (067)` | `CODE NO. M95058`, top right | 95058–95065 |
| `RULE-10` / `EXEMPT` / `MANAGERIAL`, stacked | none | `TC 13229`, top right | 13229 |

The five-digit title code follows the letter `M` (managerial) or `TC`; a competitive class title prints it bare, `C – XI` with `CODE NO. 10217`. The three-digit agency code is the one the City's budget and spending data use. A service or occupational group code in brackets (`[061]`, `OCCUPATIONAL GROUP [277]`, `[043.1]`) is not an agency code. Some second lines carry no code at all (`VARIOUS CITY DEPARTMENTS`), and a title can wrap onto two lines, with a parenthetical on the second (`VICE PRESIDENT` / `(NEW YORK CITY PUBLIC HOUSING PRESERVATION TRUST)`).

The footer gives a date on the left and `PAGE n OF m` on the right: `R 05.08.1985`, `12.21.94`, `02.24.2020`, `9.3.2014`. The date is month, day, year. What the `R` prefix marks is not confirmed (probably a revision). 13229 has no footer.

Sections, in this order, each under an underlined heading: `Duties and Responsibilities` (also `Duties and Responsibilities:` and, in older specifications, `General Statement of Duties and Responsibilities`), `Examples of Typical Tasks` (absent from the two `C-X` samples), `Qualification Requirements`, `Direct Lines of Promotion`. A section that runs onto the next page repeats its heading with `(continued)`. 13229 has no headings: it is a few paragraphs of duties.

## Fields

`<name>.expected.json` gives, as printed: `title_code`, `code_as_printed`, `classification`, `service`, `agency`, `agency_code`, `title`, `date_as_printed`, `date` (ISO), `pages` and `sections` (headings in order). A field the document does not print is `null`.

## Traps

- The header and footer repeat on every page, so a reader that strips running headers and footers deletes the code, the classification and the date. pdf-ocr 0.2.5 did this: the code was missing from the text of 7 of the 11 samples, and the date from 9. Since 0.2.6 the first page keeps its header and the last page its footer.
- Handwriting in the margin is read into the nearest line: on 82989, "FLSA CODE E" joins the title as "SANITARIAN E".
- The title is the first underlined, centred line, not the first line. A reader that guesses from the first line, or from the file name, gets it wrong: pdf-ocr 0.2.5's title fact was the file name for 10 of 11. The title is the paragraph right above the first heading, below the header; when there are no headings (13229), the line right below the code.
- The Job Title column of the title viewer's own data (`extracted_data.csv`) is cut at 30 characters and sometimes starts with header text (`[043.1] AGE 1 OF 2 BRIDGE AND TUNNEL LIEUTENANT`), so it is not a reference for the title.
- OCR misreads to check: on 95063, "DOHMR" for "DOHMH".

## Today

pdf-ocr 0.2.6 (`samples/pdf-ocr-output.jsonl`, and the text as `samples/<code>.txt`, with a link to each page of the PDF from page 2 on): 63 of the 64 expected values appear in its text (0.2.5: 38), its title fact is right for 11 of 11 (0.2.5: 0) and its date fact for the 10 of 10 that print a date (0.2.5: 0). The one value missing is 13229's classification, printed as three stacked lines that the scan reads in another order. It recognises the format with a rule written in its code (`front.rs` in [moss-registry](https://github.com/Symbiosis-Lab/moss-registry/tree/main/plugins/pdf-ocr/native)); stating that rule as data in this folder is still open (see the [README](../../README.md)). On 40 specifications with a text layer, drawn at random from the title viewer and checked by hand, its title is right for 40 and its date matches the viewer's effective date for all 37 that have one; they are not samples here yet. `samples/collection.json` lists the samples with their SHA-256, source address and agency code.
