# XLSX to CSV Converter

A Python-based tool for converting Excel (.xlsx) files to CSV format.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd /Users/ragnarpitla/Documents/VS\ Code\ Repo/CustomAgents4VSCode-by-RagnarPitla/12-TVH/xlsx2csv
pip install -r requirements.txt
```

### 2. Basic Usage

```bash
# Convert first sheet to CSV (same name as input)
python xlsx2csv_converter.py data.xlsx

# Convert to specific output file
python xlsx2csv_converter.py data.xlsx output.csv

# Convert a specific sheet
python xlsx2csv_converter.py data.xlsx --sheet "Sheet2"

# Convert all sheets to separate CSVs
python xlsx2csv_converter.py data.xlsx --all-sheets

# Use semicolon delimiter (for European locales)
python xlsx2csv_converter.py data.xlsx --delimiter ";"

# Just show file info without converting
python xlsx2csv_converter.py data.xlsx --info
```

## 📖 Full Command Reference

```
usage: xlsx2csv_converter.py [-h] [--sheet SHEET_NAME] [--all-sheets]
                              [--delimiter DELIMITER] [--encoding ENCODING]
                              [--info]
                              input_file [output_file]

Arguments:
  input_file              Path to the input XLSX file
  output_file             Path to the output CSV file (optional)

Options:
  -h, --help              Show this help message
  --sheet, -s SHEET_NAME  Name of the specific sheet to convert
  --all-sheets, -a        Convert all sheets to separate CSV files
  --delimiter, -d CHAR    CSV delimiter character (default: comma)
  --encoding, -e ENCODING Output file encoding (default: utf-8)
  --info, -i              Show file information without converting
```

## 🐍 Using as a Python Module

```python
from xlsx2csv_converter import convert_xlsx_to_csv, get_xlsx_info

# Convert a file
created_files = convert_xlsx_to_csv(
    input_file="data.xlsx",
    output_file="output.csv",
    sheet_name="Sales",      # Optional: specific sheet
    all_sheets=False,        # Optional: convert all sheets
    delimiter=",",           # Optional: CSV delimiter
    encoding="utf-8"         # Optional: file encoding
)

# Get file information
info = get_xlsx_info("data.xlsx")
print(info)
```

## 📁 Files in this Directory

| File                    | Description                                 |
| ----------------------- | ------------------------------------------- |
| `xlsx2csv_converter.py` | Main Python conversion script               |
| `requirements.txt`      | Python dependencies                         |
| `xlsx2csv.agent.md`     | VS Code Copilot agent for guided conversion |
| `README.md`             | This documentation                          |

## 🤖 Using the VS Code Agent

This tool includes a VS Code Copilot agent. To use it:

1. Open VS Code with GitHub Copilot installed
2. Open Copilot Chat
3. Type `@xlsx2csv` followed by your request
4. The agent will guide you through the conversion process

Example prompts:

- `@xlsx2csv Convert my sales.xlsx file to CSV`
- `@xlsx2csv Show me info about data.xlsx`
- `@xlsx2csv Convert all sheets in report.xlsx`

## 🔧 Troubleshooting

### "openpyxl is not installed"

```bash
pip install openpyxl
```

### "pandas is not installed"

```bash
pip install pandas
```

### Permission denied

Make sure the script is executable:

```bash
chmod +x xlsx2csv_converter.py
```

### File not found

Use the full path to your XLSX file:

```bash
python xlsx2csv_converter.py /full/path/to/your/file.xlsx
```

## 📝 License

Part of the CustomAgents4VSCode repository.
