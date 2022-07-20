import Chart from './components/Chart.tsx';
import Orders from './components/Orders.tsx';
import Title from './components/Title.tsx';

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
