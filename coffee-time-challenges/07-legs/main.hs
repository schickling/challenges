module Main where

legs :: Int
legs = head [ x | x <- [1..], let d = x * 4, let h = 200 - d, x + h `div` 2 == 72 ]

main :: IO()
main = print legs
