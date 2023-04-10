import streamlit as st
import pandas as pd
import joblib


model = joblib.load('laptop_model.joblib')

ram_types = ['DDR4', 'DDR5', 'LPDDR3', 'LPDDR4',
             'LPDDR4X', 'LPDDR5', 'Unified Memory']
ram_types_encoded = list(range(len(ram_types)))

processor_options = ['Intel Celeron Dual Core Processor', 'Intel Celeron Quad Core Processor', 'Intel Pentium Dual Core Processor',                     'Intel Pentium Quad Core Processor', 'Intel Pentium Silver Processor', 'Intel Core i3 Processor', 'Intel Core i5 Processor',                     'Intel Core i7 Processor',
                     'Intel Core i9 Processor', 'AMD Ryzen 3 Dual Processor', 'AMD Ryzen 3 Quad Processor',                     'AMD Ryzen 3 Hexa Core Processor', 'AMD Ryzen 5 Dual Processor', 'AMD Ryzen 5 Quad Processor', 'AMD Ryzen 7 Octa Processor',                     'AMD Ryzen 7 Quad Processor', 'AMD Ryzen 9 Octa Processor', 'Athlon Dual Core', 'Apple Silicon']
processor_options_encoded = list(range(len(processor_options)))

storage_options = ['1 TB HDD', '1 TB HDD & 256 GB SSD', '1 TB HDD512 GB SSD', '128 GB SSD',
                   '256 GB HDD & 256 GB SSD', '256 GB SSD',                   '512 GB SSD', '1 TB SSD', '2 TB SSD']
storage_options_encoded = list(range(len(storage_options)))

os_options = ['MAC', 'Windows']
os_options_encoded = list(range(len(os_options)))

brand_options = ['Lenovo', 'ASUS', 'HP', 'DELL', 'RedmiBook', 'Realme', 'Acer', 'MSI', 'Apple',
                 'Infinix', 'Samsung', 'Vaio',                 'GIGABYTE', 'Nokia', 'Ultimus', 'AlienWare']
brand_options_encoded = list(range(len(brand_options)))


def main():

    st.title('Laptop Price Predictor')
    st.write('Enter the specifications of the laptop to get a price prediction:')

    rating = st.slider('Rating (out of 5)', 0.0, 5.0, 4.0, 0.1)
    ram = st.selectbox('RAM Size', ['4', '8', '16', '32'], index=1)
    ram_type = st.selectbox('RAM Type', ram_types, index=0)
    ram_type_encoded = ram_types_encoded[ram_types.index(ram_type)]
    processor = st.selectbox('Processor', processor_options, index=0)
    processor_encoded = processor_options_encoded[processor_options.index(processor)]
    storage = st.selectbox('Storage', storage_options, index=0)
    storage_encoded = storage_options_encoded[storage_options.index(storage)]
    os = st.selectbox('OS', os_options, index=0)
    os_encoded = os_options_encoded[os_options.index(os)]
    brand = st.selectbox('Brand', brand_options, index=0)
    brand_encoded = brand_options_encoded[brand_options.index(brand)]

    if st.button('Predict'):
        new_data = pd.DataFrame({'Rating': [rating], 'RAM Size': [
            ram], 'RAM_Type_Encoded': [ram_type_encoded], 'Processor_Type_Encoded': [processor_encoded], 'Storage_Encoded': [storage_encoded],
            'OS_Encoded': [os_encoded], 'Brand_Encoded': [brand_encoded]})

        prediction = model.predict(new_data)
        st.write(f'Estimated price: ${prediction[0]:,.2f}')


if __name__ == '__main__':
    main()
