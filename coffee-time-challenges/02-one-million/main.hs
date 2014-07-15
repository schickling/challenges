module Factorize where

factorize :: Int -> (Int, Int)
factorize x = head [(a, b) | a <- [1..], let b = x `div` a, a * b == x,  a `mod` 10 /= 0, b `mod` 10 /= 0]
