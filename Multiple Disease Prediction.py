{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "58752441",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle\n",
    "import streamlit as st\n",
    "from streamlit_option_menu import option_menu\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "def24e89",
   "metadata": {
    "scrolled": True
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/manavgora/anaconda3/lib/python3.10/site-packages/sklearn/base.py:299: UserWarning: Trying to unpickle estimator LogisticRegression from version 1.0.2 when using version 1.2.1. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:\n",
      "https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations\n",
      "  warnings.warn(\n",
      "/Users/manavgora/anaconda3/lib/python3.10/site-packages/sklearn/base.py:299: UserWarning: Trying to unpickle estimator SVC from version 1.0.2 when using version 1.2.1. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:\n",
      "https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations\n",
      "  warnings.warn(\n"
     ]
    }
   ],
   "source": [
    "# loading the saved model\n",
    "\n",
    "# loading the saved models using binary mode 'rb'\n",
    "with open('Diabetes_model.sav', 'rb') as file:\n",
    "    diabetes_model = pickle.load(file)\n",
    "\n",
    "with open('heart_disease_model.sav', 'rb') as file:\n",
    "    heart_disease_model = pickle.load(file)\n",
    "\n",
    "with open('parkinsons_model.sav', 'rb') as file:\n",
    "    parkinsons_model = pickle.load(file)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "898a94d5",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-02-29 12:14:05.182 WARNING streamlit.runtime.state.session_state_proxy: Session state does not function when running a script without `streamlit run`\n",
      "2024-02-29 12:14:05.265 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /Users/manavgora/anaconda3/lib/python3.10/site-packages/ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "# sidebar for navigate\n",
    "\n",
    "with st.sidebar:\n",
    "    \n",
    "    selected = option_menu('Multiple Disease Prediction System',\n",
    "                          ['Diabetes Prediction',\n",
    "                          'Heart Disease Prediction',\n",
    "                          'Parkinsons Prediction'],\n",
    "                          default_index = 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "c9330bb3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "c81b4c18",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "b2428c1e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "74360527",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "cc235244",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "4d647d63",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "eaeb87e1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "cc2a24cc",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "ef937d8d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "47c7b91f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "bb2ee814",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "0a0f8a7a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "017a057d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "9e29a7ed",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "23833b4a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "a55f297d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "b21339fa",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "0058b7b2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "a680d8a5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "07f06a5e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
