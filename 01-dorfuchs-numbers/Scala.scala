(0 to 5).flatMap((0 to 9).drop(_).take(5).permutations.filter(_.head != 0).toSeq.distinct.map(_.mkString(""))).sortWith(_ < _).zipWithIndex.foreach(r => println((r._2 + 1) + ": " + r._1))
