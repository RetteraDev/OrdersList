import React, { useState, useEffect } from 'react';
import Typography from '@mui/material/Typography';
import { AreaChart, Area, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';
import { API_SERVER } from '../../config.js'
import styles from './Chart.module.css';


const CustomTooltip = ({ active, payload, label }) => {
  if (active && payload && payload.length) {
    return (
      <div className= { styles.Tooltip }>
        <p className="label">{new Date(label).toLocaleDateString('ru')}</p>
        <p className="intro">{[`${payload[0].payload.CostUSD}$ (${Math.round(payload[0].payload.CostRUB*100)/100}₽)\n`]}</p>
      </div>
    );
  }

  return null;
};


export default function Chart() {
  const [stats, setStats] = useState([]);
  const [total_orders, setTotalOrders] = useState([]);
  const [total_cost_usd, setTotalCostUSD] = useState([]);
  const [total_cost_rub, setTotalCostRUB] = useState([]);
  
  function load_statistics() {
    fetch(API_SERVER + 'get_stats')
    .then((response) => response.json())
    .then((data) => {
        setStats(data.Stats);
        setTotalOrders(data.TotalOrders);
        setTotalCostUSD(data.TotalCostUSD);
        setTotalCostRUB(data.TotalCostRUB);
    });
  }

  useEffect(() => {
    load_statistics();
  }, []);

  return (
    <div>
      <Typography component="h2" variant="h6" align="right" mr={2} gutterBottom>
        Всего сделано {total_orders} заказов на сумму {total_cost_usd}$ ({Math.round(total_cost_rub*100)/100})₽
      </Typography>
      <ResponsiveContainer width="100%" height={400}>
        <AreaChart
          data={stats}
          margin={{
            top: 16,
            right: 16,
            bottom: 0,
            left: 24,
          }}
        > 
          <XAxis dataKey="DeliveryDate" tickFormatter={(tick) => (new Date(tick).toLocaleDateString('ru'))}/>
          <YAxis/>
          <Tooltip
              content={<CustomTooltip />} formatter={(value, _, props) => ([`${value}$ (${Math.round(props.payload.CostRUB*100)/100}₽)`])}
          ></Tooltip>
          <Area type="monotone" dataKey="CostUSD"/>
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
}
