module Main where

import Data.List (sortBy,nub,permutations)
import Data.List.Split (splitOneOf)

buckets :: [Int] -> [[[Int]]]
buckets xs = filter (all isValidBucket) $ map makeBuckets $ permutations (delimiters ++ xs)
  where
    delimiters = [-2,-1]
    makeBuckets = splitOneOf delimiters

isValidBucket :: [Int] -> Bool
isValidBucket xs = not $ any (`elem` differences xs) xs

differences :: [Int] -> [Int]
differences xs = nub $ concatMap (\(z:zs) -> map (\a -> z - a) zs) subLists
  where
    sortedList = sortBy (flip compare) xs
    subLists = map (`drop` sortedList) [0..length xs - 2]

main :: IO()
main = print $ buckets [1..13]
