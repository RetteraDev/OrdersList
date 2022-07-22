import React, { useState, useEffect } from 'react';
import { AreaChart, Area, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';
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
  
  function load_statistics() {
    fetch('http://127.0.0.1:5000/get_stats')
    .then((response) => response.json())
    .then((data) => {
        setStats(data.Stats);
    });
  }

  useEffect(() => {
    load_statistics();
  }, []);

  return (
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
            content={<CustomTooltip />} formatter={(value, _, props) => ([`${value}$ (${Math.round(props.payload.CostRUB*100)/100}₽)\n`])}
        ></Tooltip>
        <Area type="monotone" dataKey="CostUSD"/>
      </AreaChart>
    </ResponsiveContainer>
  );
}
