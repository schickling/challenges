module Main where

total :: Int
total = sum $ map read $ split $ replaceZeros strNumbers

strNumbers :: [String]
strNumbers = map show [1..10000]

replaceZeros :: [String] -> [String]
replaceZeros = map (map (\x -> if x == '0' then ' ' else x))

split :: [String] -> [String]
split = concatMap words

main :: IO()
main = print total
