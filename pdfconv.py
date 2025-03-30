import pdfkit
from time import sleep

# Open the file containing URLs
try:
    with open('inputurls.txt', 'r') as urls_file:
        urls = urls_file.readlines()
except FileNotFoundError:
    print("Error: 'inputurls.txt' not found. Please check the file path.")
    exit(1)

# Define options for PDF generation
options = {
    'custom-header': [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')
    ],
    'enable-local-file-access': ''
}

# Loop through URLs and convert each to a PDF
for url in urls:
    try:
        url = url.strip()
        # Extract a meaningful name from the URL
        name = url.split('/')[-2] if '/' in url else 'output'
        # Generate the PDF
        pdfkit.from_url(url, f'{name}.pdf', options=options)
        print(f"Successfully created {name}.pdf")
        sleep(2)  # Pause to avoid overwhelming the server
    except Exception as e:
        print(f"Failed to create PDF for URL: {url}. Error: {e}")
