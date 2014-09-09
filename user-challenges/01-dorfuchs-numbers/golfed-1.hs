import Data.List
import Data.Char
import Text.Printf
isAscending [] = True
isAscending [x] = True
isAscending (x:y:xs) = (x+1 == y) && isAscending (y:xs)
check x = isAscending $ map digitToInt $ sort $ show x
solve :: [Integer]
solve = filter check [10^4..10^5]
main = mapM_ (\(x, y) -> printf "%d: %d\n" x y) $ zip ([1..]::[Integer]) solve