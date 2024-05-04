# Active Learning Optimization of sEMG Data for Robust Gesture Recognition

## Team Members
- Mercury Liu
- Yuxin Lu
- Howard Wu
- Yixuan Yin

## Introduction
Our project is focused on the robust decomposition and interpretation of surface electromyography (sEMG) signals from hand and forearm muscles. By integrating active learning strategies, we aim to enhance model performance while reducing computational demands. This approach also allows us to identify key signal characteristics with higher certainty, thus improving the accuracy of gesture recognition systems.

## Project Goals
- **Identify the optimal machine learning model** for decomposing sEMG signals effectively.
- **Optimize computational efficiency** using active learning strategies without sacrificing model accuracy.
- **Traceback data characteristics** that enhance the understanding of sEMG signals.

## Background
Traumatic injuries and conditions like SCIs can impair nerve signal transmission, affecting muscle control and movement. Our project utilizes advanced machine learning techniques and active learning to interpret sEMG data, enabling gesture recognition systems to better support individuals with hand paralysis.

## Installation
Clone the repository and install the required packages:
```bash
git clone https://github.com/yuxinl915/ASR_group_proj.git
cd ASR_group_proj
conda env create -n myEnv -f env.yaml
conda activate myEnv
```

## To Run the Code
data_analysis_main.ipynb contains the implementations of feature processing, model selection, all active learning strategies.

backtrace.ipynb contains the explorations of the selected points' characteristics.



