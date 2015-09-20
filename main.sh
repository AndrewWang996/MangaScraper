mkdir Images
python scraper.py
cd Images
convert *.png chapter.pdf
rm *.png
cd ../

