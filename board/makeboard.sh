#!/bin/sh

FILES=../experiment/*.dat*
for f in $FILES
do
    ln -s $f `basename $f`
done
context --path="$(cd ..; pwd)" board.tex
