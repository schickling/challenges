module Main where

-- check if all three numbers multiplied are odd
check :: Integral a => (a, a, a) -> Bool
check (x, y, z) = (x * y * z) `mod` 2 == 1

-- Find probability that check applies to the result of throwing 3 dice
solve :: Double
solve = (fromIntegral $ length $ filter check ls) / (fromIntegral $ length ls)
        where ls = [(x, y, z) | x <- [1..6], y <- [1..6], z <- [1..6]]

-- Print results
main :: IO()
main = print solve
