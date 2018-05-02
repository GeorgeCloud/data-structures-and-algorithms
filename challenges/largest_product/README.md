# Largest product of 2 adjacent values in a 2D array
The largest_product method accepts an array of arrays with pair values that
are multiplied for later comparison to the highest stored product of pairs and
cached as highest saved value and returned until a full iteration is complete.

## Challenge
Validating matrix if matrix has two pairs and if so preform and operation on.

## Solution
Create a variable to store highest recorded product.
Iterate through array of arrays.
Assign the two values inside each array as x and y.
compare if x * y is greater than highest recorded product.
If so save it as new highest.
Else do nothing and continue to iterate.

largest-product-array.png
