
import pandas as pd

def main():
    DataSet = pd.read_csv("StarbucksSatisfactorySurvey.csv")
    DataSet.shape
    DataSet['3. Are you currently....?'].value_counts(normalize=True)
    DataSet['10. What do you most frequently purchase at Starbucks?'].value_counts(normalize=True)
    DataSet['1. Your Gender'].value_counts(normalize=True)
    DataSet['5. How often do you visit Starbucks?'].value_counts(normalize=True)
    DataSet['14. How important are sales and promotions in your purchase decision?'].value_counts(normalize=True)
    
    DataSet['3. Are you currently....?'].value_counts().plot(kind="pie")
    DataSet['10. What do you most frequently purchase at Starbucks?'].value_counts().plot(kind="line")
    DataSet['1. Your Gender'].value_counts().plot(kind="bar")
    DataSet['5. How often do you visit Starbucks?'].value_counts().plot(kind="pie")
    DataSet['14. How important are sales and promotions in your purchase decision?'].value_counts().plot(kind="pie")
    
    Choice_Coffee = DataSet[DataSet['10. What do you most frequently purchase at Starbucks?'] == 'Coffee']
    Premotion_Choice = DataSet[DataSet['14. How important are sales and promotions in your purchase decision?'] == 'Rarely']
    Frequency = DataSet[DataSet['5. How often do you visit Starbucks?'] == 'Weekly']
    Current_Position = DataSet[DataSet['3. Are you currently....?'] == 'Student']
    
    print(DataSet.count('Coffee'),
          DataSet.count('Rarely'),
          DataSet.count('Weekly'),
          DataSet.count('Student'))
    
    print(Sum(Choice_Coffee),
          Sum(Premotion_Choice),
          Sum(Frequency),
          Sum(Current_Position)
          )
    
    print(Choice_Coffee.mean,
          Choice_Coffee.median,
          Premotion_Choice.mean,
          Premotion_Choice.median,
          Frequency.mean,
          Frequency.median,
          Current_Position.mean,
          Current_Position.median
          )

if __name__ == "__main__":
    main()