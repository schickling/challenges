module Main where

-- XYZ in base10 (ten) is equal to ZYX in base9
check :: (Eq a, Num a) => (a, a, a) -> Bool
check (x, y, z) = x*10^2 + y*10 + z == z*9^2 + y*9 + x

-- Find all numbers with property 'check'
solve :: [(Int, Int, Int)]
solve = filter check [(x, y, z) | x <- [0..9], y <- [0..9], z <- [0..9]]

-- Print results
main :: IO()
main = print solve
