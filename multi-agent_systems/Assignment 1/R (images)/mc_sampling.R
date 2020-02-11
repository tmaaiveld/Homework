library(tidyverse)

# 1.1.1

x = rnorm(1000)     # sample 1000 points
x = (cos(x))^2      # compute cos(x)*cos(x)
x_avg = mean(x)     # compute the mean
x_avg
var(x)

k = 1000
avgs = rep(0,k)
n = 1000

for (i in 1:k){
  x = rnorm(n)     # sample 1000 points
  x = (cos(x))^2      # compute cos(x)*cos(x)
  avgs[i] = mean(x)
}

var(avgs)
var(x)/n

  
# 1.1.2

r = 0.3; n = 10
t = (r / sqrt(1-r^2)) * sqrt(n-2)
2*pt(t, n-2, lower=FALSE)

t_tab = c(Inf,Inf,
          12.706,4.303,3.182,2.776,
          2.571,2.447,2.365,2.306,
          2.263,2.228,2.201,2.179) 

r = t_tab/sqrt(n-2+t_tab^2)

par(mfrow=c(1,1))
plot(3:length(r), r[3:length(r)], xlab="n",ylab="minimum r")
text(3:length(r), r[3:length(r)], labels=t_tab[-c(1,2)], cex= 0.7, pos=4)
# Plot showing the minimum r required to reject $H_0$ for $\alpha = 0.05$. Different sample counts (training cycles)
# are plotted along the x-axis, while the number label indicates the critical value for the corresponding degrees of freedom
# (n-2).

tibble(N = 1:14,hey = r) %>%
  as_tibble(cbind(nms = names(.), t(.)))