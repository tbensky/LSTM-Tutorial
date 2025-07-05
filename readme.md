# Training an LSTM on classical physics motion data

This is a tutorial on how to train an LSTM neural network on a large, complex set of time domain data. By "train an LSTM," we wish to see if an LSTM can produce a smooth curve going through each of many time-dependent parameters in the data file. 

## Summary

We have a data file of 3,156 lines. Each line is formatted as follows:

* The first column of each line is the time `(1,2,3, etc)`. The units are arbitrary but can be thought of as seconds if  needed.

* The rest of the 100 columns are 25 groups of 4 floating point values, which are `x,y,vx,vy` of a classical moving particle. In other words, the `(x,y)` position and x and y coordinates of the particle's speed.

In other words, each line captures a snapshot of the position and speed of 25 particles at a given time.  The advancing lines (and times), reflect subsequent snapshots of future times of this system.

Here are some plots of the x-coordinate of the 25 particles as a function of the first 100 time steps.


We'd like to see if a trained LSTM can render a smooth line through these data points.

![p0](https://github.com/tbensky/LSTM-Tutorial/blob/main/Plots/p0.png)
![p1](https://github.com/tbensky/LSTM-Tutorial/blob/main/Plots/p1.png)
![p2](https://github.com/tbensky/LSTM-Tutorial/blob/main/Plots/p2.png)
![p3](https://github.com/tbensky/LSTM-Tutorial/blob/main/Plots/p3.png)
![p4](https://github.com/tbensky/LSTM-Tutorial/blob/main/Plots/p4.png)
![p5](https://github.com/tbensky/LSTM-Tutorial/blob/main/Plots/p5.png)
![p6](https://github.com/tbensky/LSTM-Tutorial/blob/main/Plots/p6.png)
![p7](https://github.com/tbensky/LSTM-Tutorial/blob/main/Plots/p7.png)

Could a single LSTM produce smooth curves through all of these plots?

