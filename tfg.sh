#!/bin/bash
fichero=$1
cien=100
funciones=`grep "def " < $fichero | wc -l`
n_test=`grep -i "def test" < $fichero| wc -l`
utiles=$(($funciones-$n_test))
porcentaje=$(awk "BEGIN {printf \"%.2f\",${n_test}/${utiles}*100}")
echo "$porcentaje %"
