\documentclass[12pt,a4paper]{article} % 使用标准 article 类
\setlength{\parindent}{0pt}
\usepackage{titlesec}
\titleformat{\section}[block]{\centering\Large\bfseries}{\thesection.}{1em}{}
\usepackage[utf8]{inputenc}  % 允许 utf8 编码（英文足够）
\usepackage[T1]{fontenc}     % 字体编码
\usepackage{multicol}
\usepackage{geometry}
\geometry{left=2.5cm, right=2.5cm, top=3cm, bottom=3cm}

\usepackage{titlesec}
\usepackage{hyperref}
\usepackage{graphicx}

\title{Report: ECG Signal Analysis and Privacy Preservation Based on Machine Learning}
\author{Group\_5} % 注意转义下划线
\date{\today}

\begin{document}

\maketitle
\tableofcontents
\newpage

\section{Data Collection and Labeling}

We used the following python program to generate a set of json files representing various data about the patient.

\begin{figure}[htbp]
    \centering
    \includegraphics[width=1\linewidth]{Code1.jpg}
    \label{fig:code1}
\end{figure}
Disclaimer: This data is dummy data, not related to any real data, and is only used to make a case presentation about machine learning.

\section{Data Analysis through Machine Learning}

In modern designs, deep learning models can further process raw signals or extracted features, while also leveraging the results of traditional machine learning models as a priori information. We use a chained workflow with the following workflow:

\begin{figure}[htbp]
    \centering
    \includegraphics[width=1\linewidth]{Chain.jpg}

\end{figure}

\begin{multicols}{2}
\subsection{Raw ECG Signal Input}
A 12-lead ECG signal sequence, with a sampling rate of e.g. 360 Hz, was input to the system.


\subsection{Signal Pre-processing Module}
Purpose: Improve signal quality for subsequent analysis

Filter denoising (low pass, high pass, band pass, wavelet noise reduction)
Baseline drift removal
Peak detection (Pan-Tompkins algorithm, etc. to identify R-waves)

\subsection{Traditional Feature Extraction Module}
Extract the above time domain, frequency domain, and morphological features
\vspace{1em}
Feature selection module
\vspace{1em}
Filter features using traditional machine learning methods (e.g., the following methods, with results used in subsequent models):
\vspace{1em}
Lasso Regression: for feature compression
\vspace{1em}
Random Forest: feature importance ranking
\vspace{1em}Mutual Information

\subsection{Machine Learning Models for Assisted Diagnosis}
Provide initial judgments with traditional models or “auxiliary labels” for deep learning
\vspace{1em}
SVM, Random Forest, KNN, etc. trained on extracted features
\vspace{1em}
Output predictive probabilities as additional input features to be used by subsequent neural networks

\subsection{Deep Learning Master Model}
Raw Signal + Feature Vector + Traditional Model Output ⇒ Composite Input Depth Model 
\vspace{1em}
The following model structure is selected based on the requirements:
\vspace{1em}
Model Purpose Description 1D-CNN Feature Learning Convolution is used to learn local patterns from ECG, e.g., QRS, ST-segment changes 
\vspace{1em}
Bi-LSTM Sequence Modeling Bi-directional LSTM captures time-dependence and is suitable for arrhythmia detection 
\vspace{1em}
CNN-LSTM Hybrid Models Fusion of local + global information CNN first extracts local morphological features, LSTM models long-term dependencies
\vspace{1em}
Transformer Advanced sequence modeling Understand ECG sequence changes with attention mechanism, sensitive to complex rhythm abnormalities
\vspace{1em}
✨ Technique:
\vspace{1em}
Splicing traditional features into the input of a layer of the neural network (e.g., before Transformer Encoder)
\vspace{1em}
Or add a layer of Random Forest after the output of the deep learning model for “secondary discrimination”.

\subsection{Post-Processing and Interpretation Module}
	- Explaining why a neural network determines certain types of anomalies using methods such as Grad-CAM, SHAP, LIME, etc.
	- Label the location of the anomaly (e.g., a heartbeat segment)

\subsection{Deployment Module}
	- Outputs disease type or probability of abnormality
	- Can be deployed in cloud services, wearable devices or hospital systems

\end{multicols}

\section{Privacy Protection}
Since ECG data is highly sensitive health information, data privacy protection is critical. The following measures can be taken:
\begin{multicols}{2}
\subsection{De-identification}
Remove all identifiable information (e.g., name, ID, date of birth, location, etc.) prior to data collection and sharing.\par
\vspace{1em}
Use pseudo-anonymized IDs instead of the user's real identity.

\subsection{Encryption}
Use TLS/SSL for end-to-end encryption during data transmission (e.g., ECG device upload to the cloud).
\par
\vspace{1em}
Use strong encryption algorithms such as AES to protect data during storage.

\subsection{Federated Learning}
Data is kept local to the user and models are trained on local devices.
\par
\vspace{1em}
Only model weight updates are uploaded, not raw data, thus protecting user privacy.

\subsection{Differential Privacy}
Adds noise to training data or model output to prevent back extrapolation of original user data.
\par
\vspace{1em}
Can be used to share models without revealing individual patient characteristics.

\subsection{Access Control and Auditing}
Strictly limit data access to authorized medical personnel or algorithm developers.
\par
\vspace{1em}
Regularly log and audit data access records to prevent data misuse.

\subsection{Compliance with Regulations}
Comply with international/regional privacy laws such as the General Data Protection Regulation (GDPR) or the Health Insurance Portability and Accountability Act (HIPAA).
\par
\vspace{1em}
Collect data through ethics committee approval and informed consent (Informed Consent) of users.
\end{multicols}

\section{appendice}
\begin{multicols}{2}
    

\subsection*{2.1's Representation and visualization in mechanical learning}

\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.1\linewidth]{Code2.1.jpg}
    \label{fig:code1}
\end{figure}

\subsection*{2.2's Representation and visualization in mechanical learning}
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\linewidth]{Code2.1.jpg}
    \label{fig:code2}
\end{figure}

\subsection*{2.3's Representation and visualization in mechanical learning}
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\linewidth]{Code2.1.jpg}
    \label{fig:code3}
\end{figure}

\subsection*{2.4's Representation and visualization in mechanical learning}
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\linewidth]{Code2.1.jpg}
    \label{fig:code4}
\end{figure}

\subsection*{2.5's Representation and visualization in mechanical learning}
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\linewidth]{Code2.1.jpg}
    \label{fig:code5}
\end{figure}

\subsection*{2.6's Representation and visualization in mechanical learning}
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\linewidth]{Code2.1.jpg}
    \label{fig:code6}
\end{figure}

\subsection*{2.7's Representation and visualization in mechanical learning}
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.1\linewidth]{Code2.1.jpg}
    \label{fig:code7}
\end{figure}

\end{multicols}
\end{document}