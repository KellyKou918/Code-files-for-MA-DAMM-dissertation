import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Confusion matrix data
confusion_matrix = np.array([[65353, 12727],
                             [16490, 61352]])

# Calculate total counts for each true label
total_counts = np.sum(confusion_matrix, axis=1)

# Define class labels
class_labels = ['Positive', 'Negative']

# Define class abbreviations with names
class_abbreviations = ['True Positive (TP)', 'False Negative (FN)', 'False Positive (FP)', 'True Negative (TN)']

# Calculate percentages and format the annotation strings
percentage_matrix = (confusion_matrix / total_counts[:, np.newaxis]) * 100
annotation_strings = []
for i in range(len(class_labels)):
    for j in range(len(class_labels)):
        annotation_strings.append(f"{confusion_matrix[i][j]}\n{percentage_matrix[i][j]:.1f}%\n{class_abbreviations[i * len(class_labels) + j]}")

# Create a heatmap
plt.figure(figsize=(8, 6))
heatmap = sns.heatmap(confusion_matrix, annot=np.array(annotation_strings).reshape(2, 2), fmt='', cmap='Blues', cbar=False)
plt.title('Confusion Matrix with Percentages and Abbreviations')
plt.xticks(ticks=[0.5, 1.5], labels=class_labels)
plt.yticks(ticks=[0.5, 1.5], labels=class_labels)
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()
