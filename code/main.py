import tkinter as tk
from tkinter import filedialog
import re

def process_bib_file(bib_content):

    entries = re.split(r'\n\s*\n', bib_content.strip())
    new_entries = []
    used_keys = {}  #

    for entry in entries:
        if not entry.strip().startswith('@'):
            new_entries.append(entry)
            continue

        # Extract header
        header_match = re.match(r'@(\w+)\{([^,]+),', entry)
        if not header_match:
            new_entries.append(entry)
            continue

        entry_type = header_match.group(1)
        old_key = header_match.group(2)

        # Extract the author field
        author_match = re.search(r'author\s*=\s*{([^}]+)}', entry, re.IGNORECASE)
        if author_match:
            author_field = author_match.group(1)
            # Use the first author (in case of multiple authors separated by 'and')
            first_author = author_field.split(" and ")[0].strip()
            if ',' in first_author:
                last_name = first_author.split(',')[0].strip()
            else:
                # If not comma separated, take the first token.
                last_name = first_author.split()[0].strip()

            # For hyphenated names, use only the part before the hyphen
            if '-' in last_name:
                last_name = last_name.split('-')[0]
            # For multi-part names (with a space), use the first word
            if ' ' in last_name:
                last_name = last_name.split()[0]
            new_prefix = last_name.lower()
        else:
            # If no author is found, default to using the old key as the prefix.
            new_prefix = old_key

        year_match = re.search(r'(\d{4})', old_key)
        if year_match:
            year = year_match.group(1)
            index = old_key.find(year)
            suffix = old_key[index+4:]
        else:
            year = ""
            suffix = old_key[len(new_prefix):]

        # Create ne key
        new_key = new_prefix + year + suffix

        # Prevent duplicates by appending a letter if the key is already used
        if new_key in used_keys:
            used_keys[new_key] += 1
            letter = chr(96 + used_keys[new_key])
            new_key += letter
        else:
            used_keys[new_key] = 1

        # Replace the citation key header
        new_entry = re.sub(r'^(@\w+\{)[^,]+,', r'\1' + new_key + ',', entry, flags=re.MULTILINE)
        new_entries.append(new_entry)

    # Join 
    return "\n\n".join(new_entries)


# tkinker dialogs
root = tk.Tk()
root.withdraw() 


input_file_path = filedialog.askopenfilename(
    title="Select input .bib file",
    filetypes=[("BibTeX files", "*.bib"), ("All files", "*.*")]
)

if input_file_path:
    with open(input_file_path, 'r', encoding='utf-8') as f:
        bib_content = f.read()

    # Process .bib content.
    new_bib_content = process_bib_file(bib_content)

    # Output file path
    output_file_path = filedialog.asksaveasfilename(
        title="Save output .bib file",
        defaultextension=".bib",
        filetypes=[("BibTeX files", "*.bib"), ("All files", "*.*")]
    )

    if output_file_path:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(new_bib_content)
        print("File processed and saved to:", output_file_path)
    else:
        print("Output file not selected.")
else:
    print("Input file not selected.")
