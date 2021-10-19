# Operações Básicas que todo maratonista deve saber fazer rapidamente

## Create zero matrix 2 x 3

Array.from(Array(2), \_ => Array(3).fill(0));

## Matrix number of row and column

m = mat.length // number of rows
n = mat[0].length // number of column

## Remove duplicates

array.filter((v, i, a) => a.indexOf(v) === i)
