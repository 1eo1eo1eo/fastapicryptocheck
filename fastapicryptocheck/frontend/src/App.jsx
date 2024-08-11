import React, { useEffect, useState } from 'react';
import { AppstoreOutlined, MailOutlined, SettingOutlined } from '@ant-design/icons';
import { Menu } from 'antd';
import { Spin } from 'antd'
import axios from 'axios';
import { icons } from 'antd/es/image/PreviewGroup';
import CryptocurrencyCard from './components/CryptocurrencyCard';

function getItem(label, key, icon, children, type) {
  return {
    key,
    icon,
    children,
    label,
    type,
  };
}

const App = () => {

  const [currencies, setCurrencies] = useState([])
  const [currencyId, setCurrencyId] = useState(1)
  const [currencyData, setCurrencyData] = useState(null)

  const fetchCurrencies = () =>{
    axios.get('http://127.0.0.1:8000/api/cryptocurrencies').then(response => {
      const currenciesResponse = response.data
      const menuItems = [
        getItem('Список криптовалют', 'g1', null,
          currenciesResponse.map(currency => {
            return {label: currency.name, key: currency.id}
          }),
          'group'
        )
      ]
      setCurrencies(menuItems)
    })
  }

  const fetchCurrency = () =>{
    axios.get(`http://127.0.0.1:8000/api/cryptocurrencies/${currencyId}`).then(response => {
      setCurrencyData(response.data)
    })
  }

  useEffect( () => {
    fetchCurrencies()
  }, []);

  useEffect( () => {
    setCurrencyData(null)
    fetchCurrency()
  }, [currencyId]);

  const onClick = (e) => {
    setCurrencyId(e.key)
  };
  return (
    <div className='flex'>
        <Menu
      onClick={onClick}
      style={{
        width: 256,
      }}
      defaultSelectedKeys={['1']}
      defaultOpenKeys={['sub1']}
      mode="inline"
      items={currencies}
      className='h-screen overflow-scroll'
    />
    <div className='mx-auto my-auto'>
    {currencyData ? <CryptocurrencyCard currency={currencyData}/> : <Spin size = "large"/>}
    </div>
    </div>
  );
};
export default App;