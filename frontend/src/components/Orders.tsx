import React, { useState, useEffect } from 'react';
import Button from '@mui/material/Button';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Typography from '@mui/material/Typography';


export default function Orders() {
  const [currentPage, setCurrentPage] = useState(0)
  const [hasMore, setHasMore] = useState(false)
  const [orders, setOrders] = useState([]);

  function load_more_orders() {
    fetch('http://127.0.0.1:5000/get_data?Page=' + currentPage)
    .then((response) => response.json())
    .then((data) => {
        setCurrentPage(currentPage + 1);
        setHasMore(data.HasMore);
        setOrders([...orders, ...data.Orders]);
    });
  }

  useEffect(() => {
    load_more_orders();
  }, []);

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
          {orders.map((order) => (
            <TableRow key={order.Id}>
              <TableCell align="center">{order.Id}</TableCell>
              <TableCell align="center">{order.OrderId}</TableCell>
              <TableCell align="center">{order.CostInDollars}</TableCell>
              <TableCell align="center">{order.CostInRubles}</TableCell>
              <TableCell align="center">{order.DeliveryDate}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      { hasMore &&
      <Typography align='center'>
        <Button variant="contained" onClick={load_more_orders} sx={{ mt: 3 }}>Еще</Button>
      </Typography>
      }
    </React.Fragment>
  );
}
