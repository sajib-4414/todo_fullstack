import React, { useState } from 'react';
import axios from 'axios';
import { Navigate } from 'react-router-dom';

const CreateTodo = () => {
  const [formData, setFormData] = useState({ title: '', description: '' });
  const [errors, setErrors] = useState({});
  const accessToken = localStorage.getItem('accessToken');

  const handleSubmit = (e) => {
    e.preventDefault();

    // Form validation
    const newErrors = {};
    if (!formData.title) newErrors.title = 'Title is required';
    if (!formData.description) newErrors.description = 'Description is required';
    setErrors(newErrors);

    if (Object.keys(newErrors).length === 0) {
      // Form is valid, make Axios call
      axios.post('http://localhost:8001/todos/', formData, {
        headers: {
          Authorization: `Bearer ${accessToken}`
        }
      })
        .then(response => {
          // Handle successful todo creation
          console.log('Todo created:', response.data);
          // Redirect to root domain
          window.location = "/";
        })
        .catch(error => {
          // Handle todo creation error
          console.error('Todo creation error:', error);
        });
    }
  };

  if (!accessToken) {
    // If accessToken is not present, redirect to login
    return <Navigate to="/login" />
  }

  return (
    <div>
      <h2>Create Todo</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="titleInput">Title</label>
          <input
            type="text"
            className="form-control"
            id="titleInput"
            placeholder="Enter title"
            value={formData.title}
            onChange={(e) => setFormData({ ...formData, title: e.target.value })}
          />
          {errors.title && <div className="text-danger">{errors.title}</div>}
        </div>
        <div className="form-group">
          <label htmlFor="descriptionInput">Description</label>
          <input
            type="text"
            className="form-control"
            id="descriptionInput"
            placeholder="Enter description"
            value={formData.description}
            onChange={(e) => setFormData({ ...formData, description: e.target.value })}
          />
          {errors.description && <div className="text-danger">{errors.description}</div>}
        </div>
        <button type="submit" className="btn btn-primary">Create Todo</button>
      </form>
    </div>
  );
}

export default CreateTodo;
