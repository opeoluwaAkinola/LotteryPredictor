from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import LSTM,Dense,Bidirectional,Dropout
import numpy as np
import pandas as pd
import tensorflow
from datetime import datetime, timedelta

class predict:
    def __init__(self,documents,number_of_balls):
        self.docum=documents
        self.numbe=number_of_balls

    def return_prediction(self):
        documents=self.docum
        number_of_balls=self.numbe
        scaler = StandardScaler().fit(documents.values)
        transformed_dataset = scaler.transform(documents.values)
        transformed_df = pd.DataFrame(data=transformed_dataset, index=documents.index)
        number_of_rows = documents.values.shape[0]
        window_length = 4
        number_of_features = documents.values.shape[1]
        train = np.empty([number_of_rows - window_length, window_length, number_of_features], dtype=float)
        label = np.empty([number_of_rows - window_length, number_of_features], dtype=float)
        window_length = 4
        for i in range(0, number_of_rows - window_length):
            train[i] = transformed_df.iloc[i:i + window_length, 0:number_of_features]
            label[i] = transformed_df.iloc[i + window_length:i + window_length + 1, 0:number_of_features]

        batchsize = len(documents)
        model = Sequential()
        model.add(Bidirectional(LSTM(240, input_shape=(window_length, number_of_features), return_sequences=True)))
        model.add(Dropout(0.2))
        model.add(Bidirectional(LSTM(240, input_shape=(window_length, number_of_features), return_sequences=True)))
        model.add(Dropout(0.2))
        model.add(Bidirectional(LSTM(240, input_shape=(window_length, number_of_features), return_sequences=True)))
        model.add(Dropout(0.2))
        model.add(Bidirectional(LSTM(240, input_shape=(window_length, number_of_features), return_sequences=True)))
        model.add(Dropout(0.2))
        model.add(Bidirectional(LSTM(240, input_shape=(window_length, number_of_features), return_sequences=False)))
        model.add(Dense(number_of_balls))
        model.add(Dense(number_of_features))
        model.compile(loss="mse", optimizer="rmsprop", metrics=["accuracy"])
        model.fit(train, label, batch_size=batchsize, epochs=11)

        rows_list = []
        for index, rows in documents.iterrows():
            if index > len(documents) - 4:
                if number_of_balls == 59:
                    my_list = [rows["n-1"], rows["n_2"], rows["n_3"], rows["n_4"], rows["n_5"]]
                elif number_of_balls == 11:
                    my_list = [rows["n_star_1"], rows["n_start_2"]]
                rows_list.append(my_list)
        to_predict = np.array(rows_list)
        scaled_to_predict = scaler.transform(to_predict)
        scaled_predicted_output_1 = model.predict(np.array([scaled_to_predict]))
        return scaler.inverse_transform(scaled_predicted_output_1).astype(int)[0]
