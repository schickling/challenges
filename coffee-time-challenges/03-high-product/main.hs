module Main where

import Data.List

highProduct :: [Int] -> (Int, Int)
highProduct = maximumPartition . assmblePartitions . sortPartitions . perms

maximumPartition :: [(Int, Int)] -> (Int, Int)
maximumPartition = maximumBy (\(a1, b1) (a2, b2) -> compare (a1 * b1) (a2 * b2))

assmblePartitions :: [([Int], [Int])] -> [(Int, Int)]
assmblePartitions = map (\(a, b) -> (assmble a, assmble b))

sortPartitions :: [([Int], [Int])] -> [([Int], [Int])]
sortPartitions = map (\(a, b) -> (reverse $ sort a, reverse $ sort b))

assmble :: [Int] -> Int
assmble xs = sum $ zipWith (\x y -> 10^y * x) (reverse xs) [0..]

perms :: [Int] -> [([Int], [Int])]
perms xs = concatMap allPartitions (permutations xs)

allPartitions :: [Int] -> [([Int], [Int])]
allPartitions xs = [ splitAt k xs | k <- [1..length xs - 1]]

main = putStrLn $ show $ highProduct [0..9]

