f  <- function(x) dnorm(x,0,1)
g  <- function(x) dnorm(x,mean=1,sd=2)
KL <- function(smp,p,q) mean(log(p(x)/q(x)))

x = rnorm(1000,0,1)
KL(x,p,q)