import YourComponent from './components/todolist';
import Header from './components/common/header';
import Footer from './components/common/footer';
import {BrowserRouter as Router,  Routes ,Route } from 'react-router-dom';
import Login from './components/login';
import Register from './components/register';
import MyTodos from './components/mytodos';
import CreateTodo from './components/createtodo';
function App() {
  return (
    <div>
  
      
      <Router>
      <Header/>
      <main role="main" 
      className="container"
      style={{ padding: "20px", marginTop: "100px" }}
      >
        <Routes>
            <Route exact path="" element={<MyTodos/>} />
            <Route exact path="/login" element={<Login/>} />
            <Route exact path="/register" element={<Register/>} />
            <Route exact path="/createtodos" element={<CreateTodo/>} />
        </Routes>
        </main>
      </Router>
      
     
      
     
      
      
      <Footer/>

    </div>
     
  );
}

export default App;
