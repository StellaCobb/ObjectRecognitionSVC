"""
from PIL import Image
from numpy import asarray

num = int(1)
filenum = 0
img = "obj"+ str(num) + "_" + str(filenum)


for num in range (1, 3):
    for filenum in range (10):
        if filenum % 5 == 0:
            img = "obj"+ str(num) + "__" + str(filenum) + ".png"
            imgO = Image.open(str(img)+".png")
            numpydata = asarray(img)
            print(numpydata.shape)
            filenum += 5
    num += 1
"""
         
       
from PIL import Image
from numpy import asarray
from sklearn.model_selection import train_test_split

num = int(1)
filenum = 0


X = []
Y = []
for i in range (1, 6):
    for j in range (0, 356, 5):
        img = Image.open("obj"+ str(i) + "__" + str(j) + ".png")
        
        img_array = asarray(img)
        
        img_info = img_array.flatten()
        
        X.append(img_info)
        Y.append(i)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state = 42)
from sklearn.svm import SVC

clf = SVC(class_weight='balanced', random_state=42)

parameters = {'C': [0.1, 1, 10], 'gamma': [1e-07, 1e-08, 1e-06], 'kernel' : ['rbf', 'linear']}
from sklearn.model_selection import GridSearchCV
grid_search = GridSearchCV(clf, parameters, n_jobs = -1, cv = 5)

grid_search.fit(X_train, Y_train)



print('The best model:\n', grid_search.best_params_)

clf_best = grid_search.best_estimator
pred = clf_best.predict(X_test)

print(f'The accuracy is: {clf_best.score(X_test, Y_test)*100:.1f}%')

"""  
print(len(img_array))
print(img_array[0])
print(img_info)
"""