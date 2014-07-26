module Main where

import Data.List

-- http://stackoverflow.com/a/18128184/2418739
choose :: Int -> [Int] -> [[Int]]
choose n list = concatMap permutations $ choose' list [] where
  choose' []     r = [r | length r == n]
  choose' (x:xs) r | length r == n = [r]
                   | otherwise     = choose' xs (x:r)
                                  ++ choose' xs r

bruteforce :: [Int]
bruteforce = head $ filter (\[a, b] -> a * b == completeSum - a - b) perms
  where
    numbers = [1..65502]
    perms = choose 2 numbers
    completeSum = sum numbers

main :: IO()
main = print bruteforce
