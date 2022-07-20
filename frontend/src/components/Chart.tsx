import * as React from 'react';
import { useTheme } from '@mui/material/styles';
import { LineChart, Line, XAxis, YAxis, Label, ResponsiveContainer } from 'recharts';

const data = [
    { DeliveryDate: "2019-10-20", Costs: 100 },
    { DeliveryDate: "2019-10-21", Costs: 400 },
    { DeliveryDate: "2019-10-22", Costs: 600 },
    { DeliveryDate: "2019-10-23", Costs: 20 },
    { DeliveryDate: "2019-10-24", Costs: 600 },
    { DeliveryDate: "2019-10-25", Costs: 500 },
    { DeliveryDate: "2019-10-26", Costs: 1000 }
];

export default function Chart() {
  const theme = useTheme();

  return (
    <ResponsiveContainer width="100%" height={400}>
          <LineChart
          data={data}
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