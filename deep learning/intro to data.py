from sklearn import tree


# [height , weight , shoe size]

x = [[180,80,43], [175 , 78 , 44], [190 , 80 ,44], [165 , 55 ,39], [155 , 45 , 38], [170, 56 , 39]]

y = ['male' ,'male' , 'male' , 'female' , 'female', 'female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(x,y)

prediction = clf.predict([[178, 51 ,41]])

print(prediction)