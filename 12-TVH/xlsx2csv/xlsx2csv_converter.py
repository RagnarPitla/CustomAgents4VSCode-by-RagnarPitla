#!/usr/bin/env python3
"""
XLSX to CSV Converter
=====================
A robust Python script to convert Excel (.xlsx) files to CSV format.

Usage:
    python xlsx2csv_converter.py <input.xlsx> [output.csv] [--sheet <name>] [--all-sheets] [--delimiter <char>]

Examples:
    python xlsx2csv_converter.py data.xlsx
    python xlsx2csv_converter.py data.xlsx output.csv
    python xlsx2csv_converter.py data.xlsx --sheet "Sales Data"
    python xlsx2csv_converter.py data.xlsx --all-sheets
    python xlsx2csv_converter.py data.xlsx --delimiter ";"
"""

import argparse
import os
import sys
from pathlib import Path

try:
    import openpyxl
except ImportError:
    print("Error: openpyxl is not installed.")
    print("Install it with: pip install openpyxl")
    sys.exit(1)

try:
    import pandas as pd
except ImportError:
    print("Error: pandas is not installed.")
    print("Install it with: pip install pandas")
    sys.exit(1)


def convert_xlsx_to_csv(
    input_file: str,
    output_file: str = None,
    sheet_name: str = None,
    all_sheets: bool = False,
    delimiter: str = ",",
    encoding: str = "utf-8"
) -> list:
    """
    Convert an XLSX file to CSV format.
    
    Args:
        input_file: Path to the input XLSX file
        output_file: Path to the output CSV file (optional)
        sheet_name: Specific sheet to convert (optional)
        all_sheets: Convert all sheets to separate CSV files
        delimiter: CSV delimiter character (default: comma)
        encoding: Output file encoding (default: utf-8)
    
    Returns:
        List of created CSV file paths
    """
    input_path = Path(input_file)
    
    # Validate input file
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    if input_path.suffix.lower() not in ['.xlsx', '.xls', '.xlsm']:
        raise ValueError(f"Input file must be an Excel file (.xlsx, .xls, .xlsm): {input_file}")
    
    created_files = []
    
    # Load the Excel file
    excel_file = pd.ExcelFile(input_file, engine='openpyxl')
    available_sheets = excel_file.sheet_names
    
    print(f"📊 Found {len(available_sheets)} sheet(s): {', '.join(available_sheets)}")
    
    if all_sheets:
        # Convert all sheets
        for sheet in available_sheets:
            output_name = output_file or f"{input_path.stem}_{sheet}.csv"
            if len(available_sheets) > 1 and not output_file:
                output_name = f"{input_path.stem}_{sheet}.csv"
            elif len(available_sheets) > 1 and output_file:
                base = Path(output_file).stem
                output_name = f"{base}_{sheet}.csv"
            
            output_path = input_path.parent / output_name
            df = pd.read_excel(excel_file, sheet_name=sheet)
            df.to_csv(output_path, sep=delimiter, index=False, encoding=encoding)
            created_files.append(str(output_path))
            print(f"✅ Converted sheet '{sheet}' → {output_path}")
    
    elif sheet_name:
        # Convert specific sheet
        if sheet_name not in available_sheets:
            raise ValueError(f"Sheet '{sheet_name}' not found. Available sheets: {available_sheets}")
        
        output_name = output_file or f"{input_path.stem}.csv"
        output_path = input_path.parent / output_name if not Path(output_file or "").is_absolute() else Path(output_file)
        
        df = pd.read_excel(excel_file, sheet_name=sheet_name)
        df.to_csv(output_path, sep=delimiter, index=False, encoding=encoding)
        created_files.append(str(output_path))
        print(f"✅ Converted sheet '{sheet_name}' → {output_path}")
    
    else:
        # Convert first sheet only (default)
        output_name = output_file or f"{input_path.stem}.csv"
        output_path = input_path.parent / output_name if not Path(output_file or "").is_absolute() else Path(output_file)
        
        df = pd.read_excel(excel_file, sheet_name=available_sheets[0])
        df.to_csv(output_path, sep=delimiter, index=False, encoding=encoding)
        created_files.append(str(output_path))
        print(f"✅ Converted sheet '{available_sheets[0]}' → {output_path}")
    
    return created_files


def get_xlsx_info(input_file: str) -> dict:
    """
    Get information about an XLSX file without converting it.
    
    Args:
        input_file: Path to the XLSX file
    
    Returns:
        Dictionary with file information
    """
    input_path = Path(input_file)
    
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")
    
    excel_file = pd.ExcelFile(input_file, engine='openpyxl')
    
    info = {
        "file_name": input_path.name,
        "file_size": f"{input_path.stat().st_size / 1024:.2f} KB",
        "sheets": [],
    }
    
    for sheet in excel_file.sheet_names:
        df = pd.read_excel(excel_file, sheet_name=sheet)
        info["sheets"].append({
            "name": sheet,
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": list(df.columns),
        })
    
    return info


def main():
    parser = argparse.ArgumentParser(
        description="Convert XLSX files to CSV format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s data.xlsx                    # Convert first sheet to data.csv
  %(prog)s data.xlsx output.csv         # Convert first sheet to output.csv
  %(prog)s data.xlsx --sheet "Sheet2"   # Convert specific sheet
  %(prog)s data.xlsx --all-sheets       # Convert all sheets to separate CSVs
  %(prog)s data.xlsx --delimiter ";"    # Use semicolon as delimiter
  %(prog)s data.xlsx --info             # Show file information only
        """
    )
    
    parser.add_argument(
        "input_file",
        help="Path to the input XLSX file"
    )
    
    parser.add_argument(
        "output_file",
        nargs="?",
        default=None,
        help="Path to the output CSV file (optional)"
    )
    
    parser.add_argument(
        "--sheet", "-s",
        dest="sheet_name",
        default=None,
        help="Name of the specific sheet to convert"
    )
    
    parser.add_argument(
        "--all-sheets", "-a",
        dest="all_sheets",
        action="store_true",
        help="Convert all sheets to separate CSV files"
    )
    
    parser.add_argument(
        "--delimiter", "-d",
        default=",",
        help="CSV delimiter character (default: comma)"
    )
    
    parser.add_argument(
        "--encoding", "-e",
        default="utf-8",
        help="Output file encoding (default: utf-8)"
    )
    
    parser.add_argument(
        "--info", "-i",
        action="store_true",
        help="Show file information without converting"
    )
    
    args = parser.parse_args()
    
    try:
        if args.info:
            # Show file information only
            info = get_xlsx_info(args.input_file)
            print(f"\n📁 File: {info['file_name']}")
            print(f"📏 Size: {info['file_size']}")
            print(f"📑 Sheets: {len(info['sheets'])}")
            print("\n" + "=" * 50)
            for sheet in info["sheets"]:
                print(f"\n📋 Sheet: {sheet['name']}")
                print(f"   Rows: {sheet['rows']}")
                print(f"   Columns: {sheet['columns']}")
                print(f"   Column Names: {', '.join(sheet['column_names'][:5])}", end="")
                if len(sheet['column_names']) > 5:
                    print(f" ... (+{len(sheet['column_names']) - 5} more)")
                else:
                    print()
        else:
            # Convert file
            print(f"\n🔄 Converting: {args.input_file}")
            created_files = convert_xlsx_to_csv(
                input_file=args.input_file,
                output_file=args.output_file,
                sheet_name=args.sheet_name,
                all_sheets=args.all_sheets,
                delimiter=args.delimiter,
                encoding=args.encoding
            )
            print(f"\n🎉 Done! Created {len(created_files)} file(s)")
            
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
