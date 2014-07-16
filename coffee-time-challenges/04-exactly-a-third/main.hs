module Main where

-- Idea:
-- The denominator has to be exactly 4 digits long.
-- Iterate over all 4 digit permutations, multiply them
-- by 4 and check if the result consists solely of the
-- remaing 5 digits

import Data.List

-- http://stackoverflow.com/a/18128184/2418739
choose :: Int -> [Int] -> [[Int]]
choose n list = concatMap permutations $ choose' list [] where
  choose' []     r = [r | length r == n]
  choose' (x:xs) r | length r == n = [r]
                   | otherwise     = choose' xs (x:r) 
                                  ++ choose' xs r

perms :: [[Int]]
perms = choose 4 [1..9]

assemble :: [Int] -> Int
assemble = foldl1 (\acc x -> acc * 10 + x)

dissemble :: Int -> [Int]
dissemble 0 = []
dissemble x = dissemble (x `div` 10) ++ [x `mod` 10]

areEqual :: [Int] -> [Int] -> Bool
areEqual a b = sort a == sort b

isThird :: [Int] -> Bool
isThird xs = areEqual xs complement
  where complement = [1..9] \\ dissemble numerator
        numerator = 3 * assemble xs

toPairs :: [Int] -> (Int, Int)
toPairs x = (a, a * 3) where a = assemble x

result :: [(Int, Int)]
result = map toPairs $ filter isThird perms

main :: IO()
main = print result
