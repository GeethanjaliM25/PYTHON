import matplotlib.pyplot as plt
study_hours=[2,4,5,6,8,10]
exam_scores=[60,65,75,80,90,95]
plt.scatter(study_hours,exam_scores,color='blue',marker='o',label='students')
plt.xlabel('study hours')
plt.ylabel('exam scores')
plt.title('scatter plot of study hours vs exam scores')
plt.legend()
plt.show()