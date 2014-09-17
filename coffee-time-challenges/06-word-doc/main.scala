object WordDoc {
    def main(arg: Array[String]) {
        val number_list = for(i <- 1 to 10000) yield i.toString;
        val daughter_list = for(el<-number_list) yield el.replace('0', ' ');
        var sum = 0;
        for(el <- daughter_list) {
            for(n <- el.split(' ')) {
                if(n.length > 0){
                    sum += n.toInt;
                }
            }
        }
        println(sum);
    }
}