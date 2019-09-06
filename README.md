# Animerec

## Authors

- Wai-Kin Tsui
- Ethan (Yi) Lee

## How to run

* `./animerec.py <username>` prints the top five recommendations for a user.
* `./animerec.py <username> <series_ID>` predicts the rating a given user would give to a series.
The series ID is the number in the URL of the MyAnimeList page for the series.
This may be used for evaluation purposes.

***If this stops working, chances are myanimelist.net may have changed their website format.
When that happens, unfortunately this repository is no longer actively maintained.***

## Abstract

For our final project, we plan to set up a recommendation system for anime television series based on
the watch histories of users who share similar tastes to the target user.

## Algorithm

In order to achieve this, we will utilize a vector-based search model. Each user is represented as a
vector, and each series they have watched is represented as a component of their vector, with the value
of the component being the rating they gave for that series. We will retrieve user ratings from
Myanimelist.net. The generation of recommendations will be done by finding the user vectors that are
closest neighbors to the target vector, and then predicting the rating that the target user might give to
series they haven’t watched based on the (normalized) average rating given by those neighbors to those series.
The method of calculating similarity will be dot-product, as it is not sensitive to the norm of the
vector, which represents the number of series a user has watched.

Additionally, for predicted ratings, we will implement a critical popularity feature that checks to see
how many of the neighboring users have watched the given series. If the number of neighbors that have
watched the series is below 10, this might cause the predicted rating to be less accurate, as there is
less data from which to calculate the predicted rating. As a result, the program will output a warning
that tells the user that the series is comparatively unpopular, and that those results should be taken
into context.

Docstrings are available to describe the functions of each source file.

## Evaluation

We will evaluate the success of the project by repeatedly picking a random target user, removing one of
their watched series’ ratings, and then predicting their rating using the algorithm outlined above. We
will then compare the predicted rating and the actual rating. Please see RESULTS.md for the results.

## Assessment of risk

We are planning on crawling user profiles on Myanimelist.net, which are not forbidden from being
crawled by the website’s robots.txt file. We will aim to extract approximately 5000 profiles over 4 days,
which would be equivalent to roughly 50 profiles per hour, or less than one user per minute on average,
which is comparable to, if not slower than, what a human would be expected to be able to do. We will
access the website once every 10 minutes, each time extracting at most 20 profiles.

## Future Directions

If time permits, we could explore something similar to IDF-weighting. This could be done by
assigning popular series lower weights for the closest-neighbors algorithm to see if it improves the evaluation.
We could also explore additional options for people to choose recommendations either from all users or
only users who have watched a similar number of series, multiple target users in case people might
want to look for recommendations for series to watch with friends, or genre filters that will allow
people to find recommendations of a certain type.
