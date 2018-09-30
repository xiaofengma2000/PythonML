import numpy

from sklearn import datasets
from sklearn.model_selection import GridSearchCV, train_test_split, ShuffleSplit, KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import confusion_matrix, f1_score
from sklearn.base import clone
data = datasets.make_moons(n_samples=10000, noise=0.4, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(data[0], data[1], test_size=0.2, random_state=42)

grid = GridSearchCV(DecisionTreeClassifier(), {"max_leaf_nodes":[3,4,5,6,7]}, cv=5)
grid.fit(X_train, y_train)

rs = ShuffleSplit(n_splits=100, test_size=0.9, random_state=42)
scores = []
for index, (train_index, _) in enumerate(rs.split(X_train)):
    X_train_2 = [X_train[i] for i in train_index]
    y_train_2 = [y_train[i] for i in train_index]
    tree = clone(grid.best_estimator_) # DecisionTreeClassifier(max_leaf_nodes=4)
    tree.fit(X_train_2, y_train_2)
    scores.append(f1_score(y_test, tree.predict(X_test)))

print(numpy.mean(scores))
