import * as React from 'react';
import Button from '@mui/material/Button';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Typography from '@mui/material/Typography';


const rows = [
    { Id: 1, OrderNumber: 600, CostDollar: 10, CostRuble: 600, DeliveryDate: "2019-10-24" },
    { Id: 2, OrderNumber: 601, CostDollar: 20, CostRuble: 1200, DeliveryDate: "2019-10-24" },
    { Id: 3, OrderNumber: 602, CostDollar: 30, CostRuble: 1800, DeliveryDate: "2019-10-24" }
];

function load_more_orders(event: React.MouseEvent) {
  event.preventDefault();
}

export default function Orders() {
  return (
    <React.Fragment>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell align="center">№</TableCell>
            <TableCell align="center">Заказ №</TableCell>
            <TableCell align="center">Стоимость, $</TableCell>
            <TableCell align="center">Стоимость, ₽</TableCell>
            <TableCell align="center">Дата поставки</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.Id}>
              <TableCell align="center">{row.Id}</TableCell>
              <TableCell align="center">{row.OrderNumber}</TableCell>
              <TableCell align="center">{row.CostDollar}</TableCell>
              <TableCell align="center">{row.CostRuble}</TableCell>
              <TableCell align="center">{row.DeliveryDate}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      <Typography align='center'>
        <Button variant="contained" onClick={load_more_orders} sx={{ mt: 3 }}>Еще</Button>
      </Typography>
    </React.Fragment>
  );
}
