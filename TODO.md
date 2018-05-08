# TODO list

## Clone a copy

The command below should allow you to clone a copy of the repo.

git clone https://github.com/ethanlee515/animerec

I'll give you push/edit privilege later if/when you create a github account.
Or just get your code to me in a .zip or .tar.gz, it's whatever.

## Familiarize yourself

We're working on animelist.py at the moment. Skim through it.
It's the web crawler. Try running it using a username as the command line argument
(python3 animelist.py ethan515). It should print out a vector.
The keys are supposed to be integers. They're anime IDs.

## Z-Scores

Now normalize the scores by returning z-scores in makeVec instead of raw scores.
Some functions that might help you are numpy.std, numpy.mean, and numpy.asarray.

## Data set collection

Start collecting data after that! The actual implementation is up to you.
Just ensure good robot citizenship. We don't want to launch DoS attacks or get banned.

I would recommend doing it on a separate python script and call the userToVec function.
But do whatever works best for you.
