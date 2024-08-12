import { Card, Space } from "antd"


function CryptocurrencyCard(props) {

    const {currency} = props

    const price = Math.round(currency.quote.USD.price * 100) / 100
    const percent_change_24h = Math.round(currency.quote.USD.percent_change_24h * 1000) / 1000
    const percent_change_90d = Math.round(currency.quote.USD.percent_change_90d * 1000) / 1000

    return (
      <div>
        <Card
        title={
            <div className="flex items-center gap-3">
                <img src={`https://s2.coinmarketcap.com/static/img/coins/64x64/${currency.id}.png`}/>
                <span>{currency.name}</span>
            </div>
        }
        style={{
            width: 500,
            height: 300
        }}
        >
          <p>Текущая цена: {price} $</p>
          <p>Изменение за 24 часа: {percent_change_24h} %</p>
          <p>Изменение за 90 дней : {percent_change_90d} %</p>
        </Card>
      </div>
    )
  }
  
  export default CryptocurrencyCard;