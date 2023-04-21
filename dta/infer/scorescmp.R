#!/usr/bin/R -f

accs <- read.table( "scorescmp.csv", header=TRUE, sep="," )
cor.test( accs[[ "acc2gold" ]], accs[[ "acc2bsl" ]], method="pearson", alternative="two.sided" )
cor.test( accs[[ "acc2gold" ]], accs[[ "acc2bsl" ]], method="kendall", alternative="two.sided" )

