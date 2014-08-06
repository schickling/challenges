
-- Get the numbers x and y, that don't contain any zeroes and have x*y=10**6
solve :: (Int, Int)
solve = (5^6, 2^6)

-- Get a string for printing
showDetails :: (Int, Int) -> String
showDetails (x, y) = show x ++ " * " ++ show y ++ " = 1 000 000"

-- Print results
main :: IO()
main = print $ showDetails solve