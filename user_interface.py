import streamlit as st
import pandas as pd
import plotly.express as px
from optimization.optimizer import Optimizer
from ai.demand_forcasting import DemandForecasting
from ai.anomaly_detection import anomaly_detection
from ai.route_optimization import route_optimization


def main():
    st.set_page_config(page_title='NextGen Supply Chain Optimizer', layout='wide')

    # Custom CSS styling
    st.markdown("""
        <style>
        .title {
            font-size: 48px;
            font-weight: bold;
            color: #1f77b4;
            text-align: center;
            margin-bottom: 30px;
        }
        .header {
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 20px;
        }
        .upload-button {
            background-color: #1f77b4;
            color: white;
            font-weight: bold;
            padding: 10px 20px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        .optimize-button {
            background-color: #27ae60;
            color: white;
            font-weight: bold;
            padding: 10px 20px;
            border-radius: 5px;
            margin-top: 30px;
        }
        .results-container {
            background-color: #f2f2f2;
            padding: 20px;
            border-radius: 5px;
            margin-top: 30px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">NextGen Supply Chain Optimizer</div>', unsafe_allow_html=True)

    # Upload data files
    st.markdown('<div class="header">Upload Data</div>', unsafe_allow_html=True)
    inventory_data = upload_data('Inventory Data')
    products_data = upload_data('Products Data')
    suppliers_data = upload_data('Suppliers Data')
    transportation_data = upload_data('Transportation Data')
    orders_data = upload_data('Orders Data')
    external_data = upload_data('External Data')

    # AI-powered demand forecasting
    st.markdown('<div class="header">AI-Powered Demand Forecasting</div>', unsafe_allow_html=True)
    demand_forecast = demand_forecasting(orders_data, external_data)
    st.dataframe(demand_forecast)

    # AI-powered anomaly detection
    st.markdown('<div class="header">AI-Powered Anomaly Detection</div>', unsafe_allow_html=True)
    anomalies = anomaly_detection(inventory_data, orders_data)
    st.dataframe(anomalies)

    # Optimize supply chain
    if st.button('Optimize Supply Chain', key='optimize_button', class_='optimize-button'):
        with st.spinner('Optimizing supply chain...'):
            try:
                data = {
                    'inventory': inventory_data,
                    'products': products_data,
                    'suppliers': suppliers_data,
                    'transportation': transportation_data,
                    'orders': orders_data,
                    'external': external_data,
                    'demand_forecast': demand_forecast,
                    'constraints': {},  # Provide the necessary constraints data
                    'objectives': {}  # Provide the necessary objectives data
                }
                optimizer = Optimizer({})  # Provide the necessary configuration
                optimized_data, performance_metrics = optimizer.optimize(data)
                st.success('Supply chain optimization completed!')
            except Exception as e:
                st.error(f'Error during supply chain optimization: {str(e)}')

        # Display optimized results
        st.markdown('<div class="header">Optimized Results</div>', unsafe_allow_html=True)

        with st.container():
            col1, col2 = st.columns(2)

            with col1:
                st.markdown('<div class="results-container">', unsafe_allow_html=True)
                st.subheader('Demand Forecast')
                st.dataframe(demand_forecast)
                st.markdown('</div>', unsafe_allow_html=True)

            with col2:
                st.markdown('<div class="results-container">', unsafe_allow_html=True)
                st.subheader('Supplier Allocation')
                supplier_allocation_df = pd.DataFrame(optimized_data['best_solution']['supplier_allocation'], index=['Quantity']).T
                st.dataframe(supplier_allocation_df)
                st.markdown('</div>', unsafe_allow_html=True)

        with st.container():
            col1, col2 = st.columns(2)

            with col1:
                st.markdown('<div class="results-container">', unsafe_allow_html=True)
                st.subheader('Optimized Transportation')
                transportation_df = pd.DataFrame(optimized_data['best_solution']['transportation'])
                st.dataframe(transportation_df)
                st.markdown('</div>', unsafe_allow_html=True)

            with col2:
                st.markdown('<div class="results-container">', unsafe_allow_html=True)
                st.subheader('Optimized Inventory')
                inventory_df = pd.DataFrame(optimized_data['best_solution']['inventory']).T
                st.dataframe(inventory_df)
                st.markdown('</div>', unsafe_allow_html=True)

        # AI-powered route optimization
        st.markdown('<div class="header">AI-Powered Route Optimization</div>', unsafe_allow_html=True)
        optimized_routes = route_optimization(transportation_data)
        st.dataframe(optimized_routes)

        # Display optimized metrics
        st.markdown('<div class="header">Optimized Metrics</div>', unsafe_allow_html=True)

        metrics_df = pd.DataFrame(performance_metrics, index=['Value']).T
        st.dataframe(metrics_df)

        # Visualize optimized metrics
        fig = px.bar(metrics_df, x=metrics_df.index, y='Value', title='Optimized Metrics')
        st.plotly_chart(fig)


def upload_data(data_name):
    uploaded_file = st.file_uploader(f'Upload {data_name}', type=['csv', 'xlsx'], key=data_name)
    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file)
            return data
        except Exception as e:
            st.error(f'Error uploading {data_name}: {str(e)}')
    return None


if __name__ == '__main__':
    main()