from scipy import stats
import collections

#Load the data into a pandas, clean it
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)



#Write a script called "chi_squared.py" that loads the data, cleans it, performs the chi-squared test, and prints the result. Push your code to Github and enter the link below.