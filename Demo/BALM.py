import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

def fetch_and_parse(url):
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')

def extract_tables(soup):
    tables = []
    for idx, table in enumerate(soup.find_all('table'), start=1):
        caption = table.find('caption')
        if caption:
            title = caption.get_text(strip=True)
        else:
            prev_heading = table.find_previous(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            title = prev_heading.get_text(strip=True) if prev_heading else f'Bảng {idx}'

        description = f'Bảng được trích xuất từ phần: \"{title}\"'

        try:
            df = pd.read_html(StringIO(str(table)))[0]
            tables.append({
                'title': title,
                'description': description,
                'html': str(table),
                'data': df
            })
        except Exception as e:
            print(f"⚠️ Lỗi khi đọc bảng '{title}': {e}")
    return tables

def display_table_by_title(tables, title):
    found = False
    for table in tables:
        if title.lower() in table['title'].lower():
            print(f"\n🧾 Tiêu đề: {table['title']}")
            print(f"📄 Mô tả: {table['description']}")
            print("📊 Dữ liệu bảng:")
            print(table['data'])
            found = True
    if not found:
        print(f"❌ Không tìm thấy bảng với tiêu đề: {title}")

def save_all_tables_to_excel(tables, filename='tables_output.xlsx'):
    if not tables:
        print("❌ Không có bảng hợp lệ để lưu vào Excel.")
        return
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        for table in tables:
            sheet_name = table['title'][:31] or f'Sheet{tables.index(table)+1}'
            table['data'].to_excel(writer, sheet_name=sheet_name, index=False)
    print(f"\n✅ Đã lưu {len(tables)} bảng vào file: {filename}")

# ---- Main chạy ----
url = 'https://www.w3schools.com/html/html_tables.asp'
soup = fetch_and_parse(url)
tables = extract_tables(soup)

requested_title = 'Company'  # Bạn có thể đổi tiêu đề này
display_table_by_title(tables, requested_title)
save_all_tables_to_excel(tables)
