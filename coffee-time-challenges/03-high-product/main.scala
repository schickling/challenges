object HighProduct {
    def main(arg: Array[String]) {
        var max_product = BigInt(0);
        var a_max = BigInt(0L);
        var b_max = BigInt(0L);
        val digits = List(0, 1, 2, 3, 4, 5, 6, 7, 8, 9);
        for (c <- digits.combinations(4)) {
            // Sort the digits so that the highest number gets built
            val a = c.sorted(Ordering[Int]);
            val b = (digits filterNot a.contains).sorted(Ordering[Int]);
            // calculate number a
            var anum = BigInt(0L);
            for ((digit, place) <- a.zipWithIndex) {
                anum += digit * scala.math.pow(10, place).toInt;
            }
            // calculate number b
            var bnum = BigInt(0L);
            for ((digit, place) <- b.zipWithIndex) {
                bnum += digit * scala.math.pow(10, place).toInt;
            }

            // calculate number a
            if(anum*bnum > max_product){
                max_product = anum*bnum;
                a_max = anum;
                b_max = bnum;
            }
        }

        println("%d • %d = %d".format(a_max, b_max, max_product));
    }
}