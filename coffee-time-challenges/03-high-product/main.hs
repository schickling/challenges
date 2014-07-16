module Main where

import Data.List (sortBy)

highProduct :: [Int] -> (Int, Int)
highProduct = foldl distribute (0, 0) . sortBy (flip compare)

distribute :: (Int, Int) -> Int -> (Int, Int)
distribute (a, b) x
  | a > b     = (a, b * 10 + x)
  | otherwise = (a * 10 + x, b)

main :: IO()
main = print $ highProduct [0..9]
