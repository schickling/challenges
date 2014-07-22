module Main where

import Data.List (sortBy,nub,permutations)
import Data.List.Split (splitOneOf)

-- -1 and 0 are bucket delimiters
buckets :: [[[Int]]]
buckets = filter (all isValidBucket) $ map makeBuckets $ permutations [-1..13]
  where
    makeBuckets = splitOneOf [0,-1]

isValidBucket :: [Int] -> Bool
isValidBucket xs = not $ any (`elem` differences xs) xs

differences :: [Int] -> [Int]
differences xs = nub $ concatMap (\(z:zs) -> map (\a -> z - a) zs) subLists
  where
    sortedList = sortBy (flip compare) xs
    subLists = map (`drop` sortedList) [0..length xs - 2]

main :: IO()
main = print buckets
