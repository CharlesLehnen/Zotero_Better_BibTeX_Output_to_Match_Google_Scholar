# Zotero Better BibTeX Output to Match Google Scholar

A Python script that standardizes BibTeX citation keys exported from Zotero with Better BibTeX to match the automatic citation format used by Google Scholar.

**If you use this script, please support the project by starring this repository!**

## Purpose

When generating a bibliography for a LaTeX document in **VSCode, Overleaf, or another LaTeX editor**, Zotero’s Better BibTeX plugin exports citation keys that differ from Google Scholar’s format.

This script fixes **two major inconsistencies** in the citation keys:

1. **Hyphenated last names** (e.g., `auger-methe2021guide` → `auger2021guide`).
2. **Multiple last names separated by spaces** (e.g., `canorodriguez2018dieta` → `cano2018dieta`).

## Usage

### Exporting via Zotero

For best results, adjust Better BibTeX’s Citation Key Formula in Zotero:

1. Download Better BibLaTeX plugin: https://retorque.re/zotero-better-bibtex/
2. Open Zotero.
3. **Tools > Plugins > settings icon > Install Plugin From File...**
4. Go to **Edit > Settings > Better BibTeX**.
5. Paste the following into **Citation Key Formula** box:

   ```plaintext
   [auth:lower][year][veryshorttitle:lower]
   ```

6. When exporting, **right-click the collection > **Export Collection > Select **Better BibTeX**.

*Note: you may need to **highlight all the citations in your collection > right-click > Better BibTeX > Refresh BibTeX Key***

This process ensures that citation keys follow a structured format, making it easier for this script to process them correctly.

### Running the Script

#### Option 1: Using the .exe File (Windows Only)

1. **Ensure Python 3 is installed** on your computer.
2. **Run the `main.exe` file**.
3. **Select the input `.bib` file** when prompted.
4. **Choose an output file location** for the corrected `.bib` file.

The script will process the BibTeX entries and save a cleaned version.


#### Option 2: Running the Python Script directly

1. **Ensure Python 3 is installed** on your computer.
2. **Clone this repository** or download the script to your local machine.
3. **Run the script** using the command:

   ```bash
   cd code
   python main.py
   ```

4. **Select the input `.bib` file** when prompted.
5. **Choose an output file location** for the corrected `.bib` file.

The script will process the BibTeX entries and save a cleaned version.

---

### Input and Output Examples

#### Example Input (Incorrect Zotero Output)

```bibtex
@article{auger-methe2021guide,
  author = {Auger-Méthé, Marie and Newman, Ken},
  date = {2021},
}

@article{canorodriguez2018dieta,
  author = {Cano Rodríguez, Carlos Alfredo},
  date = {2018},
}
```

#### Example Output (Google Scholar-Style)

```bibtex
@article{auger2021guide,
  author = {Auger-Méthé, Marie and Newman, Ken},
  date = {2021},
}

@article{cano2018dieta,
  author = {Cano Rodríguez, Carlos Alfredo},
  date = {2018},
}
```

## Notes and assumptions

- Corrects hyphenated last names → Keeps only the first part.
- Fixes two-part last names → Uses only the first surname.
- Prevents duplicates → Appends suffixes (a, b, c, …) if necessary.
- Preserves formatting → Entries that are already correct remain unchanged.
- Works with all BibTeX entry types → `@article`, `@book`, `@inproceedings`, etc.

## Citation

If you use this project, please cite it appropriately.

**Example Citation:**

Lehnen, Charles (2025). “Zotero Better BibTeX Output to Match Google Scholar”. GitHub repository. https://github.com/CharlesLehnen/Zotero_Better_BibTeX_Output_to_Match_Google_Scholar

**BibTeX:**

```bibtex
@misc{lehnen2025bibtex,
  author = {Lehnen, Charles},
  title = {Zotero Better BibTeX Output to Match Google Scholar},
  year = {2025},
  howpublished = {\url{https://github.com/CharlesLehnen/Zotero_Better_BibTeX_Output_to_Match_Google_Scholar}}
}
```

## License

This project is licensed under the BSD 3-Clause License - see the `LICENSE.md` file for details.
