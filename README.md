# Animerec

## Authors

- Wai-Kin Tsui
- Ethan (Yi) Lee

## How to run

* `./animerec.py <username>` Prints the top five recommendations for a user.
* `./animerec.py <username> <series_ID>`
Predicts the rating a given user would give to a series.
The series ID is the number in the URL of the MyAnimeList page for the series.
This could be used for evaluation purposes.

## Abstract

For our final project, we plan to set up a recommendation system for anime television series based on
the watch history of users who share similar tastes to the target user. If time permits, we will also allow
additional features such as an option for people to choose recommendations either from all users or
only users who have watched a similar number of series, multiple target users in case people might
want to look for recommendations for series to watch with friends, and genre filters that will allow
people to find recommendations of a certain type.

## Algorithm

In order to achieve this, we will utilize a vector-based search model. Each user is represented as a
vector, and each series they have watched is represented as a component of their vector, with the value
of the component being the rating they gave for that series. We will retrieve user ratings from
Myanimelist.net. The generation of recommendations will be done by finding the user vectors that are
closest neighbors to the target vector, and then predicting the rating that the target user might give to
series they haven’t watched based on the (normalized) average rating given by those neighbors to those series.
The method of calculating similarity will be dot-product, as it is not sensitive to the norm of the
vector, which represents the number of series a user has watched.

Docstrings are available describing every source file.

## Evaluation

We will evaluate the success of the project by repeatedly picking a random target user, removing one of
their watched series’ ratings, and then predicting their rating using the algorithm outlined above. We
will then compare the predicted rating and the actual rating. Please see RESULTS.md for the result.

## Assessment of risk

We are planning on crawling user profiles on Myanimelist.net, which are not forbidden from being
crawled by the website’s robots.txt file. We will aim to extract approximately 5000 profiles over 4 days,
which would be equivalent to roughly 50 profiles per hour, or less than one user per minute on average,
which is comparable to, if not slower than, what a human would be expected to be able to do. We will
access the website once every 10 minutes, each time extracting at most 20 profiles.

## Future Directions

It might be nice to explore something in the spirit of IDF-weighing.
That is, possibly assign popular series lower weights for the closest-neighbors
algorithm and see if it improves the evaluation.
