# 1.2.1

n = 100
x = runif(n,-5,5)
y = dnorm(x,0,1)

par(mfrow=c(1,2))
plot(x,y, main="mapping uniform X to N(0,1)")
plot(x^2,y, main="Chi-square distribution of X^2")

p = rnorm(10000)
q = dnorm(p)
plot(p,q)

# Importance sampling:
n = 500; a = -5; b = 5; mu = 0; sigma = 1
x = runif(n,a,b)

phi <- function(x) x^2
f   <- function(x) dnorm(x,mu,sigma)
g   <- function(x) 1/(b-a) 

imp_samples = phi(x) * f(x)/g(x)
mean(imp_samples)
max(imp_samples)
plot(x,imp_samples, main="U(-5,5) to X^2 for X ~ N(0,1)")

# 1.2.2
par(mfrow=c(1,1))
curve(f(x), xlim=c(-1,1))

n = 500; a = -1; b = 1
x = runif(n,a,b)

phi <- function(x) x^2
f   <- function(x) (1 + cos(pi*x))/2
g   <- function(x) 1/(b-a)

imp_samples = phi(x) * f(x)/g(x)
plot(x,imp_samples,main="U(-1,1) to X^2 for X ~ p_f(x)")

mean(imp_samples)
var(imp_samples)/n
  