import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Navigate } from 'react-router-dom';

const MyTodos = () => {
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
        const response = await axios.get('http://localhost:8001/todos/', {
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
  if (redirectToLogin) {
    // If redirectToLogin is true, redirect to login page
    return <Navigate to="/login" />
  }

  return (
    <div>
      <h2>My Todos</h2>
      <ul className="list-group">
        {todos.map(todo => (
          <li key={todo.id} className="list-group-item">
            <strong>Title: </strong>{todo.title}
            <br />
            <strong>Description: </strong>{todo.description}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default MyTodos;
