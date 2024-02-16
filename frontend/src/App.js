import Header from './components/common/header';
import Footer from './components/common/footer';
import {BrowserRouter as Router,  Routes ,Route } from 'react-router-dom';
import Login from './components/login';
import Register from './components/register';
import TodoDashBoard from './components/tododashboard';
import CreateUpdateTodo from './components/createupdatetodo';
import ManageUsers from './components/manageusers';
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
            <Route exact path="" element={<TodoDashBoard/>} />
            <Route exact path="/login" element={<Login/>} />
            <Route exact path="/register" element={<Register/>} />
            <Route exact path="/manageusers" element={<ManageUsers/>} />
            <Route exact path="/todos/:id?" element={<CreateUpdateTodo/>} />
        </Routes>
        </main>
      </Router>
      
     
      
     
      
      
      <Footer/>

    </div>
     
  );
}

export default App;
