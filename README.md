# Multiplication

Functions for traditional grade-school multiplication, Karatsuba multiplication, and a thresholded version of Karatsuba multiplication for integers, treating the inputs as arrays of bits.

## Motivation

I wanted to compare the run times of regular multiplication, Karatsuba multiplication, and thresholded Karatsuba multiplication.

## How To Use

### Karatsuba

Call the function **karatsuba** with the two parameters being lists of numbers representing the binary numbers to multiply. The function will return the result of the multiplication.

### Grade-School

Call the function **gradeschool** with the two parameters being lists of numbers representing the binary numbers to multiply. The function will return the result of the multiplication.

### Thresholded Karatsuba

Call the function **threshold** with the first two parameters being lists of numbers representing the binary numbers to multiply, and the last parameter being the threshold for when to use gradeschool or karatsuba method. The function will return the result of the multiplication.

## Reference

*Algorithms* by S. Dasgupta, C.H. Papadimitriou, and U.V. Vazirani
