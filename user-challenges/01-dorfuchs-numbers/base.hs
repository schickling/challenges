import Data.List (sort)
import Data.Char (digitToInt)
import Text.Printf

-- Check if the given list of numbers is ascending by exactly one
isAscending :: (Eq a, Num a) => [a] -> Bool
isAscending [] = True
isAscending [x] = True
isAscending (x:y:xs) = (x+1 == y) && isAscending (y:xs)

-- Check if the digits that are in the given number are in an intervall
-- So for 12345, 54321, 45321 the function returns True
-- but for 02345 it returns False
check :: Show a => a -> Bool
check x = isAscending $ map digitToInt $ sort $ show x

-- Find all numbers with property 'check' that have 5 digits
solve :: [Integer]
solve = filter check [10^4..10^5]

-- Format and print results
main :: IO()
main = mapM_
        (\(x, y) -> printf "%d: %d\n" x y)
        $ zip
            ([1..]::[Integer])
            solve
