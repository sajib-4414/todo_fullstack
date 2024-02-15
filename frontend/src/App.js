
import './App.css';
import YourComponent from './components/todolist';
import Header from './components/header';
import Footer from './components/footer';
import {BrowserRouter as Router,  Routes ,Route } from 'react-router-dom';
import Login from './components/login';
import Register from './components/register';
import MyTodos from './components/mytodos';
function App() {
  return (
    <div>
  
      <Header/>
      <main role="main" 
      className="container"
      style={{ padding: "20px", marginTop: "100px" }}
      >
      <Router>
        <Routes>
            <Route exact path="" element={<YourComponent/>} />
            <Route exact path="/login" element={<Login/>} />
            <Route exact path="/register" element={<Register/>} />
            <Route exact path="/mytodos" element={<MyTodos/>} />
        </Routes>
      </Router>
      </main>
     
      
     
      
      
      <Footer/>

    </div>
     
  );
}

export default App;
