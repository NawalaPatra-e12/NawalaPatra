# import_books_script.py
import os
import django

# Set the DJANGO_SETTINGS_MODULE to point to your project's settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "csv_test.settings")

# Initialize Django
django.setup()

import csv
from django.core.management.base import BaseCommand
from library.models import Book  # Adjust the import path to match your actual model
import chardet

# Determine the encoding of the CSV file
with open('book40copy2.csv', 'rb') as rawdata:
    result = chardet.detect(rawdata.read(10000))

# Use the detected encoding
encoding = result['encoding']

# Open the file with the detected encoding
with open('book40copy2.csv', 'r', encoding=encoding) as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    for row in reader:
        # Process the data
        book = Book(
                image_url=row['image_url'],
                title=row['title'],
                author=row['author'],
                category=row['category'],
                # Assign other fields as needed
            )

        book.save()

