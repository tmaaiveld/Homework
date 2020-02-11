epsilon_power <- function(x){
  results = c()
  for (n in x){
    result <- n^(1+runif(1))
    results = c(results,result)
  }
  return(results)
}

sumHarm <- function(t){
  result = 0
  results = c()
  for (n in t){
    result = result + (1/n) 
    results = c(results,result) 
  }
  return(results)
}

# This plot shows the sum series for 1/t, 1/t^2 and 1/t^(1+e) with epsilon sampled uniformly from range [0,1]. The curve represents the logarithmic series (log(t)).
par(mfrow=c(1,2))
plot(sumHarm(1:100), col='turquoise', xlab='t',ylab='f(t)')
points(sumHarm(epsilon_power(1:100)), col='skyblue')
points(sumHarm((1:100)^2), add=TRUE, col='skyblue4')
curve(log(x),add=TRUE)

sumHarm(1:100)/log(1:100)
# This plot shows the same function values, but proportional to log(t). These series appear convergent, which shows that the regret, which is approximated by the sum of the series of the selection probability of an action multiplied by its opportunity gap.

plot(sumHarm((1:100)^2)/log(1:100), col='skyblue4', xlab='t', ylab='f(t)/log(t)')
points(sumHarm(epsilon_power(1:100))/log(1:100), col='skyblue')
points(sumHarm(1:100)/log(1:100), add=TRUE, col='turquoise')

# Still unsure about interpretation... 
# The series are all lower bounded by a fixed factor of log(t). For larger t, there is some lower converged value 
# take another look at the slides to give a theoretical explanation maybe
