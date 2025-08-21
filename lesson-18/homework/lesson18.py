import pandas as pd

df = pd.read_csv('tackoverflow_qa.csv')
df[df['creationdate'] < '2014-01-01']
df[df['score'] > 50]
df[df['score'].between(50, 100)]
df[df['ans_name'] == 'Scott Boston']
df[df['ans_name'].isin(['Demitri', 'doug', 'Mike Pennington', 'Scott Boston', 'David Underhill'])]
#df[(df['creationdate'].between('2014-03-01', '2014-10-31') & (df['ans_name']== 'Unutbu') & (df['score'] < 5))]

df[(df['score'].between(5, 10)) | 
   (df['viewcount'] > 10000)]

df[df['ans_name']!= 'Scott Boston']

tit = pd.read_csv('titanic.csv')

df0 = tit[(tit['Sex']== 'female')
    & (tit['Pclass']==1)
    & (tit['Age'].between(20, 30))
    
]

df1 = tit[
    tit['Fare']>100
]

tit[(tit['Survived']== 0)
    &(tit['Parch'] == 0)
    &(tit['SibSp'] == 0)
    
    ]

df2 = tit[(tit['Embarked']== 'S')
    &(tit['Fare'] >= 50)    
    ]

df3 = tit[(tit['Parch'] == 1)
    &(tit['SibSp'] == 1)
    
    ]

df4 = tit[(tit['Survived']== 1)
    &(tit['Age'] <= 15)
    
    ]

tit[(tit['Cabin'] != 'NaN')
    &(tit['Fare'] >= 200)    
    ]

df5 = tit[(tit['PassengerId'] % 2 == 1)
    ]

df6 = tit[(tit['Ticket'].duplicated(keep = False))
    ]

df7 = tit[(tit['Name'].str.contains('Miss'))
        &(tit['Pclass']== 1)
    ]
