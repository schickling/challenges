module TwoBase where

findBase :: (Int, Int, Int)
findBase = head [(x, y, z) | x <- [1..9], y <- [1..9], z <- [1..9], assemble x y z == (asBase9 $ assemble z y x)]

asBase9 :: Int -> Int
asBase9 x = accBase9 x 0
  where
    accBase9 0 _ = 0
    accBase9 x i = 10^i * (x `mod` 9) + accBase9 (x `div` 9) (i + 1)

assemble :: Int -> Int -> Int -> Int
assemble x y z = x*100 + y*10 + z
