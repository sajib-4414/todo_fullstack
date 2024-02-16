import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link, Navigate } from 'react-router-dom';

const TodoDashBoard = () => {
  const [todos, setTodos] = useState([]);
  const [redirectToLogin, setRedirectToLogin] = useState(false);

  useEffect(() => {
    const fetchTodos = async () => {
      try {
        const accessToken = localStorage.getItem('accessToken');
        if (!accessToken) {
          // If access token is not found, set redirectToLogin to true
          setRedirectToLogin(true);
          return;
        }
        const response = await axios.get(`${process.env.REACT_APP_API_HOST}/todos/`, {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        });
        setTodos(response.data);
      } catch (error) {
        console.error('Error fetching todos:', error);
      }
    };

    fetchTodos();
  }, []);

  const handleMarkTodo = async (id, done) => {
    try {
      const accessToken = localStorage.getItem('accessToken');
      if (!accessToken) {
        // If access token is not found, set redirectToLogin to true
        setRedirectToLogin(true);
        return;
      }
      const response = await axios.put(`${process.env.REACT_APP_API_HOST}/todos/${id}/`, { ...todos.find(todo => todo.id === id), done: !done }, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });
      // Update the todo in the UI
      setTodos(prevTodos => prevTodos.map(todo => todo.id === id ? response.data : todo));
    } catch (error) {
      console.error('Error updating todo:', error);
    }
  };

  const handleDeleteTodo = async (id) => {
    try {
      const accessToken = localStorage.getItem('accessToken');
      if (!accessToken) {
        // If access token is not found, set redirectToLogin to true
        setRedirectToLogin(true);
        return;
      }
      await axios.delete(`${process.env.REACT_APP_API_HOST}/todos/${id}/`, {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      });
      // Remove the todo from the UI
      setTodos(prevTodos => prevTodos.filter(todo => todo.id !== id));
    } catch (error) {
      console.error('Error deleting todo:', error);
    }
  };

  if (redirectToLogin) {
    // If redirectToLogin is true, redirect to login page
    return <Navigate to="/login" />
  }

  return (
    <div>
      <h2>My Todos</h2>
      <ul className="list-group">
        {todos.map(todo => (
          <li key={todo.id} className={`list-group-item d-flex justify-content-between align-items-center ${todo.done ? 'text-muted' : ''}`}>
            <div>
              <strong style={{ textDecoration: todo.done ? 'line-through' : 'none' }}>{todo.title}</strong>
              <br />
              <span style={{ textDecoration: todo.done ? 'line-through' : 'none' }}>{todo.description}</span>
            </div>
            <div>
              <button className="btn btn-sm btn-info mr-2" style={{marginRight:'10px'}} onClick={() => handleMarkTodo(todo.id, todo.done)}>
                {todo.done ? 'Mark as Pending' : 'Mark as Done'}
              </button>
              <Link to={`/todos/${todo.id}`} className="btn btn-sm btn-primary mr-2" style={{marginRight:'10px'}} >Edit</Link>
              <button className="btn btn-sm btn-danger" onClick={() => handleDeleteTodo(todo.id)}>Delete</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TodoDashBoard;
