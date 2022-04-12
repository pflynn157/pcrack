#!/bin/bash
echo ""
echo "DEMO 1"
echo "Simple word list- 'password' only."
echo ""

echo "Generating word list..."
echo "CMD: python3 ./guess.py lists/simple.txt -rc-words 2 -rc-upper -rc-syms"

python3 ./guess.py lists/simple.txt -rc-words 2 -rc-upper -rc-syms

echo "Done"
echo ""
echo "Word count:"
wc -l words_out.txt
echo ""

echo "-----------------------------"
echo ""
echo "Running password cracker..."
echo ""


./gc 5f4dcc3b5aa765d61d8327deb882cf99

./gc 999c2ede8077c8cca439658e4bffcc90

./gc 5e8e08028571734ce76068a97d56a32d

./gc 350310b6de1650447ec723b1a5df8e96

echo ""
echo "Done!"
echo ""

