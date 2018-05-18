## Evaluation of code

We use the ratings of a given MyAnimeList account to evaluate the success of the algorithm.
We do this by predicting the rating of series already watched and rated by the user, to see
if the algorithm is able to successfully align with the user's tastes.

## Test results 1

Username: Gaburiru

Test results for a random list of IDs of series watched by the user are as follows:

* Test 1
Input:
`./animerec.py Gaburiru 11757`
- Output:
`You've given it a rating of 7. Now let's pretend you haven't watched it...
Predicted rating: 7.42`

* Test 2
Input:
`./animerec.py Gaburiru 19429`
Output:
`You've given it a rating of 5. Now let's pretend you haven't watched it...
Predicted rating: 6.64`

* Test 3
Input:
`./animerec.py Gaburiru 18247`
Output:
`You've given it a rating of 8. Now let's pretend you haven't watched it...
Unpopular series; take prediction with a grain of salt.
Predicted rating: 7.67`

* Test 4
Input:
`./animerec.py Gaburiru 10620`
`Output:
You've given it a rating of 9. Now let's pretend you haven't watched it...
Predicted rating: 6.9`

* Test 5
Input:
`./animerec.py Gaburiru 33834`
Output:
`You've given it a rating of 3. Now let's pretend you haven't watched it...
Unpopular series; take prediction with a grain of salt.
Predicted rating: 4.89`

* Test 6
Input:
`./animerec.py Gaburiru 21881`
Output:
`You've given it a rating of 8. Now let's pretend you haven't watched it...
Predicted rating: 6.65`

* Test 7
Input:
`./animerec.py Gaburiru 6213`
Output:
`You've given it a rating of 7. Now let's pretend you haven't watched it...
Unpopular series; take prediction with a grain of salt.
Predicted rating: 7.57`

* Test 8
Input:
`./animerec.py Gaburiru 15583`
Output:
`You've given it a rating of 6. Now let's pretend you haven't watched it...
Predicted rating: 7.5`

* Test 9
Input:
`./animerec.py Gaburiru 32526`
Output:
`You've given it a rating of 7. Now let's pretend you haven't watched it...
Unpopular series; take prediction with a grain of salt.
Predicted rating: 7.25`

* Test 10
Input:
`./animerec.py Gaburiru 9041`
Output:
`You've given it a rating of 8. Now let's pretend you haven't watched it...
Predicted rating: 6.32`

## Test results 2

Username: ethan515

Test results for a random list of IDs of series watched by the user are as follows:

* Test 1
Input:
`./animerec.py ethan515 4224`
Output:
`You've given it a rating of 10. Now let's pretend you haven't watched it...
Predicted rating: 7.14`

* Test 2
Input:
`./animerec.py ethan515 18671`
Output:
`You've given it a rating of 9. Now let's pretend you haven't watched it...
Predicted rating: 7.61`

* Test 3
Input:
`./animerec.py ethan515 30276`
Output:
`You've given it a rating of 2. Now let's pretend you haven't watched it...
Predicted rating: 8.5`

* Test 4
Input:
`./animerec.py ethan515 14813`
Output:
`You've given it a rating of 5. Now let's pretend you haven't watched it...
Predicted rating: 7.72`

* Test 5
Input:
`./animerec.py ethan515 23273`
Output:
`You've given it a rating of 7. Now let's pretend you haven't watched it...
Predicted rating: 9.54`

* Test 6
Input:
`./animerec.py ethan515 11499`
Output:
`You've given it a rating of 7. Now let's pretend you haven't watched it...
Unpopular series; take prediction with a grain of salt.
Predicted rating: 5.74`

* Test 7
Input:
`./animerec.py ethan515 2924`
Output:
`You've given it a rating of 9. Now let's pretend you haven't watched it...
Unpopular series; take prediction with a grain of salt.
Predicted rating: 6.77`

* Test 8
Input:
`./animerec.py ethan515 15809`
Output:
`You've given it a rating of 5. Now let's pretend you haven't watched it...
Predicted rating: 7.13`

* Test 9
Input:
`./animerec.py ethan515 1575`
Output:
`You've given it a rating of 8. Now let's pretend you haven't watched it...
Predicted rating: 9.13`

* Test 10
Input:
`./animerec.py ethan515 21881`
Output:
`You've given it a rating of 8. Now let's pretend you haven't watched it...
Predicted rating: 6.53`

## Summary of results

For user Gaburiru, 9 out of 10 predicted ratings were within 2 of their actual rating.
For user ethan515, 4 out of 10 predicted ratings were within 2 of their actual rating.
This discrepancy may be due to the number of series rated by each user:
Gaburiru has rated 71 series, while ethan515 has rated 38 series.
Having more rated series helps the algorithm to find better matches for the target user,
which in turn increases the accuracy of the prediction.
Additionally, the number of "unpopular" series (not watched by at least 10 neighbors) differs as a result:
4 "unpopular" series were found for Gaburiru, while 2 "unpopular" series were found for ethan515.
As Gaburiru has rated significantly more series, the proportion of unpopular series thus
is also likely to increase as a result.
