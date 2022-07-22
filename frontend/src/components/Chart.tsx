import React, { useState, useEffect } from 'react';
import { useTheme } from '@mui/material/styles';
import { LineChart, Line, XAxis, YAxis, Label, ResponsiveContainer } from 'recharts';


export default function Chart() {
  const theme = useTheme();

  const [stats, setStats] = useState([]);
  
  function load_statistics() {
    fetch('http://127.0.0.1:5000/get_stats')
    .then((response) => response.json())
    .then((data) => {
        setStats([...stats, ...data.Stats]);
    });
  }

  useEffect(() => {
    load_statistics();
  }, []);

  return (
    <ResponsiveContainer width="100%" height={400}>
          <LineChart
          data={stats}
          margin={{
              top: 16,
              right: 16,
              bottom: 0,
              left: 24,
          }}
          >
          <XAxis
              dataKey="DeliveryDate"
              stroke={theme.palette.text.secondary}
              style={theme.typography.body2}
          />
          <YAxis
              stroke={theme.palette.text.secondary}
              style={theme.typography.body2}
          >
              <Label
              angle={270}
              position="left"
              style={{
                  textAnchor: 'middle',
                  fill: theme.palette.text.primary,
                  ...theme.typography.body1,
              }}
              >
              Cумма заказов
              </Label>
          </YAxis>
          <Line
              isAnimationActive={false}
              type="monotone"
              dataKey="Costs"
              stroke={theme.palette.primary.main}
              dot={false}
          />
          </LineChart>
    </ResponsiveContainer>
  );
}
