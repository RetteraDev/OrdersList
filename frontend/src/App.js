import Chart from './components/Chart/Chart.tsx';
import Orders from './components/Orders/Orders.tsx';
import Title from './components/Title/Title.tsx';

function App() {
  return (
    <div className="App">
      <Title>Статистика</Title>
      <Chart/>
      <Title>Список заказов</Title>
      <Orders/>
    </div>
  );
}

export default App;
