# **Problem 4 – Spam Detection Using Artificial Immune Systems (AIS) - Negative Selection Algorithm(NSA)**

## **Overview**
This project applies an Artificial Immune System approach—specifically the Negative Selection Algorithm (NSA)—to the SMS Spam Collection v1 dataset.
The NSA model learns the structure of normal (ham) SMS messages and identifies spam as anomalies based on detector matches.

The workflow includes:
* text cleaning
* char-level TF-IDF vectorization
* binarization
* NSA detector generation
* hyperparameter tuning and evaluation

The SMS Spam Collection v1 contains 5,574 English SMS messages, each labeled as either ham (legitimate) or spam.


## **Data Source**
Spam Collection Original dataset can be found at: <br/>
[https://archive.ics.uci.edu/dataset/228/sms+spam+collection](https://archive.ics.uci.edu/dataset/228/sms+spam+collection)


## Repository:
Project_4 <br/>
   ├── README <br/>
   ├── data <br/>
   │   ├── readme <br/>
   │   └── SMSSpamCollection <br/>
   ├── models <br/>
   │   └──tfidf_vectorizer <br/>
   ├── notebook <br/>
   └── report_reference <br/>

## Requirements:
* Python 3.8+
* Libraries:
    * numpy, pandas, matplotlib, seaborn
    * ipython (for display styling)

Install(local):
```sh
pip install numpy pandas matplotlib seaborn
```

## **Implementation Details**




## **Quick start**
1. Ensure the SMS Spam Collection data are placed in: `Project_4/data/`
2. Open the notebook: `NSA_SMS_SpamDetection.ipynb`
3. Run all cells from top to bottom.  <br/>


## **Parameters:**
* **Dataset**
    - Source file: `SMSSpamCollection` (SMS Spam Collection)
    - Encoding: `ham = 0`, `spam = 1`

* **Data split**
    - Train (ham only): 60% of ham  →  2 895 messages
    - Validation: 965 ham + 373 spam
    - Test:       965 ham + 374 spam

* **Vectorizer (final) – char-level TF-IDF**
    - analyzer    = "char_wb"
    - ngram_range = (3, 5)
    - max_df      = 0.95
    - min_df      = 2
    - sublinear_tf = True

* **Binarization**
    - τ (tau) = 0.01

* **NSA detector model (final)**
    - k             = 30      (active bits per detector)
    - r_min         = 1
    - r_max         = 3
    - max_detectors = 5000
    - max_tries     = 100000
    - batch_size    = 1000
    - sampling      = "antiprofile"
    - random_state  = 42
    - k_hits        = 1       (decision threshold)



