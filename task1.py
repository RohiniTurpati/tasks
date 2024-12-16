import pdfplumber

def extract_tables_from_page(pdf_path, page_number):
    with pdfplumber.open(pdf_path) as pdf:
        if page_number < 0 or page_number >= len(pdf.pages):
            return None
        page = pdf.pages[page_number]
        tables = page.extract_tables()
        return tables

def format_table_output(tables):
    output = ""
    if tables:
        for i, table in enumerate(tables):
            output += f"\nTable {i + 1}:\n"
            for row in table:
                output += " | ".join(str(cell) for cell in row) + "\n"
    else:
        output += "No tables found on this page."
    return output

def handle_query(user_query, pdf_path):
    try:
        page_number = int(user_query.split("page")[1].strip()) - 1
    except (IndexError, ValueError):
        return "Invalid query format. Please specify a valid page number."

    tables = extract_tables_from_page(pdf_path, page_number)
    if tables is None:
        return f"The specified page {page_number + 1} does not exist in the PDF."

    response = f"Tables found on page {page_number + 1}:\n"
    response += format_table_output(tables)
    return response

if __name__ == "__main__":
    pdf_path = r"rgp.pdf"  # Replace with your PDF file path
    user_query = input("Enter your query: ")
    response = handle_query(user_query, pdf_path)
    print(response)