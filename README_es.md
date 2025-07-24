Question:
An electrocardiogram (ECG) records the electrical signals in the heart. 
It's a common and painless test used in clinics to quickly detect heart problems and monitor the heart's health.
(1) Discuss how to design a machine learning-based system to automatically detect heart problems,
 including data acquisition, labelling, feature selection, classifier training and testing.
(2) Discuss how to preserve data privacy in designing the above system.

Information source: 
Spurious data generated using GetData.py.


Chained workflows:

Raw ECG signal →
  → Signal pre-processing →
    → feature extraction →
      → feature selection →[Traditional ML auxiliary classification]
                        ↘  
 original signal + Selected Features + secondary label → depth model（CNN/LSTM/Transformer）→ Projected results
                                                             ↘
                                                    Post-processing and Interpretability Module