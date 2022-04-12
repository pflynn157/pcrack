#!/bin/bash
echo ""
echo "DEMO 2"
echo "English dictionary word list"
echo ""

echo "Generating word list..."
echo "CMD: python3 ./guess.py lists/words.txt -rc-words 2 -rc-upper -rc-syms"

python3 ./guess.py lists/words.txt -rc-words 1

echo "Done"
echo ""
echo "Word count:"
wc -l words_out.txt
echo ""

echo ""
echo "Done!"
echo ""

